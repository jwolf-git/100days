# new_list = [1, 2, 3]
# new_new_list = [n+1 for n in new_list]
#
# print(new_new_list)
#
# name = "Angela"
# name_list = [letter for letter in name]
# print(name_list)
# test_list = [num*2 for num in range(1,5)]
# print(test_list)
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# upper_names = [name.upper() for name in names if len(name) > 5]
# print(upper_names)
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# new_numbers = [n*n for n in numbers]
# print(new_numbers)
# list_of_strings = input().split(',')
#
# numbers = [int(num) for num in list_of_strings]
# result = [num for num in numbers if num % 2 == 0]
# print(result)

# with open("file.txt") as file1:
#     list1 = file1.readlines()
#
# with open("file2.txt") as file2:
#     list2 = file2.readlines()
#
# result = [int(num) for num in list1 if num in list2]
#
# print(result)

# dictionary format: new_dict ={new_key:new_value for item in list}
# import random
#
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
#
# students_scores = {student:random.randint(1, 100) for student in names}
# print(students_scores)
#
# passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
#
# print(passed_students)
# result = {key:value for (key, value) in dictionary.items() if test}
# sentence = input()
# result = {word:len(word) for word in sentence.split()}
#
#
# print(result)
# weather_c = eval(input())
#
# weather_f = {day: temp * 9 / 5 + 32 for (day, temp) in weather_c.items()}
#
# print(weather_f)
