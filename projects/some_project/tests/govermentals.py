from golem import actions as a
from projects.some_project.actions_helper import my_actions
from projects.some_project.pages import new_order_page_form

description = ''

tags = ['']

pages = ['home_page', 'new_order_page_header', 'new_order_page_form', 'new_order_page_footer']

table = new_order_page_form.TableHelper()

def setup(data):
    pass

def test(data):
    a.navigate((data.env.url).format(data.env.login, data.env.password))
    a.click(home_page.addNewOrderButton)
    a.wait(3)
    a.click(new_order_page_header.orderTypeDropdown)
    a.click(new_order_page_header.orderTypeDropdownElement('Governmentals'))
    a.send_keys(new_order_page_header.nameInput, 'test_name')
    a.wait(3)
    a.click(new_order_page_form.documentTypeDropdown)
    a.click(new_order_page_form.documentTypeDropdownElement('ADOPTION PETITION'))
    a.send_keys(new_order_page_form.numberOfPages, '1')
    my_actions.scrollingMethod(0, 1000)
    a.click(new_order_page_footer.addToOrderButton)
    print(a.get_element_text(table.findElementByTitle('none', 3)))


def teardown(data):
    pass