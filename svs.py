#!/usr/bin/env python3
import os
import os.path
import argparse
import logging


class Sv_Switch:
    #PATH_SV = "/etc/sv/"
    #PATH_SERVICE = "/var/service/"
    PATH_SV = "/tmp/sv/"
    PATH_SERVICE = "/tmp/service/"

    def __init__(self):

        self.services_available = self._get_services(self.PATH_SV)
        self.services_enabled = self._get_services(self.PATH_SERVICE)
        # Check if there are servives that don't boot on startup
        if os.path.isdir(self.PATH_SERVICE + "down/"):
            self.services_enabled_down = self._get_services(self.PATH_SERVICE + "down/")
        else:
            self.services_enabled_down = []


    def _get_services(self, path):
        """Returns a list of directories (that are services) in a chosen path."""
        services = []
        for directory in os.listdir(path):
            if os.path.isdir(path + directory) and not directory == "down": # Do not include the folder 'down'
                services.append(directory)
        return services

    def enable_service(self, service):
        if service not in self.services_enabled and service not in self.services_enabled_down \
           and service in self.services_available:
            os.symlink(self.PATH_SV + service, self.PATH_SERVICE + service, True)
            logging.debug(f"{service} enabled.")
        else:
            # Service already exists
            logging.warning(f"Service {service} already Enabled!")


    def disable_service(self, service):
        if service in self.services_enabled:
            os.unlink(self.PATH_SERVICE + service)
            logging.debug(f"{service} disabled.")
        elif service in self.services_enabled_down:
            os.unlink(self.PATH_SERVICE + "down/" + service)
            logging.debug(f"down/{service} disabled.")
        else:
            # Service not enabled
            logging.warning(f"Service {service} already Disabled")

    def list_services(self):
        pass

def main(args):
    svs = Sv_Switch()


    # Move to correct action
    if f"{args.action}".lower() == "enable":
        svs.enable_service(args.service)
    elif f"{args.action}".lower() == "disable":
        svs.disable_service(args.service)
    elif f"{args.action}".lower() == "list":
        svs.list_services()


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

