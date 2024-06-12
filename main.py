import sys
import numpy as np
from PySide6.QtWidgets import QApplication
from model.image_model import ImageModel
from viewmodel.image_view_model import ImageViewModel
from view.image_view import ImageView
from model.light_model import Light
from model.camera_model import Camera
from model.object_model import Sphere, Plane

def main():
    camera = Camera(np.array([-70, 0, 0]), np.array([-70, 0, -200]), np.array([0, 1, 0]))
    light = Light(np.array([-250, -100, 0]), np.array([1, 1, 1]), np.array([1, 1, 1]), np.array([1, 1, 1]))
    objects = [
        Sphere(np.array([-200, 0, 100]), 50, np.array([1, 0, 0]), np.array([1, 0, 0]), np.array([1, 0, 0]), 80),
        Plane(np.array([100, 0, 100]), np.array([1, 0, 0]), np.array([0, 1, 0]), np.array([0, 1, 0]), np.array([0, 1, 0]), 100)
    ]
    app = QApplication(sys.argv) # ^^
    model = ImageModel(camera, light, objects, [80, 80])
    viewModel = ImageViewModel(model)
    view = ImageView(viewModel)
    view.show()
    sys.exit(app.exec())

if __name__=="__main__":
    main()
