import numpy as np
from PySide6.QtCore import QTimer, QSize, Qt
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton

class ImageView(QWidget):
    def __init__(self, viewModel):
        super().__init__()
        self._viewModel = viewModel
        self._viewModel.imageChanged.connect(self.update_pixmap)
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.pixmap_label = QLabel()
        self.layout.addWidget(self.pixmap_label)
        self.run_button = QPushButton('RUN')
        self.run_button.clicked.connect(self.run)
        self.layout.addWidget(self.run_button)
        self.setLayout(self.layout)
    
    def run(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self._viewModel.calculations)
        self.timer.start(0)
    
    def update_pixmap(self, viewport):
        height, width, channels = viewport.shape
        pixmap = QPixmap.fromImage(QImage(viewport.tobytes(), width, height, width*channels, QImage.Format_RGB888))
        pixmap = pixmap.scaled(QSize(500, 500), aspectMode=Qt.KeepAspectRatio)
        self.pixmap_label.setPixmap(pixmap)
