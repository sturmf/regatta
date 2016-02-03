function newRegatta(name)  {
    console.log("You chose new: " + name)
    openRegatta(name + ".rgs")
}

function openRegatta(url) {
    console.log("You chose open: " + url)
    mainWindow.filename = url

    // Here we first create a model instance with the given filename and then load the gui
    var component = qRegattaFactory.createObject(mainWindow, {filename: mainWindow.filename})
    pageLoader.setSource("regatta.qml", {regatta: component})


}