a1 = 11
b1 = 1
a2 = 1010
b2 = 1011

def add_binary(a, b):
    """
    return bin(int(a,2) + int(b, 2))[2:]
    """
    """
    a_bin = int(a,2)
    b_bin = int(b,2)
    
    bin_res = bin(a_bin + b_bin)
    return bin_res[2:]
    """

print(add_binary(a1, b1))
print(add_binary(a2, b2))