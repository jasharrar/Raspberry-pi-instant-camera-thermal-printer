# Raspberry-pi-instant-camera-thermal-printer
Raspberry pi instant camera with thermal printer

<br>Raspberry pi Zero
<br>Camera Module
<br>Thermal Printer
<br>Led for flash
<br>Button

<br>Pre-requisites: (install cups and gpio utils)
<br>sudo apt-get install libcups2-dev libcupsimage2-dev git build-essential cups system-config-printer wiringpi

<br>Configure CUPS
<br>Set up the camera in raspi-config
<br>connect usb printer and install drivers, search for ZJ-58 drivers on GIT
<br>add a GPIO button for the shutter to GPIO 21 and GND
<br>add a bright LED to GPIO 5 and GND

<br>run the script!
