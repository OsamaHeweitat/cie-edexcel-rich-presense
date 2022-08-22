import sys, os, time, json
os.chdir(sys._MEIPASS)
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox
from gui import Ui_MainWindow
from pypresence import Presence

client_id = "1008722576035565578"
RPC = Presence(client_id)
RPC.connect()

with open(os.path.dirname(__file__) + "/dict.json/dict.json") as f:
    data = f.read()
js = json.loads(data)

os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
app = QApplication(sys.argv)
class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi(self)
        self.cieIgcseBox.activated.connect(lambda x: self.comboBoxChanged(self.cieIgcseBox, self.cieIgcseBox.currentText()))
        self.edexcelIgcseBox.activated.connect(lambda x: self.comboBoxChanged(self.edexcelIgcseBox, self.edexcelIgcseBox.currentText()))
        self.cieALevelBox.activated.connect(lambda x: self.comboBoxChanged(self.cieALevelBox, self.cieALevelBox.currentText()))
        self.edexcelALevelBox.activated.connect(lambda x: self.comboBoxChanged(self.edexcelALevelBox, self.edexcelALevelBox.currentText()))


    def comboBoxChanged(self, box:QComboBox, subject:str):
        if(box.objectName() == "cieIgcseBox"):
            code_name = js[box.currentText()[-4:]]
            RPC.update(details=subject, state="CAIE IGCSE", large_image=code_name, large_text=code_name.title().replace("_", " "), start=time.time())
        elif(box.objectName() == "edexcelIgcseBox"):
            RPC.update(details=subject, state="Edexcel IGCSE", large_image=js[subject], large_text=subject, start=time.time())
        elif(box.objectName() == "cieALevelBox"):
            code_name = js[box.currentText()[-4:]]
            RPC.update(details=subject, state="CAIE A-Level", large_image=code_name, large_text=code_name.title().replace("_", " "), start=time.time())
        elif(box.objectName() == "edexcelALevelBox"):
            RPC.update(details=subject, state="Edexcel IAL", large_image=js[subject], large_text=subject, start=time.time())

window = Window()
window.show()
sys.exit(app.exec_())
