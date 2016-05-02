#!python3
## argsparse.py (optional)
## This file is just to get an idea how arguments passed are parsed inside the scripts.

import argparse

parser = argparse.ArgumentParser(description='Tose App')

parser.add_argument('serie', type=str,
                    help='Serie')

# Season
parser.add_argument('-s', type=int,
                    help='Season')

# Episode
parser.add_argument('-e', type=int,
                    help='Episode')

args = parser.parse_args()

if len(str(args.s)) > 2:
    parser.error("Season number cannot be larger than 2")
if len(str(args.e)) > 2:
    parser.error("Episode number cannot be larger than 2")

print("Argument values:")
print(("Serie: " + args.serie + "\t" + "Season: " + str(args.s) + "\t" + "Episode: " + str(args.e)))