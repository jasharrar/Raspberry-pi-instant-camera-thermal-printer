# Raspberry-pi-instant-camera-thermal-printer
Raspberry pi instant camera with thermal printer

<br>Raspberry pi Zero
<br>Camera Module
<br>Thermal Printer (mine needs a minimum 2a @ 5v to run)
<br>Led for flash (i got a super bright 3.3v white LED online, but if you only have a 5v one use a NPN transistor inline)
<br>Buttons
<br>Locking button with LED
<br>For power im using a DFRobot MP2636 and a single lipo cell 

<br>Pre-requisites: (install cups and gpio utils)
<br>sudo apt-get install libcups2-dev libcupsimage2-dev git build-essential cups system-config-printer wiringpi

<br>Configure CUPS
<br>Set up the camera in raspi-config
<br>connect usb printer and install drivers, search for ZJ-58 drivers on GIT
<br>add a GPIO button for the shutter to GPIO 21 and GND
<br>add a bright LED to GPIO 5 and GND

<br>run the script!
<br> just added a few extra lines to run second flash LED, shutdown button and system LED

<img src="https://github.com/jasharrar/Raspberry-pi-instant-camera-thermal-printer/blob/master/camera2.jpg" alt="camera" style="width:500px;height:600px;">
