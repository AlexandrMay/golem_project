from golem import actions as a
from projects.some_project.actions_helper import my_actions


description = 'Testing of Account alert appearing when account field is empty'

tags = ['example']

pages = ['new_order_page_header', 'home_page', 'new_order_page_form', 'new_order_page_footer']

def setup(data):
    pass

def test(data):
    a.navigate((data.env.url).format(data.env.login, data.env.password))
    a.click(home_page.addNewOrderButton)
    a.wait(3)
    a.click(new_order_page_header.orderTypeDropdown)
    a.click(new_order_page_header.orderTypeDropdownElement(data.order_type))
    a.click(new_order_page_form.documentTypeDropdown)
    a.click(new_order_page_form.documentTypeDropdownElement(data.document_type))
    a.send_keys(new_order_page_form.numberOfPages, data.num_of_pages)
    a.send_keys(new_order_page_form.numberOfLots, data.num_of_lots)
    a.click(new_order_page_form.partiesTab)
    a.send_keys(new_order_page_form.firstNameInput(data.section), data.first_name)
    my_actions.scrollingMethod(0, 1000)
    a.click(new_order_page_footer.addToOrderButton)
    a.assert_equals(a.get_element_text(new_order_page_header.accountAlert), data.alert_text)

def teardown(data):
    pass
