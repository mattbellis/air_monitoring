
# Week 2 (05/28/2018 - 06/01/2018)

## Day 6 [Memorial Day]:
 * Designed potential model for how to hook sensors up to vacuum tube
 * Tiny holes in vacuum tube (will eventually be sealed) to thread wires through 
    * But also, attach strings to pitot tube in order ot create tension to keep pitot tube in middle of vacuum tube
 * Velcro used to secure the sensors down to the tube, velcro is easy to use because it creates a tight bond when attached but can be easily removed when trial is done
 * Zip tie to keep wires together (organizational purposes more than utility)
 
 ## Day 7:
  * Potential prototypes for apparatus
  * Get a code to make a Red LED blink while Pitot tube is calibrating the 0 level and a green LED to blink when the pitot tube starts to measure and collect data.
  * Barometer, temp & humid sensor, and pitot tube all collecting data, all connecting to arduino and breadboard. Using all three the goal is to calculate a more precise density and velocity of air.
       * Some issues; the air isnt completelt dry air- using Humid air:
            * https://www.brisbanehotairballooning.com.au/calculate-air-density/

## Day 8:
 * What is humidity? 
      * http://www.edinformatics.com/math_science/what_is_humidity.htm
     
*Bellis' comments after we talked with Prof. Rhoads.* 

Do we need a high vacuum vacuum pump? These won't shut down, but pull less air through them, on the order of 10's of liters per minute. 
* https://www.coleparmer.com/i/gast-high-capacity-vacuum-pump-doa-p704-aa/0706140?PubID=UX&persist=true&ip=no&gclid=EAIaIQobChMI2viBifyt2wIVCR6GCh2snQwJEAQYBCABEgI4hPD_BwE
* https://www.ebay.com/itm/DENTAL-MEDICAL-HYGIENIST-PORTABLE-HIGH-SUCTION-VACUUM-UNIT-PUMP-SELF-CONTAINED/282623326841?epid=518553083&hash=item41cda9ba79:g:qocAAOSwgeRZntiF

A multistage impactor will allow us to look at different sizes of the particulate. We want micro-sized particles because they will stay suspended in air. Particles that are 10's of microns will settle. 

We can normalize to air volume, not mass. 

A ball flow meter will allow us to calibrate the system. 
* https://www.google.com/search?q=ball+flow+meter&oq=ball+flow+meter&aqs=chrome..69i57j0l5.3040j0j7&sourceid=chrome&ie=UTF-8

There are holders for the filters!
* https://www.google.com/search?ei=7-wOW_PVC86P5wLMw7qwBQ&q=air+filter+open+face+holder&oq=air+filter+open+face+holder&gs_l=psy-ab.3..33i21k1.2664.4767.0.4854.11.10.1.0.0.0.96.791.9.9.0....0...1.1.64.psy-ab..1.8.705...33i22i29i30k1j33i160k1.0.7_x71_iXi8k

But they cost about $50 each!
* http://www.skcinc.com/catalog/product_info.php?products_id=189
* https://shop.pall.com/us/en/laboratory/microbiological-qc/equipment-pumps-manifolds-spare-parts/open-face-filter-holders-zidgri78l6k
* https://www.thomassci.com/scientific-supplies/Filter-Holder
* https://us.vwr.com/store/product/4829630/open-face-filter-holder-pall-laboratory

Can we 3D print a holder! Maybe by modifiying a design of something else? 
* https://www.thingiverse.com/search/page:7?q=filter+holder&sa=&dwh=85b0eee314e9d7
* https://www.thingiverse.com/thing:2485988
* https://www.thingiverse.com/thing:2480965

## Day 9:
  * Work on prototype of tube attachment that will have pitot tube
   * Potentially thinking of getting bluetooth arduino
  * Try to 3-D print a filter holder because filter holders cost around $300
   * The filters we have are 4.5 cm roughly, would 8 of them to amount to the 15 cm sized filter
  * Thinking about attaching a cone to the end of the pitot tube hose and then the pitot tube hose to the vacuum with a filter in front of pitot
  * Probably will need ball flow meter, possibly a manometer if we need density
   * Whilst we could calculate density somehow, it is confusing because there are different equations for dry air and humid but Dr.Rhoads said that humid air doesn't really matter
   
## Day 10

Possible relevant article [PIXE and XRF analysis of atmospheric aerosols from a site in the West area of Mexico City](https://www.sciencedirect.com/science/article/pii/S0168583X13007581)
  
   





# Week 1 (5/21/2018-5/25/2018)

**Notes** 
## Day 1:
* I learned what exactly an arudino is as well as the parts to an arduino
*  I was issued an arduino (well Adadfruit Metro but basically the same thing), breadboard, a box LED's, a box of resistors and a box of wires
*  I learned to wire the Adafruit and breadboard so an LED would blink
*  Basically an intro to what we are doing as well as getting familiar with our work space
        
## Day 2 :
* I spent time learning how to wire the circuit for multiple LED's
* That took me literally all day to figure out because of software issues on the computer
  * I purchased an adapter due to my computer being a Macbook Pro Sierra version 10.13.4 therefore it does not have a normal USB port. It was a USB-C to USB adapter cable by Apple, bought from Best Buy for $20.52      
  * Turns out it was actually just my security settings, eventually got the lights blinking
  * I was issued a pitot tube, pitot tube measures Voltage but we need it to measure air pressure
    * How are we going to go about this...?
* We need to know total mass of air that flows through the tube
  * Volts to pressure?
  * 1024 reading = 5V (analog)
        
## Day 3:
* We will be spending time logging information as well as testing the pitot tube
* I personally need to figure out how to connect the tube, I have been reading links and stuff about the tubes
   * Pitot Tube Information:  
        * https://www.grc.nasa.gov/www/k-12/VirtualAero/BottleRocket/airplane/pitot.html
        * https://en.wikipedia.org/wiki/Pitot_tube
        * https://www.grc.nasa.gov/www/k-12/VirtualAero/BottleRocket/airplane/bern.html 
    * Velocity equation help:  
         * https://physics.stackexchange.com/questions/95620/relation-between-pressure-velocity-and-area  
   * Data Sheet to convert Voltage to Pressure: 
        * https://www.mouser.com/ProductDetail/NXP-Freescale/MPXV7002DP?qs=sGAEpiMZZMvhQj7WZhFIALpLlyV3lh9L9vMZsod5OrI%3d
 ## Day 4:
  * We fixed the code for the pitot tube, we made it so the offset corrected itself 
  * We learned how to connect the temp/humidity sensor to the arduino
       * We had issues with the code but it turns out Lauren just did the wrong one, we needed to download a few things and eventually it was working. That and there were slight modifications to the wiring.
            * https://learn.adafruit.com/dht/dht-circuitpython-code
                    
 ## Day 5:
  * Today's goal was to rewire the temp/humidity sensor just to make sure we can replicate it
  * We are going to try and set up the barometer to get barometric pressure readings, temp readings and altitude readings
  * It took us 5 hours of rewiring, recoding , searching the web and just ultimately wanting to die before we realized that we just needed to solder the pins to the barometer sensor
  * We added to the code to calculate air density using measurements that we obtain through the sensor
  * Overall very successful day, next step is to assemble/mount the sensors onto a vacuum
       * Useful links: 
            * https://learn.adafruit.com/using-mpl3115a2-with-circuitpython/hardware
            * https://www.brisbanehotairballooning.com.au/calculate-air-density/
        
