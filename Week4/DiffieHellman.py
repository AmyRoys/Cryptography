p = 3083 #public modulus
g = 5

def find_primitive_root(p,g):
    powers = set()
    for i in range(1, p):
        powers.add(pow(g, i, p))
    if len(powers) == p - 1:
        return True
    return False

print(find_primitive_root(p,g))

