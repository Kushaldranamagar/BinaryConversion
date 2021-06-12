def or_gate(b1,b2):
    return b1|b2


def and_gate(b1,b2):
    return b1&b2


def xor_gate(b1,b2):
    return b1^b2


def not_gate(b1):
    return (~b1)+2


def nand_gate(b1,b2):
    return not_gate(and_gate(b1,b2))


def nor_gate(b1,b2):
    return not_gate(or_gate(b1,b2))
