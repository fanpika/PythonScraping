# -*- encoding: utf-8 -*-

import os
from indeed import get_jobs as get_indeed_jobs
from stackoverflow import get_jobs as get_so_jobs
from save import save_to_file

os.system('clear')

indeed_jobs = get_indeed_jobs()
# print(indeed_jobs)

so_jobs = get_so_jobs()
# print(so_jobs)

jobs = indeed_jobs + so_jobs
# print(jobs)

save_to_file(jobs)
# save_to_file([])