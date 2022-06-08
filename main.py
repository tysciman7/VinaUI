import sys
import VinaUI



if __name__ == '__main__':
    app = VinaUI.QtWidgets.QApplication(sys.argv)
    MainWindow = VinaUI.QtWidgets.QMainWindow()
    ui = VinaUI.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


