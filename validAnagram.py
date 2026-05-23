def valid_anagram(s, t):
    letter_counts = {}
    length = len(s)

    for letter in s:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
    
    for letter in t:
        if letter_counts.get(letter, 0):
            letter_counts[letter] -= 1
            length -= 1
        else:
            return False
    
    return length == 0
        


a = "listen"
b = "silent"

print(valid_anagram(a, b))
