from ModelEnum import ModelEnum
from InvalidModelException import InvalidModelException

from Models.Mbart50LargeModel import Mbart50LargeModel

class NeuralSpellChecker:

    def __init__(self, model):
        
        try: 
            modelEnum = ModelEnum(model)
        except ValueError:
            raise InvalidModelException(f"Invalid model: {model}") from None

        if modelEnum == ModelEnum.MBART50_LARGE:
            self.model = Mbart50LargeModel()

    def check(self, text):
        # TODO: Implement the spell checking
        pass
