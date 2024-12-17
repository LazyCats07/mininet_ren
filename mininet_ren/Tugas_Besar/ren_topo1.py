from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch
from mininet.log import setLogLevel, info

class MyTopo(Topo):
    "Simple topology example."

    def build(self):
        "Create custom topology."

        # Add switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')

        # Add hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')
        h8 = self.addHost('h8')

        # Add links between hosts and switches
        self.addLink(s1, h1)
        self.addLink(s2, h2)
        self.addLink(s3, h3)
        self.addLink(s3, h4)
        self.addLink(s4, h5)
        self.addLink(s5, h6)
        self.addLink(s6, h7)
        self.addLink(s6, h8)

        # Add links between switches to form a ring
        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(s3, s4)
        self.addLink(s4, s5)
        self.addLink(s5, s6)
        self.addLink(s6, s1)

# Function to run Mininet with this topology
def run():
    "Run the topology with a single controller."
    topo = MyTopo()
    net = Mininet(topo=topo, controller=Controller, switch=OVSKernelSwitch, autoSetMacs=True)

    # Add default controller
    info("** Adding Controller\n")
    net.addController('c0', ip='10.109.253.152', port=6633)

    # Start the network
    info("** Starting Network\n")
    net.start()

    # Test network connectivity
    info("** Testing Network Connectivity\n")
    net.pingAll()

    # Start CLI for user interaction
    info("** Starting CLI\n")
    net.interact()

    # Stop the network
    info("** Stopping Network\n")
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')  # Set Mininet log level
    run()
