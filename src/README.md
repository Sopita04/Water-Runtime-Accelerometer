## info
This is the code for the accelerometer. This folder includes different data processing techniques and previous iterations of code.

## AccelertionPlots
This code plots the x y and z accelerations on serial the serial monitor.

## DFT
This code calculate a Fast Fourier Transform on the x axis of the acceleration to identify specific frequencies in the vibration signals. 
Needed setup: arduinoFFT.h (Enrique Condes), python: python -m pip install pyserial matplotlib numpy, COM 4

## FFTPowerAndTimer
This code calculates the power of the the vibration signal in the frequency domain in a specified frequency band. It also includes a timer of flow.
Needed setup: arduinoFFT.h (Enrique Condes), COM 4
