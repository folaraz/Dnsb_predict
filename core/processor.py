import pickle as pk
import pandas as pd
import os
from .model import test

CUR_PATH = os.sep.join(os.path.realpath(__file__).split(os.sep)[:-1])


class Processor:
    def __init__(self, model_path, file_path):
        self.gbr = pk.load(open(model_path, "rb"))
        self.file_path = file_path

    def run(self):
        submission = pd.read_csv(self.file_path)
        submission.iloc[:, 1] = self.gbr.predict(test)
        submission.to_csv(os.path.join(CUR_PATH, '..', 'output', 'send.csv'), index=None)
