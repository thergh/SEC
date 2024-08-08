import sys
from collections import Counter
import math
import ast

def KSA(K):
    n = len(K)
    j = 0
    # tablica T - 256 elementow (powtarzane bajty klucza)
    T = [K[i%n] for i in range(256)]
    # S na tablica postaci S[0]=0, S[1]=1, ..., S[255]=255
    S = list(range(256))
    # generuj permutacje tablicy S na podstawie klucza
    for i in range(256):
        j = (j + S[i] + T[i]) % 256
        S[i], S[j] = S[j], S[i] #zamien S[i] z S[j]
    return S


def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        yield K


def RC4(key, data):
    S = KSA([ord(c) for c in key])
    keystream = PRGA(S)
    return bytes([c ^ next(keystream) for c in data])


def main():
    # message
    # input output
    if len(sys.argv) == 3:
        cypher_path = sys.argv[1]
        key_path = sys.argv[2]
        
        with open(cypher_path) as f:
            cypher = ast.literal_eval(f.read().strip())
            f.close()
            
        with open(key_path) as f:
            key = str(f.read())
            f.close()
        
        decrypted = RC4(key, cypher)
        
        output = open("decoded.txt", 'w')
        output.write(str(decrypted))
        output.close()
        print(decrypted)
        
    return


if __name__ == "__main__":
    main()
    
    
# usage:
# python3 rc4_decode.py cyphertext.txt key.txt