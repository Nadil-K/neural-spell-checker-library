from enum import Enum

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