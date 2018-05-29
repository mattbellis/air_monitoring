
# Week 1 (5/21/2018-5/25/2018)

**Notes** 
## *Day 1 *:
* I learned what exactly an arudino is as well as the parts to an arduino
*  I was issued an arduino (well Adadfruit Metro but basically the same thing), breadboard, a box LED's, a box of resistors and a box of wires
*  I learned to wire the Adafruit and breadboard so an LED would blink
*  Basically an intro to what we are doing as well as getting familiar with our work space
        
## *Day 2 *:
* I spent time learning how to wire the circuit for multiple LED's
* That took me literally all day to figure out because of software issues on the computer
  * I purchased an adapter due to my computer being a Macbook Pro Sierra version 10.13.4 therefore it does not have a normal USB port. It was a USB-C to USB adapter cable by Apple, bought from Best Buy for $20.52      
  * Turns out it was actually just my security settings, eventually got the lights blinking
  * I was issued a pitot tube, pitot tube measures Voltage but we need it to measure air pressure
    * How are we going to go about this...?
* We need to know total mass of air that flows through the tube
  * Volts to pressure?
  * 1024 reading = 5V (analog)
        
## *Day 3 *:
           * We will be spending time logging information as well as testing the pitot tube
           * I personally need to figure out how to connect the tube, I have been reading links and stuff about the tubes
              https://www.grc.nasa.gov/www/k-12/VirtualAero/BottleRocket/airplane/pitot.html
              https://en.wikipedia.org/wiki/Pitot_tube
              https://www.grc.nasa.gov/www/k-12/VirtualAero/BottleRocket/airplane/bern.html 
              
             Velocity equation help:  https://physics.stackexchange.com/questions/95620/relation-between-pressure-velocity-and-area  
            
            +Data Sheet to convert Voltage to Pressure: https://www.mouser.com/ProductDetail/NXP-Freescale/MPXV7002DP?qs=sGAEpiMZZMvhQj7WZhFIALpLlyV3lh9L9vMZsod5OrI%3d
 ## *Day 4*:
              + We fixed the code for the pitot tube, we made it so the offset corrected itself 
              + We learned how to connect the temp/humidity sensor to the arduino
                    ++ We had issues with the code but it turns out Lauren just did the wrong one, we needed to download a few things and eventually it was working. That and there were slight modifications to the wiring.
                    
              https://learn.adafruit.com/dht/dht-circuitpython-code
                    
## Day 5:
              + Today's goal was to rewire the temp/humidity sensor just to make sure we can replicate it
              + We are going to try and set up the barometer to get barometric pressure readings, temp readings and altitude readings
              + It took us 5 hours of rewiring, recoding , searching the web and just ultimately wanting to die before we realized that we just needed to solder the pins to the barometer sensor
              + We added to the code to calculate air density using measurements that we obtain through the sensor
              + Overall very successful day, next step is to assemble/mount the sensors onto a vacuum
              
              https://learn.adafruit.com/using-mpl3115a2-with-circuitpython/hardware
              https://www.brisbanehotairballooning.com.au/calculate-air-density/

# Week 2 (05/28/2018 - 06/01/2018)
        


