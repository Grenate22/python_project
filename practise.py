import re
email='pe.teradetunji30@gmail.com adelusi.adetunji.1003@fuoye.edu'
print('Emailmatches:',len(re.findall('[\w][\w.-].[A-Za-z]',email)))
print(re.findall('[\w]{1,20}[\w.-]{2,3}.[A-Za-z]{2,3}',email))