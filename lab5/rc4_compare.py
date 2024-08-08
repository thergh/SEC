from collections import Counter
import math
import sys
import ast

def xor_bytes(byte_seq1, byte_seq2):
    return bytes(a ^ b for a, b in zip(byte_seq1, byte_seq2))


def calculate_entropy(data: bytes) -> float:
    if not data:
        return 0.0

    byte_count = Counter(data)

    total_bytes = len(data)
    probabilities = [count / total_bytes for count in byte_count.values()]

    entropy = -sum(p * math.log2(p) for p in probabilities)

    return entropy


def check_ascii_range(data: bytes):
    for x in data:
        if x > 127:
            return False
    return True

def main():
    if len(sys.argv) == 3:
        cypher_path_1 = sys.argv[1]
        cypher_path_2 = sys.argv[2]
        
        with open(cypher_path_1) as f:
            cypher1 = ast.literal_eval(f.read().strip())
            f.close()
            
        with open(cypher_path_2) as f:
            cypher2 = ast.literal_eval(f.read().strip())
            f.close()
        
        xored = xor_bytes(cypher1, cypher2)
        # print(xored)
        
        print("\nBytes converted to integers:")
        for x in xored:
            print(x)
            
        print()
        print("Bytes in ascii range: ", check_ascii_range(xored))
        entropy = calculate_entropy(xored)
        print("Entropy: ", entropy)
        
    return


if __name__ == "__main__":
    main()
    
# usage:
# python3 rc4_compare.py cyphertext_k1_b.txt cyphertext_k2_a.txt