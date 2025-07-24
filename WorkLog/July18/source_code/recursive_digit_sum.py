def superDigit(n, k):
    def digit_sum(num):
        return sum(int(i) for i in num)

    intial = digit_sum(n) * k
    while intial >= 10:
        intial = digit_sum(str(intial))
    return intial
