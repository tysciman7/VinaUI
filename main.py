import sys
import VinaUI
import directoryManager
import runFunctions

if __name__ == '__main__':
    # Initializes VinaUI Application
    app = VinaUI.QtWidgets.QApplication(sys.argv)
    MainWindow = VinaUI.QtWidgets.QMainWindow()
    ui = VinaUI.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    # Initializes Config File and associated paths
    directoryManager.init_config(ui)
    ui.init_all()
    runFunctions.init_paths()



    # Ends Application
    sys.exit(app.exec_())


