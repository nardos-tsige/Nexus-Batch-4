# 2460. Apply Operations to an Array

**Difficulty:** Easy
**Topics:** Array, Simulation

## Problem

Given a 0-indexed array `nums` of size `n` consisting of non-negative integers, apply `n - 1` operations to this array where, in the `ith` operation (0-indexed):

- If `nums[i] == nums[i + 1]`, multiply `nums[i]` by `2` and set `nums[i + 1]` to `0`. Otherwise, skip this operation.

After performing all the operations, shift all the `0`'s to the end of the array.

Return the resulting array. Operations are applied sequentially, not all at once.

### Example 1
Input: nums = [1,2,2,1,1,0]
Output: [1,4,2,0,0,0]

### Example 2
Input: nums = [0,1]
Output: [1,0]

### Constraints
- `2 <= nums.length <= 2000`
- `0 <= nums[i] <= 1000`
