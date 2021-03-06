# -*- coding: utf-8 -*-
import json
import sys
import numpy as np
sys.path.append('/home/kurosatou3104/solar_init/solar_main') 
import access_ as acc
import pandas as pd
import datetime

def main(para):

  print(para)
  PA = acc.PiAccess(para["bookname"],para["sheetname"],para["keyname"]) 
  PA.backup_to_googledrive('40:F10000', './../storage/'+para["sheetname"]+'_'+str(datetime.date.today())+'.csv', para["sheetname"]+'_'+str(datetime.date.today())+'.csv', para['google_drive_id'])
  PA.move_range("B2:B32", "G2:G32")
  PA.range_fill("B2:B32", 0.0)
  PA.range_clear("A41:K20000")



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
    try:
      print(' try  backup   ')
      main(para)
      print('   succes   ')
    except:
      print('  para[backup] == on  :  failed   ')
