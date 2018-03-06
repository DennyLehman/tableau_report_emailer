# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 12:01:54 2018

@author: Denny.Lehman
"""

import win32com.client
olMailItem = 0x0
attachment_filepath = r'D:\Users\Denny.Lehman\Desktop\attachment_test.txt'
obj = win32com.client.Dispatch("Outlook.Application")
newMail = obj.CreateItem(olMailItem)
newMail.Subject = "My Subject"
newMail.Body = "My Body"
newMail.To  = "Leo.Burlett@sunnova.com"
newMail.Attachments.Add(Source=attachment_filepath)

with open(attachment_filepath , 'r') as myfile:
   data=myfile.read()
   
newMail.Display
newMail.Send()
