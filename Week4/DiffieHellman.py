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

def find_all_primitive_roots(p):
    primitive_roots = []
    for g in range(1, p):
        powers = set()
        for i in range(1, p):
            powers.add(pow(g, i, p))
        if len(powers) == p - 1:
            primitive_roots.append(g)
    return primitive_roots

print(find_all_primitive_roots(p))

# B = 2920
# def find_shared_secret(B):
