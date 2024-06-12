import numpy as np
from PySide6.QtCore import QObject, Signal

class ImageViewModel(QObject):
    imageChanged = Signal(np.ndarray)

    def __init__(self, model):
        super().__init__()
        self._model = model
        self._init = self._model._objects[0].center
        self.g = 0.98
        self.t = 1
        self.v = 0

    def calculations(self):
        if self._model._objects[0].center[0] >= 20: # boundary line
            self.v = -self.v
            self._model._objects[0].center[0] = 20
        self.v += self.g*self.t
        self._model._objects[0].center[0] += self.v*self.t+0.5*self.g*(self.t*self.t)
        self._model.calculations()
        self.imageChanged.emit((self._model.viewport*255).astype(np.uint8))
