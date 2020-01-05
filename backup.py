# -*- coding: utf-8 -*-

import json
import numpy as np
from .solar_main import access_
import access_ as acc
import pandas as pd
import datetime

def main(para):

  print(para)
  PA = acc.PiAccess(para["bookname"],para["sheetname"],para["keyname"]) 
  PA.backup_to_googledrive('A40:F10000', './../storage/'+para["sheetname"]+'_'+str(datetime.date.today())+'.csv', para["sheetname"]+'_'+str(datetime.date.today())+'.csv', para['google_drive_id'])
  # PA.range_clear("A40:K20000")



if __name__ == '__main__':

  try:
    with open("./../certification/para.json") as f:
      para = json.load(f)
  except:
    with open("./certification/para.json") as f:
      para = json.load(f)
  print('succseslly read parameter file')
  print(para)


  if para['backup'] == 'on':

    print(' try  backup   ')
    main(para)
    print('   succes   ')

    print('  para[backup] == on  :  failed   ')
