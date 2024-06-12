import numpy as np

class Light:
    def __init__(self, center, ambient, diffuse, specular):
        self.center = center
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
