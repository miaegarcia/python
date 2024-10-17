def computePower(x, y):
    result = 1
    for i in range(y):
        result = result * x
    return result

print(computePower(2, 3))


def temperatureRange(readings):
    min_value = readings[0]
    max_value = readings[0]
    for number in readings:
        if number < min_value:
            min_value = number
        if number > max_value:
            max_value = number
    return (min_value, max_value)

print(temperatureRange([15, 14, 17, 20, 23, 28, 20]))


def isWeekend(day):
    if day == 6 or day == 7:
        return True
    else:
        return False

print(isWeekend(6))


def fuel_efficiency(distance, fuel):
    efficiency = distance / fuel
    return efficiency

print (fuel_efficiency(70, 21.5))



def decodeNumbers(n):
    last_digit = n % 10
    rest_of_number = n // 10

    multiplier = 1
    while rest_of_number > 0:
        rest_of_number = rest_of_number // 10
        multiplier = multiplier * 10
    return last_digit * multiplier + (n // 10)

print(decodeNumbers(12345))


def find_min_with_for_loops(nums):
    min_num = nums[0] 
    for num in nums:
        if num < min_num:
            min_num = num
    return min_num

print(find_min_with_for_loops([2024, 98, 131, 2, 3, 72]))

def find_min_with_while_loops(nums):
    i = 0
    min_num = nums[0]

    while i < len(nums):
        if nums[i] < min_num:
            min_num = nums[i]
        i = i + 1
    return min_num

print(find_min_with_while_loops([2024, 98, 131, 2, 3, 72]))


def vowel_and_consonant_count(text):
    vowels = "AEIOUaeiou"
    vowel_count  = 0
    consonant_count = 0
    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
        else:
            consonant_count += 1
    return (vowel_count, consonant_count)

print(vowel_and_consonant_count("UC Berkeley, founded in 1868!"))


def digital_root(num):
    sum_of_digits = 0
    while num > 0:
        sum_of_digits += num % 10
        num = num // 10
    return sum_of_digits

print(digital_root(2468))
