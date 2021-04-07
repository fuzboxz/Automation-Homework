# Automation-Homework
The Automation Home Assignment has two components: 
1. Python - Scrapy webscraping and Google Drive uploader
2. Google App Script - Spreadsheet parsing, Google Forms creation and email sending
## Requirements
The Python part of the automation has been developed with **Python 3.9.2**, so 3.9 is recommended, but theoretically anything above 3.6 should work. MacOS was used for development, so Unix/Linux type operating systems are supported.
## Installation:
To install the Python part of the application use your shell to execute the *install.sh* shell script:
```
./install.sh
```
This will activate the local virtual environment, install the Python dependencies and open up the browser for authentication. **The app can't upload the CSV to Google Drive without authentication!** 

If you ever need to run authentication manually, execute the following command in the root folder of the repositry:
```
python Library\GoogAuth.py
```

To install the Google App script part of the home assignment go to https://script.google.com, create a new project, delete all content from default code.gs file and paste everything from the code.gs file in this repo. Additionally, you need to add the Google Sheets API by clicking on the plus button next to the Services text on the left side. For the script to work you also need to create a Google Sheet with the name **automation_email** where the A columns contain the list of email addresses.
## Running the application
If you followed the installation steps correctly, the commands below should scrape IMDB and upload a Google Sheet containing the top5 results and yield back the id of the Google Sheet that was uploaded.
``` 
source bin/activate
python main.py
```
To run the Google App Script portion of the assignment, run the default/SpreadsheettoForm function on App Script.
## Setting up the automation
To automate the execution of the web scraping, you can use *crontab*. Run *crontab -e* and paste the following command into the window, which will run the script automically every Sunday at 12:00 UTC. **For this to work, the contents of this repo need to be under /opt/Automation-Homework and on MacOS you might need to enable Full-Disk Access for the cron binary!**
```
0 12 * * 0 /opt/Automation-Homework/automate.sh >/dev/null 2>&1
```
To automate the Google App Script part of the project, open the project that you created during the installation. Click on the alarm clock icon/triggers menu, add a trigger with the following settings: week timer, every Sunday, 3-4 PM (UTC is 1PM Budapest time, but let's delay it by two hours to be on the safe side) and set the notification frequency to weekly. **This part will not work if there is not top5 and automation_email Spreadsheet present in Google Drive!**
