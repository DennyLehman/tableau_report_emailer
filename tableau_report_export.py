# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 14:25:06 2018

@author: leo.burlett
"""

import time
import os

print("OS.system running...")
start = time.time()
os.system(r'cmd /C D:\Users\leo.burlett\tableau_report_export.bat')

print("The OS process took {0} time to run".format(time.time()-start))






