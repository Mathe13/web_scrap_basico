from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')

#browser.find_element_by_class_name(name)           #Elements that use the CSS class name
#browser.find_element_by_css_selector(selector)     #Elements that match the CSS selector
#browser.find_element_by_id(id)                     #Elements with a matching id attribute value
#browser.find_element_by_link_text(text)            #<a> elements that completely match the text provided
#browser.find_element_by_partial_link_text(text)    #<a> elements that contain the text provided
#browser.find_element_by_name(name)                 #Elements with a matching name attribute value
#browser.find_element_by_tag_name(name)             #Elements with a matching tag name (case insensitive; an <a> element is matched by 'a' and 'A')
