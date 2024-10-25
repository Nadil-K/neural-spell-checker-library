from Models.ModelAbstract import ModelAbstract

from transformers import MT5Tokenizer, MT5ForConditionalGeneration
import tqdm

class Mt5BaseModel(ModelAbstract):
    def __init__(self, from_pretrained):

        if not from_pretrained:
            print('Loading MT5 Base Model with tokenizer...')
            self.tokenizer = MT5Tokenizer.from_pretrained("google/mt5-small")
            self.model = MT5ForConditionalGeneration.from_pretrained("google/mt5-small")
        else:
            print('MT5 Base Model with tokenizer from custom directory...')
            self.tokenizer = None
            self.model = None

    def check(self, text):
        pass