"""
Unique Paths II (Medium)
URL: https://leetcode.com/problems/unique-paths-ii/

Problem Description:
You are given an m x n integer array grid. A robot starts at the top-left corner
and tries to reach the bottom-right corner, moving only down or right. Obstacles
are marked as 1, spaces as 0. Return the number of unique paths.

Examples:
    Example 1: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]] -> 2
    Example 2: obstacleGrid = [[0,1],[0,0]] -> 1

Constraints:
    - 1 <= m, n <= 100
    - obstacleGrid[i][j] is 0 or 1.
"""


def uniquePathsWithObstacles(obstacleGrid: list[list[int]]) -> int:
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    dp = [[0] * n for _ in range(m)]

    if obstacleGrid[0][0] == 0:
        dp[0][0] = 1

    for r in range(m):
        for c in range(n):
            if obstacleGrid[r][c] == 1:
                dp[r][c] = 0
                continue
            if r == 0 and c == 0:
                continue
            if r == 0:
                dp[r][c] = dp[r][c - 1]
            elif c == 0:
                dp[r][c] = dp[r - 1][c]
            else:
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

    return dp[m - 1][n - 1]
