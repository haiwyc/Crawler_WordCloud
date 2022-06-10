import os

class Public(object):

    def getpath(self):
        return os.path.dirname(os.path.abspath(__file__)).split("com")[0]

    def pathjoin(self,*path):
        return os.path.join(*path)

    def getfliename(self,name):
        return name+".txt"