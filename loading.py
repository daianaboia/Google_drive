from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from os import listdir
from os.path import isfile, join

gauth = GoogleAuth()           
drive = GoogleDrive(gauth)  

upload_file_list =  [f for f in listdir('/Users/daianaboia/Programmazione/ProgettoTommaso/Insider_bozza/script/ch/') if isfile(join('/Users/daianaboia/Programmazione/ProgettoTommaso/Insider_bozza/script/ch/', f))]
print(upload_file_list)
for upload_file in upload_file_list:
	gfile = drive.CreateFile({'title': upload_file,'parents': [{'id': '19FUBoFa5Y7KxdGlvrWMUYe_w8aPqFBNc'}]})	# Read file and set it as the content of this instance.
	gfile.SetContentFile("/Users/daianaboia/Programmazione/ProgettoTommaso/Insider_bozza/script/ch/"+upload_file)
	gfile.Upload() # Upload the file.