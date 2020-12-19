# -*- encoding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python"

def get_last_page(): 
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  # print(soup)
  pagination = soup.find("div", {"class":"s-pagination"})
  # print(pagination)

  pages = pagination.find_all("a")
  last_page = pages[-2].text.strip()
  return int(last_page)

def extract_job(html):
  # https://lets-hack.tech/programming/languages/python/bs4-text-or-string/
  title = html.find("h2").find("a", {"class":"s-link"})["title"].strip()
  company_span, location_span = html.find("h3").find_all("span", recursive=False)
  company = company_span.text.strip().replace("\n", " ").replace("\r", " ")
  location = location_span.text.strip().replace("\n", " ").replace("\r", " ")
  job_id = html["data-jobid"].strip()
  
  # print(f"company: {company}")
  # print(f"location: {location}")
  # print(f"job_id: {job_id}")

  return {"title":title, "company":company, "location":location, "link":f"https://stackoverflow.com/jobs/471608/{job_id}"}

def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):
    # print(f"&start={page*LIMIT}")
    print(f"Scraping Stackoverflow: page: {page}")
    result = requests.get(f"{URL}&pg={page+1}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class":"-job"})
    
    for result in results:
      jobs.append(extract_job(result))
  return jobs

def get_jobs():
  last_page = get_last_page()
  # return extract_jobs(last_page)
  return extract_jobs(4)