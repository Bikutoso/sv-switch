#!/usr/bin/env python3
import os
import os.path
import sys
import argparse

from typing import List

class Sv_Switch:
    #PATH_SV = "/etc/sv/"
    #PATH_SERVICE = "/var/service/"
    # Dummy Service location
    PATH_SV = "/tmp/svs/sv/"
    PATH_SERVICE = "/tmp/svs/service/"

    def __init__(self) -> None:
        self.services_available = self._get_services(self.PATH_SV)
        self.services_enabled = self._get_services(self.PATH_SERVICE)
        self.services_disabled = list(set(self.services_available) - set(self.services_enabled))


    def _get_services(self, path) -> List[str]:
        """Returns a list of directories (that are services) in a chosen path."""
        services = []
        for directory in os.listdir(path):
            if os.path.isdir(path + directory):
                services.append(directory)
        return services

    @staticmethod
    def _list2str(strlist) -> str:
        """Converts a list to a comma seperated string."""
        return ", ".join(sorted(strlist))

    def enable_service(self, args) -> None:
        """Creates symlink for selected service."""
        if args.service not in self.services_enabled and args.service in self.services_available:
            os.symlink(self.PATH_SV + args.service, self.PATH_SERVICE + args.service, True)
        elif args.service in self.services_available:
            # Service already enabled
            sys.exit(f"Service {args.service} already Enabled!")
        else:
            # Service does not exist
            sys.exit(f"Service {args.service} not found")


    def disable_service(self, args) -> None:
        """Removes symlink for selected service."""
        if args.service in self.services_enabled:
            os.unlink(self.PATH_SERVICE + args.service)
        elif args.service in self.services_available:
            # Service not enabled
            sys.exit(f"Service {args.service} already Disabled!")
        else:
            # Service does not exist
            sys.exit(f"Service {args.service} not found")

    def list_services(self, args) -> None:
        """Prints a list of all Enabled/Disabled services."""
        print(f"Enabled:  {self._list2str(self.services_enabled)}")
        print(f"Disabled: {self._list2str(self.services_disabled)}")

class Argument_Parse():
    def __init__(self, svs):
        self.svs = svs
        self.setup_args()

    def setup_args(self):
        # Argparse Parsing
        self.parser = argparse.ArgumentParser()
        self.subparsers = self.parser.add_subparsers()
    
        # Service List
        self.svlist = self.subparsers.add_parser("list", help="Lists available services")
        self.svlist.set_defaults(func=self.svs.list_services)

        # Service Enable
        self.svenable = self.subparsers.add_parser("enable", help="Enables service")
        self.svenable.add_argument("service")
        self.svenable.set_defaults(func=self.svs.enable_service)

        # Service Disable
        self.svdisable = self.subparsers.add_parser("disable", help="Disables service")
        self.svdisable.add_argument("service")
        self.svdisable.set_defaults(func=self.svs.disable_service)

    def execute(self):
        # Parse arguments and execute correct class function
        self.args = self.parser.parse_args()
        self.args.func(self.args)

def main():
    svs = Sv_Switch()
    args = Argument_Parse(svs)
    args.execute()

if __name__ == "__main__":
    # Enter main function
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
