num = 178871
first_half = int(str(num)[:3])
second_half = int(str(num)[3:])
if sum(int(digit) for digit in str(first_half)) == sum(int(digit) for digit in str(second_half)):
    print("Счастливый билет")
else:
    print("Несчастливый билет")