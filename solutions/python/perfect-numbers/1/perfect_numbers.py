def classify(number):
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    if number == 1:
        return "deficient"
    factors = [1]
    for i in range(2, int(number ** 0.5) + 1):  # loops from 2 to the sqrt of the number
        if number % i == 0:
            factors.append(i)
            factors.append(number // i) #gives you int instead of a float
    perf_num = sum(set(factors))
    if perf_num == number:
        return "perfect"
    if perf_num > number:
        return "abundant"
    return "deficient"
    