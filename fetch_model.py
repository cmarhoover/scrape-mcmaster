# -*- coding: utf-8 -*-
"""
Scrape 3D models from McMaster-Carr.

Requirements: msedgedriver.exe is in the same folder as this script.
"""
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time

test_part_numbers=['98173A200', '7529K105', '93250A440']

def fetch_model(part_numbers, delay=3):
    if type(part_numbers) is str:
        part_numbers=[part_numbers]
    
    #Start browser
    options = Options()
    driver = webdriver.Edge(options = options)
    
    #For each part number
    for part_number in part_numbers:
        driver.get('https://www.mcmaster.com/' + str(part_number) + '/')
        #Pause for page to load
        time.sleep(10)    
        #Find Download Dropdown and Select STEP
        try:
            try:
                select = Select(driver.find_element_by_xpath("//*[starts-with(@class, 'Dropdown_buttonDropdown')]"))
                select.select_by_visible_text('3-D STEP')
                submit_button = driver.find_element_by_xpath("//*[starts-with(@class, 'CadControl_downloadButton')]")
            except NoSuchElementException:
                time.sleep(delay)
            finally:
                submit_button.click()        
        except:
            print('No button found or other error occured')
        finally:
            time.sleep(delay)
            
    driver.close()
    driver.quit
    
fetch_model(test_part_numbers)
