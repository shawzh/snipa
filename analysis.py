from bokeh.plotting import figure, output_file, show
from utils.dbUtils import *
from collections import Counter
class graph(object):

    def __init__(self):
        self.x = []
        self.y = []

        conn = dbUtils().getConn()
        cur = conn.cursor()
        cur.execute("select poto from PACKETS_REC")
        data = cur.fetchall()

        c = Counter(data)
        for k in c:
            self.x.append(k[0])
            self.y.append(c[k])


    def createBarGraph(self):
        # output to static HTML file
        output_file("lines.html")

        # # create a new plot with a title and axis labels
        # p = figure(title="协议分布", x_axis_label='x', y_axis_label='y')
        #
        # # add a line renderer with legend and line thickness
        # p.line(x, y, legend="Temp.", line_width=2)
        a = self.x.__repr__()
        p1 = figure(plot_width=400, plot_height=400,title="协议分布"+a,x_axis_type="linear")

        p1.vbar(x=[1,2,3,4],width=0.5, bottom=0,
               top=self.y, color="#CAB2D6")


        # show the results


        show(p1)



