def sum_digits(num):
    sum_digit = 0; temp = num
    while (temp>0):
        digit = temp % 10  # grab last digit
        sum_digit += digit # add digit to the sum        
        temp //= 10 # // 10 to strip a digit
    return sum_digit

digits = int(input("Please input a 4-digit number:"))
if (digits<1000 or digits>9999):
    print("Only positive number is supported.")    
else:
    sum_of_digit = sum_digits(digits)
    print(f'Digit sum of "{digits}"={sum_of_digit}.')
