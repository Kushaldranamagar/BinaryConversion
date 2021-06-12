def BinToDeci(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal * 2 + int(digit)
    return decimal


def deci_to_Bin_Conversion(num):
    bnr = bin(num).replace('0b', '')
    x = bnr[::-1]  # this reverses an array
    while len(x) < 8:
        x += '  0'
    bnr = x[::-1]
    return bnr


def binToBin_Conversion(number):
    flag = True
    a_ = 8 - len(number)
    reminder = number.zfill(a_ + len(number))  # zfill Adds 0's At the beginning Of The String.
    number = str(reminder)
    return number
