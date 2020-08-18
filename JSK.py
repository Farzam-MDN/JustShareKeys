import winput
import time
import random

global counter1
global counter2
global counter3
global counter4
global counter5
global counter6
global counter7
counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
counter5 = 0
counter6 = 0
counter7 = 0


def mouse_callback( event ):
    if event.action == winput.WM_LBUTTONDOWN:
        SendKeyPressData('LMB')
        print("Left mouse button press at {}".format( event.position ))
    
def keyboard_callback( event ):
    #we need counters because it prints two times per event!
    global counter1
    global counter2
    global counter3
    global counter4
    global counter5
    global counter6
    global counter7
    #theeventcode = event.vkCode
    if event.vkCode == winput.VK_SPACE:
        
        if counter1 == 0:
            SendKeyPressData('Space')
            print('Space')
            counter1 = 1
        
        elif counter1 == 1:
            counter1 = 0
         
    elif event.vkCode == winput.VK_RETURN:
        if counter2 == 0:
             SendKeyPressData('Enter')
             print('Enter')
             counter2 = 1
             
        elif counter2 == 1:
            counter2 = 0
         
    elif event.vkCode == winput.VK_ESCAPE:
        if counter3 == 0:
             SendKeyPressData('Esc')
             print('Esc')     
             counter3 = 1
             
        elif counter3 == 1:
            counter3 = 0
    
    elif event.vkCode == winput.VK_LEFT:
        if counter4 == 0:
             SendKeyPressData('Left')
             print('Left') 
             counter4 = 1
             
        elif counter4 == 1:
            counter4 = 0
         
    elif event.vkCode == winput.VK_RIGHT:
        if counter5 == 0:
            SendKeyPressData('Right')
            print('Right')
            counter5 = 1
            
        elif counter5 == 1:
            counter5 = 0
         
         
    elif event.vkCode == winput.VK_LSHIFT:
        if counter6 == 0:
             SendKeyPressData('Shift')
             print('Shift')
             counter6 = 1
             
        elif counter6 == 1:
            counter6 = 0
         
    #VK_NAVIGATION_LEFT      
    #VK_NAVIGATION_RIGHT 
    
    if event.vkCode == winput.VK_NUMLOCK: # quit on pressing Numlock. make it later in a way that it can be switched back on
        if counter7 == 0:
            SendKeyPressData('NumLock')
            print('NumLock was pressed the server will pause')
            counter7 = 1
            #print('Numlock was pressed. Keyshare is on pause.')
        elif counter7 == 1:
            counter7 = 0  
     
           #winput.stop()
           
    #to stop keyshare press multiply key
    if event.vkCode == winput.VK_MULTIPLY : # quit on pressing Numlock. make it later in a way that it can be switched back on
        
        print('Multipy was pressed the keyshare stopped')
        winput.stop()   
        
        
        
        
def SendKeyPressData(keyname):
    #this should connect with the front-end
    #write in a log file
    with open("log.txt","w") as f: 
         # a totally random string on line 1 which is id of keypress
        n = random.random() 
        f.write(str(n)[2:9])
        f.write('\n')
        
        f.write(str(keyname))
        f.write('\n')
        position = Mousemovement()
        f.write(str(position[0]) + ' ' + str(position[1]))
        
        f.close()
         
        # if str(keyname) == 'NumLock':
        #     f.close()
        
        
    

def Mousemovement():
    position = winput.get_mouse_pos()
    return [position[0],position[1]]


def StartApp():
    print("Press Num Lock to quit")
        
    # hook input    
    winput.hook_mouse( mouse_callback )
    winput.hook_keyboard( keyboard_callback )
    
    # enter message loop
    winput.wait_messages()
    
    # remove input hook
    winput.unhook_mouse()
    winput.unhook_keyboard()
    
    
    
#Program
StartApp()