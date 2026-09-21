def is_armstrong_number(number):
    n = len(str(number))
    original_number = number
    armstrong = 0
    while number > 0:
        armstrong += (number % 10) ** n
        number = number // 10

    return armstrong == original_number