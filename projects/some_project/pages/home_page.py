from golem import actions

golemDriver = actions.get_browser()

addNewOrderButton = ('id', 'addNewOrder', 'addNewOrderButton')

ordersTab = ('css', '#orders > a', 'ordersTab')

captureTab = ('css', '#capture > a', 'captureTab')

indexingTab = ('css', '#indexing > a', 'indexingTab')

verificationTab = ('css', '#verification > a', 'verificationTab')

headersCounter = ('css', '.fleft > h3 > span', 'headersCounter')

def tabsValues():
    return golemDriver.find_all(css='.navigation > nav > ul > li > a > span')



