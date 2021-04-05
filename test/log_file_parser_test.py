import unittest

from ipaddress import ip_network, ip_address
from ip_address_reader import log_file_parser, exceptions


class LogFileParserTest(unittest.TestCase):
    def test_invalid_input_file_path(self):
        with self.assertRaises(exceptions.InvalidParameterValue):
            log_file_parser.LogFileParser("log-file-parser.invalid.file.log")

    def test_empty_input_file_path(self):
        with self.assertRaises(exceptions.InvalidParameterValue):
            print("Raising exception.")
            log_file_parser.LogFileParser("")

    def test_empty_ip_subnet(self):
        file_parser = log_file_parser.LogFileParser("small-test-log-file.log")
        file_parser.filter_log_file_by_ip_subnet("")

        self.assertEqual(0, file_parser.get_successful_matches())
        self.assertEqual(0, file_parser.get_invalid_ips())

    def test_ip_addresses_and_matches_w_subnet(self):
        file_parser = log_file_parser.LogFileParser("small-test-log-file.log")
        file_parser.filter_log_file_by_ip_subnet(ip_network("180.76.15.0/24"))

        self.assertEqual(7, file_parser.get_successful_matches())
        self.assertEqual(1, file_parser.get_invalid_ips())

    def test_ip_addresses_and_matches_w_ip(self):
        file_parser = log_file_parser.LogFileParser("small-test-log-file.log")
        file_parser.filter_log_file_by_ip_subnet(ip_network("31.184.238.128/32"))

        self.assertEqual(3, file_parser.get_successful_matches())
        self.assertEqual(1, file_parser.get_invalid_ips())


if __name__ == '__main__':
    unittest.main()
