This app sends out an alert when a slot become available on the COWIN page. 

Please install the WebDriver for your Browser. 
For chrome, you can download it from -> https://chromedriver.storage.googleapis.com/index.html?path=90.0.4430.24/

Also, please check the requirements folder and ensure you have all the dependencies. You can run the following command: 
pip install -r requirements.txt

This should install all the dependencies.

After unzipping, please edit the location of the webdriver in line 46 on slot_alert.py

To try if it works, you can change the mat-option-39 in line#69 to mat-option-63.

It refreses the page every 10 secs, and if a vaccination slot becomes available, it throws a pop up and an alert sound.

Reach out to me if you face any issues.  

You have the option of selecting either 18+ or normal results. (You can uncomment it out if you want to see 18+ slots,line 15-18)
