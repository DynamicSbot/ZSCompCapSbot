import bs4
import html5lib
import html5lib
from html5lib import sanitizer
from html5lib import treebuilders
import urllib
import requests

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
USER_TOKEN = ''
USER_SECRET = ''
RETURN_URL = 'http://localhost:8000'
from linkedin import linkedin

def get_company_name_and_employee_count(symbol):
    """Given a company symbol, this function will return a touple of the (company name, symbol, total employees, how positions they are hiring for, and what percentage open positions over total employees"""
    
    url = 'http://finance.yahoo.com/q/pr?s='+symbol+'+Profile'
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.text, 'html5lib')
    
    index_location = str(soup.title.next)
    second_index_location =  index_location.split(' ')
    location = second_index_location.index('|')
    number_of_employees = int (soup.find(text='Full Time Employees:').next.next.replace(',',''))
    company_nombre = slipknot[location+1]
    authentication = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET, USER_TOKEN, USER_SECRET, RETURN_URL, linkedin.PERMISSIONS.enums.values())
    application = linkedin.LinkedInApplication(authentication)
    response = application.search_job(params={'company-name' : company_nombre, 'count': 40})
    data = response['numResults']
    hiring_percent = (float(data) / float(number_of_employees)) * 100
    profile = company_nombre, symbol.upper(), number_of_employees, data, ('%.2f' % hiring_percent)
    return profile

#print get_company_name_and_employee_count('msft')

def pretty_print(symbol):
    open_positions = get_company_name_and_employee_count(symbol)
    print open_positions[0], open_positions[1], "|", "current number of employees:", fortune[2], "|", "number of positions they are hiring for:", fortune[3], "|", "hiring positions as a percent of current employees:", open_positions[4]
    
