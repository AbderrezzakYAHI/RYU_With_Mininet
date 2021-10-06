from mininet.topo import Topo


class MyTopo(Topo):
    "Simple topology example."

    def __init__(self):
        "Create custom topo."

        # Initialize topology
        Topo.__init__(self)

        # Add hosts and switches
        leftHost = self.addHost('h1')
        rightHost = self.addHost('h2')
	leftHost =self.addHost('h3')
	rightHost = self.addHost('h4')
	leftHost =self.addHost('h5')
        leftHost =self.addHost('h5')
        leftSwitch = self.addSwitch('s101')
        rightSwitch = self.addSwitch('s102')
        rightSwitch = self.addSwitch('s103')
	uprightSwitch=self.addSwitch('s105')
	upleftSwitch=self.addSwitch('s104')


        # Add links
	self.addlink(upleftSwitch, leftSwitch, bw=1000, delay="1ms", loss=0)
	self.addlink(rightSwitch, upleftSwitch,  bw=1000, delay="1ms", loss=0)
	self.addlink(uprightSwitch, leftSwitch, bw=1000, delay="1ms", loss=0)
	self.addlink(rightSwitch, upleftSwitch,  bw=1000, delay="1ms", loss=0)
        self.addlink(rightSwitch, upleftSwitch,  bw=1000, delay="1ms", loss=0)
        self.addLink(leftHost, leftSwitch, bw=10, delay="1ms", loss=0)
        self.addLink(leftSwitch, rightSwitch, bw=5, delay="10ms", loss=0)
        self.addLink(rightSwitch, rightHost, bw=10, delay="1ms", loss=0)


class brings(Topo):
    def __init__(self):
        Topo.__init__(self)
        host={}
        switch={}

        # TODO: add the description of the topology here




topos = {'mytopo': (lambda: MyTopo()),
         'brings': (lambda: brings())
        }
