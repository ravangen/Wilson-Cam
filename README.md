# Wilson Cam
Capture an image from a webcam and upload to Dropbox.

## Equipment
All components used are older versions and can easily be replaced by something newer.

**NOTE**: Since I only have a small memory card, I mount the operating system from the USB drive and only use the card to boot from using BerryBoot.

### Hardware
- [Raspberry Pi 1 Model B](https://www.raspberrypi.org/products/model-b/)
- 512MB SD Card
- 8GB USB Flash Drive
- [TP-LINK TL-WN725N](http://www.tp-link.com/lk/products/details/cat-11_TL-WN725N.html) (wireless USB adapter)
- [Microsoft Lifecam VX-3000](https://www.microsoft.com/hardware/en-ca/d/lifecam-vx-3000) (webcam)
- USB Hub

### Software
- [BerryBoot](http://www.berryterminal.com/doku.php/berryboot)
- [Debian Jessie Raspbian](https://www.raspberrypi.org/downloads/raspbian/)
- [Dropbox](https://www.dropbox.com/)

### Setup
1. Using your computer, install BerryBoot onto the SD Card (see http://www.berryterminal.com/doku.php/berryboot)
1. Assemble Raspberry Pi and plug in
  1. Place SD Card in slot
  1. Plug the USB drive in one USB slot
  1. Plug the USB hub into the other USB slot
  1. Connect any additional USB devices into the hub (e.g. keyboard, mouse, webcam, wifi adapter)
  1. Connect a monitor with a HDMI cable
  1. Connect to the internet with an ethernet cable
1. Install Jessie Raspbian to the USB drive using BerryBoot
1. Configure wireless adapter to connect to wifi so that a wired connection is not necessary
1. `git clone` this repository
