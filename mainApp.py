import myApp
import sys

app = myApp.QtWidgets.QApplication(sys.argv)
MainWindow = myApp.QtWidgets.QMainWindow()
ui = myApp.Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

sys.exit(app.exec_())