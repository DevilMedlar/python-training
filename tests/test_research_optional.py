import importlib.util
import unittest


AVAILABLE = all(importlib.util.find_spec(name) is not None for name in ("numpy", "scipy"))
if AVAILABLE:
    import numpy as np
    from examples.research_optional import paired_differences, run, simulate, theoretical_mean_mse


@unittest.skipUnless(AVAILABLE, "Optional NumPy/SciPy research environment is not installed")
class ResearchTests(unittest.TestCase):
    def test_closed_form_mean_mse(self):
        self.assertEqual(theoretical_mean_mse(0, 100), 0.01)
        self.assertAlmostEqual(theoretical_mean_mse(0.1, 100), 0.109)
        self.assertEqual(theoretical_mean_mse(1, 100), 1.0)

    def test_invalid_simulation_inputs(self):
        for probability in (-0.1, 1.1, float("nan"), float("inf")):
            with self.subTest(probability=probability), self.assertRaises(ValueError):
                simulate(0, 0, probability)
        with self.assertRaises(TypeError):
            simulate(0, True, 0.1)
        with self.assertRaises(ValueError):
            simulate(0, 0, 0.1, observations=0)

    def test_stable_task_identity_is_independent_of_evaluation_order(self):
        forward = {i: simulate(1, i, 0.1, observations=20) for i in range(8)}
        backward = {i: simulate(1, i, 0.1, observations=20) for i in reversed(range(8))}
        for i in forward:
            np.testing.assert_array_equal(forward[i], backward[i])

    def test_pairing_sign_and_shape(self):
        np.testing.assert_array_equal(paired_differences([[4, 1], [0, 2]]), [3, -2])
        for losses in ([], [1, 2], [[1, 2, 3]], [[float("nan"), 1]], [[-1, 2]]):
            with self.subTest(losses=losses), self.assertRaises(ValueError):
                paired_differences(losses)

    def test_small_end_to_end_preserves_raw_evidence(self):
        result = run(replicates=40, observations=20, resamples=199)
        again = run(replicates=40, observations=20, resamples=199)
        self.assertEqual(result, again)
        for scenario in result["results"]:
            losses = np.array(scenario["raw_losses_mean_median"])
            self.assertEqual(losses.shape, (40, 2))
            self.assertAlmostEqual(float((losses[:, 0] - losses[:, 1]).mean()),
                                   scenario["paired_mse_difference_mean_minus_median"])
            low, high = scenario["difference_ci95"]
            self.assertTrue(np.isfinite([low, high]).all())
            self.assertLessEqual(low, high)
