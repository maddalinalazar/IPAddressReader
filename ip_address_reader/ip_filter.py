from ipaddress import ip_network, ip_address

# from ip_address_reader.exceptions import InvalidParameterValue, IllegalArgumentValue
import exceptions


class SubnetIPFilter:
    ip_v4_address_max_mask_value = 32
    ip_v4_address_version = 4
    ip_v6_address_max_mask_value = 128
    ip_v6_address_version = 6
    input_ip_address_value = ''
    input_ip_filter_value = ''
    input_ip_address_version = ''
    ip_network_value = ''

    def __init__(self, input_filter_value):
        # this parameter should be validated: if the path provided exists and it is a file
        if not input_filter_value:
            print('No IP/Subnet provided for the filter: {}'.format(input_filter_value))
            raise exceptions.InvalidParameterValue("The IP/Subnet provided for the filter is invalid.")

        # split the input_value by / to get the IP and the mask
        input_filter_tokens = input_filter_value.split("/")

        ip_address_construct = self.__retrieve_ip_address(input_filter_tokens)
        self.input_ip_address_version = int(ip_address_construct.version)
        self.input_ip_address_value = str(ip_address_construct)

        formatted_ip_subnet_value = "{}/{}".format(self.input_ip_address_value,
                                                   self.__retrieve_ip_subnet_mask_value(self.input_ip_address_version,
                                                                                        input_filter_tokens))

        try:
            self.ip_network_value = ip_network(formatted_ip_subnet_value)
        except Exception:
            print("The subnet derived from the provided input is invalid: {}.".format(formatted_ip_subnet_value))
            raise exceptions.InvalidParameterValue(
                "The subnet derived from the provided input is invalid: {}.".format(formatted_ip_subnet_value))

    def __retrieve_ip_address(self, input_filter_ip_address_tokens):
        ip_address_value = input_filter_ip_address_tokens[0]

        try:
            return ip_address(ip_address_value)
        except Exception:
            print("The value provided for IP is invalid: {}.".format(ip_address_value))
            raise exceptions.InvalidParameterValue("The value provided for IP is invalid: {}.".format(ip_address_value))

    def __retrieve_ip_subnet_mask_value(self, ip_address_version, input_filter_ip_address_tokens):
        input_filter_mask_value = ''

        # this will let us know if the input was an ip or a mask
        if len(input_filter_ip_address_tokens) > 1:
            input_filter_mask_value = input_filter_ip_address_tokens[1]

        if ip_address_version == self.ip_v4_address_version:
            return self.__validate_subnet_mask_value(self.ip_v4_address_max_mask_value, input_filter_mask_value)
        elif ip_address_version == self.ip_v6_address_version:
            return self.__validate_subnet_mask_value(self.ip_v6_address_max_mask_value, input_filter_mask_value)
        else:
            print("Can't match the IP's version with the provided mask. IP version: {}, mask value: {}".format(
                ip_address_version, input_filter_mask_value))
            raise exceptions.IllegalArgumentValue(
                "Can't match the IP's version with the provided mask. IP version: {}, mask value: {}".format(
                    ip_address_version, input_filter_mask_value))

    def __validate_subnet_mask_value(self, ip_subnet_max_allowed_value, input_filter_mask_value):
        if not input_filter_mask_value:
            return ip_subnet_max_allowed_value

        if int(input_filter_mask_value) > ip_subnet_max_allowed_value:
            print("The value for the IP mask is invalid. Input parameter value: {}, allowed max: {}".format(
                input_filter_mask_value, ip_subnet_max_allowed_value))
            raise exceptions.InvalidParameterValue(
                "The value for the IP mask is invalid. Input parameter value: {}, allowed max: {}".format(
                    input_filter_mask_value, ip_subnet_max_allowed_value))

        return input_filter_mask_value

    def get_filter_value(self):
        return self.input_filter_value

    def get_subnet(self):
        return self.ip_network_value
