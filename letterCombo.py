class Solution:
    def letterCombinations(self, digits):
        buttons = {'1':"", '2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],
        '6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}

        mapping = []
        mappings_len = 1

        for num in digits:
            if num == '9' or num == '7':
                mappings_len *= 4
            else:
                mappings_len *= 3

        #print(mappings_len)
        for x_time in range(0,mappings_len):
            mapping.append('')

        letter_position = 0
        queue = [1]
        switch_on = False
        for digit in digits:
            letters = buttons[digit]
            letters_len = len(letters)
            if switch_on:
                queue.append(letters_len * queue[letter_position - 1])
            switch_on = True
            count = 0
            y = 0
            i = 0
            cycle = 0

            while (y < letters_len):
                if (queue[letter_position] * i) >= mappings_len:
                    i = 0
                    cycle += 1

                mapping[queue[letter_position] * i + cycle] += letters[y]
                count += 1
                print(mapping)
                print('\n')

                if count == mappings_len // letters_len:
                    y += 1
                    count = 0
                i += 1

            letter_position += 1
            print(queue)




answer = Solution()

answer.letterCombinations('7')