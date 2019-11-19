from golem import actions

def scrollingMethod(x, y):
    actions.execute_javascript('window.scrollTo({}, {})'.format(x, y))

def expandAllTableElements():
    actions.execute_javascript("var rows = document.querySelectorAll('tr'); for(let i = 0; i < rows.length; i++) { rows[i].style.display=''}")

def scrollToTableElement(text):
    actions.execute_javascript("var list = document.querySelectorAll(`td > span`); const obj = Array.prototype.find.call(list, (item)=>item.innerText === '{}').getBoundingClientRect(); const a = obj.x; const b = obj.y; window.scrollTo(a, b)".format(text))