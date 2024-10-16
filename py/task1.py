def sum_two_smallest_numbers(numbers):
    if len(numbers) >= 4:
        print(numbers)
        a = min(numbers)
        numbers.remove(a)
        b = min(numbers)
        print(a, b)
        return a+b

print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))

# z.append(a)
# z.append(b)
# return sum(z)