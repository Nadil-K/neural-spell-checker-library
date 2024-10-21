from enum import Enum

from Models.Llama31BaseModel import Llama31BaseModel
from Models.Mbart50LargeModel import Mbart50LargeModel
from Models.Mt5BaseModel import Mt5BaseModel
from Models.SinBertLargeModel import SinBertLargeModel
from Models.XlmrBaseModel import XlmrBaseModel

class ModelEnum(Enum):
    """
    Enum class for all the models supported by the 
    Neural Spell Checker Library
    """

    LLAMA_31_8B = "meta-llama/Llama-3.1-8B"
    MBART50_LARGE = "facebook/mbart-large-50"
    MT5_BASE = "google/mt5-base"
    XLMR_BASE = "FacebookAI/xlm-roberta-base"
    SINBERT_LARGE = "NLPC-UOM/SinBERT-large"


    def getModelClass(modelEnum):

        modelClasses = {
            ModelEnum.LLAMA_31_8B: Llama31BaseModel,
            ModelEnum.MBART50_LARGE: Mbart50LargeModel,
            ModelEnum.MT5_BASE: Mt5BaseModel,
            ModelEnum.XLMR_BASE: XlmrBaseModel,
            ModelEnum.SINBERT_LARGE: SinBertLargeModel
        }
        return modelClasses[modelEnum]