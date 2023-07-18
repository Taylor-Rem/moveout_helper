from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
from moveout_helper import Moveout_Helper


class App(QWidget):
    def __init__(self):
        super().__init__()

        self.helper = Moveout_Helper()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        self.setLayout(vbox)

        self.btn = QPushButton("Next", self)
        self.btn.clicked.connect(self.on_click)

        vbox.addWidget(self.btn)

    def on_click(self):
        self.helper.next_step()


if __name__ == "__main__":
    # the below lines set up a PyQt5 application
    app = QApplication([])
    ex = App()  # create an instance of our App class
    ex.show()  # show the UI
    app.exec_()  # start the application event loop
