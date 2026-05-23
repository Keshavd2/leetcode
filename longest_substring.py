def longest_substring(s):
    left, right = 0, 0
    max_length = 0
    substring = set()

    while(right < len(s)):
        if s[right] in substring:
            substring.remove(s[left])
            left += 1
        else:
            substring.add(s[right])
            right += 1

        if right - left > max_length:
            max_length = right - left
    
    return max_length

a = "abcdef"
print(longest_substring(a))