# Unique Paths II (Medium)

**URL:** https://leetcode.com/problems/unique-paths-ii/

## Problem Description

You are given an `m x n` integer array `grid`. A robot starts at the top-left corner (`grid[0][0]`) and tries to reach the bottom-right corner (`grid[m - 1][n - 1]`). The robot can only move down or right.

An obstacle and space are marked as `1` or `0` respectively. A path cannot include any obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

## Examples

### Example 1
- **Input:** `obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]`
- **Output:** `2`

### Example 2
- **Input:** `obstacleGrid = [[0,1],[0,0]]`
- **Output:** `1`

## Constraints

- `m == obstacleGrid.length`, `n == obstacleGrid[i].length`
- `1 <= m, n <= 100`
- `obstacleGrid[i][j]` is `0` or `1`.
