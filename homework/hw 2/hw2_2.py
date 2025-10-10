RandomNumbers = [18, 59, 35, 1, 47, 35, 22, 27, 38, 50, 98, 99, 31, 19, 37, 93, 78, 91, 31, 79]

even_count = sum(1 for num in RandomNumbers if num % 2 == 0)

print('Number of even numbers: ', even_count)