# old way
def square(num):
    return num**2


print(square(4))

# lambda function
numbers = [1, 2, 3, 4, 5]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
