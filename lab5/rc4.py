import sys
from collections import Counter
import math

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


def xor_bytes(byte_seq1, byte_seq2):
    return bytes(a ^ b for a, b in zip(byte_seq1, byte_seq2))



def calculate_entropy(data: bytes) -> float:
    if not data:
        return 0.0

    # Count the frequency of each byte in the data
    byte_count = Counter(data)

    # Calculate the probability of each byte
    total_bytes = len(data)
    probabilities = [count / total_bytes for count in byte_count.values()]

    # Calculate the entropy
    entropy = -sum(p * math.log2(p) for p in probabilities)

    return entropy



k1 = "SecretKey"
k2 = "gibberishewdsfxz"

plain1 = b"aaaHello, World!"
plain2 = b"aaaGoodbye, World!"


ca1 = RC4(k1, plain1)
cb1 = RC4(k1, plain2)
ca2 = RC4(k2, plain1)

print("Ciphertext 1:", ca1)
print("Ciphertext 2:", ca2)

da1 = RC4(k1, ca1)
db1 = RC4(k1, cb1)


print("Decrypted: 1", da1)
print("Decrypted: 2", db1)

x1 = xor_bytes(ca1, cb1)
x2 = xor_bytes(cb1, ca2)
print("xored: 1, 2: ", x1)
print("entropy: ", calculate_entropy(x1))
print("xored: 2, 3: ", x2)
print("entropy: ", calculate_entropy(x2))

