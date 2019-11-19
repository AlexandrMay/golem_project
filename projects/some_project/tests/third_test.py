from golem import actions as a

description = 'Test is checking the accordance of counters of the tabs with the headers values in tabs'

tags = ['example']

pages = ['home_page']

def setup(data):
    pass

def test(data):
    a.navigate((data.env.url).format(data.env.login, data.env.password))
    a.wait(10)
    tabs = [home_page.ordersTab, home_page.captureTab, home_page.indexingTab, home_page.verificationTab]
    valuesFromUI = []
    valuesFromHeaders = []
    for i in home_page.tabsValues():
        valuesFromUI.append(a.get_element_text(i))
    print(valuesFromUI)
    for i in range(len(tabs)):
        a.click(tabs[i])
        a.wait(2)
        valuesFromHeaders.append(a.get_element_text(home_page.headersCounter))
    print(valuesFromHeaders)
    for i in range(len(valuesFromHeaders)):
        a.assert_equals(valuesFromUI[i], valuesFromHeaders[i])

def teardown(data):
    pass