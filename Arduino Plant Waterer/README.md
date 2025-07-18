# Arduino Automatic Plant Watering System

Welcome to my Arduino-powered Automatic Plant Watering System! This project uses a moisture sensor, water pump, and microcontroller logic to keep your plants hydrated—no more forgetting to water them or worrying while you're away.

## Features

- Real-time soil moisture monitoring
- Automatic watering based on customizable threshold
- LCD display for live feedback (via I2C module)
- Status LED indicators (dry/wet/watering)
- Optional delay between checks to conserve power

## Hardware Used

- Arduino Uno (or compatible)
- Soil Moisture Sensor (analog)
- Water Pump (5V or 12V with driver/transistor circuit)
- Relay Module or MOSFET
- I2C LCD Display (16x2)
- LED + Resistor (optional for status indication)
- Power Supply (USB or external)
- Jumper wires, breadboard, or soldered PCB

## Files

- `plant_watering.ino` — main Arduino code
- `README.md` — project overview (this file)
- [`System Diagram` — circuit layout](Arduino Plant Waterer/System Diagram)
- ['Media' - photos that show my project's journey](./Arduino%20Plant%20Waterer/Media)

## How It Works

1. The moisture sensor reads the soil's moisture level.
2. If the moisture is below the set threshold, the Arduino activates the pump.
3. The pump runs for a defined time to water the plant.
4. The LCD shows moisture percentage and system status.
5. The process loops with a short delay to avoid overwatering.

## Setup Instructions

1. Connect all components as shown in the wiring diagram.
2. Upload the `plant_watering.ino` sketch to your Arduino.
3. Adjust the `moistureThreshold` variable in the code to fit your plant’s needs.
4. Power the system and monitor output via LCD or Serial Monitor.

## Future Improvements

- Wi-Fi connectivity (ESP8266/ESP32) for remote monitoring
- Smartphone app or web interface
- Multiple plant support
- Battery + solar charging

## Project Photos

Coming Soon
