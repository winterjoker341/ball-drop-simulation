import sys
import numpy as np
from PySide6.QtWidgets import QApplication
from model.image_model import ImageModel
from viewmodel.image_view_model import ImageViewModel
from view.image_view import ImageView
from model.light_model import Light
from model.sphere_model import Sphere

def main():
    light = Light(np.array([-100, -100, 0]), np.array([1, 1, 1]), np.array([1, 1, 1]), np.array([1, 1, 1]))
    objects = Sphere(np.array([0, 0, 0]), 50, np.array([1, 0, 1]), np.array([1, 1, 0]), np.array([1, 1, 1]), 80)

    app = QApplication(sys.argv) # ^^
    model = ImageModel(light, objects, [250, 250])
    viewModel = ImageViewModel(model)
    view = ImageView(viewModel)
    view.show()
    sys.exit(app.exec())

if __name__=="__main__":
    main()
