from ModelEnum import ModelEnum
from InvalidModelException import InvalidModelException
from EvaluateModelException import EvaluateModelException

class NeuralSpellChecker:

    def __init__(self, model, from_pretrained=False):
        
        try: 
            modelEnum = ModelEnum(model)
        except ValueError:
            raise InvalidModelException(f"Invalid model: {model}") from None

        modelClass = ModelEnum.getModelClass(modelEnum)
        self.modelClassInstance = modelClassInstance = modelClass(from_pretrained)

        self.model = modelClassInstance.model
        self.tokenizer = modelClassInstance.tokenizer

    def evaluate(self, text=None, src=None):

        if text is None and src is None:
            raise EvaluateModelException("Either text or src is required") from None
        else:
            self.modelClassInstance.evaluate(text, src)



    ### Helper functions

    def get_tokenizer(self):
        return self.tokenizer
    
    def get_model(self):
        return self.model