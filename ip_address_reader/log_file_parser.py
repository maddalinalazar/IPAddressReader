from pathlib import Path
from ipaddress import ip_network, ip_address

from exceptions import InvalidParameterValue

class LogFileParser:
    path_to_log_file = ''
    ip_address_split_token = " - - "

    def __init__(self, log_file_path):
        # this parameter should be validated: if the path provided exists and it is a file
        if not log_file_path or not Path(log_file_path).exists():
            print('The path specified does not exist: {}'.format(log_file_path))
            raise InvalidParameterValue("The path provided for the log file is invalid.")
        self.path_to_log_file = log_file_path

        self.successful_matches = 0
        self.invalid_ip_values = 0

    def get_successful_matches(self):
        return self.successful_matches

    def get_invalid_ips(self):
        return self.invalid_ip_values

    # This method will return the log lines that contain an IP that is a member of the provided subnet
    def filter_log_file_by_ip_subnet(self, ip_subnet_input):
        # validate the ip_subnet_input to not be empty or something
        if not ip_subnet_input:
            print('Invalid subnet value. Won\'t find any matches. Exiting...')
            return 

        # read the file line by line
        with open(self.path_to_log_file) as log_file:
            for log_line in log_file:
                raw_ip_address_string = log_line.split(self.ip_address_split_token)[0]
                # check if the given IP exists 
                # try to create an IP address from the IP string of the lof
                try :
                    curent_ip_address = ip_address(raw_ip_address_string)
                    if curent_ip_address in ip_subnet_input:
                        print('{}'.format(log_line))
                        self.successful_matches += 1
                except Exception:
                    self.invalid_ip_values += 1
        log_file.closed 

        print('Method found {} matching ips.'.format(self.successful_matches))
        print('Method skipped {} possible invalid ips.'.format(self.invalid_ip_values))
