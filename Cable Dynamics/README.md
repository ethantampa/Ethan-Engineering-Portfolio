# Cable Dynamics Analysis

This project focuses on the **vibrational analysis of electronic cables** through experimental testing and data processing. Using a DAQ system, accelerometer, modal hammer, and QuickDAQ software, the project collects and processes time-domain data to analyze cable dynamics in the frequency domain. A custom Python script is used to automate analysis and visualization of the dynamic response characteristics of the cables.

## Project Summary

- **Objective:** To evaluate the dynamic behavior (natural frequency, damping ratio, etc.) of various electronic cables through experimental vibration testing. 
- **Hardware Used:**
  - DAQ (Data Acquisition Device)
  - Accelerometer
  - Modal Hammer
- **Software Used:**
  - [QuickDAQ](https://www.digilent.com/shop/quickdaq/)
  - Python (Data Processing and Visualization)

## Python Script Features
- Reads files exported from QuickDAQ (or any uploaded .tab files)
- Automatically extracts data and calculates:
  - Natural frequency
  - Damping ratio
  - Logarithmic decrement
  - Harmonics
- Plots:
  - Time-domain force and acceleration
  - Frequency-domain magnitude and coherence response



