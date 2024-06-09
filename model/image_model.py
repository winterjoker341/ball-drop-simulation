import numpy as np
import math

def normalize(vec):
    return vec/np.linalg.norm(vec)

class ImageModel:
    def __init__(self, light, objects, size):
        self._light = light
        self._objects = objects
        self._size = size
        self.target = np.array([0, 0, 0])
        self.eye = np.array([0, 0, -100])
        self.vec_v = np.array([0, 1, 0])
        self.viewport = np.zeros((self._size[0], self._size[1], 3))
        self.pre_calculations()
        self.calculate_viewport_size()
        self.calculate_shifting_vectors()
    def pre_calculations(self):
        self.vec_t_n = normalize(self.target-self.eye)
        self.vec_b_n = normalize(np.cross(self.vec_v, self.vec_t_n))
        self.vec_v_n = np.cross(self.vec_t_n, self.vec_b_n)
    def calculate_viewport_size(self):
        self.g_x = (self._size[1]/2)*math.tan(math.pi/4)
        self.g_y = self.g_x*(self._size[0]-1)/(self._size[1]-1)
    def calculate_shifting_vectors(self):
        self.vec_q_x = (2*self.g_x/(self._size[1]-1))*self.vec_b_n
        self.vec_q_y = (2*self.g_y/(self._size[0]-1))*self.vec_v_n
        self.vec_p_1m = self.vec_t_n*(self._size[1]/2)-self.g_x*self.vec_b_n-self.g_y*self.vec_v_n
    def calculations(self):
        for i in range(1, self._size[0]+1):
            for j in range(1, self._size[1]+1):
                vec_r_ij = normalize(self.vec_p_1m+self.vec_q_x*(i-1)+self.vec_q_y*(j-1))
                self.viewport[i-1][j-1] = np.clip(self.phong_reflection_model(self._light, self._objects, self.eye, vec_r_ij), 0, 1)
    def phong_reflection_model(self, light, objects, s, d):
        v = s-objects.center
        t = objects.intersect(v, d)
        if t == -1:
            return np.array([1, 1, 1])

        x = s+t*d
        L = normalize(x-light.center)
        V = normalize(x-s)
        N = objects.get_normal(x)
        H = normalize(L+V)
        
        I_p = np.zeros((3))
        I_p += objects.ambient*light.ambient
        I_p += objects.diffuse*light.diffuse*np.dot(L, N)
        I_p += objects.specular*light.specular*math.pow(max(0, np.dot(N, H)), objects.shininess)
        return I_p
