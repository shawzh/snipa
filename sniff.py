from scapy.all import *
import time

class Sniff():

    def __init__(self):
        pass


    @staticmethod
    def startDefaultSniff(iface):
        print("start sniff")
        return sniff(iface=iface, count=30)

    def Sniff(self,**kwargs):

        # todo more than one args ?
        if kwargs['count'] != '':
            print(int(kwargs['count']))

            return sniff(iface=kwargs['iface'],count=int(kwargs['count']))
        if kwargs['timeLimit'] != '':
            # todo should add "time.time()"
            current = time.time()

            return sniff(iface=kwargs['iface'],timeout=int(kwargs['timeLimit']))

        if kwargs['filter'] != '':
            return sniff(iface=kwargs['iface'],filter=kwargs['filter'])


