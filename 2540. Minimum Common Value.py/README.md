# 2540. Minimum Common Value

**Difficulty:** Easy
**Topics:** Array, Binary Search, Two Pointers
**Link:** https://leetcode.com/problems/minimum-common-value/

---

## Problem Statement

Given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst `nums1` and `nums2`, return `-1`.

An integer is common to both arrays if it appears at least once in each.

### Example 1
Input: nums1 = [1,2,3], nums2 = [2,4]
Output: 2
Explanation: The smallest element common to both arrays is 2.

### Example 2
Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
Output: 2
Explanation: 2 and 3 are common; 2 is the smallest.

### Constraints
- `1 <= nums1.length, nums2.length <= 10^5`
- `1 <= nums1[i], nums2[j] <= 10^9`
- Both arrays are sorted in non-decreasing order.

---
