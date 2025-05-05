from .model import AraFixModel
from .preprocess import preprocess
from .postprocess import postprocess

class AraFix:
    def __init__(self):
        self.model = AraFixModel()
        
    def correct(self, text):
        """Full pipeline: preprocess -> model -> postprocess"""
        
        # correct multiple sentences
        if isinstance(text, list):
            preprocessed = [preprocess(t) for t in text]
            print("Correcting ...")
            model_outputs = [self.model.predict(t)[0] for t in preprocessed]
            results = [postprocess(m, p) for m, p in zip(model_outputs, preprocessed)]
            return results

        # correct single sentence
        preprocessed = preprocess(text)
        print("Correcting ...")
        model_output = self.model.predict(preprocessed)
        model_output = model_output[0]
        result = postprocess(model_output, preprocessed)
        return result
    
    
    def evaluate(self, references, hypotheses):

        from jiwer import cer, wer
        from .der import der

        if isinstance(references, list) or isinstance(hypotheses, list):
            der_scores = [der(ref, hyp) for ref, hyp in zip(references, hypotheses)]

        metrics = {
            "cer": cer(references, hypotheses),
            "wer": wer(references, hypotheses),
            "der": sum(der_scores) / len(der_scores) if der_scores else 0,
        }

        return metrics
