# -*- coding: utf-8 -*-
import numpy as np
import gspread
from oauth2client.service_account import ServiceAccountCredentials

class PiAccess():
  def __init__(self, bookname, sheetname, keyname):
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    #ダウンロードしたjsonファイルを同じフォルダに格納して指定する
    credentials = ServiceAccountCredentials.from_json_keyfile_name(keyname, scope)
    gc = gspread.authorize(credentials)
    # 共有設定したスプレッドシートの名前を指定する
    self.worksheet = gc.open(bookname).worksheet(sheetname)

  def test(self):
    print (self.worksheet.cell(10,2))
    self.worksheet.append_row(["-", 123, 456, "testgs"])
    print('succesful')

  def get_latest_values(self, number = 1):# example "A17:D10000"
    print(self.worksheet.acell('A35').value)
    last_row_number = int(self.worksheet.acell('A35').value)
    print(last_row_number + 1 - number)

    print('A' + str(last_row_number +1 -number))

    print(self.worksheet.acell('A' + str(last_row_number +1 -number)).value)
    print('A' + str(last_row_number +1 -number) + ':F' + str(last_row_number +1 -number) )
    # print(self.worksheet.row_count)
    # print(self.worksheet.findall('test'))
    return self.worksheet.range('A' + str(last_row_number +1 -number) + ':F' + str(last_row_number +1 -number))


  def append(self, value_list):
    self.worksheet.append_row(value_list) # example ["-", 123, 456, "testgs"]

  def range_clear(self, rangetxt):

    cell_list = self.worksheet.range(rangetxt) # example "A17:D10000"
    for cell in cell_list:
        cell.value = ""
    self.worksheet.update_cells(cell_list)

  def backup(self, filename):
    sheet = np.array(self.worksheet.get_all_values()).astype(np.unicode)
    np.savetxt(filename, sheet, delimiter = ",", fmt = "%s")
    print('print in backup - sheet[:,0] - ')
    print(sheet[:,0])
    print('------------------------------------------')


if __name__ == '__main__':
  PA = PiAccess('loger_test', 'sheet1', './../certification/miyamori.json')
  PA.test()
  PA.append(["-", 123, 456, "testgs"])
  PA.backup('./../storage/csv.csv')
  PA.range_clear("A17:L20000")