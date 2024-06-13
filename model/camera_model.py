import numpy as np

class Camera:
    def __init__(self, target, eye, vec_v):
        self.target = target
        self.eye = eye
        self.vec_v = vec_v
