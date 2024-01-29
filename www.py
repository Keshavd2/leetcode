class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return Solution.isMatching(self, s, p)
     
    def isMatching(self, s, p, index = 0, result = "") -> bool:
        if len(p) == 0 and len(s) > 0:
                return False
                
        while (index < len(s)) or (len(s) == 0 and len(p) > 0):
            i = index
            #print(i)
            value_of_s_char = "" if len(s) == 0 else s[i]
            if len(p) <= i:
                #print("0: %s" % result)
                return False
            else:
                value_of_p_char = "" if len(p) == 0 else p[i]
            
            #if characters match or p character is ?
            if value_of_s_char == value_of_p_char or value_of_p_char == '?':
                result += value_of_s_char

            #if p character is *
            elif value_of_p_char == '*':
                p_str_split = p.split('*',1)                                                        #split string and replace * with empty set or with character x times
                for numTimes in range(0,len(s) + 1):                                                    #let num times be a big as number of characters of s that haven't been checked
                    new_p_str = p_str_split[0] + ('?' * numTimes) + p_str_split[1]      #make new p string 
                    #print(new_p_str)
                    if Solution.isMatching(self, s, new_p_str, i, result):                          #recursively call method, and return True if p and s are matching else False
                        #print("True")
                        return True
                    else:
                        #print("False")
                        continue

            # else if character do not much and therefore p is not a matching string
            elif value_of_s_char != value_of_p_char:
                #print("1: %s" % result)
                return False
            
            #update index value
            index += 1

        #after both strings characters have been checked, see if they are matching. If not, return false
        if result == s:
            #print("length of p: %s" % len(p))
            if len(s) != len(p):
                for ind in range(len(s), len(p)):
                    if p[ind] != '*':
                        #print("2: %s" % result)
                        return False
            return True
        else:
            #print("2: %s" % result)
            return False

solu = Solution()
print("This answer is %s" % solu.isMatch("babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab", "***bba**a*bbba**aab**b"))