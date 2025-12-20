# long way
even_numbers = []

for num in range(21):
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)

# list comprehension way
even_numbers2 = [num for num in range(21) if num % 2 == 0]
print(even_numbers2)

# using list comprehensions to create list of tuples
numbers = [1, 2, 3, 4, 5]
result = [(num, "Even") if num % 2 == 0 else (num, "Odd") for num in numbers]
print(result)

# using filter()
words = ["tree", "sky", "mountain", "river", "cloud", "sun"]


def is_long_word(word):
    return len(word) > 4


long_words = list(filter(is_long_word, words))
print(long_words)

# map()
celsius = [0, 10, 20, 30, 40]


def to_fahrenheit(temp):
    return (temp * 9 / 5) + 32


fahrenheit = list(map(to_fahrenheit, celsius))
print(fahrenheit)
