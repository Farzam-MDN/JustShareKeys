# JustShareKeys

![JustShareKeys Logo](https://i.imgur.com/iC78CHh.png)

JustShareKeys (abbreviated as JSK) is An application that syncs your keystrokes and mouse button presses with any other computer in the world! The application uses FTP for communication between server and clients. Syncing keystrokes and button presses allow multiple computers to sync their videos even if they are playing them from different platforms. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need the following in order to run the application as it is intended on your machine:

```
Python 3 or above
Pip package installer for python
An FTP server with decent loading speed 

```

### Installing and Running the application

First clone this repository or download it manually to a working directory on your computer.
Thereafter, open terminal/cmd inside the JustShareKeys directory on your computer.
Now Run the following command in your terminal/cmd:

```
pip install -r requirements.txt
```
After all the requirements are installed, open config.txt file in JustShareKeys directory.
Also open config-example.txt and help.txt file in the same directory. Now try to set up your config.txt file by reading the guide in help.txt file and looking at config-example.txt file.
As a result your config.txt file should look similar to this:

```
ftp.example.com
admin
password
JustShareKeys
http://example.com/JustShareKeys/log.txt

```
After the config file is set up we are ready to run the application. But before doing that all the previous steps need to be done on another machine (since exactly one machine will be server and at least one machine will be client). The client machine does not need to have the FTP credentials in the config.txt file and they can be left empty.  Thus, it is only mandatory to provide line 5 of the config.txt for the client (the first four lines can be empty and fifth line should be filled in).

After the client machine is set up and configured, go on the server machine and run the following command in JustShareKeys directory:

```
py JSK.py
```
This will run the JustShareKeys application (which should always be running on server machine not the client). This application saves your last keystroke in a file named 'log.txt', which is the exact file that will be later uploaded to your FTP server. For doing a quick test press 'Enter' key on your server machine. 
In Jsk.py on your server machine you should now be able to see a message stating that the key 'Enter' has been pressed. This application currently works with the following keys: Esc, Enter, Right arrow, Left arrow, Left Mouse Button, Space, Shift (shift button does not result in shift being pressed on client machine. It moves the cursor of the client to the location of the cursor where shift button was pressed on the server machine. More on that later.), NumLock (NumLock key will be used to pause the server. More on that later).   
While JSK.py is running on server run the following command in JustSharKeys directory on your server machine (open a new terminal/cmd).

```
py Connect.py

```
Now you should be prompted with a message asking for an input. Type 'server' without the quotation marks and press enter key.
Now the server should be ready for sending keystrokes and mouse button presses. A quick test: press 'Enter' Key on server computer and Connect.py should show a message stating 'Enter' key has been pressed.   
Now keep Connect.py and JSK.py running on server machine and move to the client machine.
On the client machine open a terminal/cmd in JustShareKeys directory and run the following command.

```
py Connect.py

```
Now you should be prompted with a message asking for an input. Type 'client' without the quotation marks and press enter key.
A quick test: go to the client machine open a Youtube video. Now go to the server machine and press 'Right arrow' key followed by 'Space' key. Now on the client machine the Youtube video should be fast forwarded and stopped as a result. Also if you look inside the terminal (which is running Connect.py) you should see messages stating 'Enter' key and 'Right arrow' key have been pressed. If this quick test was successful then everything is set!
To learn how to better use the application read the section below (titled: running the tests) 



## Running the tests

These tests help users better understand how this application is meant to be used. 

### Syncing videos 

This test will help you sync videos playing on different machines.

do the following:


1) Run the app on a server machine and a client machine (if you don't know how to do that check 'Installing and Running the application' section in this readme file). 

2) Now press Numlock on server machine to pause process of sharing the keys. 

3) Open a video on both of the machines (The video does not need to be online and it can be playing via any platform)

4) Pause the video on both machines and bring the video to the very start (at 00:00). make the video full screen on the client machine. 

5) Now on server machine bring terminal that is running Connect.py partially over screen of the video that is paused. Now type 'y' without quotation marks in the terminal and press enter (Now your keypresses are being shared). 

6) Lastly on the server machine  Click on the video that is paused.

7) The video should now be playing at almost the same time on both machines. Now on server machine press 'Right Arrow' key.

8) The video should now be forwarded on both machines landing at almost the same time of the video. Now on server machine press 'Space' key followed by 'Esc' key.

9) The video should now be paused on both machines and the video might even be out of Fullscreen mode on the client machine (depends on whether or not 'Esc' Key disables Fullscreen). Now on server machine move your cursor to anywhere on the screen and press 'Left Shift' key. 

10) Now the cursor of the client machine should be moving to another location. 
Now on server machine Press 'Multiply' button. This stops the keyshare process on the server machine.

11) Now on server machine Press 'NumLock' button. This pauses the server. Now on server machine bring terminal that is running Connect.py and type 'n' without quotation marks in the terminal and press enter (now your server is stopped).

11) Now you close all the terminals on both machines.





## Contributing

Feel free to fork and expand this project! Send a pull request if you would like to add your code to the project.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/WozniakManiac/JustShareKeys/releases). 

## Authors

* **Farzam Madani** - *Creation of the core application* - [WozniakManiac](https://github.com/WozniakManiac)

See also the list of [contributors](https://github.com/WozniakManiac/JustShareKeys/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/WozniakManiac/JustShareKeys/blob/master/LICENSE) file for details

## Acknowledgments

* Big thanks to anyone whose library is used for this project 
* This project is inspired by Syncplay, Parsec and Opentogethertube!


