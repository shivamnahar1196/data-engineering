# TODO Nielsen 1: You are given two strings s1 and s2 consisting of lowercase characters.
#  You need to return true, if s2 contains a permutation of s1, or false otherwise.
#  In other words, return true if one of s1's permutations is the substring of s2.The function isPermutation() accepts
#  the parameters string s1 and s2. Complete the function isPermutation() and returns the check_string in boolean format
#  . For Example: If the string s1 is tac and s2 is catering
#  then one of the permutation of tac i.e. cat is present in the catering, Hence return true.
#  Constraints: 1<=s1.size,s2.size<=1000 # Input: # s1=qwd # s2= wdfijewjewewswf Output: # check_string= False

from itertools import permutations


def isPermutation(s1, s2) -> bool:
    len_s1 = len(s1)
    len_s2 = len(s2)

    if len_s1 > len_s2:
        return False

    # Generate all permutations of s1
    for perm in permutations(s1):
        print(perm)
        """
        ('q', 'w', 'd')
        ('q', 'd', 'w')
        ('w', 'q', 'd')
        ('w', 'd', 'q')
        ('d', 'q', 'w')
        ('d', 'w', 'q')
        """
    perms_s1 = [''.join(perm) for perm in permutations(s1)]
    print(perms_s1)  # ['qwd', 'qdw', 'wqd', 'wdq', 'dqw', 'dwq']

    # Check if any permutation of s1 is a substring of s2
    for perm in perms_s1:
        if perm in s2:
            return True

    return False


if __name__ == '__main__':
    s1 = 'qwd'
    s2 = 'wdijewjewewswf'
    print(isPermutation(s1, s2))

# TODO Incedo 1: # o/p = [5, 7, 9] I want to get the output with the help of map function in python.
num1 = [1, 2, 3]
num2 = [4, 5, 6]
#

# Method - 1

def myfunc(l1: int, l2: int) -> int:
    return l1 + l2


x = list(map(myfunc, num1, num2))
print(x)

# Method - 2
a = zip(num2, num1)
print(a)
for i in a:
    print(i)

fl = []
for tp in a:
    fl.append(tp[0] + tp[1])

# TODO Tiger Analytics 1 Given list of companies with their face values in the stock market,write a Python code to:
#  Get the company's name along with its face value for the company which has the maximum and the minimum face values.
#  Sort this list based on face values in increasing order.

stock_market = {
    'AXIS BANK': 7,
    'BHARTI AIRTEL': 5,
    'COAL INDIA': 10,
    'ITC': 1,
    'TCS': 3,
    'L&T': 2,
    'RELIANCE': 9,
    'KOTAK BANK': 8,
    'AMERICAN EXPRESS': 11
}

# Sort in descending/ascending order
stock_market = sorted(stock_market.items(), key=lambda x: x[1], reverse=True)
print(stock_market)  # returns list of tuples.

# Max:
print(stock_market[0])

# Min:
print(stock_market[-1])
"""
Expected Output:

Maximum Face Value: (11, 'AMERICAN EXPRESS')
Minimum Face Value: (1, 'ITC')
Sorted List based on Face Values (Increasing Order):
[(1, 'ITC'), (2, 'L&T'), (3, 'TCS'), (5, 'BHARTI AIRTEL'), (7, 'AXIS BANK'), (8, 'KOTAK BANK'), (9, 'RELIANCE'),
(10, 'COAL INDIA'), (11, 'AMERICAN EXPRESS')]

"""

# TODO Tiger Analytics 2: A list of tuples is given below, containing the candidate's name and their heights(in cm).
#  Write a Python code to sort this list using Lambda functions according to the heights of the CANDIDATES
candidate_details = [('John', 168), ('Joseph', 160), ('Arun', 178), ('Vishal', 172)]
# Expected o/p: [('Joseph', 160), ('John', 168), ('Vishal', 172), ('Arun', 178)]

final = sorted(candidate_details, key=lambda x: x[1])
print(final)

# TODO Tiger Analytics 3: List of 3 letters. Write a Python code to concatenate this list with another list of numbers
#  whose range varies from 1 to 3 (3 is included).
letters_list = ['A', 'B', 'C']
# Expected Output:['A1', 'B1', 'C1', 'A2', 'B2', 'С2', 'АЗ', 'ВЗ', 'СЗ']

new_list = [i for i in range(1, 4)]
# print(new_list)
final = [word + str(num) for num in new_list for word in letters_list]
print(final)

# TODO Micron 1: find the longest sequence of consecutive numbers

list1 = [1, 3, 4, 5, 21, 22, 23, 2, 9, 8, 10, 11]

flag = True
final_dic = {}
count = 0
a = []

for i in range(len(list1)):
    if i > 0 and list1[i] - list1[i - 1] == 1:
        if flag:
            a.append(list1[i - 1])
            flag = False
        count += 1
        a.append(list1[i])
    else:
        if count > 0:  # Check if there was a sequence
            final_dic[tuple(a)] = count + 1  # Count + 1 to include the initial number of the sequence
            count = 0
            a = []
        flag = True

# Check for the last sequence if it extends to the end of the list
if count > 0:
    final_dic[tuple(a)] = count + 1

print(final_dic)


"""
--- Some Advance Questions ----
"""

# TODO : Turing 1:
"""
Strings are called Identical if they contain the same characters.
• For example, "good" and "god" are similar since both consist of characters 'g', 'o', and 'd'.
• However, "python" and "yarn" are not similar since they do not contain similar characters.
Find the number of sets (x, y) such that 0 < x < y <= str.length - 1 and the two strings strs[i] and strs[il are
identical.
Example 1:
• Input: strs = ["good", "god", "yarn", "bac", "aabc"].
• Output: 2
• Explanation: There are 2 pairs that satisfy the conditions:
- X = 0 and y = 1 : both strs[0] and strs[1] only consist of characters 'g', 'o' and 'd'.
-X= 3 and y = 4 : both strs[3] and strs[4] only consist of characters 'a', 'b', and

Example 2:
Input: words = ["cba", "nba", "dba"]
Output: 0
Explanation: Since there does not exist any pair that satisfies the conditions, we return

• Explanation: There are 2 pairs that satisfy the conditions:
- X = 0 and y = 1 : both strs[0] and strs[1] only consist of characters 'g', 'o' and 'd'.
-X= 3 and y = 4 : both strs[3] and strs[4] only consist of characters 'a', 'b'
"""

from typing import List
from collections import defaultdict


# Input: strs = ["good", "god", "yarn", "bac", "aabc"]

# Below can be given as an input to test
#  good god yarn bac aabc

def solution(strs: List[str]) -> int:
    frozenset_count = defaultdict(int)
    print(frozenset_count)  # defaultdict(<class 'int'>, {})

    for s in strs:
        char_set = frozenset(s)
        # char_set = set(s)
        frozenset_count[char_set] += 1
    print(frozenset_count)
    # defaultdict(<class 'int'>, {frozenset({'o', 'd', 'g'}): 2, frozenset({'y', 'n', 'r', 'a'}): 1,
    # frozenset({'a', 'b', 'c'}): 2})

    count_pairs = 0
    for value in frozenset_count.values():
        print(f'values: {value}')
        if value > 1:
            count_pairs += value * (value - 1) // 2
            print(f'count_pairs: {count_pairs}')
    return count_pairs


if __name__ == '__main__':
    # line = input()
    # arr = line.strip().split()
    arr = ["good", "god", "yarn", "bac", "aabc"]
    output = solution(arr)
    print(output)

# TODO : Turing 2:
"""
Given an array of 'N' integers, the cost of a range (subarray) is defined as the 
sum of the values in the range squared. That is, if the sum of the values of the range is S, its cost is S?.
Your task is to determine the largest cost of any contiguous subarray within the given array.

Examples 1:
Input: arr = [1, -1, 1, -1, 1]
Output: 1
Explanation: The maximum sum is 1, and its square is 1
Examples 2:
Input: arr = [1, 2, 3]
Output: 36
Explanation: The sum of the entire array is 6, and its square is 36
Constraints:
• The integers in the array 'arr[i]' can be positive, negative, or zero.
• 0 >= arr.length <= 10^5
"""

from typing import List


def squared_sum(arr: List[int]) -> int:
    if not arr:
        return 0

    max_squared_sum = 0  # Initialize max_squared_sum to 0
    current_sum = 0

    for num in arr:
        current_sum = max(num, current_sum + num)
        max_squared_sum = max(max_squared_sum, current_sum ** 2)

    return max_squared_sum


# Example usage:
if __name__ == "__main__":
    # line = input()
    # arr = [int(i) for i in line.strip().split()]
    # print(squared_sum(arr))
    arr = [1, -1, 1, -1, 1]
    print(squared_sum(arr))  # Output: 1

    arr = [1, 2, 3]
    print(squared_sum(arr))  # Output: 36

# TODO Turing 3: Given a string s and an integer k, return the maximum number of vowel letters in any substring
#  of s with length k. Vowel letters in English are 'a','e', 'i', 'o','u'.

"""
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters.
# 1 <= k <= s.length
"""

def max_vowels(s: str, k: int) -> int:
    """ function to calculate above ques"""
    vow_list = ['a', 'e', 'i', 'o', 'u']
    word_len = len(s) + 1
    count_list = list()

    st = 0
    # a = s[st:k]
    while k <= word_len:
        count = 0
        for word in s[st:k]:
            if word in vow_list:
                count += 1
                # print(count)
        count_list.append(count)
        st = k
        k += k
        # a = s[st:k]
    # print(count_list)
    return max(count_list)


a = "aeiou"
p = 2

print(max_vowels(a, p))

# TODO Turing 4: Given an integer array nums, return an array answer such that answer[i] is equal to
#  the product of all the elements of nums except nums[i].The product of any prefix or suffix of nums is guaranteed
#  to fit in a 32-bit integer.You must write an algorithm that runs in O(n) time and
#  without using the division operation. # Follow up: Can you solve the problem in O(1) extra space complexity?
#  (The output array does not count as extra space for space complexity analysis.)

"""
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""

# Approach: 1
import copy

# my_list = [1, 2, 3, 4]
my_list = [-1, 1, 0, -3, 3]
# l = [1, 2, 3, 4]

mul = 1
final_list = []
for i in my_list:
    l = copy.deepcopy(my_list)
    # print(f'l: {l}')
    l.pop(my_list.index(i))
    # print(f'After pop list: {l}')
    mul = 1
    for num in l:
        mul *= num
    # print(f'mul: {mul}')
    final_list.append(mul)

print(final_list)

# # Approach 2: (Handling the time complexity conditions.)

from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)

    # Initialize arrays to store left and right products
    left_products = [1] * n  # [1, 1, 1, 1]
    right_products = [1] * n

    # Calculate left_products
    for i in range(1, n):
        left_products[i] = left_products[i - 1] * nums[i - 1]

    # Calculate right_products
    for i in range(n - 2, -1, -1):
        right_products[i] = right_products[i + 1] * nums[i + 1]

    # Calculate the final answer array
    # [1, 1, 2, 6] (left_products) | [24, 12, 4, 1] (right_products)
    answer = [left_products[i] * right_products[i] for i in range(n)]

    return answer


# Example usage:
num_list = [1, 2, 3, 4]

# print(product_except_self(num_list))  # Output: [24, 12, 8, 6]
