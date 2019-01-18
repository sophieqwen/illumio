import unittest
import firewall

class FirewallTest(unittest.TestCase):
    def test_rules1(self):
        fw = firewall.Firewall("rules1.csv")
        self.assertEqual(fw.accept_packet("inbound", "tcp", 80, "192.168.1.2"), True)
        self.assertEqual(fw.accept_packet("inbound", "udp", 53, "192.168.2.1"), True)
        self.assertEqual(fw.accept_packet("outbound", "tcp", 10234, "192.168.10.11"), True)
        self.assertEqual(fw.accept_packet("inbound", "tcp", 81, "192.168.1.2"), False)
        self.assertEqual(fw.accept_packet("inbound", "udp", 24, "52.12.48.92"), False)

    def test_rules2(self):
        fw = firewall.Firewall("rules2.csv")
        self.assertEqual(fw.accept_packet("inbound", "tcp", 80, "192.168.1.2"), True)
        self.assertEqual(fw.accept_packet("inbound", "udp", 53, "192.168.2.1"), False)
        self.assertEqual(fw.accept_packet("outbound", "tcp", 10234, "192.168.10.11"), False)
        self.assertEqual(fw.accept_packet("inbound", "tcp", 81, "192.168.1.2"), True)
        self.assertEqual(fw.accept_packet("inbound", "udp", 24, "52.12.48.92"), False)

        def test_rules3(self):
            fw = firewall.Firewall("rules3.csv")
            self.assertEqual(fw.accept_packet("inbound", "tcp", 0, "192.168.1.2"), True)
            self.assertEqual(fw.accept_packet("inbound", "udp", 53, "192.168.2.1"), False)
            self.assertEqual(fw.accept_packet("outbound", "tcp", 10234, "192.168.10.11"), False)
            self.assertEqual(fw.accept_packet("inbound", "tcp", 81, "192.168.1.2"), False)
            self.assertEqual(fw.accept_packet("inbound", "udp", 24, "52.12.48.92"), False)

main = FirewallTest()
main.test_rules1()
main.test_rules2()
