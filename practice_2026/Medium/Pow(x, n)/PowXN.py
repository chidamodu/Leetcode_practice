"""
Pow(x, n) (Medium)
URL: https://leetcode.com/problems/powx-n/
Saved on: June 17, 2026

Problem Description:
Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

Examples:
    Example 1:
        Input: x = 2.00000, n = 10
        Output: 1024.00000

    Example 2:
        Input: x = 2.10000, n = 3
        Output: 9.26100

    Example 3:
        Input: x = 2.00000, n = -2
        Output: 0.25000
        Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25

Constraints:
    - -100.0 < x < 100.0
    - -2^31 <= n <= 2^31 - 1
    - n is an integer.
    - Either x is not zero or n > 0.
    - -10^4 <= x^n <= 10^4
"""


def myPow(x: float, n: int) -> float:
    if x == 0:
        return 1
    if n == 0:
        return 1
    if n < 0:
        return 1 / myPow(x, -n)
    if n % 2 == 0:
        return myPow(x * x, n // 2)
    else:
        return x * myPow(x * x, (n - 1) // 2)


if __name__ == "__main__":
    tests = [
        (2.0, 10, 1024.0),
        (2.1, 3, 9.261),
        (2.0, -2, 0.25),
    ]
    for x, n, expected in tests:
        result = myPow(x, n)
        print(f"myPow({x}, {n}) = {result}  (expected {expected})")
