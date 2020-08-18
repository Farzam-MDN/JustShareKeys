import ftplib


import time


global oldmsg
global themsg
oldmsg = ''

global oldid
global theid
oldid = ''

import wget
import os
import keyboard
import mouse
import autopy


global downloadedfilepath

global status
status = True



filename = 'log.txt'

global FTPaddress
FTPaddress = ''
global FTPusername
FTPusername = ''
global FTPpassword
FTPpassword = ''
global FTPdestinationdirectoryname
FTPdestinationdirectoryname = ''
global Addressoflogfileonserver
Addressoflogfileonserver = ''




def config():
    global FTPaddress 
    global FTPusername
    global FTPpassword
    global FTPdestinationdirectoryname
    global Addressoflogfileonserver
    try:
        
        #first get the FTP credentials
        lines = []
        f = open('config.txt')
        for line in f:
            lines.append(line.rstrip('\n'))
        f.close()
        
        
        FTPaddress = str(lines[0])
        FTPusername = str(lines[1])
        FTPpassword = str(lines[2])
        FTPdestinationdirectoryname = str(lines[3])
        Addressoflogfileonserver = str(lines[4])

       
        
            
            
      
        
        
        #print(FTPaddress + FTPusername + FTPpassword + FTPdestinationdirectoryname + Addressoflogfileonserver)
        #fs.close()
        return 'done'
        
    except:
        print("An exception was thrown. Please Check whether config.txt file is in directory with the correct information.")
        answer = input('Do you like to continue: (y/n)')
        if answer == 'n' or answer == 'N':
            print('Closing the App..')
            return 'close'
            
        else:
            print("Restarting the App..")
            return 'restart'
         
    

def startapp():

    #config 
    configresult = config()    
    if configresult == 'done':
    
        #get input
        answer = input('Hello there. Are you client or server?')
        if answer == 'server' or answer == 'Server':
            print('Server is running. Go open JustShareKeys.py to start sharing your keys.')
            #os.system('JustShareKeys.py')
            runserver()
    
        elif answer == 'client' or answer == 'Client':
            runclient()
            
    elif configresult == 'restart':
        startapp()
        
    elif configresult == 'close':
        pass
        
  
        

def runserver():
    global status
    global oldmsg
    global oldid
    global theid
    global FTPaddress 
    global FTPusername
    global FTPpassword
    global FTPdestinationdirectoryname
    global Addressoflogfileonserver

    # f = open("log.txt", "r")
    # lines = f.readlines()
    # lineid = lines[0]
    # linekey = lines[1]

    # theid = lineid
    # if theid != oldid:
    #             oldid = theid
    
    #revert the try
    try:

        while status == True:
                f = open("log.txt", "r")
                lines = f.readlines()
                lineid = lines[0]
                linekey = lines[1]
                theid = lineid
                # print('The key is: ' + linekey)
                # print('The id is: ' + lineid)
    
                # if theid != oldid:
                #     oldid = theid
    
                if lineid != oldid and "Num" not in linekey :
                    
                       
                        ftp = ftplib.FTP(FTPaddress)
                        
                        ftp.login(FTPusername,FTPpassword)
    
                        #print(ftp.pwd())
                        ftp.cwd('public_html')
                        #print(ftp.pwd())
                        
                        ftp.cwd(FTPdestinationdirectoryname)
                        ##print(ftp.pwd())
    
                        print('The key pressed is: ' + linekey)
                        oldid = lineid
                        myfile = open("log.txt",'rb')
                        ftp.storlines('STOR ' + filename , myfile)
    
                elif "Num" in linekey and lineid != oldid:    
                        ftp = ftplib.FTP(FTPaddress)
                        
                        
                        ftp.login(FTPusername,FTPpassword)
                            
                        #print(ftp.pwd())
                        ftp.cwd('public_html')
                        #print(ftp.pwd())
                        ftp.cwd(FTPdestinationdirectoryname)
                        ##print(ftp.pwd())
    
                        print('The key pressed is: ' + linekey)
                        oldid = theid
                        f.close()
                        myfile = open("log.txt",'rb')
                        ftp.storlines('STOR ' + filename , myfile)
    
                        print('Numlock was pressed. The operation is on pause!')
                        answer = input('Would you like to proceed the connection (answer: y/n)?')
                        if answer == 'n' or answer == 'N':
                           print('You are now disconnected. To start the server rerun the app.')
                           status = False
    
    
                f.close()
                time.sleep(0.001)
    
    #revert            
    except:
             time.sleep(0.001)
            
             runserver()

            #print("An exception occurred")
        #IndexError()




def runclient():
    global status
    global oldmsg
    global oldid
    global theid
    global downloadedfilepath
    try:
        while status == True:
            downloadedfilepath = wget.download(Addressoflogfileonserver)
            f = open(downloadedfilepath, "r")
            lines = f.readlines()
            lineid = lines[0]
            linekey = lines[1]
            linemouseposition = lines[2]
            theid = lineid


            f.close()
            os.remove(downloadedfilepath)
            if lineid != oldid:
                #keyboard and mouse click if and if
                print(linekey)
                oldid = lineid

                if("pace" in str(linekey)):
                    print('Now Space should be pressed!')
                    keyboard.send("space")

                elif("nter" in str(linekey)):
                    print('Now Enter should be pressed!')
                    keyboard.send("enter")

                elif("MB" in str(linekey)):
                    print('Now LMB should be pressed!')
                    mouse.click(button='left')

                elif("sc" in str(linekey)):
                    print('Now Esc should be pressed!')
                    keyboard.send("escape")

                elif("hift" in str(linekey)):

                    positionarr = linemouseposition.split(' ')
                    print('Shift was pressed. Mouse moves to: ' + 'X = ' + positionarr[0] + ' , Y = ' + positionarr[1] )
                    autopy.mouse.smooth_move(int(positionarr[0]),int(positionarr[1]))  #smooth move is slow
                    #autopy.mouse.move(int(positionarr[0]),int(positionarr[1]))

                elif("eft" in str(linekey)):
                    print('Now Left arrow button should be pressed!')
                    keyboard.send("left")

                elif("ight" in str(linekey)):
                    print('Now Right arrow button should be pressed!')
                    keyboard.send("right")

#never pause the client you should only close the tab to end
                elif("umLock" in str(linekey)):
                    print('host paused/unpaused the connection.')
##                    answer = input('Would you like to proceed the connection (answer: y/n)?')
##                    if answer == 'n' or answer == 'N':
##                        print('You are now disconnected. To start the client rerun the app.')
##                        status = False
    except:
        try:
            f.close()
            os.remove(downloadedfilepath)
            time.sleep(0.001)
            runclient()

        except FileNotFoundError:
            time.sleep(0.001)
            runclient()

        except:
            time.sleep(0.001)
            runclient()





#program

startapp()

