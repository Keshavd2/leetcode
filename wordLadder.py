import copy

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        output = [['hot']]
        #currentSet = set(beginWord)
        currentSet = set('hot')
        while(True):

            possible_next_words_indices = []
            set_intersection_norms = []
            max_number = 0

            for i in range(0, len(wordList)):
                set_length = (len(currentSet.intersection(set(wordList[i]))))
                if set_length == len(currentSet) and i < len(wordList) - 1:
                    set_length = 0
                set_intersection_norms.append(set_length)
            
            max_number = max(set_intersection_norms)

            for i in range(0,len(set_intersection_norms)):
                if set_intersection_norms[i] == max_number:
                    possible_next_words_indices.append(i)

            

            duplication_num = len(possible_next_words_indices)

            
            
            duplicate_list = output.deepcopy()
            print(duplicate_list)


            for numTimes in range(duplication_num - 1):
                for stuff_inside in duplicate_list:
                    output.append(stuff_inside)

            #output = (output * duplication_num)


            fraction_count = len(output) // duplication_num
            count = 0
            print(output)

            for index in possible_next_words_indices:
                for i in range(fraction_count):
                    print("index: %s" % index)
                    print("word: %s" % wordList[index])
                    print(output[count])
                    output[count].append(wordList[index])
                    print(output)
                    count += 1
            
                    
                        
                
            print(output[0])
            output[0][0] = 'hit'
            print(max_number)
            print(fraction_count)
            print(set_intersection_norms)
            print(possible_next_words_indices)
            print(output)
            
            break

problem = Solution()
problem.findLadders('hit', 'cog', ["hot","dot","dog","lot","log","cog"])