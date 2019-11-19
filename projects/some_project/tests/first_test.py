from golem import actions as a
from projects.some_project.rest_helper import api_service
import requests

description = 'Test is checking the values from ui tabs and response of "GetQueuesItemCounts" query'

tags = ['example']

pages = ['home_page']

def setup(data):
    pass

def test(data):
    #Ui part: navigating to mainpage and getting the values of counters for all tabs
    a.navigate((data.env.url).format(get_secrets().login, get_secrets().password))
    a.wait(10) #waiting for page loading
    valuesFromUI = []
    for i in home_page.tabsValues():
        valuesFromUI.append(a.get_element_text(i)) #filling the array by parsed values from ui
    print(valuesFromUI)
    #Getting coockies from browser to send http-request
    cookiesFromUi = a.get_cookie(data.env.cookieName)
    sessionId = cookiesFromUi['value']
    #Sending an http-reques using 'requests' python library
    response = requests.get(data.env.getItemsLink, headers={"Cookie": "{}={}".format(data.env.cookieName, sessionId)})
    receivedValues = api_service.deserializationOfResponse(response, api_service.neededParameters)
    print(receivedValues)
    for i in range(len(receivedValues)):
        a.assert_equals(valuesFromUI[i], receivedValues[i])

def teardown(data):
    pass
