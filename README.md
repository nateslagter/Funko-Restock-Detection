# Funko-Restock-Detection

This Python script was created by me in order to monitor a few certain webpages to see if they were updated with new stock; I was constantly missing out on drops, so I wanted something that would just tell me when the product has restocked.

There is most certainly faster bots, better bots, all of that out there; however, I wanted something quick and dirty that I could write myself.

**How it works**

This bot functions on the idea that each website has a slightly different way of saying how the product is out of stock; it checks the site against the parameters I have listed, and if it is different, sends an email out saying that the product has restocked.
The products are listed in a dictionary; the key is the name of the product, and the value is a 2 - tuple with the link and the name of the site that contains the product.

**Features**

As of right now, this bot is only capable of detcting restocks from the official Funko website, Hot Topic, BoxLunch, and GameStop. More functionality will be added later on. It sleeps in between each check as to not overload the websites with unecessary requests. The program will run on a continuous loop until stopped by the user in the terminal.

**How to Run**

As of right now, this is just a simple python script. You will need to go in and manually edit the dictionary var that stores the Funko products you are looking for. Along with this, you will need to run it from your favorite terminal in order to get results. To have the program email you when it detects a restock, you must fill in your email info, and make sure you have an app password so the script can long onto your account and send the email. 

**_The Plan_**

The goal for this project is to eventually run on a tiny MySQL Database that stores all the funkos you are looking for, have a nice looking GUI that allows for navigation of the program without editing the source code, and bug fixes that will improve the overall experience.

**Contacting Me**

I am an amateur coder; if you have any complaints or any suggestions, please feel free to reach out to me at nateslagter@gmail.com , or just message me in GitHub.
