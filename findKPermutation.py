import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        permutation = [str(num) for num in range(1, n + 1)]

        index = 0
        enter_w_loop = False
        for num in range(n-1, 0, -1):
            if k == 1:
                break
            num1_factorial, num_factorial = math.factorial(num + 1), math.factorial(num)
            while k <= num1_factorial and k > num_factorial:
                k -= num_factorial
                if k > num_factorial:
                    index += 1
                enter_w_loop = True
            if enter_w_loop:
                num_to_move = permutation[n - num + index]
                permutation.remove(num_to_move)
                permutation.insert(n - 1 - num, num_to_move)
                index = 0
                enter_w_loop = False

        result = ''
        for num in permutation:
            result += str(num)
        return result

answer = Solution()
print(answer.getPermutation(9,150000))