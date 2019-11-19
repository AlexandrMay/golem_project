from golem import actions as a
from projects.some_project.actions_helper import my_actions
from projects.some_project.rest_helper import api_service

description = 'Order creation and payment flow (processing to the Capture queue)'

tags = ['order_workflow']

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
    a.click(new_order_page_form.partiesTab)
    a.send_keys(new_order_page_form.firstNameInput(data.section), data.first_name)
    a.send_keys(new_order_page_form.firstNameInput(data.section2), data.first_name)
    a.click(new_order_page_form.propertiesTab)
    a.send_keys(new_order_page_form.parcelIdInput, data.parceId)
    a.send_keys(new_order_page_header.nameInput, data.name)
    a.wait(3)
    my_actions.scrollingMethod(0, 1000)
    a.click(new_order_page_footer.addToOrderButton)
    a.click(new_order_page_footer.orderSummaryCheckout)
    balance = a.get_element_text(new_order_page_form.balanceOwed)
    a.click(new_order_page_form.paymentMethodDropdown)
    a.click(new_order_page_form.paymentMethodDropdownElement(data.payment_method))
    a.send_keys(new_order_page_form.amountInput, balance)
    a.click(new_order_page_footer.orderPaymentCheckout)
    api_service.writeToJson('order_number', a.get_element_text(new_order_page_header.orderNumber), 'doc_number', a.get_element_text(new_order_page_form.documentNumber))

def teardown(data):
    pass
