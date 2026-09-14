"""Optional paired estimator experiment, adapted from the supplied Phase 4 draft.

NumPy/SciPy are optional; install requirements-research.txt for the recorded
environment. This is an established teaching comparison, not a novel finding.
Intervals describe Monte Carlo uncertainty under each specified simulator.
"""

import argparse
import json
import math
import platform

import numpy as np
import scipy
from scipy.stats import bootstrap


ROOT_SEED = 20260914
SCENARIOS = ((0, 0.0), (1, 0.1))


def _count(value, name, minimum=0):
    if type(value) is not int:
        raise TypeError(f"{name} must be an integer, excluding booleans")
    if value < minimum:
        raise ValueError(f"{name} must be at least {minimum}")


def theoretical_mean_mse(contamination, observations):
    _count(observations, "observations", 1)
    if isinstance(contamination, bool) or not isinstance(contamination, (int, float)):
        raise TypeError("contamination must be numeric")
    if not math.isfinite(contamination) or not 0 <= contamination <= 1:
        raise ValueError("contamination must lie between 0 and 1")
    return ((1 - contamination) + 100 * contamination) / observations


def simulate(scenario_id, replicate_id, contamination, observations=100, root_seed=ROOT_SEED):
    """Return mean/median squared errors on the SAME zero-centered dataset."""
    _count(scenario_id, "scenario_id")
    _count(replicate_id, "replicate_id")
    _count(root_seed, "root_seed")
    theoretical_mean_mse(contamination, observations)
    rng = np.random.default_rng(np.random.SeedSequence([scenario_id, replicate_id, root_seed]))
    values = rng.normal(0.0, 1.0, size=observations)
    contaminated = rng.random(observations) < contamination
    values[contaminated] = rng.normal(0.0, 10.0, size=int(contaminated.sum()))
    estimates = np.array([values.mean(), np.median(values)])
    return estimates**2


def paired_differences(losses):
    losses = np.asarray(losses, dtype=float)
    if losses.ndim != 2 or losses.shape[1] != 2 or losses.shape[0] < 1:
        raise ValueError("losses must have shape (replications, 2)")
    if not np.isfinite(losses).all() or (losses < 0).any():
        raise ValueError("squared losses must be finite and nonnegative")
    return losses[:, 0] - losses[:, 1]


def run(replicates=1000, observations=100, resamples=4999):
    _count(replicates, "replicates", 3)
    _count(observations, "observations", 2)
    _count(resamples, "resamples", 100)
    results = []
    for scenario_id, contamination in SCENARIOS:
        losses = np.array([
            simulate(scenario_id, replicate_id, contamination, observations)
            for replicate_id in range(replicates)
        ])
        differences = paired_differences(losses)
        inference_rng = np.random.default_rng(
            np.random.SeedSequence([scenario_id, 999999, ROOT_SEED, 1])
        )
        interval = bootstrap(
            (differences,), np.mean, confidence_level=0.95,
            method="BCa", n_resamples=resamples, batch=100, rng=inference_rng,
        ).confidence_interval
        if not np.isfinite([interval.low, interval.high]).all():
            raise ValueError("degenerate interval; inspect the data and inference design")
        results.append({
            "scenario_id": scenario_id,
            "contamination_probability": contamination,
            "mean_estimator_mse": float(losses[:, 0].mean()),
            "median_estimator_mse": float(losses[:, 1].mean()),
            "paired_mse_difference_mean_minus_median": float(differences.mean()),
            "difference_ci95": [float(interval.low), float(interval.high)],
            "theoretical_mean_mse": theoretical_mean_mse(contamination, observations),
            "raw_losses_mean_median": losses.tolist(),
        })
    return {
        "python": platform.python_version(), "platform": platform.platform(),
        "numpy": np.__version__, "scipy": scipy.__version__, "root_seed": ROOT_SEED,
        "generator": "NumPy default_rng / PCG64; SeedSequence([scenario, replicate, root])",
        "observations_per_dataset": observations,
        "independent_datasets_per_scenario": replicates,
        "bootstrap": {"method": "BCa", "resamples": resamples, "batch": 100,
                      "confidence_level": 0.95,
                      "inference_entropy": "[scenario_id, 999999, root_seed, 1]"},
        "limitations": "per-scenario Monte Carlo intervals; no multiplicity adjustment; "
                       "simulated symmetric populations; record code/environment separately",
        "results": results,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--replicates", type=int, default=1000)
    parser.add_argument("--observations", type=int, default=100)
    parser.add_argument("--resamples", type=int, default=4999)
    args = parser.parse_args(argv)
    try:
        result = run(args.replicates, args.observations, args.resamples)
    except ValueError as error:
        parser.error(str(error))
    print(json.dumps(result, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
