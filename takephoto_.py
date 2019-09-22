# -*- coding: utf-8 -*-
import json, time, datetime
import picamera


class PiLoger():
  def __init__(self):
    pass

  def get_dummy_data(self):
    pass

def main():
  try:
    with open("./../certification/unique_name.json") as f:
      para = json.load(f)
  except:
    with open("./certification/unique_name.json") as f:
      para = json.load(f)

  with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    dt_now = datetime.datetime.now()
    camera.capture('../storage/photo/'+para['sheetname']+'_'+str(datetime.date.today()) + '_' + str(dt_now.hour * 60 + dt_now.minute) + '.jpg')
    print("took photo")

if __name__ == '__main__':
  main()
