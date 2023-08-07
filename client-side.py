import socket
import sys
import time
import os

def text_out(text: str) -> None:
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)

print("     [ ] CLIENT CONFIGURATIONS -")
host=input("   [ server address ] ::  ")
if host=="":
   host="localhost"
   text_out("   [ default ] :: localhost")
   print("")
else:
   pass

while True:
    portStr=input("   [ port number 1000-9999 ] ::  ")
    try: 
        port = int(portStr)   
    except:
       port = 12345678
    if (type(port) is int) and (port>=1000 and port<=9999):
       break
    else:
       text_out("   [ invalid ] ::  invalid port!!\n")
       print("")

bufferSize=1048576


client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host,port))




class file:
    def __init__(self,x,y):
       self.x,self.y=x,y
    def compress(contents,filename):
       message=contents+"<_SEPARATOR_>"+filename
       return message   
       
    def findExtension(file):
        # This function gonna return the filename(base) of the file,
        # From the link provided other wise return the filename
        if "/" in file:
            splitted=file.split("/")
            filename=splitted[-1:]
            return filename[0]
        else:
            filename=file
            return filename    
            
    def openFile(file_dir,ext):
       extAll=ext.split(".")
       extension=extAll[1]
       all="jpg jpeg gif png JPEG tiff mp4 mp3 dox ppx avi pdf wav ogg zip bin csv exe ico svg bat dat sql tar gz "
       # Here we'll deal with those non-text files
       if extension in all:
           return ''
       # Here we'll deal with the text natured files
       else:
           f=open(file_dir,"rt")
           contents=f.read()
       return contents

    def separate(data):
        # Spliting the data received as content and filename
        texts=data.split("<_SEPARATOR_>")
        datas=texts[0]    
        ext=texts[1]
        return datas,ext
 
 
 
 
os.system("clear")
print("\n\n")
text_out("    [ chat ] :: CHAT WITH THE SERVER NOW ! ")
print("")


print("\n")
# Main loop
while True:
  try:
    # SENDING 
    message=input(" [ You ]::  ")
    message=f'''{message}'''
    if(message=="file"):
     # When user wants to send the files
     try:
          file_dir=input("         [File-Name] e.g(./file.py) :: ")
          # Finding the file name extensiom
          extension=file.findExtension(file_dir)
          # Here we read the file
          contents=file.openFile(file_dir,extension)
          
          # This make sure that the files which are being transfered are,
          # Text based and not binaries.
          # In the future upgrades we'll be able to transfer them.
          if(contents==""):
              client.send("STOPPED".encode())
              text_out("    [ 403 ] :: Binary files are not allowed!!")
              print("")
              break 
          message=file.compress(contents,extension)
     except:
          #using this in debug mode
          client.send("STOPPED".encode())
          text_out("     [ 400 ] :: No such File or Directory!!")
          print("")
          break 
    client.send(message.encode())
    
    # RECEIVING 
    data=client.recv(bufferSize).decode()
    text_out(" [ server ]::  ")
    # Always convert all responses to strings
    received=str(data)

    # Receiving segment
    if(received=="STOPPED"):
       # If the server response is STOPPED, then abolish all the processes
       text_out("\n       [ 500 ] :: It seems server is down!!!")
       print("")
       break
    
    # checks whether received is a file or a normal string
    compare=int(received.find("<_SEPARATOR_>"))
    if(compare>=0):
      contents,filename=file.separate(received)     
      text_out(f"\n        [ incoming... ] :: INCOME FILE DETECTED - {filename} ")
      print("")
      response=input(f"     [ x ] Accepting {filename}? [y/n] ::  ")
      if response=='y' or response=='Y':
          file_path=input("     [ directory ] :: Where should the file be saved? \n     [ default ] :: Present Directory:: ")
          if(file_path==""):
             os.system(f"echo '{contents}' > {filename}")
             text_out("    [ received ] ::  current directory!!")
             print("")
          else:
             os.system(f"cd {file_path} && echo '{contents}' > {filename}")
             text_out(f"     [ saved ] :: {filename} saved! ")
             print("")
      else:
          print("")
          text_out("     [ 200 ] :: A file successfully deleted!!")
          print("")
          break 
    else:
      text_out(received)
      print("")
  
  except KeyboardInterrupt:
   client.send("STOPPED".encode())
   text_out("   ")
   print("")
   break 
   
   
client.close()
