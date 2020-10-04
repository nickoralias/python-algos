def karatsuba(x, y):
    x , y = str(x), str(y)
    maxlen = max(len(x), len(y))
    n = maxlen if (maxlen % 2 == 0) else maxlen + 1 # ensure each string is divisible by 2
    x = x.zfill(n)
    y = y.zfill(n)

    a = x[:len(x)//2]
    b = x[len(x)//2:]
    c = y[:len(y)//2]
    d = y[len(y)//2:]

    ac = int(a)*int(c) if ((len(a) == 1) and (len(c) == 1)) else karatsuba(int(a), int(c))
    bd = int(b)*int(d) if ((len(b) == 1) and (len(d) == 1)) else karatsuba(int(b), int(d))
    a_plus_b = int(a) + int(b)
    c_plus_d = int(c) + int(d)
    ad_plus_bc = (a_plus_b * c_plus_d - ac - bd) if ((len(str(a_plus_b)) == 1) and (len(str(c_plus_d)) == 1)) else karatsuba(a_plus_b, c_plus_d) - ac - bd


    return((10**n)*int(ac) + (10**(n//2))*(ad_plus_bc) + int(bd))

def main():
    print(karatsuba(5678, 1234))
    print(karatsuba(123, 45))
    print(karatsuba(12, 345))

if __name__ == '__main__':
    main()
