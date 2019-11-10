from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)

folder_id = '15_LEaSQI_c_8DdibdUMLzC2pOFcBzJAI'
f = drive.CreateFile({'title': 'test.jpg',
                      'mimeType': 'image/jpeg',
                      'parents': [{'kind': 'drive#fileLink', 'id':folder_id}]})
f.SetContentFile('sin.gif')
f.Upload()

