from abc import ABC, abstractmethod
from EvaluateModelException import EvaluateModelException

class ModelAbstract(ABC):
    def __init__(self, from_pretrained):
        self.tokenizer = None
        self.model = None
        pass

    def evaluate(self, text, src):
        if not src is None:
            self.evaluateFromFile(src)
        elif type(text) == str:
            self.evaluateFromString(text)
        elif type(text) == list:
            self.evaluateFromList(text)
        else:
            raise EvaluateModelException("Invalid input type") from None
    
    @abstractmethod
    def evaluateFromString(self, text):
        pass

    @abstractmethod
    def evaluateFromList(self, text):
        pass

    @abstractmethod
    def evaluateFromFile(self, src):
        pass