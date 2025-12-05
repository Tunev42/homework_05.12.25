def even_odd_generator(n):
    for i in range(n + 1):
        yield "четное" if i % 2 == 0 else "нечетное"
gen1 = even_odd_generator(5)
print("1. Генератор четных/нечетных чисел:")
print(list(gen1))

fizzbuzz_list = ["FizzBuzz" if i % 15 == 0 else"Fizz" if i % 3 == 0 else"Buzz" if i % 5 == 0 else i for i in range(1, 101)]
print(fizzbuzz_list[:20])

numbers = [5, 12, 8, 15, 3, 20]
gen3 = (num if num > 10 else 0 for num in numbers)

print(list(gen3))

n = 10
even_odd_dict = {i: "even" if i % 2 == 0 else "odd" for i in range(1, n + 1)}

print(even_odd_dict)


strings = ["hello", "world", "python", "generator", "test", "example"]
def string_length_generator(strings_list):
    for s in strings_list:
        yield len(s) if len(s) <= 5 else 5

gen5 = string_length_generator(strings)

print(list(gen5))


numbers2 = [1, -2, 3, -4, 5, -6, 7]
positive_list = [num if num > 0 else 0 for num in numbers2]


print(positive_list)


import math
numbers3 = [4, -9, 16, -1, 25]
gen7 = (math.sqrt(num) if num > 0 else 0 for num in numbers3)


print(list(gen7))


numbers4 = [1, 2, 3, 4, 5, 6]
power_list = [num ** 2 if num % 2 == 0 else num ** 3 for num in numbers4]


print(power_list)


def number_category_generator(numbers_list):
    for num in numbers_list:
        yield "High" if num > 50 else "Medium" if 20 <= num <= 50 else "Low"

numbers5 = [10, 25, 60, 15, 30, 5, 100]
gen9 = number_category_generator(numbers5)


print(list(gen9))