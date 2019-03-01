import json
from selenium import webdriver
import pywinauto
import time
import pandas as pd
import os
import shutil

appState = {
    "recentDestinations": [
        {
            "id": "Save as PDF",
            "origin": "local"
        }
    ],
    "selectedDestinationId": "Save as PDF",
    "version": 2
}

profile = {'printing.print_preview_sticky_settings.appState': json.dumps(appState)}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('prefs', profile)
chrome_options.add_argument('--kiosk-printing')

driver = webdriver.Chrome("/Users/pulseid/Documents/pdf2image2/chromedriver 2",chrome_options=chrome_options)
driver.maximize_window()



#load df
url_df = pd.read_csv('links.csv')
url_df.columns = ['name', 'link']

#loop url, save as pdf


for i in range(len(url_df)):
    urls = str(url_df['link'].iloc[i])
    print(urls)
    driver.get(urls)
    driver.execute_script('window.print();')


    a_check = lambda: pywinauto.findwindows.find_windows(title=u'Print' , class_name='#32770')[0]

    try:
        dialog = pywinauto.timings.Timings.wait_until_passes(5, 1, a_check)
        window = pwa_app.window_(handle=dialog)
        window.SetFocus()
        ctrl = window['&Print']
        ctrl.Click()
        # need an explicit wait to allow the print to go through so we can quit the browser instance
        time.sleep(5)
    except Exception as e:
        print(e)

    #add number to files
    filepath = '/Users/pulseid/Downloads'
    dirpath = '/bookpages/'
    filename = max([filepath + "/"+ f for f in os.listdir(filepath)], key=os.path.getctime)
    newfilename = filepath + '/books' + filename[24:-4] +'_' +  str(i) + '.pdf'
    print(newfilename)
    shutil.move(os.path.join(filepath, filename), newfilename)



driver.close()