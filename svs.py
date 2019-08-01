#!/usr/bin/env python3
import os
import os.path
import argparse
import logging

def main_enable(args):
    print(f"Enable {args.service}!")
    pass

def main_disable(args):
    print(f"Disable {args.service}!")
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices = ["Enable", "Disable"])
    parser.add_argument("service", help="Service to Enable/Disable")
    parser.add_argument("-v", "--verbose", type = int, help = "Increase output verbosity")
    args = parser.parse_args()

    if args.action == "Enable":
        main_enable(args)
    elif args.action == "Disable":
        main_disable(args)


