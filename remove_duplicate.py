import sys
import os
from datetime import datetime

def get_non_duplicate_email():
  email_list = []
  global count
  with open('email_data.txt') as f:
    for line in f:
      list_size = sys.getsizeof(email_list)
      line = line.rstrip()
      count+=1
      if line not in email_list:
        email_list.append(line)
        yield line

t1 = datetime.now()
count=0

print("Start")

with open('output.txt', 'w') as f:
    for email in get_non_duplicate_email():
      f.write("%s\n" % email)
    print("Done")

t2 = datetime.now()

print("Number of records %s" % (count))
print("Time spent : %s second." % ((t2-t1).total_seconds()))


