import numpy as np

class Plane:
    def __init__(self, point, normal, ambient, diffuse, specular, shininess):
        self.point = point
        self.normal = normal
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.shininess = shininess

    def intersect(self, s, d):
        if np.dot(d, self.normal) <= 0 or np.dot(self.point-s, self.normal) <= 0:
            t = np.inf
        else:
            t = np.dot(self.point-s, self.normal)/np.dot(d, self.normal)
        return t
    
    def get_normal(self, x):
        return self.normal