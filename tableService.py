import datetime
from PyQt5.QtGui import QStandardItem


class TableService():

    def __init__(self,pcaps,model):

        self.pcaps = pcaps

        self.model = model
    def insertDataToTable(self):
        for p in self.pcaps:
            # 只有一层
            time = datetime.datetime.fromtimestamp(p.time).strftime("%Y-%m-%d %H:%M:%S")
            if p.payload.name == 'NoPayload':
                row = [time,
                       p.fields['src'],
                       p.fields['dst'],
                       p.name,
                       len(p.original),
                       p.original]

            # 共两层
            elif p.payload.payload.name == 'NoPayload':
                row = [time,
                       p.payload.fields['psrc'],
                       p.payload.fields['pdst'],
                       p.payload.name,
                       len(p.original),
                       p.payload.original]
            # 共三层
            elif p.payload.payload.payload.name == 'NoPayload' or p.payload.payload.payload.payload.name == 'NoPayload':
                row = [time,
                       p.payload.fields['src'],
                       p.payload.fields['dst'],
                       p.payload.payload.name,
                       len(p.original),
                       p.payload.payload.original]

            elif p.payload.payload.name == 'ICMP':
                row = [time,
                       p.payload.fields['src'],
                       p.payload.fields['dst'],
                       p.payload.payload.name,
                       len(p.original),
                       p.payload.payload.original]
            else:
                print('miss')
                continue

            if (row[2] == '239.255.255.250'):
                row[3] = 'SSDP'

            rowCount = self.model.rowCount()
            for n, key in enumerate(row):
                item = QStandardItem(str(key))
                self.model.setItem(rowCount, n, item)