def AND(a, b):
    return a & b

def OR(a, b):
    return a | b

def NOT(a):
    return 1 - a

def NAND(a, b):
    return NOT(AND(a,b))

def NOR(a,b):
    return NOT(OR(a,b))

def XOR(a,b):
    return a ^ b


print("AND Gate")
print(AND(1,1))

print("OR Gate")
print(OR(1,0))

print("NOT Gate")
print(NOT(1))

print("NAND Gate")
print(NAND(1,1))

print("NOR Gate")
print(NOR(0,0))

print("XOR Gate")
print(XOR(1,0))