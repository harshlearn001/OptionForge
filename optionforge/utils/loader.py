"""
OptionForge
engine/loader.py
"""

from pathlib import Path
import pandas as pd


class Loader:

    def __init__(self):

        self.option_path = None
        self.future_path = None
        self.spot_path = None

    def load_option(self, file_path):

        self.option_path = Path(file_path)

        return pd.read_csv(self.option_path)

    def load_future(self, file_path):

        self.future_path = Path(file_path)

        return pd.read_csv(self.future_path)

    def load_spot(self, file_path):

        self.spot_path = Path(file_path)

        return pd.read_csv(self.spot_path)