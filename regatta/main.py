import os
import sys

from PyQt5 import QtCore, QtQml, QtQuick, QtWidgets

from q_regatta import QRegatta


#def main():
osname = os.name.lower()
sysplatform = sys.platform.lower()
windows = os.name.lower() == "nt" and sysplatform.startswith("win")

QtQml.qmlRegisterType(QRegatta, 'Regatta', 1, 0, 'Regatta')

app = QtWidgets.QApplication(sys.argv)

# Create the QML engine
engine = QtQml.QQmlEngine(app)
engine.quit.connect(app.quit)

# Load the main.qml file and create the toplevel component 
component = QtQml.QQmlComponent(engine)
currentFilePath = os.path.dirname(os.path.abspath(__file__))
mainFilepath = os.path.join(currentFilePath, "main.qml")
if windows:
    mainFilepath = mainFilepath.replace('\\', '/')
qmlFile = QtCore.QUrl("file:///" + mainFilepath)
component.loadUrl(qmlFile)
topLevelItem = component.create()

topLevelItem.show()
sys.exit(app.exec_())
 
#if __name__ == "__main__":
#    main()

   
