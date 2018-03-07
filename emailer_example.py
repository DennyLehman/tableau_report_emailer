# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 12:01:54 2018

@author: Denny.Lehman
"""

import win32com.client
recipient_list = ['leo.burlett@sunnova.com;','denny.lehman@sunnova.com']

olMailItem = 0x0
attachment_filepath = r'D:\Users\leo.burlett\.spyder-py3\Sheet1.pdf'
obj = win32com.client.Dispatch("Outlook.Application")
newMail = obj.CreateItem(olMailItem)
newMail.Subject = "My Subject"
newMail.Body = "My Body"
newMail.To  = ''.join(recipient_list)
newMail.Attachments.Add(Source=attachment_filepath)

# with open(attachment_filepath , 'r') as myfile:
#   data=myfile.read()
   
newMail.Display
newMail.Send()
