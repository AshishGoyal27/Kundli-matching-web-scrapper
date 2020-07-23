from os import path
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
import csv

docData=[]
with open("input.csv") as doc:
	docRead = csv.reader(doc, delimiter=',')
	for row in docRead:
		docData.append(row)

a = [(docData[i][0:8])for i in range(1,(len(docData)))]
print("Total no. of queries: ",len(a))

def getQueryResult(b_name, b_dob, b_tob, b_pob, g_name, g_dob, g_tob, g_pob):
    url = "https://www.astrosage.com/freechart/matchmaking.asp"
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('log-level=3')
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    sleep(6)
    element = driver.find_element_by_xpath('//*[@id="name1"]')
    element.send_keys(b_name)
    m = b_dob.split("-")
    element1 = driver.find_element_by_xpath('//*[@id="roundborder"]/div[4]/div/div/form/div[1]/fieldset/select[1]')
    if m[0][0] == "0":
        element1.send_keys(m[0][1])
    else:
        element1.send_keys(m[0])
    
    element2 = driver.find_element_by_xpath('//*[@id="roundborder"]/div[4]/div/div/form/div[1]/fieldset/select[2]')
    element2.send_keys(m[1])
    element3 = driver.find_element_by_xpath('//*[@id="roundborder"]/div[4]/div/div/form/div[1]/fieldset/input[2]')
    element3.send_keys(m[2])

    n = b_tob.split(":")
    element4 = driver.find_element_by_xpath('//*[@id="roundborder"]/div[4]/div/div/form/div[1]/fieldset/select[3]')
    if n[0][0] == "0":
        element4.send_keys(n[0][1])
    else:
        element4.send_keys(n[0])

    element5 = driver.find_element_by_xpath('//*[@id="roundborder"]/div[4]/div/div/form/div[1]/fieldset/select[4]')
    if n[1][0] == "0":
        element5.send_keys(n[1][1])
    else:
        element5.send_keys(n[1])

    element6 = driver.find_element_by_xpath('//*[@id="roundborder"]/div[4]/div/div/form/div[1]/fieldset/select[5]')
    if n[2][0] == "0":
        element6.send_keys(n[2][1])
    else:
        element6.send_keys(n[2])

    element7 = driver.find_element_by_xpath('//*[@id="place1"]')
    element7.send_keys(b_pob)


    element11 = driver.find_element_by_xpath('//*[@id="name2"]')
    element11.send_keys(g_name)
    m1 = g_dob.split("-")
    elementa2 = driver.find_element_by_xpath('//*[@id="roundborder"]/div[4]/div/div/form/div[2]/fieldset/select[1]')
    if m1[0][0] == "0":
        elementa2.send_keys(m1[0][1])
    else:
        elementa2.send_keys(m1[0])
    element13 = driver.find_element_by_xpath('//*[@id="roundborder"]/div[4]/div/div/form/div[2]/fieldset/select[2]')
    element13.send_keys(m1[1])
    element14 = driver.find_element_by_xpath('//*[@id="roundborder"]/div[4]/div/div/form/div[2]/fieldset/input[2]')
    element14.send_keys(m1[2])

    n1 = g_tob.split(":")
    element15 = driver.find_element_by_xpath('//*[@id="roundborder"]/div[4]/div/div/form/div[2]/fieldset/select[3]')
    if n1[0][0] == "0":
        element15.send_keys(n1[0][1])
    else:
        element15.send_keys(n1[0])

    element16 = driver.find_element_by_xpath('//*[@id="roundborder"]/div[4]/div/div/form/div[2]/fieldset/select[4]')
    if n1[1][0] == "0":
        element16.send_keys(n1[1][1])
    else:
        element16.send_keys(n1[1])

    element17 = driver.find_element_by_xpath('//*[@id="roundborder"]/div[4]/div/div/form/div[2]/fieldset/select[5]')
    if n1[2][0] == "0":
        element17.send_keys(n1[2][1])
    else:
        element17.send_keys(n1[2])
    element18 = driver.find_element_by_xpath('//*[@id="place2"]')
    element18.send_keys(g_pob)
    driver.find_element_by_xpath('//*[@id="roundborder"]/div[4]/div/div/form/div[4]/input[1]').click()
    driver.find_element_by_xpath('//*[@id="form2"]/div[4]/input[2]').click()
    sleep(10)
    code = driver.page_source.encode('utf-8')
    soup = bs(code, 'lxml')
    bt = soup.find_all('ul',{"class" : "mrt-10 mrb-10"})
    l = []
    for i in bt:
        l.append(i.text)
    s = l[0].split("\n")
    return s
    

def mainloop(a):
    if path.exists('confirm.csv'):
        pass
    else:
        with open('confirm.csv', 'w', newline='') as file1:
            writer = csv.writer(file1)
            writer.writerow(('Boy_Name', 'Girl_Name', 'Ashtakoot Matching', 'Mangal Dosha', 'Conclusion'))
        file1.close()
    for i in range(len(a)):
        try:
            remarks = getQueryResult(a[i][0], a[i][1],a[i][2], a[i][3],a[i][4], a[i][5],a[i][6], a[i][7])
            with open('confirm.csv', 'a', newline='') as file2:
                writer = csv.writer(file2)
                writer.writerow((a[i][0], a[i][4], remarks[1], remarks[2], remarks[3].lstrip()))
            print('Boy Name is: '+a[i][0], '\tGirl Name is: '+a[i][4],'\nAshtakoot Matching: '+remarks[1], '\nMangal Dosha: '+remarks[2], '\n'+remarks[3].lstrip())
        except Exception as e:
            print(e)
            with open('confirm.csv', 'a', newline='') as file2:
                writer = csv.writer(file2)
                writer.writerow((a[i][0], a[i][4], 'SKIPPING', 'SKIPPING','SKIPPING'))
            print(a[i][0], a[i][4], 'SKIPPING', 'SKIPPING','SKIPPING')
mainloop(a)

#a = getQueryResult("amar", "07-Jul-98", "11:00:01", "delhi", "suman", "09-Jun-99", "03:00:50", "sultan")
