from abc import ABC,abstractmethod


class Computer(ABC): #ABC = Abstract base class
    
    
    @abstractmethod   # this method is void
    def process(self,app):
        pass

    def run(self,app):
        self.process(app)

class Laptop(Computer):
    def process(self,app):
        print(f"{app} processing through laptp")

class Mobile(Computer):
    def process(self,app):
        print(f"{app} processing through mobile")

dell=Laptop()
dell.run("chrome")
dell.run("pubg")

samsung = Mobile()
samsung.run("camera")
samsung.run("pubg")