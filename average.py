def average(values):
    """Return the mean of a list of numbers."""
    total = 0
    for v in values:
        total += v
    return total / len(values) - 1
