#!/usr/bin/python3
#By: ZanderC0de

import os
import time
import warnings
import argparse
from selenium import webdriver
from colorama import Fore,init
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

init()

#COLOURS
white = Fore.LIGHTWHITE_EX
green = Fore.LIGHTGREEN_EX
blue = Fore.LIGHTBLUE_EX
red = Fore.LIGHTRED_EX
yellow = Fore.LIGHTYELLOW_EX
cyan = Fore.LIGHTCYAN_EX
purple = Fore.LIGHTMAGENTA_EX


#                      CONFIG
#########################################################
warnings.filterwarnings("ignore", category=Warning)
driver_chrome = 'chromedriver'
chrome_options = Options()
chrome_options.add_argument("--headless")#FOR HIDDEN EXECUTE
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
try:
    driver = webdriver.Chrome(options=chrome_options, executable_path=driver_chrome)

except:
    print(red+"ERROR! YOU NOT HAVE CHROMEDRIVER.\nDOWNLOAD IT FOR LINUX AND EXECUTE './install.sh'")
    exit()
##########################################################


def banner():
    os.system("clear")

    textBanner = """
     ▄▄▄·  ▐ ▄ ▄▄▄▄▄▄▄▄ . ▄▄· ▄▄▄ .·▄▄▄▄  ▄▄▄ . ▐ ▄ ▄▄▄▄▄ ▄▄·       
    ▐█ ▀█ •█▌▐█•██  ▀▄.▀·▐█ ▌▪▀▄.▀·██▪ ██ ▀▄.▀·•█▌▐█•██  ▐█ ▌▪▪     
    ▄█▀▀█ ▐█▐▐▌ ▐█.▪▐▀▀▪▄██ ▄▄▐▀▀▪▄▐█· ▐█▌▐▀▀▪▄▐█▐▐▌ ▐█.▪██ ▄▄ ▄█▀▄ 
    ▐█ ▪▐▌██▐█▌ ▐█▌·▐█▄▄▌▐███▌▐█▄▄▌██. ██ ▐█▄▄▌██▐█▌ ▐█▌·▐███▌▐█▌.▐▌
    ▀  ▀ ▀▀ █▪ ▀▀▀  ▀▀▀ ·▀▀▀  ▀▀▀ ▀▀▀▀▀•  ▀▀▀ ▀▀ █▪ ▀▀▀ ·▀▀▀  ▀█▄▀▪
    """

    print(purple+textBanner)

def oneDocument():
    url = "https://apps.procuraduria.gov.co/webcert/inicio.aspx?tpo=1"
    driver.get(url)
    time.sleep(3.5)
    driver.find_element(By.ID, 'ddlTipoID').click()
    time.sleep(0.8)
    driver.find_element(By.XPATH, '//option[2]').click()
    driver.find_element(By.ID, 'txtNumID').send_keys(document)
    time.sleep(1)
    
    print(yellow+"\n[*]"+green+" Searching to " + red + document + "...")

    while True:
        time.sleep(0.9)
        questi_on = driver.find_element(By.ID, 'lblPregunta')

        r = questi_on.text
        
        if 'Cuanto es 3 - 2' in r:
            driver.find_element(By.ID,'txtRespuestaPregunta').send_keys('1')
            break

        elif 'Capital del Atlantico' in r:
            driver.find_element(By.ID, 'txtRespuestaPregunta').send_keys('barranquilla')
            break

        elif 'Cuanto es 4 + 3' in r:
            driver.find_element(By.ID, 'txtRespuestaPregunta').send_keys('7')
            break

        elif 'Cuanto es 9 - 2' in r:
            driver.find_element(By.ID, 'txtRespuestaPregunta').send_keys('7')
            break

        elif 'Cuanto es 6 ÷ 2' in r:
            driver.find_element(By.ID, 'txtRespuestaPregunta').send_keys('3')
            break

        elif 'Cuanto es 5 + 3' in r:
            driver.find_element(By.ID, 'txtRespuestaPregunta').send_keys('8')
            break

        elif 'Cuanto es 2 X 3' in r:
            driver.find_element(By.ID, 'txtRespuestaPregunta').send_keys('6')
            break

        elif 'Cuanto es 3 X 3' in r:
            driver.find_element(By.ID, 'txtRespuestaPregunta').send_keys('9')
            break

        elif 'Cual es la Capital de Antioquia' in r:
            driver.find_element(By.ID, 'txtRespuestaPregunta').send_keys('medellin')
            break

        elif 'Cual es la Capital del Vallle del Cauca' in r:
            driver.find_element(By.ID, 'txtRespuestaPregunta').send_keys('cali')
            break
            
        elif 'Cual es la Capital de Colombia' in r:
            driver.find_element(By.ID, 'txtRespuestaPregunta').send_keys('bogota')
            break
        
        else:
            driver.find_element(By.ID, 'ImageButton1').click()
            time.sleep(1.5)
    
    time.sleep(1.5)
    driver.find_element(By.ID, 'btnConsultar').click()

    time.sleep(1.5)


    try:
        posiError = driver.find_element(By.ID, 'ValidationSummary1')
        Err = posiError.text
        if 'INGRESADO NO SE ENCUENTRA' in Err:
            print(red+"THE PERSON NOT REGISTER IN THE SYSTEM")
            driver.quit()
            exit()

    except:
        pass
        
    name = driver.find_element(By.XPATH, '//div[@id="divSec"]/div')
    ant = driver.find_element(By.XPATH, '//div[@id="divSec"]/h2[2]')


    print(f'''\n{green}
    -------------------------------------------------------------{cyan}

    {yellow}[*]{cyan} {name.text}
    \n   {yellow} [*]{purple} {ant.text}   
    {green}
    --------------------------------------------------------------

    ''')

    driver.quit()

def multipleDoc():

    try:
        nLine = os.popen("cat " + listDoc + " | wc -l").read()
    except:
        exit()

    url = "https://apps.procuraduria.gov.co/webcert/inicio.aspx?tpo=1"
    driver.get(url)

    file = open(listDoc)
    content = file.readlines()

    for x in range(int(nLine)):

        time.sleep(3.5)
        driver.find_element(By.ID, 'ddlTipoID').click()
        time.sleep(0.8)
        driver.find_element(By.XPATH, '//option[2]').click()
        driver.find_element(By.ID, 'txtNumID').send_keys(content[x])
        time.sleep(1)

        while True:
            time.sleep(0.9)
            questi_on = driver.find_element(By.ID, 'lblPregunta')

            r = questi_on.text
        
            if 'Cuanto es 3 - 2' in r:
                driver.find_element(By.ID,'txtRespuestaPregunta').send_keys('1')
                break

            elif 'Capital del Atlantico' in r:
                driver.find_element(By.ID, 'txtRespuestaPregunta').send_keys('barranquilla')
                break

            elif 'Cuanto es 4 + 3' in r:
                driver.find_element(By.ID, 'txtRespuestaPregunta').send_keys('7')
                break

            elif 'Cuanto es 9 - 2' in r:
                driver.find_element(By.ID, 'txtRespuestaPregunta').send_keys('7')
                break

            elif 'Cuanto es 6 ÷ 2' in r:
                driver.find_element(By.ID, 'txtRespuestaPregunta').send_keys('3')
                break

            elif 'Cuanto es 5 + 3' in r:
                driver.find_element(By.ID, 'txtRespuestaPregunta').send_keys('8')
                break

            elif 'Cuanto es 2 X 3' in r:
                driver.find_element(By.ID, 'txtRespuestaPregunta').send_keys('6')
                break

            elif 'Cuanto es 3 X 3' in r:
                driver.find_element(By.ID, 'txtRespuestaPregunta').send_keys('9')
                break

            elif 'Cual es la Capital de Antioquia' in r:
                driver.find_element(By.ID, 'txtRespuestaPregunta').send_keys('medellin')
                break

            elif 'Cual es la Capital del Vallle del Cauca' in r:
                driver.find_element(By.ID, 'txtRespuestaPregunta').send_keys('cali')
                break

            elif 'Cual es la Capital de Colombia' in r:
                driver.find_element(By.ID, 'txtRespuestaPregunta').send_keys('bogota')
                break
        
            else:
                driver.find_element(By.ID, 'ImageButton1').click()
                time.sleep(1.5)
    
        time.sleep(1.5)
        driver.find_element(By.ID, 'btnConsultar').click()

        time.sleep(1.5)

        try:
            posiError = driver.find_element(By.ID, 'ValidationSummary1')
            Err = posiError.text

        except:
            pass

        if 'INGRESADO NO SE ENCUENTRA' in Err:
            print(red+"THE DOCUMENT "+ content[x] + " NOT BEING IN THE SYSTEM")
            driver.refresh()

        else:
            name = driver.find_element(By.XPATH, '//div[@id="divSec"]/div')
            ant = driver.find_element(By.XPATH, '//div[@id="divSec"]/h2[2]')

            print(f'''\n{green}
    -------------------------------------------------------------{cyan}

    {yellow}[*]{cyan} {name.text}
    \n   {yellow} [*]{purple} {ant.text}   
    {green}''')

            driver.refresh()

def main():
    banner()
    global document,listDoc
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", '--document',help="Document of the person :)")
    parser.add_argument("-f", '--file',help="If you want inveting multiple people")
    args = parser.parse_args()
    document = args.document
    listDoc = args.file

    if args.file:
        multipleDoc()
        exit()

    elif args.document:
        oneDocument()
        exit()

    else:
        print(red+"Error! usage: python3 AntecedentCO.py -h")

if __name__ == '__main__':
    main()
