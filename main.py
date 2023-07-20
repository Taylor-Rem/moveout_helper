from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
from moveout_helper import Moveout_Helper
from webdriver_operations import WebDriverOperations


class App(QWidget):
    def __init__(self):
        super().__init__()

        self.helper = Moveout_Helper(self)
        self.webdriver = WebDriverOperations()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        self.setLayout(vbox)

        self.add_btn = QPushButton("Add", self)
        self.skip_btn = QPushButton("Skip", self)
        self.quit_btn = QPushButton("Quit", self)

        self.add_btn.clicked.connect(self.add)
        self.skip_btn.clicked.connect(self.skip)
        self.quit_btn.clicked.connect(self.quit_app)

        vbox.addWidget(self.add_btn)
        vbox.addWidget(self.skip_btn)
        vbox.addWidget(self.quit_btn)

    def add(self):
        self.helper.add_button()

    def skip(self):
        self.helper.next_step()

    def quit_app(self):
        self.close()
        self.webdriver.driver.quit()


if __name__ == "__main__":
    app = QApplication([])
    ex = App()
    ex.show()
    app.exec_()
