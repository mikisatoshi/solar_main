# -*- coding: utf-8 -*-
import json
import numpy as np
import access as acc
import pandas as pd
import datetime

def main():
  with open("./../certification/unique_name.json") as f:
    para = json.load(f)
  print(para)
  PA = acc.PiAccess(para["bookname"],para["sheetname"],para["keyname"])
  PA.backup('./../storage/now/'+para["sheetname"]+'_'+str(datetime.date.today())+'.csv')
  PA.range_clear("A17:K20000")

if __name__ == '__main__':
  main()