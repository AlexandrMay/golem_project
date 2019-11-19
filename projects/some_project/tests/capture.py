from golem import actions as a
from projects.some_project.actions_helper import my_actions
#from projects.some_project.pages import new_order_page_form

description = ''

tags = ['']

pages = ['home_page', 'new_order_page_header', 'new_order_page_form', 'new_order_page_footer']

#table = new_order_page_form.TableHelper('OrderQueue')

def setup(data):
    pass

def test(data):
    a.navigate((data.env.url).format(data.env.login, data.env.password))
    a.click(home_page.captureTab)
    a.wait(3)
    a.focus_element(new_order_page_form.runningManByDocNumber('AA0012919'))
    a.click(new_order_page_form.runningManByDocNumber('AA0012919'))
    a.wait(5)
    #print(a.get_element_text(new_order_page_form.findElementByString('Department', '20191002000145')))
    #print(a.get_element_text(new_order_page_form.findElementByHeaderTitle('Customer', 3)))
    

def teardown(data):
    a.close_browser()