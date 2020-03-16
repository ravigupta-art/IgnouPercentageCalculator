# IGNOU PERCENTAGE CALCULATOR (BA/BCOM/BDP)
Percentage Calculator for IGNOU BA/BDP/BCOM programmes.

## Downloads:
Download for your operating system and platform:
- [Windows10-64bit](https://github.com/ravigupta-art/IgnouPercentageCalculator/raw/master/dist/IgnouPercentageCalculator_BA_BDP_BCOM_64bit.exe)
- [Windows10-32bit](https://github.com/ravigupta-art/IgnouPercentageCalculator/raw/master/dist/IgnouPercentageCalculator_BA_BDP_BCOM_32bit.exe)
- [Linux-64bit](https://github.com/ravigupta-art/IgnouPercentageCalculator/raw/master/dist/IgnouPercentageCalculator_BA_BDP_BCOM)

## Preview (screenshot):
![Ignou Percentage Calculator (BA/BCOM/BDP) -- v1.0alpha screenshot](/docs/images/IgnouPercentageCalculator_BA_BDP_BCOM_preview.png "Ignou Percentage Calculator (BA/BCOM/BDP) -- v1.0alpha screenshot")

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

### Video tour of the application
<iframe width="560" height="315" src="https://www.youtube.com/embed/4xlI0KbvjO8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

