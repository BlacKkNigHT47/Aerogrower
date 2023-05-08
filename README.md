# Aerogrower
** A RaspberryPi based aerophonics Plant grower. **
![The AeroGrower](images/Aerogrower.jpeg)

## Introduction
 - Aeorophonics and Hydrophonics is when plants are grown without a growth medium (soil) instead the roots of the plant are fed a 

 - How are they grown
 
 - Water Irrigation & nutrients supply types
    - Sprayer
    - Drip feeding

 - In this project we propose to use Ultrasonic Mister to generate nutrient filled water solution as a mist in order to grow a plant.

 ## Benefits

 ## Required componets
    1. Raspberry Pi
    2. Breadboard
    3. Humidistat
    4. Piezo electric mister
    5. Relay
    6. LEDs


 ## Setup
The plant roots are kept in a chamber where they are constantly exposed to air, a humidistat determins the amount of humidity.
Under this chamber the water and nutrients solution tank is placed.
An Ultrasonic Pieze electric disk (mister) is placed on top of the solution tank. Therefore it is within the  Roots chamber.

## How does it work

   A Raspberry Pi monitors the Humidity through the Humidistat. When it detects a low amount of humidity, it turns ON the Piezo electric mister giving the plant the moisture and the nutrients that it needs.

   When the humidity is back to required levels, it turns OFF the Pieze electric mister. 

