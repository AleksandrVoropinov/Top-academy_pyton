# import random
#
# exceptions = [ValueError, TypeError, SyntaxError, OSError, ZeroDivisionError]
#
# summa = 0
#
# while summa < 666:
#     summa += int(input('Введите число: '))
#     if random.randint(1, 13) == 1:
#         raise random.choice(exceptions)
#     print('ok')

###############################################################################

# string = 'fgdhqwehrtupot'
#
# h1 = string.index('h')
# h2 = string.rindex('h')
# print(string[h1 + 1:h2][::-1])

# string = 'fgdhqwehrtupot'
#
# start = -1
# end = -1
#
# for i in range(len(string)):
#     if string[i] == 'h':
#         start = i
#         break
#     print(start)
# for i in range(len(string) - 1, 0, -1):
#     if string[i] == 'h':
#         end = i
#         break
#     print(string[start + 1:end][::-1])

###############################################################################

# nums = [1, 7, 3, 6, 5, 6]
# nums = [1, 2, 3]
# nums = [2, 1, -1]
# pivot = -1
#
# for i in range(len(nums)):
#     if sum(nums[:i]) == sum(nums[i + 1:]):
#         pivot = i
#         break
# print(pivot)

# nums = [1, 7, 3, 6, 5, 6]
#
# pivot = -1
#
# for i in range(len(nums)):
#     if len(nums[:i]) == len(nums[i + 1:]):
#         pivot = i
#         break
# print(pivot)

###############################################################################

# import re

# text = 'milk how dogs phyton'

# match = re.search(r'\w{4}', text)  # Поиск первого вхождения
# print(match.group())

# matches = re.findall(r'\b\w{4,}\b', text)  # \b граница слова в данном случае {4}
# print(matches)

###############################################################################

# import re
#
# text = '1234 124 748 78 5 147'
#
# match = re.findall(r'\b\d{3}\b', text)
# print(match)

###############################################################################

# import re
#
# dates = '10.12.2001 15/01/2004 14.02.14 18-05-2024'
#
# match = re.findall(r'\d\d\.\d\d\.\d\d\d\d', dates)  # \d{2}\.\d{2}\.\d{4}
# match_sub = re.sub(r'\d{2}/\d{2}/\d{4}', r'dd.mm.yyyy', dates)
# print(match)
# print(match_sub)

###############################################################################

# import re
#
# text = 'Ivan, Bob; Maria, Petr'
#
# names = re.split(r'[,;]', ''.join(text.split()))
# print(names)

###############################################################################

# import re
#
# tels = '+79999999998 +7 (999)9999998 +7 (999)-999-9998 +7 (999)-99-999-78'
#
# correct_num = re.findall(r'\+7 \(\d{3}\)-\d{2}-\d{3}-\d{2}', tels)  # \s можно ставить вместо пробелов если они есть в строке
# print(correct_num)

###############################################################################

# import re
#
# emails = 'tetsmail.ru test@mail.ru test123@mail.com test@mail!ru'
#
# correct_mails = re.findall(r'\w+@\w{2,20}\.[a-z0-6]{2,3}', emails)
# print(correct_mails)

###############################################################################

# import re
#
# text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys '\
#        'standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to ' \
#        'make a type specimen book. It has survived not only five centuries, ' \
#        'but also the leap into electronic typesetting,'
#
#  correct_text = re.findall(r'\b\w{4}\b', text)
#  print(correct_text)
# correct_text = re.findall(r',', text)
# print(correct_text)

###############################################################################

# import re
#
# text = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'
#
# number_1 = re.findall(r'[А,В,Е,К,М,Н,О,Р,С,Т,У,Х]\d{3}\w{2}\d{2,3}', text)
# number_2 = re.findall(r'[А,В,Е,К,М,Н,О,Р,С,Т,У,Х]\w{2}\d{3}\d{2,3}', text)
# print(number_1)
# print(number_2)

###############################################################################

# import requests
#
# url = 'http://www.columbia.edu/~fdc/sample.html'
# response = requests.get(url)
#
# text = response.text
# print(response.status_code)
# headings = re.findall(r'<h3 id="\w*">(.*)</h3>', text)
# print(headings)

###############################################################################

# text = '4567'
#
# if re.match(r'\d{4}', text):
#     print('ok')
# print(re.match(r'\d{4}', text))

# import math

# from math import sin, cos, tan
# print(dir(math))  # Показывает все методы в библиотеке math
# value = '__main__'
# print(__name__ == value)
# print(dir(__name__))

###############################################################################
