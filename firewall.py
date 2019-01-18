import csv
import ipaddress

class Firewall:
    def __init__(self, file):
        self.rules = []
        with open(file) as csvfile:
            readcsv = csv.reader(csvfile, delimiter=',')
            for row in readcsv:
                self.rules.append(row)

    def accept_packet(self, direction, protocol, port, ip_address):
        for rule in self.rules:
            if rule[0] == direction and rule[1] == protocol:
                allowed_ports = rule[2]
                allowed_ips = rule[3]

                port_range = [None] * 2
                ip_range = [None] * 2

                if allowed_ports.find("-") == -1:
                    port_range[0] = port_range[1] = allowed_ports
                else:
                    port_range = allowed_ports.split("-")

                if allowed_ips.find("-") == -1:
                    ip_range[0] = ip_range[1] = ipaddress.IPv4Address(allowed_ips)
                else:
                    ip_range = allowed_ips.split("-")
                    ip_range[0] = ipaddress.IPv4Address(ip_range[0])
                    ip_range[1] = ipaddress.IPv4Address(ip_range[1])

                if int(port_range[0]) <= port <= int(port_range[1]) and ip_range[0] <= ipaddress.IPv4Address(ip_address) <= ip_range[1]:
                    return True
        return False
