import os
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class ImageAnnotator(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the layout
        self.setWindowTitle("Image Annotator")
        self.setGeometry(100, 100, 800, 600)
        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)

        # Left panel layout
        self.left_panel_layout = QVBoxLayout()

        # List widget to show image files
        self.file_list_widget = QListWidget()
        self.file_list_widget.itemClicked.connect(self.load_image)
        self.left_panel_layout.addWidget(self.file_list_widget)

        # Load folder button
        self.load_folder_button = QPushButton("Load Folder")
        self.load_folder_button.clicked.connect(self.open_folder)
        self.left_panel_layout.addWidget(self.load_folder_button)

        # Add the left panel to the main layout
        self.main_layout.addLayout(self.left_panel_layout, 1)

        # Image display area
        self.image_label = QLabel("Select an image to annotate")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setFixedSize(600, 600)
        self.main_layout.addWidget(self.image_label, 3)

    def open_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Image Folder")
        if folder_path:
            self.load_images_from_folder(folder_path)

    def load_images_from_folder(self, folder_path):
        # Clear the list widget
        self.file_list_widget.clear()

        # Get image files from the selected folder
        supported_formats = [".png", ".jpg", ".jpeg", ".bmp", ".gif"]
        for file_name in os.listdir(folder_path):
            if any(file_name.lower().endswith(ext) for ext in supported_formats):
                self.file_list_widget.addItem(file_name)

        # Store folder path for later use
        self.current_folder_path = folder_path

    def load_image(self, item):
        # Load and display the selected image
        image_file_path = os.path.join(self.current_folder_path, item.text())
        pixmap = QPixmap(image_file_path)
        self.image_label.setPixmap(
            pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageAnnotator()
    window.show()
    sys.exit(app.exec_())
