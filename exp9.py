import re 
text="""
Hello student!
for any queries contact abc@gmail.com or teacher123@college.edu.
you can also contact support@yahoo.com
"""

email_pattern=r'[a-zA-zx0-9,_%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

emails=re.findall(email_pattern,text)

print("Email addresses found: ")

for email in emails:
    print(email)
