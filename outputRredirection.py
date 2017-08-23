class TextArea(object):
    def __init__(self):
        self.buffer = []

    def write(self, *args, **kwargs):
        self.buffer.append(args)




# print to TextArea
# print("testA")
# print("testB")
# print("testC")
#
# text_area, sys.stdout = sys.stdout, stdout

# print to console
#print(text_area.buffer)