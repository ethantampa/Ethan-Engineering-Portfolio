# Cable Dynamics Analysis

This project focuses on the **vibrational analysis of electronic cables** through experimental testing and data processing. Using a DAQ system, accelerometer, modal hammer, and QuickDAQ software, the project collects and processes time-domain data to analyze cable dynamics in the frequency domain. 

A custom Python script automates the extraction of physical characteristics such as natural frequency, damping ratio, and harmonics — providing both numerical results and visual plots.

## Project Summary

- **Objective:** To evaluate the dynamic behavior (natural frequency, damping ratio, etc.) of various electronic cables through experimental vibration testing. 
- **Hardware Used:**
  - DAQ (Data Acquisition Device)
  - Accelerometer
  - Modal Hammer
- **Software Used:**
  - [QuickDAQ](https://www.digilent.com/shop/quickdaq/)
  - Python (Data Processing and Visualization)

## [Python Script](Vibration_Data_Analyzer.py)
- Reads files exported from QuickDAQ (or any uploaded .tab files)
- Automatically extracts data and calculates:
  - Natural frequency
  - Damping ratio
  - Logarithmic decrement
  - Harmonics
- Plots:
  - Time-domain force and acceleration
  - Frequency-domain magnitude and coherence response



