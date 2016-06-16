#!/bin/python

############################################################
# This application is being made in order for me
#     to learn 'BeautifulSoup' and 'selenium'.
# It is intended to be useful really only to me,
#     but could easily be adapted for wider use.
# One possible potential use case would be to scrape LinkedIn for
#     info needed to fill in an application on one of those awful
#     job posting portals.
# Objective: scrape my employment history from LinkedIn and format it as HTML
############################################################

from bs4 import BeautifulSoup
from selenium import webdriver

def linscrape():
    #imitate web browser
    driver = webdriver.Chrome(executable_path='path/to/chromedriver')
    profile_link = 'https://www.linkedin.com/in/user'
    driver.get(profile_link)
    html = driver.page_source

    #initialize soup, identify 2 main sections
    soup = BeautifulSoup(html, 'html.parser')
    #summary is not currently printed or used
    #    but it may be useful down the line
    summary = soup.find('section', {'id':'summary'})
    experience = soup.find('section', {'id':'experience'})

    #grab all job titles, placing them in a list
    job_title = []
    for title in experience.findAll('span',{'data-field-name':'Position.Title'}):
        job_title.append(title.getText())

    #grab all employers, placing them in a list
    job_company = []
    for company in experience.findAll('span',{'data-field-name':'Position.CompanyName'}):
        job_company.append(company.getText())

    #grab all job descriptions, placing them in a list
    job_desc = []
    for desc in experience.findAll('p',{'class':'description'}):
        job_desc.append(desc.getText())

    #initialize empty string to which we will append our formatted info
    job_history = ""
    #iterate through each item appending them to our HTML as we go -
    #    employer #1, title #1, desc #1, employer #2, title #2, etc
    for i in range(len(job_desc)):
        job_history += '<div class="row"><div class="col-sm-4"><br /><br /><h1>' + job_company[i] + '</h1></div><div class="col-sm-8">'
        job_history += '<h3>' + job_title[i] + '</h3>'
        job_history += '<p>' + job_desc[i] + '</p></div></div>'

    #print the HTML, which is now useable. We can prettify it if we want, also
    print(job_history)


if __name__ == '__main__':
    linscrape()
