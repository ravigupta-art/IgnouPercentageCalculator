#!/usr/bin/env Python3 
from os import path
import sys
import PySimpleGUI as sg
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

bundle_dir = getattr(sys, '_MEIPASS', path.abspath(path.dirname(__file__)))
path_to_dat = path.join(bundle_dir, 'course_details.dat')


sg.theme('DarkGrey2')

# getting maximum score for each courses in BA/BDP/BCOM programmes at IGNOU
course_details = {}
with open((path_to_dat), "r") as f:
    for line in f:
        key, value = line.strip().split(':')
        course_details[key] = int(value)



layout = [  [sg.Text('IGNOU PERCENTAGE CALCULATOR (BA/BCOM/BDP)', size=(60, 1), justification='center', font=('ubuntu', 15), relief=sg.RELIEF_RIDGE)],
            [sg.Text('Enter your Enrollment no. (only for BA/BDP/BCOM programmes):')],      
            [sg.In(size=(20,1), key='enrollmentNo')],      
            [sg.Txt('Choose your programme code (BA/BDP/BCOM):')],
            [sg.InputCombo(('BA', 'BDP', 'BCOM'), key='programmeCode', size=(6, 1), default_value='BA')],      
            #[sg.In(size=(6,1), key='programmeCode')],
            [sg.Text('_'*100, size=(60,1), justification='center')],       
            [sg.Text('', size=(60,0), key='output', font=('ubuntu', 14))],      
            [sg.Button('Calculate Percentage', bind_return_key=True)],
            [sg.Text(' '*2, size=(60,0), justification='center')], 
            [sg.Text("*NOTE: \n 1. This application needs an active internet connection to fetch the result from the IGNOU's official website. \n 2. The percentage calculated can be inaccurate/invalid, or the application might crash for some reasons. \n 3. Read more about the known issues here:- \n     https://github.com/ravigupta-art/IgnouPercentageCalculator#known-issues", size=(95,0))]]     

window = sg.Window('IGNOU PERCENTAGE CALCULATOR (BA/BCOM/BDP) -- v1.0alpha', layout )      

while True:      
    event, values = window.read()      

    if event is not None:      
        try:
            enrollmentNo = str(values['enrollmentNo'])      
            programmeCode = str(values['programmeCode'])
            result_url = 'https://gradecard.ignou.ac.in/gradecardB/Result.asp?eno=' + enrollmentNo + '&program=' + programmeCode + '&hidden_submit=OK'      
            uClient = uReq(result_url)     
            page_html = uClient.read()
            uClient.close()
            page_soup = soup(page_html,"html.parser")
            table_html = page_soup.table
            table = table_html
            headings = [td.get_text() for td in table_html.find("tr").find_all("td")]
            datasets = []
            for row in table.find_all("tr")[1:]:
            	dataset = dict(zip(headings, (td.get_text() for td in row.find_all("td"))))
            	datasets.append(dataset)
            def percentage(data):
            	score = 0
            	total_marks = 0
            	percent = 0
            	for i in range(len(data)):
            	    if datasets[i]['  Status '] == 'Completed':
            	        course_code = datasets[i]['  Course Code ']
            	        if course_details[course_code] == 100:
            	            score += 0.3 * int(datasets[i]['  Asgn1 ']) + 0.7 * int(datasets[i]['  Term End Theory '])
            	            total_marks += 100
            	        else:
            	            score += (0.3 * int(datasets[i]['  Asgn1 '])) / 2 + (0.7 * int(datasets[i]['  Term End Theory '])) / 2
            	            total_marks += 50
            	    else:
            	        print("All courses not completed.")
            	percent = (score / total_marks) * 100
            	#rounded_percentage = round(percent, 2)
            	print ("Percent = {}%".format(percent))
            	return percent
            percent = str(percentage(datasets))
        except:      
            table_html = 'Invalid'      

        window['output'].update('Total Percentage: ' + percent)     
    else:      
        break      
