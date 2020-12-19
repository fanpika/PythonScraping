# -*- encoding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def get_last_page(): 
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  # print(soup)
  pagination = soup.find("div", {"class":"pagination"})
  # print(pagination)

  pages = pagination.find_all("a")
  last_page = pages[-2].text.strip()
  return int(last_page)

def extract_job(html):
  # https://lets-hack.tech/programming/languages/python/bs4-text-or-string/
  title = html.find("h2", {"class":"title"}).find("a")["title"].strip()
  company = html.find("span", {"class":"company"}).text.strip().replace("\r", " ")
  location = html.find("div", {"class":"recJobLoc"})["data-rc-loc"].strip()
  job_id = html["data-jk"].strip()

  return {
    "title":title, 
    "company":company, 
    "location":location, "link":f"https://www.indeed.com/viewjob?jk={job_id}"
    }

def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):
    # print(f"&start={page*LIMIT}")
    print(f"Scraping Indeed: page: {page}")
    result = requests.get(f"{URL}&start={page*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class":"jobsearch-SerpJobCard"})
    
    for result in results:
      jobs.append(extract_job(result))
  return jobs

def get_jobs():
  last_page = get_last_page()
  # print(last_page)
  # return extract_jobs(last_page)
  return extract_jobs(2)