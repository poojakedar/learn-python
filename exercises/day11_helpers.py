"""Day 11 exercise helper module."""


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def is_adult(age):
    return age >= 18


def percentage(part, total):
    if total == 0:
        raise ValueError("Total cannot be zero")
    return (part / total) * 100
