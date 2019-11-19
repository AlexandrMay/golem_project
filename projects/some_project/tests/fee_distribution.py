from golem import actions as a
from projects.some_project.actions_helper import my_actions
from projects.some_project.rest_helper import api_service

description = ''

tags = []

pages = ['home_page', 'new_order_page_form', 'capture_tab_page']

def setup(data):
    pass

def test(data):
    a.navigate((data.env.url).format(data.env.login, data.env.password))
    a.wait(3)
    a.click(new_order_page_form.runningManByOrderNumber('20191001000218'))
    a.click(new_order_page_form.editOrderSummaryButton)
    a.wait(3)
    my_actions.scrollingMethod(0, 1000)
    a.click(new_order_page_form.editOITFundsButton)
    print(a.get_element_text(new_order_page_form.findElementByColumnIndex('Recordings', 1)))



def teardown(data):
    pass