
function openFile() {    
    console.log("You chose: " + fileOpenDialog.fileUrls)
    pageLoader.source = "" // unload any previous regatta
    pageLoader.source = "regatta.qml"
}
