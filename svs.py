#!/usr/bin/env python3
import os
import os.path
import argparse
import logging

PATH_SV = "/etc/sv/"
PATH_SERVICE = "/var/service/"

def get_services(path):
    """Returns a list of directories (that are services) in a chosen path."""
    services = []
    for directory in os.listdir(path):
        if os.path.isdir(path + directory) and not directory == "down": # Do not include the folder 'down'
            services.append(directory)
    return services

def enable_service(args):
    pass

def disable_service(args):
    pass

def main(args):
    services_available = get_services(PATH_SV)
    services_enabled = get_services(PATH_SERVICE)
    # Check if there are servives that don't boot on startup
    if os.path.isdir(PATH_SERVICE + "down/"):
        services_enabled_down = get_services(PATH_SERVICE + "down/")
    else:
        services_enabled_down = None

    # Move to correct action
    if f"{args.action}".lower() == "enable":
        enable_service(args)
    elif f"{args.action}".lower() == "disable":
        disable_service(args)
    elif f"{args.action}".lower() == "list":
        pass


if __name__ == "__main__":
    # Argparse Parsing
    parser = argparse.ArgumentParser()
    parser.add_argument("action", help="[List, Enable, Disable]")
    parser.add_argument("service", help="Service to Enable/Disable")
    #parser.add_argument("-v", "--verbose", type = int, help = "Increase output verbosity")
    args = parser.parse_args()

    # Enter main function
    try:
        main(args)
    except KeyboardInterrupt:
        quit()

