"""
Write a function that that takes a positive integer as a parameter.
The function should return the sum of all the multiples of 3 and/or 5 less than (but not equal to) the number passed in

example
sum_of_multiples(10)
returns 23
3 + 5 + 6 + 9
"""

def sum_of_multiples(num):
    aggregate = 0
    multiples_of_3_or_5 = [number for number in range(num) if number % 3 == 0 or number % 5 == 0]
    for number in multiples_of_3_or_5:
        aggregate = aggregate + number
    return aggregate

def test_sum_of_multiples_solution():
    assert sum_of_multiples(10) == 23
    assert sum_of_multiples(20) == 78
    assert sum_of_multiples(0) == 0
    assert sum_of_multiples(1) == 0
    assert sum_of_multiples(200) == 9168
    assert sum_of_multiples(64) == 933

test_sum_of_multiples_solution()

# CHALLENGE: refactor to use list comprehension