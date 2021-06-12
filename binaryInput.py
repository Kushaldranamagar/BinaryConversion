from validation import *
from adder import *
from conversion import *


def no_of_input_1():
    p = input("Enter the binary number: ")
    if bin_validation(p):
        return no_of_input_1()
    else:
        print()
        return p


def no_of_input_2():
    q = input("Enter another binary number: ")
    if bin_validation(q):
        return no_of_input_2()
    else:
        print()
        return q


def bin_to_bin():
    p = no_of_input_1()
    q = no_of_input_2()

    r = binToBin_Conversion(p)
    s = binToBin_Conversion(q)
    t = adder(r, s)

    u = BinToDeci(p)
    v = BinToDeci(q)
    sum_ = u + v
    w = int(sum_)
    if int(w) > 255:
        print("Please enter values whose total value is less than 11111111 and greater than zero")
        print()
        return bin_to_bin()

    return r, s, t, u, v, w


def bfinal_output():
    r, s, t, u, v, w = bin_to_bin()
    print("\nThe value is inserted successfully.\n")
    print("\n-------------------------------------------FINAL CONVERSION-----------------------------------\n")
    print("------------------------DECIMAL OUTPUT-----------------------------BINARY OUTPUT-----------------")
    print("                            " + str(u) + "                                       " + str(r) + "   ")
    print("+                          +" + str(v) + "                                       " + str(s) + "   ")
    print("                     ====================                        ====================            ")
    print("+                          " + str(w) + "                                       " + str(t) + "   ")
    print("\n")
