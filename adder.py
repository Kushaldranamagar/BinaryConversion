from gates import *

def adder(b1,b2):
    carry = 0
    c= ["0","0","0","0","0","0","0","0"]
    for i in range(len(b1)-1,-1,-1):
        bit1 = int(b1[i])
        bit2 = int(b2[i])

        #for sum
        xor1 = xor_gate(bit1,bit2)
        nand1 = nand_gate(xor1,carry)
        or1 = or_gate(xor1,carry)
        sum1_ = and_gate(or1, nand1)
        c[i] = str(sum1_)

        #for carry
        and1 = and_gate(bit1,bit2)
        and2 = and_gate(xor1,carry)
        nor1 = nor_gate(and1,and2)
        carry = not_gate(nor1)
    return "".join(c)


