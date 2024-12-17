"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

     # Initialize Mininet
    net = Mininet(controller=Controller, switch=OVSKernelSwitch, autoSetMacs=True)

    info("** Adding Controller\n")
    c0 = net.addController('c0', ip='10.109.253.152',port=6633)

    def build( net ):
        "Create custom topo."

        # Add switches
        s1 = net.addSwitch('s1')
        s2 = net.addSwitch('s2')
        s3 = net.addSwitch('s3')
        s4 = net.addSwitch('s4')
        s5 = net.addSwitch('s5')
        s6 = net.addSwitch('s6')

        # Add host
        h1 = net.addHost('h1')
        h2 = net.addHost('h2')
        h3 = net.addHost('h3')
        h4 = net.addHost('h4')
        h5 = net.addHost('h5')
        h6 = net.addHost('h6')
        h7 = net.addHost('h7')
        h8 = net.addHost('h8')

        # Add links
        net.addLink(s1,h1)
        net.addLink(S2,h2)
        net.addLink(s3,h3)
        net.addLink(s3,h4)
        net.addLink(s4,h5)
        net.addLink(s5,h6)
        net.addLink(s6,h7)
        net.addLink(s6,h8)

        # add switch
        net.addLink(s1,s2)
        net.addLink(s2,s3)
        net.addLink(s3,s4)
        net.addLink(s4,s5)
        net.addLink(s5,s6)
        net.addLink(s6,s1)

  
topos = { 'mytopo': ( lambda: MyTopo() ) }