from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from os import listdir
from os.path import isfile, join

gauth = GoogleAuth()           
drive = GoogleDrive(gauth)  

upload_file_list =  [f for f in listdir('path') if isfile(join('path', f))]
print(upload_file_list)
for upload_file in upload_file_list:
	gfile = drive.CreateFile({'title': upload_file,'parents': [{'id': 'googledrivefolderid'}]})	# Read file and set it as the content of this instance.
	gfile.SetContentFile("path"+upload_file)
	gfile.Upload() # Upload the file.
