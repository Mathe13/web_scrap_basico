#exercicio tirado de http://eliasnogueira.com/arquivos_blog/selenium/desafio/2desafio/
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Firefox()#cria o objeto
browser.get('http://eliasnogueira.com/arquivos_blog/selenium/desafio/2desafio/')#abre o site

#nome
browser.find_element_by_id('name_rg').click()#clica em name_rg para ativar name_hv
nome=browser.find_element_by_id('nome_pessoa')
nome.clear()#limpa o campo
nome.send_keys('matheus')#digita o novo nome
browser.find_element_by_xpath("//input[@type='button' and @value='Salvar']").click()
Wait(browser,10).until(EC.visibility_of(browser.find_element_by_id('name_rg')))
#email
browser.find_element_by_id('email_rg').click()#clica em name_rg para ativar name_hv
nome=browser.find_element_by_id('email_value')
nome.clear()#limpa o campo
nome.send_keys('matheuslimaaa13@gmail.com')#digita o novo nome
browser.find_element_by_css_selector("#email_hv_editing_section > input[value='Salvar']").click()
Wait(browser,10).until(EC.visibility_of(browser.find_element_by_id('email_rg')))
#telefone
browser.find_element_by_id('phone_rg').click()#clica em name_rg para ativar name_hv
nome=browser.find_element_by_id('phone_value')
nome.clear()#limpa o campo
nome.send_keys('51 980290467')#digita o novo nome
browser.find_element_by_css_selector("#phone_hv_editing_section > input[value='Salvar']").click()
