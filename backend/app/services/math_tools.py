def average(values):
    return sum(values) / len(values) if values else 0


def percent_change(first, last):
    if first == 0:
        return 0
    return ((last - first) / first) * 100
