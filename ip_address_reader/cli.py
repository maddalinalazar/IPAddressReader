import argparse
import sys


import ip_filter, log_file_parser

if __name__ == '__main__':
    import os
    import sys
    print(os.getcwd())
    for i in sys.path:
        print(i)

    ip_parser = argparse.ArgumentParser(description='List the log lines that match a given IP.')

    ip_parser.add_argument('--path', metavar='./path/to/your/log/file', type=str, help='the path to the log file',
                           required=True)
    ip_parser.add_argument('--ip', metavar='178.93.28.59 or 180.76.15.0/24', type=str,
                           help='the IP or CIDR subnet mask that we want to filter by', required=True)

    arguments = ip_parser.parse_args()
    log_file_path = arguments.path
    filter_ip = arguments.ip

    print("filtering by IP: {}...\n".format(filter_ip))
    print("log file path: {}...\n".format(log_file_path))

    if not log_file_path:
        print('The path specified for the log file is null or empty.')
        sys.exit()

    if not filter_ip:
        print('The IP/Subnet specified for the log file is null or empty.')
        sys.exit()

    subnet_ip_filter = ip_filter.SubnetIPFilter(filter_ip)
    log_file_parser.LogFileParser(log_file_path).filter_log_file_by_ip_subnet(subnet_ip_filter.get_subnet())
