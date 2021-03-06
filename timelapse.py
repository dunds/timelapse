from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import picamera
import datetime

# snap a photo using picamera (e.g. 'images/2016-06-11 04:03:09.269776.jpg')
camera = picamera.PiCamera()
img_name = 'images/' + str(datetime.datetime.now()) + '.jpg'
camera.capture(img_name)

# auth to gdrive
gauth = GoogleAuth()
creds = "secret.txt"
gauth.LoadCredentialsFile(creds)

if gauth.credentials is None:
    gauth.CommandLineAuth()
elif gauth.access_token_expired:
    gauth.Refresh()
else:
    gauth.Authorize()

gauth.SaveCredentialsFile(creds)

# upload the photo to gdrive
drive = GoogleDrive(gauth)
f = drive.CreateFile()
f.SetContentFile(img_name)
f.Upload()
