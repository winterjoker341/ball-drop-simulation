import numpy as np
from PySide6.QtCore import QObject, Signal

class ImageViewModel(QObject):
    imageChanged = Signal(np.ndarray)

    def __init__(self, model):
        super().__init__()
        self._model = model
    def calculations(self):
        self._model.calculations()
        self.imageChanged.emit(self._model.viewport)
