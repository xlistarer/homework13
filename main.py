'''
Задание 1

Напишите программу Python для определения количества локальных переменных, объявленных в функции.




Задача 2

Напишите программу Python для доступа к функции внутри функции (советы: используйте функцию, которая возвращает другую функцию)


Задача 3

Напишите функцию под названием `choose_func`, которая принимает список из числа и 2 функции обратного вызова. Если все числа внутри списка положительные, выполнить первую функцию в этом списке и вернуть ее результат. В противном случае вернуть результат второго
'''
def first():
    a= 1
    b= 6747
    str1="dbuineml"
    gh='jjjj'
    print(first.__code__.co_nlocals)


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]
def choose_func(nums: list, func1, func2):
    for i in nums:
        if i<0:
            return func2(nums)
    return func1(nums)
def second(func1,num):
    if func1(num)>3:
        return func1
def num_plus3(num):
    return num+3
if __name__ == '__main__':
    first()
    # Assertions
    print(list(map(second(num_plus3,5),[8,9,8,7])))
    nums1 = [1, 2, 3, 4, 5]

    nums2 = [1, -2, 3, -4, 5]




    assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]

    assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]





