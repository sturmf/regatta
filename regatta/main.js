function newRegatta(name)  {
    console.log("You chose new: " + name)
    openRegatta(name + ".rgs")
}

function openRegatta(url) {
    console.log("You chose open: " + url)
    // Here we first create a model instance with the given url and then load the gui
    // There are two reasons for this, one is that we want to have a fully constructed
    // model before the gui reads out properties, the other is that we don't want to
    // have the model imported in the gui or it otherwise couldn't be loaded in qtcreator
    // anymore
    var component = qRegattaFactory.createObject(mainWindow, {filename: url})
    pageLoader.setSource("regatta.qml", {regatta: component})
}