rom mininet.topo import Topo


class irs2020(Topo):
    "Simple topology example."

    def __init__(self):
        "Create custom topo."

        # Initialize topology
        Topo.__init__(self)

        # Add hosts and switches
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
	h7 = self.addHost('h7')
        h8 = self.addHost('h8')
	s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
	s5 = self.addSwitch('s5')
	s6 = self.addSwitch('s6')
	s7 = self.addSwitch('s7')
 	h1.cmd("brctl addbr brvlan10")
        h3.cmd("brctl addbr brvlan20")
        h1.cmd("brctl addif brvlan10 h1-eth0")
        h1.cmd("brctl addif brvlan10 h1-eth1")
        h1.cmd("brctl addif brvlan10 h1-eth4.10")
        h3.cmd("brctl addif brvlan20 h3-eth2")
        h3.cmd("brctl addif brvlan20 h3-eth3")
        h3.cmd("brctl addif brvlan20 h3-eth4.20")
        h1.cmd("ifconfig brvlan10 up")
        h3.cmd("ifconfig brvlan20 up")

        # Add links
        self.addLink(s1, h1)
        self.addLink(s1, h2)
        self.addLink(s1, s5)
	self.addLink(s1, s2)
	self.addLink(s2, h3)
        self.addLink(s2, h4)
        self.addLink(s2, s5)
	self.addLink(s2, s3)
 	self.addLink(s5, s6)
	self.addLink(s5, s7)
        self.addLink(s3, h5)
        self.addLink(s3, h6)
	self.addLink(s3, s6)
	self.addLink(s3, s4)
        self.addLink(s4, h7)
        self.addLink(s4, h7)
        self.addLink(s4, s6)
        self.addLink(s6, s7)


topos = {'irs2020': (lambda: irs2020())}
