import numpy as np
from PySide6.QtCore import QObject, Signal

class ImageViewModel(QObject):
    imageChanged = Signal(np.ndarray)

    def __init__(self, model):
        super().__init__()
        self._model = model
        self.g = 0.98
        self.t = 0

    def calculations(self):
        if self._model._objects[0].center[0] <= 100: # boundary line
            self._model._objects[0].center[0] += self.g*self.t
            self.t += 1
        self._model.calculations()
        self.imageChanged.emit((self._model.viewport*255).astype(np.uint8))
