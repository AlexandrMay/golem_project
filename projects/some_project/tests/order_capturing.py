from golem import actions as a
from projects.some_project.actions_helper import my_actions
from projects.some_project.rest_helper import api_service

description = 'Order capturing flow'

tags = ['order_workflow']

pages = ['home_page', 'capture_tab_page']

def setup(data):
    pass

def test(data):
    a.navigate((data.env.url).format(get_secrets().login, get_secrets().password))
    a.click(home_page.captureTab)
    a.wait(3)
    a.click(capture_tab_page.startBatchScan)
    a.wait(3)
    a.click(capture_tab_page.startScanButton)
    a.wait(40)
    a.click(capture_tab_page.editButton)
    a.send_keys(capture_tab_page.docGroupInput(), data.doc_group)
    a.wait(2)
    a.press_key(capture_tab_page.docGroupInput(), 'ENTER')
    a.send_keys(capture_tab_page.docTypeInput(), data.doc_type)
    a.wait(2)
    a.press_key(capture_tab_page.docTypeInput(), 'ENTER')
    a.send_keys(capture_tab_page.docNumber(), api_service.readFromJson('doc_number'))
    a.clear_element(capture_tab_page.pagesInput())
    a.send_keys(capture_tab_page.pagesInput(), a.get_element_text(capture_tab_page.imagesField))
    a.click(capture_tab_page.editButton)
    a.wait(7)
    a.click(capture_tab_page.saveAndExit)

def teardown(data):
    pass