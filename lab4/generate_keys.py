import random
import sys
import math
import sympy


sys.setrecursionlimit(4000)


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True



def egcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = egcd(b, a % b)
        return gcd, y, x - (a // b) * y
    

def generate_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    # primes_list = sieve(int(phi / 10))
    # e = primes_list[random.randrange(len(primes_list))]
    
    # e = prime_candidate(random.randrange(phi // 10, phi // 2))
    
    # e = prime_in_range(phi // 10, phi // 2)
    e = sympy.randprime(phi // 10, phi // 2)
    
    
    gcd, x, y = egcd(e, phi)

    if gcd != 1:
        raise ValueError("Exponent is not co-prime with phi")
    
    d = x % phi
    
    public_key = (e, n)
    private_key = (d, n)
    
    return public_key, private_key


def main():
    # p = 7919
    # q = 7907
    binary_size = int(sys.argv[1])
    decimal_max = pow(2, binary_size - 1)
    
    p = sympy.randprime(decimal_max // 2, decimal_max)
    q = sympy.randprime(decimal_max // 2, decimal_max)
    
    # asserting that p != q
    while p == q:
        p = sympy.randprime(decimal_max // 2, decimal_max)
        q = sympy.randprime(decimal_max // 2, decimal_max)
    
    k1 = generate_keys(p, q)
    k2 = generate_keys(p, q)
    
    # printing results to files
    path_a = "./key_a.txt"
    path_b = "./key_b.txt"
    f = open(path_a, 'w')
    f.write(str(k1[0][0]))
    f.write("\n")
    f.write(str(k1[0][1]))
    f.write("\n")
    f.write(str(k1[1][0]))
    f.write("\n")
    f.write(str(k1[1][1]))
    f.close()
    
    f = open(path_b, 'w')
    f.write(str(k2[0][0]))
    f.write("\n")
    f.write(str(k2[0][1]))
    f.write("\n")
    f.write(str(k2[1][0]))
    f.write("\n")
    f.write(str(k2[1][1]))
    f.close()
        
       
    print(str(k1[0][0])) 
    print("((public), (private)) == ((e, n), (d, n))")
    print(k1)
    print(k2)



# give size in bits as argument
# ((public), (private)) == ((e, n, d, n))
if __name__ == "__main__":
    main()
