# the-Garbage-Projeckt

This is "The Garbage Project" the following code are made to be run on the Raspberry Pi 4 with the Raspbian OS.

## Installation

Use the default python interpreter. Installing OpenCV on the pi is very tricky. Most of the instruction is based on
https://raspberrypi-guide.github.io/programming/install-opencv#install-prerequisites

1. terminal the code below. This is the only way that I worked.
   apparently opencv must be 4.5.3.56 to work on pi 4.

```
sudo apt-get update
sudo apt-get install build-essential cmake pkg-config libjpeg-dev libtiff5-dev libjasper-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libfontconfig1-dev libcairo2-dev libgdk-pixbuf2.0-dev libpango1.0-dev libgtk2.0-dev libgtk-3-dev libatlas-base-dev gfortran libhdf5-dev libhdf5-serial-dev libhdf5-103 python3-pyqt5 python3-dev -y
pip install opencv-python==4.5.3.56
pip install -U numpy
```

## Capturing

use the file capture.py
to capture images from the camera.
