from golem import actions as a
from projects.some_project.actions_helper import my_actions
from projects.some_project.rest_helper import api_service

description = 'Order indexing flow'

tags = ['order_workflow']

pages = ['home_page', 'new_order_page_form', 'new_order_page_footer']

def setup(data):
    pass

def test(data):
    a.navigate((data.env.url).format(data.env.login, data.env.password))
    a.click(home_page.indexingTab)
    my_actions.expandAllTableElements()
    my_actions.scrollToTableElement(api_service.readFromJson('order_number'))
    a.wait(20)

def teardown(data):
    pass
