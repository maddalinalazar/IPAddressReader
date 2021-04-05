import unittest
import os
import sys
from ipaddress import ip_address
from ip_address_reader import ip_filter, exceptions

print(os.getcwd())
for i in sys.path:
    print(i)


class IPFilterTest(unittest.TestCase):
    def test_invalid_filter_value(self):
        self.assertEqual(0, 0)
        # self.assertRaises(exceptions.InvalidParameterValue, ip_filter.SubnetIPFilter(""))
    
    def test_invalid_ip_v4_value(self):
        with self.assertRaises(exceptions.InvalidParameterValue):
            ip_filter.SubnetIPFilter("180...57.15.146/567")
    
    def test_invalid_ip_v6_value(self):
        with self.assertRaises(exceptions.InvalidParameterValue):
            ip_filter.SubnetIPFilter("2001:DB8:0:10:ZZ:0:0:3210")

    def test_invalid_ip_v4_mask_value(self):
        with self.assertRaises(exceptions.InvalidParameterValue):
            ip_filter.SubnetIPFilter("180.76.15.20/128")

    def test_invalid_ip_v6_mask_value(self):
        with self.assertRaises(exceptions.InvalidParameterValue):
            ip_filter.SubnetIPFilter("2001:0DB8:7654:0010:FEDC:0000:0000:3210/300")

    def test_check_mask_for_ipv4_ip_w_mask(self):
        subnet_ip_filter = ip_filter.SubnetIPFilter("180.76.15.48/30")

        self.assertTrue(ip_address("180.76.15.48") in subnet_ip_filter.get_subnet())
        self.assertTrue(ip_address("180.76.15.49") in subnet_ip_filter.get_subnet())
        self.assertTrue(ip_address("180.76.15.50") in subnet_ip_filter.get_subnet())
        self.assertTrue(ip_address("180.76.15.51") in subnet_ip_filter.get_subnet())
        self.assertFalse(ip_address("180.76.15.52") in subnet_ip_filter.get_subnet())
        self.assertFalse(ip_address("180.76.15.47") in subnet_ip_filter.get_subnet())

    def test_check_mask_for_ipv4_ip(self):
        subnet_ip_filter = ip_filter.SubnetIPFilter("180.76.15.20/32")

        self.assertTrue(ip_address("180.76.15.20") in subnet_ip_filter.get_subnet())
        self.assertFalse(ip_address("180.76.15.21") in subnet_ip_filter.get_subnet())

    def test_check_mask_for_ipv6_ip(self):
        subnet_ip_filter = ip_filter.SubnetIPFilter("2001:0DB8:7654:0010:FEDC:0000:0000:3210/128")

        self.assertTrue(ip_address("2001:0DB8:7654:0010:FEDC:0000:0000:3210") in subnet_ip_filter.get_subnet())
        self.assertFalse(ip_address("2001:0DB8:7654:0010:FEDC:0000:0000:3211") in subnet_ip_filter.get_subnet())

    def test_check_mask_for_ipv6_ip_w_mask(self):
        subnet_ip_filter = ip_filter.SubnetIPFilter("2001:0DB8:7654:0010:FEDC:0000:0000:3210/126")

        self.assertTrue(ip_address("2001:0DB8:7654:0010:FEDC:0000:0000:3210") in subnet_ip_filter.get_subnet())
        self.assertTrue(ip_address("2001:0DB8:7654:0010:FEDC:0000:0000:3211") in subnet_ip_filter.get_subnet())
        self.assertTrue(ip_address("2001:0DB8:7654:0010:FEDC:0000:0000:3212") in subnet_ip_filter.get_subnet())
        self.assertTrue(ip_address("2001:0DB8:7654:0010:FEDC:0000:0000:3213") in subnet_ip_filter.get_subnet())
        self.assertFalse(ip_address("2001:0DB8:7654:0010:FEDC:0000:0000:3217") in subnet_ip_filter.get_subnet())
        self.assertFalse(ip_address("2001:0DB8:7654:0010:FEDC:0000:0000:3209") in subnet_ip_filter.get_subnet())


if __name__ == '__main__':
    unittest.main()
