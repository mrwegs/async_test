# from inspect import getgeneratorstate
#
#
# def is_palindrome(num):
#     # Пропуск чисел с одним разрядом
#     if num // 10 == 0:
#         return False
#     temp = num
#     reversed_num = 0
#
#     while temp != 0:
#         reversed_num = (reversed_num * 10) + (temp % 10)
#         temp = temp // 10
#
#     if num == reversed_num:
#         return True
#     else:
#         return False
#
#
# def infinite_palindromes():
#     num = 100
#     while True:
#         if is_palindrome(num):
#             i = yield num
#             print(f'Печатаю число, полученное из внешней функции: {i}')
#             if i == 'stop':
#                 raise StopIteration
#             if i is not None:
#                 num = i
#         num += 1
#
#
# pal_gen = infinite_palindromes()
# for i in pal_gen:
#     print(f'Печатаю число, полученное из генератора: {i}')
#     if i > 100_000:
#         pal_gen.send('stop')
#     digits = len(str(i))
#     pal_gen.send(10 ** digits)
#


def average():
    count = 0
    summ = 0
    average = None

    while True:
        number = yield average
        count += 1
        summ += number
        average = round(summ / count)

