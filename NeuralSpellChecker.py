from ModelEnum import ModelEnum
from InvalidModelException import InvalidModelException


class NeuralSpellChecker:

    def __init__(self, model, from_pretrained=False):
        
        try: 
            modelEnum = ModelEnum(model)
        except ValueError:
            raise InvalidModelException(f"Invalid model: {model}") from None

        modelClass = ModelEnum.getModelClass(modelEnum)
        modelClassInstance = modelClass(from_pretrained)

        self.model = modelClassInstance.model
        self.tokenizer = modelClassInstance.tokenizer

    def check(self, text):
        # TODO: Implement the spell checking
        pass



    ### Helper functions

    def get_tokenizer(self):
        return self.tokenizer
    
    def get_model(self):
        return self.model