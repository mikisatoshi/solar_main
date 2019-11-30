# -*- coding: utf-8 -*-
import json
import datetime
import numpy as np
from math import sin,cos



import access_ as acc

class PiLoger():
  def __init__(self, ch = 8):
    self.ch = ch

  def get_dummy_data(self):
    dt_now = datetime.datetime.now()
    value = dt_now.hour * 60 + dt_now.minute
    values = [str(datetime.datetime.now()), value, sin(value/100.0), "test"]
    # for i in range(100):
    #   print(sin(i/100))
    return values

  def get_data(self):
    import bme280_
    dt_now = datetime.datetime.now()
    value = dt_now.hour * 60 + dt_now.minute
    values = bme280_.getData()
    return  ["-",str(datetime.datetime.now()), value, values[0], values[1]/1000, values[2], 0 ,0, 0, 0, "test"]





def main(para):

  PA = acc.PiAccess(para["bookname"],para["sheetname"],para["keyname"])

  PL = PiLoger(ch = 8)
  PA.append(PL.get_data())


def main_logger_test(para):
  print(para)

  PA = acc.PiAccess(para["bookname"],para["sheetname"],para["keyname"])
  PL = PiLoger(ch = 4)
  PA.append(PL.get_dummy_data())


if __name__ == '__main__':

  try:
    with open("./../certification/para.json") as f:
      para = json.load(f)
  except:
    with open("./certification/para.json") as f:
      para = json.load(f)
  print('succseslly read parameter file')
  print(para)


  if para['logger_test'] == 'on':
    try:
      print(' try  logger_test   ')
      main_logger_test(para)
      print('   succes   ')
    except:
      print('  para[logger_test] == on  :  failed   ')
      # pass

  if para['logger'] == 'on':
    try:
      print(' try  logger   ')
      main(para)
      print('   succes   ')
    except:
      print('  para[logger] == on  :  failed   ')
      pass

  if para['takephoto'] == 'on':
    try:
      import takephoto_
      # takephoto.main()
      pass
    except:
      pass
