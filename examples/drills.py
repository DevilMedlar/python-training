"""Selected beginner references; attempt the corresponding drill first.

Preconditions: numeric collections contain ordinary finite numbers; text inputs
are strings; unique_in_order receives strings. These small calculations are not
general external-input parsers. Functions that explicitly reject an invalid
parameter say so below. Numeric annotations are intentionally omitted here.
"""


def split_minutes(minutes):
    if type(minutes) is not int:
        raise TypeError("minutes must be an integer")
    if minutes < 0:
        raise ValueError("minutes must be nonnegative")
    return divmod(minutes, 60)


def initials(name):
    result = ""
    for part in name.split():
        result += part[0].upper()
    return result


def valid_score(score):
    return 0 <= score <= 100


def total_through(n):
    if type(n) is not int:
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be nonnegative")
    total = 0
    for value in range(1, n + 1):
        total += value
    return total


def positive_values(values):
    result = []
    for value in values:
        if value > 0:
            result.append(value)
    return result


def unique_in_order(values):
    result = []
    seen = set()
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result


def word_counts(text):
    counts = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def average(values):
    return sum(values) / len(values) if values else None


def count_at_least(values, target):
    count = 0
    for value in values:
        if value >= target:
            count += 1
    return count


def contains_value(values, target):
    for value in values:
        if value == target:
            return True
    return False
