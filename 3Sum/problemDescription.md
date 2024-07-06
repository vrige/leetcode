# Three Sum

## Problem Statement

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

## Examples

### Example 1

**Input:** `nums = [-1, 0, 1, 2, -1, -4]`  
**Output:** `[[-1, -1, 2], [-1, 0, 1]]`  
**Explanation:** The triplets `[-1, -1, 2]` and `[-1, 0, 1]` meet the requirements. Note that the output order does not matter, so `[[ -1, 0, 1], [-1, -1, 2]]` is also correct.

### Example 2

**Input:** `nums = [0, 1, 1]`  
**Output:** `[]`  
**Explanation:** The array does not contain any triplets that meet the requirements.

### Example 3

**Input:** `nums = [0, 0, 0]`  
**Output:** `[[0, 0, 0]]`  
**Explanation:** The only triplet that meets the requirements is `[0, 0, 0]`.

## Constraints

- `0 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`
