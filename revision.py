# first_name = "Tony"
# last_name = "Stark"
#
# print(first_name + " " +  last_name)

# age = int(input("Enter your age: "))
#
# if age > 0:
#     new_age = int(age) + 2
#     print(new_age)
# else:
#     print("Age can't be negative")

# numbers = []
#
# for i in range(0,10):
#     numbers.append(i)
#
# print(numbers)

# subjects = ["English", "Maths", "Physics", "Chemistry", "Computer Science"]
# subject_marks = []
#
# for subject in subjects:
#     mark = int(input(f"Enter {subject} marks: "))
#     subject_marks.append(mark)
#
# Total = sum(subject_marks)
#
# percentage = Total/len(subject_marks)
# print(f"The subject marks are {subject_marks}")
# print(f"congrats!! You have scored {percentage} percentage.")

# Two Sum problem

# def find_unique_pairs(nums, target):
#     seen = set()
#     output = set()
#
#     for num in nums:
#         complement = target - num
#         if complement in seen:
#             output.add(tuple(sorted((complement, num))))
#         seen.add(num)
#
#     return list (output)
#
# nums = [1, 2, 8,  3, 4, 5, 6, 7, 8, 2, 9, 10]
# target = 10
# print(find_unique_pairs(nums, target))

# Checking for a palindrome

# def is_Palindrome (s):
#     left, right = 0, len(s)-1
#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1
#     return True
#
# word = input("Enter a word: ")
#
# if is_Palindrome(word):
#     print("Yes, it is a Palindrome")
# else:
#     print("No, it is not a Palindrome")

# def is_Palindrome(s):
#     return s == s[::-1]
#
# word = input("Enter a word: ")
# print(is_Palindrome(word))
#
# if is_Palindrome(word):
#     print("It is a Palindrome")
# else:
#     print("It is not a Palindrome")

x = 10
for i in range(10):
    print("*")