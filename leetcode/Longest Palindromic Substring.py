# https://leetcode.com/problems/longest-palindromic-substring/

def is_palindrome(string, b, e):
    m = (b + e) >> 1
    while b <= m:
        if string[b] != string[e]:
            return False
        b += 1
        e -= 1
    return True


def find_palindrome(s, str_len, l, r):
    while 0 <= l and l < str_len and 0 <= r and r < str_len:
        if s[l] != s[r]:
            break
        l -= 1
        r += 1
    return s[l+1:r]


assert find_palindrome('abba', 4, 1, 1) == 'b'
assert find_palindrome('abba', 4, 1, 2) == 'abba'
assert find_palindrome('aabbaa', 6, 2, 2) == 'b'
assert find_palindrome('aabbaa', 6, 2, 3) == 'aabbaa'
assert find_palindrome('racecar', 7, 3, 3) == 'racecar'
assert find_palindrome('racecarh', 8, 3, 3) == 'racecar'
assert find_palindrome('aracecar', 8, 4, 4) == 'racecar'
assert find_palindrome('zracecary', 9, 4, 4) == 'racecar'


class Solution:
    def longestPalindrome(self, s: str) -> str:
        c_indices = dict()
        
        for i in range(len(s)):
            c = s[i]
            if c in c_indices:
                c_indices[c].append(i)
            else:
                c_indices[c] = [i]

        maxlen = 1
        result = s[0]

        for idx_list in c_indices.values():
            n = len(idx_list) - 1
            l = 0
            r = n

            while l < r and r <= n:
                b = idx_list[l]
                e = idx_list[r]
                substr_len = e - b + 1
                if substr_len > maxlen and s[b:e+1] == s[b:e+1][::-1]:
                    maxlen = substr_len
                    result = s[b:e+1]
                    
                if r - 1 != l:
                    r -= 1
                else:
                    l += 1
                    r = n
        
        return result

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_len = 1
        result = s[0]
        for i in range(n):
            pld = find_palindrome(s, n, i, i)
            if len(pld) > max_len:
                max_len = len(pld)
                result = pld

            pld = find_palindrome(s, n, i, i+1)
            if len(pld) > max_len:
                max_len = len(pld)
                result = pld
            
        return result


solution = Solution()

assert solution.longestPalindrome("zradarraarh") == "radar"
assert solution.longestPalindrome("zraarradarh") == "radar"
assert solution.longestPalindrome("zradarcarh") == "radar"
assert solution.longestPalindrome("sracecarj") == "racecar"
assert solution.longestPalindrome("sracecar") == "racecar"
assert solution.longestPalindrome("racecar") == "racecar"
assert solution.longestPalindrome("bbbaabbc") == "bbaabb"
assert solution.longestPalindrome("bbaabbc") == "bbaabb"
assert solution.longestPalindrome("bbaabb") == "bbaabb"
assert solution.longestPalindrome("zradarh") == "radar"
assert solution.longestPalindrome("babad") == "bab"
assert solution.longestPalindrome("cbbd") == "bb"
assert solution.longestPalindrome("cc") == "cc"
assert solution.longestPalindrome("ac") == "a"
assert solution.longestPalindrome("a") == "a"
assert solution.longestPalindrome("aaaabcaaa") == "aaaa"
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
r = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
assert solution.longestPalindrome(s) == r

print("\nAll tests passed.\n")
