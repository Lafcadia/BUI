from mcserverbackup import observe
from ui import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
import sys
from multiprocessing import Process as P
import multiprocessing as m

def customObserve(path, timer, file_type, q):
    q.start()
    p = P(target=observe, args=(path, timer, file_type))
    p.start()
    p.join()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.path = ""
        self.q = None
        self.timer = None
        self.file_type = ""
        self.started = False
        self.ui.StartStop.clicked.connect(self.startStopper)
        self.ui.chooser.clicked.connect(self.chooser)
    
    def chooser(self):
        self.path = QFileDialog.getExistingDirectory(self, "Choose the Directory to Monitor", "./")
        QMessageBox.information(self, "Path to monitor is chosen!", "Path to monitor is chosen!")
    
    def startStopper(self):
        self.file_type = "tar" if self.ui.comboBox.currentText() == "Save as tar" else ("zip" if self.ui.comboBox.currentText() == "Save as zip" else None)
        self.timer = float(self.ui.lineEdit.text())
        if not self.started:
            self.started = True
            self.ui.StartStop.setText("Stop")
            self.q = m.Queue()
            customObserve(self.path, self.timer, self.file_type, self.q)
        else:
            self.started = False
            self.ui.StartStop.setText("Start")
            self.q.put(0)
            self.q.get()

if __name__ == "__main__":
    m.freeze_support()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())