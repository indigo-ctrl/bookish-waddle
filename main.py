import random

numbers = [random.randint(1, 100) for _ in range(10)]
print(numbers)

sum_numbers = sum(numbers)
print(sum_numbers)

max_number = max(numbers)
min_number = min(numbers)
print(max_number, min_number)

sorted_asc = sorted(numbers)
print(sorted_asc)

sorted_desc = sorted(numbers, reverse=True)
print(sorted_desc)

squares = [x ** 2 for x in numbers]
print(squares)

filtered_numbers = [x for x in numbers if x % 2 != 0]
print(filtered_numbers)
