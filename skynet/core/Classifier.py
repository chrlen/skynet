import BaseService
import abc


class Classifier(BaseService):
    def __init__(self, args, kwargs):
        super(Classifier).__init__(args, kwargs)

    @abc.abstractmethod
    def classify(self, data):
        """ Implement this method to classify the passed data """
