# -*- coding: utf-8 -*-
import json
import datetime
import numpy as np
from math import sin,cos



import access_ as acc
import ADS1x15


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
    self.init_get_adc_data()

    try:
      value = self.adc.read_adc_difference(0, gain=self.GAIN)
    except:
      value = -1
 
    values = bme280_.getData()
    return  [str(datetime.datetime.now()), -value*(3.28/4645), values[0], values[1]/1000, values[2], "test"]


  def init_get_adc_data(self):
    self.adc = ADS1x15.ADS1115()
    self.GAIN = 1




def main(para):

  PA = acc.PiAccess(para["bookname"],para["sheetname"],para["keyname"])
  PL = PiLoger(ch = 6)
  PA.append(PL.get_data())


def main_logger_test(para):
  print(para)

  PA = acc.PiAccess(para["bookname"],para["sheetname"],para["keyname"])
  PL = PiLoger(ch = 4)
  PA.append(PL.get_dummy_data())


def make_hour_report(para):
  """
  ここの処理はGCP上で動かす前提なので、時間がGSTとなるため、日本時間に直す処理が必要になる
  """
  PA = acc.PiAccess(para["bookname"],para["sheetname"],para["keyname"])

  values = PA.get_latest_values(number = 0)
  print(values)
  nowtime = datetime.datetime.now() + datetime.timedelta(hours=9)

  if (nowtime - values[0]) < datetime.timedelta(minutes=15):
    updatetime = nowtime.hour
    PA.update_acell('D'+str(int(updatetime+2)),values[1])
    PA.update_acell('E'+str(int(updatetime+2)),values[2])

  if nowtime.hour == 0:
    updatetime = nowtime.day
    PA.update_acell('B'+str(int(updatetime+1)),values[1])

      




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


  if para['logger'] == 'on':
    try:
      print(' try  logger   ')
      main(para)
      print('   succes   ')
    except:
      print('  para[logger] == on  :  failed   ')
      pass


  if para['make_hour_report'] == 'on':
    try:
      print(' try  make_hour_report   ')
      make_hour_report(para)
      print('   succes   ')
    except:
      print('  para[make_hour_report] == on  :  failed   ')




  if para['takephoto'] == 'on':
    try:
      import takephoto_
      # takephoto.main()
      pass
    except:
      pass
