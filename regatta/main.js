function newRegatta(name)  {
    console.log("You chose new: " + name)
    openRegatta(name + ".rgs")
}

function openRegatta(url) {
    console.log("You chose open: " + url)
    mainWindow.filename = url
    pageLoader.source = "" // unload any previous regatta
    pageLoader.source = "regatta.qml"
}