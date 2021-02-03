# Task : print id number only from email id input using regular expression
import re
# for i in range(10):
#     print("\"19003191"+str(i)+"@kluniversity.in\",")
mails = '''
190031910@kluniversity.in
190031911@kluniversity.in
190031912@kluniversity.in
190031913@kluniversity.in
190031914@kluniversity.in
190031915@kluniversity.in
190031916@kluniversity.in
190031917@kluniversity.in
190031918@kluniversity.in
190031919@kluniversity.in
'''

# pattern = '^19003....'
pattern = re.compile(r'(\d+)?@kluniversity.in')
idnum = pattern.sub(r'\1', mails)
matches = pattern.finditer(mails)
for i in matches:
    print(i.group(1))
