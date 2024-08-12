#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from config.settings import ALLOWED_HOSTS

import socket

# PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    print(f'IP address: {IPAddr}')
    if IPAddr not in ALLOWED_HOSTS:
        ALLOWED_HOSTS.append(IPAddr)

    print(f'Allowed Hosts: {ALLOWED_HOSTS}')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
