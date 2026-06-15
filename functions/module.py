def sum_data(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        total = 0
        for number in numbers:
            total += number
        return total