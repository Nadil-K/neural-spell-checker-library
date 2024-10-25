from abc import ABC, abstractmethod

class ModelAbstract(ABC):
    def __init__(self, from_pretrained):
        self.tokenizer = None
        self.model = None
        pass

    @abstractmethod
    def check(self, text):
        pass