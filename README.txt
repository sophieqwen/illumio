ILLUMIO FIREWALL ASSIGNMENT
Author: Sophie Wen

The main source code is in the firewall.py file. I ran my code in the terminal using "python3 -i firewall.py" when I wanted to test interactively and "python3 firewall_test.py" to test that my code passed the rules files.

a. I first tested my solution in firewall.py by simply printing out the results to each example test case. I then moved my tests into the firewall_test.py file using Python's unittest module.

b. While the allowed ports and IP addresses could have been a single value, I decided to make "port_range" and "ip_range" as lists so that I would not have to check if the port and ip_address equaled the single value in a separate case. I realized I could set both the start and end values of port_range and ip_range to be the same and compare those with the given port and ip_address. As I was using Python, I also found that the built-in csv and ipaddress modules came in very useful, as the comparison of IP addresses was essentially already built into the class.

c. If I had more time I would implement more tests and optimize the algorithm as best as I could to be efficient against 500K entries, which I was unable to test against in the given time. Since there did not seem to be any way the rules were organized I thought it was necessary to iterate through every rule. My accept_packet function runs in O(n) where n is the number of rules.

d. I believe that I would have to check the packet against every given rule in the csv file in order to correctly implement the guidelines, so I did not think there was a much more efficient way (around iterating through every rule.) I also thought that checking that the direction and protocol matched first would eliminate many rules I was checking against, as the method would not do anything if it did not pass.

I am interested in learning whatever I can! But based on how much experience I have with each team I would like to rank (most preferred first):
1. Platform team
2. Policy team
3. Data team