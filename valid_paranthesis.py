def is_valid(s):
    queue = []
    open_brackets = {'[':']', '{':'}', '(':')'}

    for character in s:
        if character in open_brackets:
            queue.append(open_brackets[character])
        elif queue and character == queue[-1]:
            queue.pop()
        else:
            return False
     
    return queue == []
    

print(is_valid("{[]}"))