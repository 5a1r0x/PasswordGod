#!/usr/bin/env python3

"""
PasswordGod - Password Generator
Developer: Syrox (5a1r0x)
License: MIT
"""

import random
import string
import colorama
import argparse

# Parser
parser = argparse.ArgumentParser(
    prog='passwordgod',
    description='PasswordGod | Password Generator',
    epilog='Generate random and secure passwords based on the chosen criteria'
)

# Add Argument
parser.add_argument('-l', '--length', help='password length [MIN 12; MAX 100]', required=True, type=int, nargs=1)
parser.add_argument('-a', '--amount', help='password amount [MIN 1; MAX -]', required=True, type=int, nargs=1, default=[1])
parser.add_argument('-s', '--symbols', help='password symbols [Recommended]', action='store_true', required=False)
parser.add_argument('-f', '--file', help='save password in file [PasswordGod.txt]', action='store_true', required=False)
parser.add_argument('-v', '--verbose', help='verbose mode', required=False, default=0, action='store_true')

# Args
args = parser.parse_args()

# Colors
red = colorama.Fore.RED
yellow = colorama.Fore.YELLOW
cyan = colorama.Fore.CYAN
reset = colorama.Fore.RESET

# Characters
lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits
symbols = "!#$%&'()*+,-./:;<=>?@[]^_`{|}~\""

# All Characters
characters = lower + upper + numbers + symbols
characters_no_symbols = lower + upper + numbers

# Generate
def password_generate():
    """Generate random and secure passwords based on the chosen criteria"""
    try:
        # Min Length
        if 12 <= args.length[0] <= 100:
            # Quantity
            for a in range(args.amount[0]):
            # Symbols
             if args.symbols:
                 password = "".join(random.choices(characters, k=args.length[0]))
                 print(f"{cyan}[PASSWORD]{reset}", password)
            # File
             if args.file:
                with open("PasswordGod.txt", "a") as file:
                    password = "".join(random.choices(characters, k=args.length[0]))
                    file.write(password + "\n")
            # Not Symbols
             if not args.symbols:
                 password = "".join(random.choices(characters_no_symbols, k=args.length[0]))
                 print(f"{cyan}[PASSWORD]{reset}", password)
        # Length Error
        else:
            print(f"{cyan}[ERROR][-l, --length LENGTH]{reset}", "Enter a number greater than or equal to 12 and less than or equal to 100")
    # Exception
    except Exception as e:
        print(f"{red}[ERROR]{reset}", e)

# Run
if __name__ == "__main__":
    password_generate()
    # Verbose
    if args.verbose and 12 <= args.length[0] <= 100:
        print(f"{yellow}[INFO]{reset}", "Password length:", args.length[0])
        print(f"{yellow}[INFO]{reset}", "Amount:", args.amount[0])
        print(f"{yellow}[INFO]{reset}", "Symbols:", args.symbols)
        print(f"{yellow}[INFO]{reset}", "File:", args.file)

