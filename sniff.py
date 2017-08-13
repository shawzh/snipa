from scapy.all import *


class Sniff():
    @staticmethod
    def startDefaultSniff( iface):
        return sniff(iface=iface, count=300)
