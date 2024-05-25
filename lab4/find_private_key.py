import math
import sys

sys.setrecursionlimit(4000)


def egcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = egcd(b, a % b)
        return gcd, y, x - (a // b) * y
    

def find_pq(e_a, d_a, n):
    # krok 1
    k_phi = e_a * d_a - 1
    t = k_phi
    
    # krok 2 
    while t % 2 == 0:
        t = t//2
    
    # krok 3
    a = 2
    while a < math.inf:
        k  = t
        while k < k_phi:
            x = pow(a,k,n)
            
            if x != 1 and x != n-1 and (x**2) %n == 1:
                p = math.gcd(x - 1, n)
                q = n // p
                return p, q
            k = k*2
        
        a +=2


def find_private(e_a, d_a, e_b, n):
    p, q = find_pq(e_a, d_a, n)
    phi_n = (p-1)*(q-1)
    x_b = egcd(e_b, phi_n)[1]
    d_b = x_b % phi_n
    return d_b
    
    
def main():
    # if input path was given
    if len(sys.argv) == 3:
        path_a = sys.argv[1]
        path_b = sys.argv[2]
        lines = []
        with open(path_a) as f:
            lines = f.read().splitlines()
            e_a = int(lines[0])
            n = int(lines[1])
            d_a = int(lines[2])
            
        with open(path_b) as f:
            lines = f.read().splitlines()
            e_b = int(lines[0])
            n = int(lines[1])
            d_b = int(lines[2])
            
            result = find_private(e_a, d_a, e_b, n)
            print(result)
        return
    
    elif len(sys.argv) == 5:
        # klucze a należą do nas
        # klucze b należą do ofiary
        e_a = int(sys.argv[1])
        d_a = int(sys.argv[2])
        e_b = int(sys.argv[3])
        n = int(sys.argv[4])
        
        result = find_private(e_a, d_a, e_b, n)
        print(result)
        return
    
    else:
        print("required arguments: e_a, d_a, e_b, n")
        return
    
 
if __name__ == "__main__":
    main()