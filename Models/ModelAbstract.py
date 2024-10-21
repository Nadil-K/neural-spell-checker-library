from abc import ABC, abstractmethod

class ModelAbstract(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def check(self, text):
        pass