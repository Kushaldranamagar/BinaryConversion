
def bin_validation(num):
    if num == "":
        print("Empty Field Found!! Please enter the valid octal number")
        print()
        return True
    try:
        check = int(num)
        if 0 > check or check > 11111111:
            print("No negative values. Please enter positive octal number")
            print()
            return True

        while check > 0:
            r = check % 10
            if r not in [0, 1]:
                print("Invalid Digit found!! Please Enter Number Having Digits 0 And 1")
                print()
                return True
            check = int(check / 10)
        return False

    except:
        print("Special character or alphabets found! Please enter number having digits only 0 to 7")
        print()
        return True


def deci_validation(num):
    if num == "":
        print("Empty Field Found!! Please enter the valid  number")
        print()
        return True
    try:
        check = int(num)
        if 0 > check or check > 255:
            print("No negative values. Please enter positive  number")
            print()
            return True
        while check > 0:
            r = check % 10
            if r not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                print("Invalid Digit Found!! Please Enter Number Between 0 and 255")
                print()
                return True
            check = int(check / 10)
        return False

    except:
        print("Special character or alphabets are found! Please enter number having digits only 0 to 7")
        print()
        return True
