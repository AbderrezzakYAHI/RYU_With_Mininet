
from mininet.topo import Topo


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
	s1 = self.addSwitch('s101')
        s2 = self.addSwitch('s102')
        s3 = self.addSwitch('s103')
        s4 = self.addSwitch('s104')
	s5 = self.addSwitch('s105')
	s6 = self.addSwitch('s106')
	s7 = self.addSwitch('s107')

        # Add links
        self.addLink(s4, s1)
        self.addLink(s2, s4)
        self.addLink(s5, s1)
	self.addLink(s3, s4)
        self.addLink(s2, s5)
        self.addLink(s3, s5)
	self.addLink(s2, h1)
        self.addLink(s3, h2)
        self.addLink(s1, h3)
	self.addLink(s2, h4)
        self.addLink(s3, h5)
        self.addLink(s1, h6)
	self.addLink(s7, s6)
        self.addLink(s6, s5)


class irs2019(Topo):
    def __init__(self):
        Topo.__init__(self)
        host={}
        switch={}

        # TODO: add the description of the topology here




topos = {'irs2020': (lambda: irs2020()),
         'irs2019': (lambda: irs2019())
        }
