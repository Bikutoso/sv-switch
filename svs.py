#!/usr/bin/env python3
import os
import os.path
import argparse
import logging


class Sv_Switch:
    #PATH_SV = "/etc/sv/"
    #PATH_SERVICE = "/var/service/"
    # Example Services
    PATH_SV = "/tmp/svs/sv/"
    PATH_SERVICE = "/tmp/svs/service/"

    def __init__(self):
        self.services_available = self._get_services(self.PATH_SV)
        self.services_enabled = self._get_services(self.PATH_SERVICE)
        self.services_disabled = list(set(self.services_available) - set(self.services_enabled))


    def _get_services(self, path):
        """Returns a list of directories (that are services) in a chosen path."""
        services = []
        for directory in os.listdir(path):
            if os.path.isdir(path + directory):
                services.append(directory)
        return services

    @staticmethod
    def _list2str(strlist):
        string = ""
        for i, item in enumerate(sorted(strlist)):
            string += item + ", " if i+2 <= len(strlist) else item
        return string


    def enable_service(self, args):
        """Creates symlink for selected service"""
        if args.service not in self.services_enabled and args.service in self.services_available:
            os.symlink(self.PATH_SV + args.service, self.PATH_SERVICE + args.service, True)
            logging.debug(f"{args.service} enabled.")
        else:
            # Service already exists
            logging.warning(f"Service {args.service} already Enabled!")


    def disable_service(self, args):
        """Removes symlink on selected service"""
        if args.service in self.services_enabled:
            os.unlink(self.PATH_SERVICE + args.service)
            logging.debug(f"{args.service} disabled.")
        else:
            # Service not enabled
            logging.warning(f"Service {args.service} already Disabled")

    def list_services(self, args):
        print(f"Enabled:  {self._list2str(self.services_enabled)}")
        print(f"Disabled: {self._list2str(self.services_disabled)}")

def main():
    svs = Sv_Switch()

    # Argparse Parsing
    parser = argparse.ArgumentParser()
    #parser.add_argument("-v", "--verbose", type = int, help = "Increase output verbosity")
    subparsers = parser.add_subparsers()
    # Service List
    svlist = subparsers.add_parser("list", help="Lists available services")
    svlist.set_defaults(func=svs.list_services)
    # Service Enable
    svenable = subparsers.add_parser("enable", help="Enables services")
    svenable.add_argument("service")
    svenable.set_defaults(func=svs.enable_service)
    #Service Disable
    svdisable = subparsers.add_parser("disable", help="Disables services")
    svdisable.add_argument("service")
    svdisable.set_defaults(func=svs.disable_service)
    #Parse and execute
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":

    # Enter main function
    try:
        main()
    except KeyboardInterrupt:
        quit()

