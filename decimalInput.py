from validation import *
from adder import *
from conversion import *


def no_of_input_1():
    p = input("Enter the decimal number     : ")
    if deci_validation(p):
        return no_of_input_1()
    else:
        return p


def no_of_input_2():
    q = input("Enter another decimal number : ")
    if deci_validation(q):
        return no_of_input_2()
    else:
        return q


def deci_to_deci():
    p = int(no_of_input_1())
    q = int(no_of_input_2())
    sum_decimal = p + q
    r = int(sum_decimal)
    if int(r) > 255:
        print("Please input value less than 255 and greater than zero")
        print()
        return deci_to_deci()

    s = deci_to_Bin_Conversion(p)
    t = deci_to_Bin_Conversion(q)
    u = adder(s, t)

    return p, q, r, s, t, u


def dfinal_output():
    p, q, r, s, t, u = deci_to_deci()
    print("\nThe value is inserted successfully.\n")
    print("\n---------------------FINAL CONVERSION-----------------------\n")
    print("------------------------DECIMAL OUTPUT-----------------------------BINARY OUTPUT-----------------")
    print("                            " + str(p) + "                                       " + str(s) + "   ")
    print("+                           +" + str(q) + "                                       " + str(t) + "   ")
    print("                     ====================                        ====================            ")
    print("+                          " + str(r) + "                                       " + str(u) + "   ")
    print("\n")
