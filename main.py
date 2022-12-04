print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote

first_name = 'John'
last_name = 'Smith'
message = first_name + ' [' + first_name[0] + '] is a coder'
lalala = '%s [%s] is a coder' % (first_name, first_name[0])
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)
a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')
# string的几种表示方式
# 1. 单双引号 + 直接带入
# 2. %s等代替，放入单双引号中
# 3.     .format()方法, 用{}代替
# # 4. f-string, 用f''代替，用{}代替
# language = 'Python'
# a,b,c,d,e,f,g = language # unpacking sequence characters into variables
# print(a) # P
# print(b) # y
# print(c) # t
# print(d) # h
# print(e) # o
# print(f) # n
# print(g) # error

# list slicing
language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) #Pyt
last_three = language[3:6]  # 3,4,5
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon
first_three = language[:-3]

greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH , reverse the string

language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto

# capitalize(): Converts (转换) the first character of the string (字符串) to capital letter
my_test_string = 'python is easy to learn'
print(my_test_string.capitalize()) # Python is easy to learn

# casefold(): Converts string into lower case
my_test_string = 'PYTHON IS EASY TO LEARN'
print(my_test_string.casefold()) # python is easy to learn

#count(): Returns the number of times a specified value occurs in a string
challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1,
print(challenge.count('th')) # 2`

#endswith(): Returns true if the string ends with the specified value
challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False

#expandtabs(): Sets the tab size of the string
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'
print(challenge.expandtabs(8))  # 'thirty  days    of      python'

#find(): Searches the string for a specified value and returns the position of where it was found
#find()方法和index()方法的区别在于，如果找不到，find()返回-1，而index()会报错,if not found, find() returns -1, while index() raises an exception
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0

#rfind(): Searches the string for a specified value and returns the last position of where it was found
#find return the first position of where it was found, rfind return the last position of where it was found
challenge = 'thirty days of python'
print(challenge.rfind('y'))  # 16
print(challenge.rfind('th')) # 17

#isalum(): Returns True if all characters in the string are alphanumeric
challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False, space is not an alphanumeric character

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False, space is not an alphanumeric character

#join(): Joins the elements of an iterable to the end of the string
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'

#strip(): Returns a trimmed version of the string
challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth')) # 'irty days of py'

#split(): Splits the string at the specified separator, and returns a list
challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']
print(type(challenge.split(', '))) # <class 'list'>