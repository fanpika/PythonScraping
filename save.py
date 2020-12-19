# -*- encoding: utf-8 -*-

import csv

def save_to_file(jobs):
  # For Windows10 : buffering=-1, encoding="utf-8", newline=''
  file = open("jobs.csv", mode="w", buffering=-1, encoding="utf-8", newline='')
  writer = csv.writer(file)
  writer.writerow(["title", "company", "location", "link"])

  for job in jobs:
    writer.writerow(list(job.values()))
  return
