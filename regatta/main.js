
function openFile(newfile) {
    if (newfile == true) {
        mainWindow.filename = ""
    }
    else {
        if (fileOpenDialog.fileUrls.length > 0) {
            mainWindow.filename = fileOpenDialog.fileUrls[0]
        } else {
            console.log("No file selected, should not happen on FileDialog.onAccepted")
            return
        }
    }

    console.log("You chose: " + mainWindow.filename)
    pageLoader.source = "" // unload any previous contacts
    pageLoader.source = "regatta.qml"

}