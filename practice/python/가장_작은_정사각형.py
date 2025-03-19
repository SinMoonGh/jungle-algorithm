
def make_gcd(x: int, k: int):
    if k  == 0:
        return x
    else:
        return make_gcd(k, x%k)


print(make_gcd(8, 22))