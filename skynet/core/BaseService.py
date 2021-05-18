import abc
import validation as val


class BaseService(abc.ABC):
    def __init__(self, args, kwargs):
        self.name = "skynode"

    def preprocess(self, data):
        return data

    def postprocess(self, data):
        return data

    def process(self, function, data):
        preprocessed = self.preprocess(data)
        val.idate_input(preprocessed)
        transformed = function(preprocessed)
        postprocessed = self.preprocess(data)
        val.idate_output(postprocessed)
        return data
