import os
import sys

from PyQt5 import QtCore, QtQml, QtWidgets

from regattaitemmodel import RegattaItemModel
from q_regatta import QRegatta

# Fixme: I have no idea why I can't put it in a method
# def main():

osname = os.name.lower()
sysplatform = sys.platform.lower()
windows = os.name.lower() == "nt" and sysplatform.startswith("win")

# PyQt class name, QML URI, major version, minor version, QML type name
QtQml.qmlRegisterType(RegattaItemModel, 'RegattaItemModel', 1, 0, 'RegattaItemModel')
QtQml.qmlRegisterType(QRegatta, 'QRegatta', 1, 0, 'QRegatta')

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
if component.status() != QtQml.QQmlComponent.Ready:
    for error in component.errors():
        print(error.toString())
    sys.exit(-1)

topLevelItem = component.create()
if not topLevelItem:
    for error in component.errors():
        print(error.toString())
    sys.exit(-1)

# Now run the main loop until the user closes the application
topLevelItem.show()
sys.exit(app.exec_())

# if __name__ == "__main__":
#     main()
