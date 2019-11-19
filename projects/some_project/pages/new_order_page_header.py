from golem import actions

golemDriver = actions.get_browser()

accountInput = ()

emailInput = ()

nameInput = ("xpath", "//input[@placeholder='Name']", "nameInput")

orderTypeDropdown = ('id', 'orderTypeId', 'orderTypeDropdown')

accountAlert = ('css', '#orderentrypanel > span', 'accountAlert')

orderNumber = ('id', 'orderNumber', 'orderNumber')

def orderTypeDropdownElement(text):
    return golemDriver.find(xpath="//select[@id='orderTypeId']/option[text()='{}']".format(text))
