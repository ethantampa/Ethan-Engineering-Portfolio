# Busbar Contact Resistance Research  
**Astronics AES – Summer 2024 Internship Project**

## Objective
Investigate how **bolt stack-up configurations**, **torque specifications**, and **bolt orientations** influence the **electrical contact resistance** in busbar connections. The goal was to optimize busbar connection design to **minimize heat generation** in low-pressure aerospace environments.

## Context
Electronic systems aboard aircraft must operate reliably at **high altitudes**, where **air pressure is low** and **convection is limited**. In such environments, **heat generated from contact resistance** becomes a critical design concern. 

## Key Research Questions
- How does **bolt torque** affect contact resistance?
- What is the role of **bolt stack-up order** (flat washer, Belleville washer, busbar layer sequence)?
- How does **bolt orientation** (vertical vs horizontal) change resistance characteristics?
- Can mechanical standardization improve electrical consistency?

## Methods
[Download the full test procedure PDF](./Busbar%20Contact%20Resistance%20Testing%20Procedure.pdf)
- Designed and assembled controlled test rigs replicating real-world busbar configurations
- Used a **4-wire Kelvin measurement** method to accurately capture micro-ohm-level resistance
- Conducted experiments at multiple torque levels and stack-up configurations for varying samples and materials
- Recorded trends in resistance vs. mechanical assembly and material

## Test Setup
### Test Rig
- Hydraulic press with load cell + DAQ for real-time force tracking of coin samples
- Torque wrench + DAQ for bolt configurations

### Contact Setups
- Small coin stacked under larger coin; contact area defined by the smaller coin
- Sample cuts of metal bolted together in varying orientations representative of busbar connections. 

### Measurement
- Micro-ohmmeter (4-wire) to track resistance while varying contact pressure

### Materials Tested
- Aluminum 6061-T6
- Aluminum 1100-H14
- Copper 110-H02

## Results Summary
- Resistance **decreased with increasing contact pressure**, then plateaued
- **Copper** showed lower and more stable resistance than **aluminum** alloys
- Dual horizontal bolts gave slightly more consistent resistance than vertical
- Washer configurations had measurable impact on variability

## Outcome
- Created a replicable test procedure for contact resistance evaluation
- Contributed to torque spec validation and contact guidelines at Astronics AES
- Research results informed design and assembly guidelines for future busbar implementations
