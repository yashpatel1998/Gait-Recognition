import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QDir, QUrl, Qt
import os
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import QThread

class appWindows(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Gait Recognition'
        self.left = 50
        self.top = 50
        self.width = 1280
        self.height = 720
        self.file_name =''
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.setWindowIcon(QIcon(os.getcwd() + "\\gait_logo.jpg"))

        """     TextBox     """
        textBox = QLineEdit()

        """     Video Widget    """
        video_widget = QVideoWidget()

        """     Close Button    """
        close_button = QPushButton("Close", self)
        close_button.setToolTip("Click to Close Window")
        close_button.clicked.connect(self.display_message_box)

        """     Select Video Button     """
        select_video_button = QPushButton("Select File", self)
        select_video_button.setToolTip("Choose File")
        select_video_button.clicked.connect(self.choose_file)

        """     Predict     """
        predict_button = QPushButton("Predict",self)
        predict_button.clicked.connect(self.start_prediction)

        """     Give Layout to Boxes      """
        hbox = QHBoxLayout()
        hbox.addWidget(select_video_button)
        hbox.addWidget(predict_button)
        hbox.addWidget(close_button)
        mainlayout = QVBoxLayout()
        mainlayout.addWidget(video_widget)
        mainlayout.addWidget(textBox)
        mainlayout.addLayout(hbox)
        self.setLayout(mainlayout)

        self.mediaPlayer.setVideoOutput(video_widget)

        self.show()

    def display_message_box(self):
        reply = QMessageBox.question(self, "Close Message", "Do you want to quit ?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()

    def close_window(self):
        QCoreApplication.instance().quit()

    def choose_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File")
        if file_name != '':
            self.file_name = file_name
            self.mediaPlayer.setMedia(
                QMediaContent(QUrl.fromLocalFile(file_name)))

    def start_prediction(self):
        file_n = self.file_name
        print(file_n)
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = appWindows()
    sys.exit(app.exec_())