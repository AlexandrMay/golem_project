from golem import actions as a

golemDriver = a.get_browser()

def firstNameInput(text):
    return golemDriver.find(xpath="//div[@class='block-header-with-bg']/label[text()='{}']/parent::div/following-sibling::div//input[@placeholder='First Name']".format(text))

partiesTab = ("xpath", "//ul[@id='orderTypeTabs']/li[@data-bind-id='partiesTab']/a", "partiesTab")

propertiesTab = ("xpath", "//ul[@id='orderTypeTabs']/li[@data-bind-id='propetiesTab']/a", "propertiesTab")

amountField = ('id', 'Payment', 'amountField')

parcelIdInput = ("xpath", "//input[@placeholder='Parcel ID']", "partiesTab")

documentTypeDropdown = ('id', 'Order_OrderItems[0]_Document_DocumentTypeId', 'documentTypeDropdown')

numberOfPages = ('id', 'NoOfPage', 'numberOfPages')

numberOfLots = ('id', 'NoOfLots', 'numberOfLots')

paymentMethodDropdown = ("xpath", "//select[@class='pagedropdown width80']")

balanceOwed = ('id', 'balanceOwed', 'balanceOwed')

amountInput = ("xpath", "//ul[@class='horizantal']/li[4]/input")

documentNumber = ("xpath", "//td[@data-column='Document_InstrumentNumber']")

newOrderItemButton = ('css', '#newOrderItem > a', 'newOrderItemButton')

editOrderSummaryButton = ('css', '.orderSummaryiconeditContainer > a', 'editOrderSummaryButton')

editOITFundsButton = ('css', '.orderSummaryBottomLinks > a', 'editOITFundsButton')

def paymentMethodDropdownElement(text):
    return golemDriver.find(xpath="//select[@class='pagedropdown width80']/option[text()='{}']".format(text))

def documentTypeDropdownElement(text):
    return golemDriver.find(xpath="//select[@id='Order_OrderItems[0]_Document_DocumentTypeId']/option[text()='{}']".format(text))


#Queue tables methods

def runningManByOrderNumber(orderNumber: str):
    if (a.get_window_title() == 'Capture Queue'):
        return golemDriver.find(xpath="//table//td[contains(text(),'{}')]/following-sibling::td/a[@class='iconbatchscan reprocess adminmode']".format(orderNumber))
    else:
        return golemDriver.find(xpath="//table//td/span[contains(text(),'{}')]/parent::td/following-sibling::td/a[@class='iconredirectorder ']".format(orderNumber))


def runningManByDocNumber(docNumber: str):
    if (a.get_window_title() == 'Capture Queue'):
        return golemDriver.find(xpath="//table//td[contains(text(),'{}')]/following-sibling::td/a[@class='iconbatchscan reprocess adminmode']".format(docNumber))
    else:
        return golemDriver.find(xpath="//table//td[contains(text(),'{}')]/following-sibling::td/a[@class='iconredirectorder ']".format(docNumber))

#Additional methods

def titleElements():
    return golemDriver.find_all(xpath="//table//tr/th")

def rawElements(index: int):
    return golemDriver.find_all(xpath="//table//tr[{}]/td".format(index))

def rawsElements():
    return golemDriver.find_all(xpath="//table//tr")

def findRawIndexByText(text: str):
    for i in range(len(rawsElements())):
        for j in range(len(rawElements(i))):
            if(a.get_element_text(rawElements(i)[j]) == text):
                return i

def findElementByHeaderTitle(title: str, raw: int):
    for i in range(len(titleElements())):
        if(a.get_element_text(titleElements()[i]) == title):
            if (a.get_window_title() == 'Order Summary'):
                return rawElements(raw)[i+1]
            else:
                return rawElements(raw)[i]

def findElementWithHeaderByString(title: str, string: str):
    for i in range(len(titleElements())):
        if(a.get_element_text(titleElements()[i]) == title):
            return rawElements(findRawIndexByText(string))[i]

def findElementByColumnIndex(string: str, index: int):
    return rawElements(findRawIndexByText(string))[index]








    