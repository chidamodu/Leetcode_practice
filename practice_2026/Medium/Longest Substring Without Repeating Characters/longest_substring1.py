
# Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without duplicate characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
# Constraints:
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

# def lengthOfLongestSubstring(s):
#     if len(s):
#         left = 0
#         right = 1
#     else:
#         return 0
#     max_length = -1
    
#     while left < right and right < len(s):
#         seen = s[left]
#         print(seen)
#         while right < len(s) and s[right] not in seen:
#             seen += s[right]
#             print(seen)
#             right += 1
#         max_length = max(max_length, len(seen))
#         seen = ""
#         left += 1
        
#     print(max_length)

# lengthOfLongestSubstring(s = "pwwkew")

# def lengthOfLongestSubstring(s):
#     if not s:
#         return 0   
#     seen = set()
#     left = 0
#     max_length = 0
    
#     # 'right' iterates once from 0 to end (O(N))
#     for right in range(len(s)):
#         # If we find a duplicate, shrink the window from the left
#         while s[right] in seen:
#             seen.remove(s[left])
#             left += 1
            
#         # Add the new character and update max length
#         seen.add(s[right])
#         print(seen)
#         max_length = max(max_length, right - left + 1)
        
#     return print(max_length)
# lengthOfLongestSubstring(s = "pwwkew")

# def lengthOfLongestSubstring(s):
#     d = {}
#     left = 0
#     result = 0
#     for right in range(len(s)):
#         if s[right] in d and d[s[right]] >= left:
#             left = d[s[right]] + 1
#         d[s[right]] = right
#         result = max(result, right-left+1)
#     print(d)
#     return print(result)   
# lengthOfLongestSubstring(s = "pwwkew")

def lengthOfLongestSubstring(s):
    if not s:
        return 0   
    seen = set()
    left = 0
    max_length = 0
    
    # 'right' iterates once from 0 to end (O(N))
    for right in range(len(s)):
        # If we find a duplicate, shrink the window from the left
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
            
        # Add the new character and update max length
        seen.add(s[right])

        max_length = max(max_length, len(seen)) 
    print(seen)  
    return print(max_length)
lengthOfLongestSubstring(s = "pwwkew")

    