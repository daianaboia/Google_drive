from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()           
drive = GoogleDrive(gauth)  

file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format('googledrivefolderid')}).GetList()

for i, file in enumerate(sorted(file_list, key = lambda x: x['title']), start=1):
	print('Downloading {} file from GDrive ({}/{})'.format(file['title'], i, len(file_list)))
	file.GetContentFile(file['title'])

