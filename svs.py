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
    parser.add_argument("action", help="[Enable, Disable]")
    parser.add_argument("service", help="Service to Enable/Disable")
    parser.add_argument("-v", "--verbose", type = int, help = "Increase output verbosity")
    args = parser.parse_args()

    if f"{args.action}".lower() == "enable":
        main_enable(args)
    elif f"{args.action}".lower() == "disable":
        main_disable(args)


