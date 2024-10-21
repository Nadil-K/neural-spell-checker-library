from ModelEnum import ModelEnum
from InvalidModelException import InvalidModelException


class NeuralSpellChecker:

    def __init__(self, model):
        
        try: 
            modelEnum = ModelEnum(model)
        except ValueError:
            raise InvalidModelException(f"Invalid model: {model}") from None

        modelClass = ModelEnum.getModelClass(modelEnum)
        
        self.model = modelClass()

    def check(self, text):
        # TODO: Implement the spell checking
        pass
