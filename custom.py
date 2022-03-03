from ocr import ocrImage

def load_model(input_dir):
    return "dummy"

def score_unstructured(model, data, query, **kwargs):
    result = ocrImage(data)
    return result
