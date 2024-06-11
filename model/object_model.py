import numpy as np
import math

class Sphere:
    def __init__(self, center, radius, ambient, diffuse, specular, shininess):
        self.center = center
        self.radius = radius
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.shininess = shininess

    def intersect(self, s, d):
        v = s-self.center
        D = math.pow(np.dot(v, d), 2)-(np.dot(v, v)-math.pow(self.radius, 2))
        if D > 0:
            p_t = -np.dot(v, d)+np.sqrt(D)
            m_t = -np.dot(v, d)-np.sqrt(D)
            t = min(p_t, m_t)
        elif D == 0:
            t = -np.dot(v, d)+np.sqrt(D)
        else:
            t = np.inf
        return t
        
    def get_normal(self, x):
        return self.center-x

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
