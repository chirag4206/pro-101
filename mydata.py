import dropbox
class Transferdata:
    def __init__(self,accesstoken):
        self.accesstoken=accesstoken
    
    def upload_file(self,filefrom,fileto):
        dbx=dropbox.Dropbox(self.accesstoken)
        with open(filefrom,'rb')as f:
            dbx.files_upload(f.read(),fileto)

def main ():
    accesstoken=""
    transferdata=Transferdata(accesstoken)
    filefrom=""
    fileto=""
    transferdata.upload_file(filefrom,fileto)
    print("file moved successfully")


main()
