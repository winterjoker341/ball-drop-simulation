import numpy as np
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton

class ImageView(QWidget):
    def __init__(self, viewModel):
        super().__init__()
        self._viewModel = viewModel
        self._viewModel.imageChanged.connect(self.update_image)
        self.initUI()
    def initUI(self):
        self.layout = QVBoxLayout()
        self.image_label = QLabel()
        self.layout.addWidget(self.image_label)
        self.show_button = QPushButton('Show')
        self.show_button.clicked.connect(self._viewModel.calculations)
        self.layout.addWidget(self.show_button)
        self.setLayout(self.layout)
    def update_image(self, viewport):
        viewport = (viewport*255).astype(np.uint8)
        height, width, channels = viewport.shape
        image = QPixmap.fromImage(QImage(viewport.tobytes(), width, height, width*channels, QImage.Format_RGB888))
        self.image_label.setPixmap(image)
