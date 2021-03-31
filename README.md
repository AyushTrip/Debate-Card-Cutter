# Card Cutting Automation

Cutting evidence for debate sucks. You have to find a good article, find the information, create the cite, add it to a document, verbatimize it just to even BEGIN highlighting and bolding. 

This is a prototype python automated way of automatically cutting evidence for competitive high school and college debate. The automater takes in an article link and uses selenium and the services of outline.com to automatically generate the information from an article. It uses the msword and python docx to save a new document containing a verbatim style version of the card. 

## Requirements - Windows Users

There are a few requirements for the program to function correctly. You will need Chrome. 

First, you need to install the chromedriver application to allow the program to scrape the article for data
1. Go to this link and install the application: https://chromedriver.chromium.org
2. Follow the steps in this YT tutorial: https://chromedriver.chromium.org


Then, you will need Python to allow the script to run. You can do this at the official website. 
https://www.python.org/downloads/


## Dependencies - Windows Users 

Open up your command prompt (CMD) after you have installed python. Type the following - 
1. ```pip install selenium```
2. ```pip install docx```

These are nessecary modules that need to be installed for the program to use them. 

## Instructions

### Article Input
Once you have loaded the program, it should pull up a small TKinter GUI. This is where you will be putting the article url for it to scrape and cut. After you have entered the url, the process should start. Typically, the entire process would take up to 30 seconds.

### Word Document
When you run the script, you may need to go to the script around line 170 where it says ```card.save('C:/Users/Desktop')``` and change the path to where you want the card document to save. Once this is up and ready, the program should be able to function with no issues


## Disclaimers
I have not fully tested this, and there are tons of issues. They could arise from outline.com being down, the article not being valid, some dependencies not being installed correctly. The card cutting mechanism isn't fully flushed out yet, but ideally it should shave a few seconds off the time it takes you to write a cite and put it in a word document with the correct formatting.

Enjoy! 
