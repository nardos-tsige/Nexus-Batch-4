# 2506. Count Pairs Of Similar Strings

**Difficulty:** Easy
**Topics:** Hash Table, String, Bit Manipulation

## Problem

Given a 0-indexed string array `words`, two strings are similar if they consist of the same set of characters.

Return the number of pairs `(i, j)` such that `0 <= i < j <= words.length - 1` and `words[i]` and `words[j]` are similar.

### Example 1
Input: words = ["aba","aabb","abcd","bac","aabc"]
Output: 2

### Example 2
Input: words = ["aabb","ab","ba"]
Output: 3

### Example 3
Input: words = ["nba","cba","dba"]
Output: 0

### Constraints
- `1 <= words.length <= 100`
- `1 <= words[i].length <= 100`
- `words[i]` consists of only lowercase English letters.
