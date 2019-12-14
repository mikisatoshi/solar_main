# -*- coding: utf-8 -*-
import numpy as np
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime as dt
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

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

  def get_latest_values(self, number = 0):# example "A17:D10000"
    print(self.worksheet.acell('A35').value)
    last_row_number = int(self.worksheet.acell('A35').value)
    row_number = int(last_row_number - number)
    print(self.worksheet.acell('A'+str(row_number)).value)

    A = self.worksheet.acell('A'+str(row_number)).value
    B = float(self.worksheet.acell('B'+str(row_number)).value)
    C = float(self.worksheet.acell('C'+str(row_number)).value)
    D = float(self.worksheet.acell('D'+str(row_number)).value)
    E = float(self.worksheet.acell('E'+str(row_number)).value)
    F = self.worksheet.acell('F'+str(row_number)).value

    JST = dt.datetime.strptime(A, '%Y-%m-%d %H:%M:%S.%f')
    print( JST + dt.timedelta(hours=9) )


    return (JST,B,C,D,E,F)


  def update_acell(self, label,value):
    self.worksheet.update_acell(label,value)


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


  def backup_to_googledrive(self, rangetxt, filename, name, folder_id):

    values = np.array(self.worksheet.range(rangetxt)).astype(np.unicode)
    np.savetxt(filename, values, delimiter = ",", fmt = "%s")


    gauth = GoogleAuth()
    gauth.CommandLineAuth()
    drive = GoogleDrive(gauth)

    f = drive.CreateFile({'title': name,
                          'mimeType': 'text/csv',
                          'parents': [{'kind': 'drive#fileLink', 'id':folder_id}]})
    f.SetContentFile(filename)
    f.Upload()

if __name__ == '__main__':
  PA = PiAccess('loger_test', 'sheet1', './../certification/miyamori.json')
  PA.test()
  PA.append(["-", 123, 456, "testgs"])
  PA.backup('./../storage/csv.csv')
  PA.range_clear("A17:L20000")