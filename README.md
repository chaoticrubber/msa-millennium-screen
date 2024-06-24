# msa-millennium-screen
A Screen for your MSA millennium, 


### Code
Code is running circuitpython, I would suggest using Thonny to install. 
Put the code and the two folders (imgs & lib) in the root of the device - always eject your CIRCUTPYTHON Drive before removing or you will have to bootload and reflash the firmware. 

### Sleep State/How do I turn this off,
You can't atleast not without disconnecting the battery, (which is three screws) however the last image in the sequence is black.bmp ( a blank image). When the last image in the sequence is loaded the code turns the screens backlight off which will be the main draw of power. 

I've not figured out how to do touch aware deepsleep states on it yet, so this could change in future. 



### You will need 
- 1x https://www.waveshare.com/product/rp2040-touch-lcd-1.28.htm - make sure to get the touch screen one, you can find these on alliexpress
- 1x battery, the device uses 1.25mm JST connectors so you need to find something that matches that or take extreme care in sodering the correct plug on. 
- some m2 threaded inserts and some 16-20mm screws, the printerbles link has more on this. 

### 3D Printing, 

I found the front piece needed a slightly larger margin to hole the screen more snuggly so I've uploaded that mod here. 

### I've also uploaded a travel case for it based on the excellent parametric case by thesamenametwice - https://www.printables.com/model/540605-parametric-box-v2-single-clasp - credit required under their license

### License 
License is mixed and depending on file, so no further clarification will be given there, all copyright belongs to respective owners
Code.py falls under MIT License


3D printed files (when provided) are edits or derivatives from - https://www.printables.com/model/538771-rp2040-lcd-128-msa
Images belong to their own respective owners.
