from golem import actions

golemDriver = actions.get_browser()

#Heading

startBatchScan = ('id', 'startBatchScan', 'startScanButton')

startScanButton = ("xpath", "//a[@class='startBatchScanBtn clickable']")

#Mapping form

editButton = ('css', '.orderAdminiconedit', 'editButton')

imagesField = ("xpath", "//td[@data-column='Scanned']/div/span", "imagesField")

def mappingInputs():
    return golemDriver.find_all(xpath="//div[@class='floating-field']/input")

def docGroupInput():
    return mappingInputs()[0]

def docTypeInput():
    return mappingInputs()[1]

def recordedYear():
    return mappingInputs()[2]

def docNumber():
    return mappingInputs()[3]

def pagesInput():
    return mappingInputs()[4]

#Footer

saveAndExit = ('css', '#addToOrderOuter > input', 'saveAndExit')