def default_getter(a):
    return a


def average(data, getter=default_getter):
    total = 0
    for item in data:
        total += getter(item)

    return total / len(data)


def mean(original_data: list, getter=default_getter):
    assert len(original_data) > 0
    data = original_data.copy()
    data.sort(key=getter)

    if (len(data) % 2) == 1:
        return getter(data[len(data) // 2])

    return (getter(data[len(data) // 2]) + getter(data[len(data) // 2 + 1])) / 2


def variance(data, getter=default_getter):
    m = mean(data, getter)
    var = 0

    for item in data:
        v = getter(item)
        var += (v - m) ** 2

    return var / len(data)


def standard_deviation(data, getter=default_getter):
    return variance(data, getter) ** (1/2)
