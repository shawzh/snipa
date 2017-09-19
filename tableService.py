import datetime
from PyQt5.QtWidgets import QTableWidgetItem


class TableService():
    def __init__(self, pcaps, model):

        self.pcaps = pcaps

        self.model = model


    def insertDataToTable(self):

        preRow = self.model.rowCount()
        self.model.setRowCount(preRow+self.pcaps.res.__len__())

        #转换数据格式


        for row in self.build():

            for n, key in enumerate(row):
                item = QTableWidgetItem(str(key))
                self.model.setItem(preRow, n, item)
            preRow = preRow+1



    def build(self):
        rows = []
        for p in self.pcaps:
            # 只有一层
            time = datetime.datetime.fromtimestamp(p.time).strftime("%Y-%m-%d %H:%M:%S")
            src = self.getSrc(p)
            dst = self.getDst(p)
            raw = self.getRaw(p)
            length = len(p.original)
            proto = self.getProto(p)

            row = [time, src, dst, proto, length, raw]
            if row[2] == '239.255.255.250':
                row[3] = 'SSDP'
            rows.append(row)
        return rows



    def getSrc(self, p):

        try:
            return p['IP'].src

        except:
            try:
                return p['ARP'].psrc
            except:
                return 'miss src'

    def getDst(self, p):
        try:
            return p['IP'].dst
        except:
            try:
                return p['ARP'].pdst
            except:
                return 'miss dst'

    def getRaw(self, p):
        try:
            return p.summary()
        except:
            return 'miss'

    def getProto(self, p):
        try:
            t = p['TCP']
            return 'TCP'
        except:
            try:
                t = p['UDP']
                return 'UDP'
            except:
                return 'ARP'
