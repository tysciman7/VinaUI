import sys
import loadMainUI
import directoryManager
import runFunctions
import os

if __name__ == '__main__':
    # Initialize Project Home Path
    directoryManager.set_project_path(os.getcwd())

    # Initializes VinaUI Application
    app = loadMainUI.QApplication(sys.argv)
    MainWindow = loadMainUI.QMainWindow()
    UIWindow = loadMainUI.MainUi()
    UIWindow.show()


    # Initializes Config File and associated paths
    directoryManager.init_config(UIWindow)
    UIWindow.init_all()
    runFunctions.init_paths()



    # Ends Application
    sys.exit(app.exec_())


