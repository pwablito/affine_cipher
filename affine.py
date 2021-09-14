#!/usr/bin/env python3

import argparse
import sys


def character_to_number(character):
    return ord(character.lower()) - ord('a')


def number_to_character(number):
    return chr(number + ord('a'))


def encrypt_number(num, a, b):
    return ((num * a) + b) % 26


def encrypt_message(message, a, b):
    numeric_message = [character_to_number(character) for character in message]
    numeric_ciphertext = [encrypt_number(num, a, b) for num in numeric_message]
    ciphertext = ''.join([number_to_character(num) for num in numeric_ciphertext])
    return ciphertext


def main():
    parser = argparse.ArgumentParser(
        description='Encrypt or decrypt a message using affine cipher.'
    )
    parser.add_argument("-a", help="value for a in ax+b mod 26", type=int, required=True)
    parser.add_argument("-b", help="value for b in ax+b mod 26", type=int, required=True)
    subparsers = parser.add_subparsers(dest='command', required=True)
    subparsers.add_parser('encrypt', help='encrypt a message')
    subparsers.add_parser('decrypt', help='decrypt a message')
    args = parser.parse_args()
    message = sys.stdin.read().strip()
    if args.command == 'encrypt':
        print(encrypt_message(message, args.a, args.b))
    elif args.command == 'decrypt':
        print(decrypt_message(message, args.a, args.b))
    else:
        exit("Invalid command")

if __name__ == "__main__":
    main()
