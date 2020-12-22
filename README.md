# IGNOU PERCENTAGE CALCULATOR (BA/BCOM/BDP/MEG)
Percentage Calculator for IGNOU BA/BDP/BCOM/MEG programmes.

## Downloads:
Download for your operating system and platform:
- [Windows10-64bit](https://github.com/ravigupta-art/IgnouPercentageCalculator/raw/master/dist/IgnouPercentageCalculator_BA_BDP_BCOM_64bit.exe)
- [Windows10-32bit](https://github.com/ravigupta-art/IgnouPercentageCalculator/raw/master/dist/IgnouPercentageCalculator_BA_BDP_BCOM_32bit.exe)
- [Linux-64bit](https://github.com/ravigupta-art/IgnouPercentageCalculator/raw/master/dist/v1.1alpha/IgnouPercentageCalculator_BA_BDP_BCOM_MEG)

## Preview (screenshot):
![Ignou Percentage Calculator (BA/BCOM/BDP/MEG) -- v1.0alpha screenshot](/docs/images/IgnouPercentageCalculator_BA_BDP_BCOM_MEG_preview.png "Ignou Percentage Calculator (BA/BCOM/BDP/MEG) -- v1.1alpha screenshot")

## How it works?
This Applicaton takes Enrollment number and his programme code from the user. Fetches the result from the official IGNOU website and then calculates the precentage. Percentage calculated is not rounded-off.

## Known Issues:
### Possible reasons for application crash
- Incorrect enrollment number (as this application does not verifies user's enrollment number)
- When enrollment number is left blank.
- Enrollment number provided is for programmes other than BA / BDP / BCOM.
- Since programmes are updated regularly at IGNOU, their corresponding courses list might not be updated in our database. Contribute to the project and update the list of courses under '/src/course_details.dat'.

### Possible reasons for invalid/inaccurate percentage
- When one or more courses are not completed by the user for their programme at IGNOU.
- When the result for either Assignment or Term End Exam (theory) might not be updated on the IGNOU website.
- Since programmes are updated regularly, their corresponding courses' credits might not be updated in our database. Contribute to the project and update the list of courses under '/src/course_details.dat'.

## Building the app from src
If you are building this app from src, follow the below steps:
- Clone the repository using `git clone https://github.com/ravigupta-art/IgnouPercentageCalculator.git`. You will need a terminal and GIT installed on your computer.
- We are using python3 and python3-tk as the main dependencies. Install them if not installed. On Linux you can install them using `sudo apt-get install python3 python3-tk`.
- CD into cloned repository using `cd IgnouPercentageCalculator`.
- Create a virtual environment named 'python3env' using `python3 -m venv python3env`.
- Activate virtual environment using `source python3env/bin/activate`(on linux) and `source python3env/Scripts/activate`(on windows).
- Install the required python packages using `pip install -r requirements.txt`
- Start developing the application. The python code and data file is in 'src' folder.
- When ready to build the executable file, go into 'src' folder using `cd src` build it using `pyinstaller  --onefile  --add-data "course_details.dat;." IgnouPercentageCalculator_BA_BDP_BCOM_MEG.py` (on windows) and `pyinstaller  --onefile  --add-data "course_details.dat:." IgnouPercentageCalculator_BA_BDP_BCOM_MEG.py` (on linux).
- Executable file will be in the 'src/dist' folder.
