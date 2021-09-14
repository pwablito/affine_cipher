#!/usr/bin/env python3

import argparse
import sys
import affine


def break_ciphertext(ciphertext, start, max_possibilities=1):
    a = 0
    possibilities = 0
    while possibilities < max_possibilities:
        for b in range(0, 26):
            try:
                decrypted = affine.decrypt_message(ciphertext, a, b)
                if decrypted.startswith(start):
                    print("a = {}, b = {}, plaintext={}".format(
                        a, b, decrypted
                    ))
                    possibilities += 1
            except ValueError:
                pass
        a += 1


def main():
    parser = argparse.ArgumentParser(
        description='Break affine cipher using start of plaintext'
    )
    parser.add_argument("-s", "--start", type=str, required=True)
    args = parser.parse_args()
    break_ciphertext(sys.stdin.read().strip(), args.start)


if __name__ == "__main__":
    main()
