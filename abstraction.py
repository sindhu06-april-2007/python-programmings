from abc import ABC,abstractmethod
class washingmachine(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def raising(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class samsung(washingmachine):
    def start(self):
        print("samsung is starting")
    def raising(self):
        print("samsung is raising")
    def stop(self):
        print("samsung is stop")
s=samsung()
s.start()
s.raising()
s.stop()
