

# Week 5 (6/18/18 - 6/22/18);
## Day 21:
 * Day at Union utilizing the Ion Accelerater
 * Analyzed all 6 samples
 * The 2.5 micro meter filters had traces of titanium?
 * Both had Cl, Ca, Cr, Fe
 * The Vacuum or Air filter didn't pick up anything other than the pristine filter
   * Is the particulate matter bouncing off? Going straight through?
   * Could adding kapton tape to the back of the filter allow the particulate to stick to the tap 
 
## Day 22:
  * Take samples for 1 hour
    * Put kapton tape behind/on the back of the filter
  * Kapton tape on the filter; start @ 10:30 AM , [0.8 micron]
    * Beginning velocities: 7 - 12 m/s
    * Velocity dropped to 7 - 9 m/s
  * Kapton tape on filter; start @ 12 PM, [2.5 micron]
    * Beginning velocities: 10 - 13 m/s
    * Remained fairly constant: 10 - 13 m/s
  * Graph layering due to precision of pitot tube
    * gpas in velocity is due to analog to digital conversion
  * Artifact of digitization, took a smooth analog data set and converted it into steps
  * Points float around because of the change in temperature
  
 * Tape Ideas:
      * Essentially snapping a filter holder with tape on it above mesh with pvs pipe, then another pipe with filter on it
      * Having a filter holder with a tube-like apparatus that holds the filter onto the holder, then a 3-D printed strip of plastic or something for the Kapton tape 
  
  
* We tried to find a correlation between temperature changes and layering/changes in velocity

* Ran 0.8 filter for 30 minutes, getting a negative pressure every now and then?

  * Temperature did not change drastically; however apparatus is in the shade
  * Biggest issue was differential pressure 
   * low teens and then up to 60's ????
  * Without filter:
   * Recorded data for 5 minutes; velocity was around 40 - 50 m/s
    


## Day 23:
  * Analyze samples in the XRF
 * On 2.5 filter;
   * Ca, Ti, Cr, Fe, Ni, Cu, Zn, Sr, Au, Mn
    * When changed to "LE" ?? (I'm guessing that means low energy), Al, Cl, K, Ca, Ti, Cr, Mn
 * In the [0.8 micron] ;
   * Ca, Cr, Fe, Ni, Cu, Zn
    * When changed to "LE"; Al, Cl, Ca, Cr, Mn, Ba
 * Just the Kapton tape:
   * Si, Fe, Ni, Zn
    * When changed to "LE"; Al, Si, Ca, Mn, Ba
    * "HE"; Ti, Fe, Ni, Zn, As
    
 * Potassium!!!!!!!!!
 * The other day there were construction workers cutting into brick, could have been left over particles from that
 * Bricks are 20% - 30% Alumina (Al2O3) and 50% - 60% Silica (SiO2) so the Silicon could be from the brick dust/debri
     * http://www.civileblog.com/bricks/#Composition
     
 * Possible use of nine-stage aerosol impactor
  

# Week 4 (06/11/2018 - 06/15/2018):
## Day 16:
 * We increased the distance between the pitot tube and the filter holder, this fixed some of our issues with getting a negative pressure
 * Took test measurements, had mesh over the filter and filter holder so the filter didn't get sucked in 
 * We used the XRF to test a few samples, we tested the inside and outside of a banana peel, a filter that was rubbed on the banana peel, a filter rubbed on the ground and kinda on a tree and a fresh, pure filter
 * The PDF's and CSV's as well as the HD Prime viewer onto a flash drive
 * Found ideas on Thinkiverse for a new filter holder that clicks in 
 * Also worked a little bit on the poster template, creating rough draft for poster on our Air Monitoring experiment
     * Helpful articles for poster:
          * https://www.nature.com/articles/d41586-018-03991-y
          * https://physicsworld.com/a/dark-matter-and-muons-are-ruled-out-as-dama-signal-source/
          
## Day 17:
 * Worked on the poster board more
 * https://science.nasa.gov/astrophysics/focus-areas/what-is-dark-energy
 * 3-D printed more filter holders
    * Links to which ones we used (previously linked in Github):
      * https://www.thingiverse.com/thing:2485988
      * https://www.thingiverse.com/thing:2480965
    * These filters holders do not work!! >:(
  * Used a cork to block air coming out of hole where pitot tubes come out
  * Ran the vacuum for 10 minutes, 20 minutes, then 30 minutes.
     * For every ten minutes she pulled in *about* 9 cubic meters of air 
     * Ten minutes - 9 m^3; 20 minutes 15 m^3; 30 minutes - 25 m^3
    
  
  
# Day 18
  * Started using data logging shields
  * Soldered the shield to the arduino
  * All day failed at finding a code to get the data to save
  * We lose analog A4, A5; digital 10, 11, 12, 13
  
  * Vacuum data should be about right!!

# Day 19

  * Failed *again* at getting the data on to the SD card,,, untill Bellis does his magic and gets it working
  * For some reason, the code crashes when anything involving the DHT22 sensor for humidity and temperature
  * For right now, we are using the barometric pressure sensor to get temperature, however will need to revisit to get a precise density using humidity
  * Tested the 0.8 micrometer filter for 30 minutes in the vacuum and another one sitting out in the open next to the vacuum.
  
# Day 20

  
  
  
# Week 3 (06/04/2018 - 06/08/2018):

## Day 11:
  * 3-D printed prototypes of the filter holder and the prototype of the apparatus that will hold the pitot tube in place within the PVC pipe
  * It took three tries to get the correct measurements for the pitot tube holder, first we tried the holder to have a diameter of 30mm, each leg was 13.5, second try was making the holder to have a diameter of 35mm and the legs to be 15mm each which was too big and the third holder has measurement of 45mm for the radius and 20.50 for each leg. Hopefully this last prototype has the correct measurements or else it's back to the drawing board
  * The filter holder only took two tries, the first try the holder was too small it wasonly 50mm in diameter whereas the new one is 52mm
  * The filter fits well onto the new filter holder
  * The next step is to mount everything onto a vacuum to see if they'll stay
  * We will be getting new filters tomorrow and figuring out what material they're made out of which will help when we analyze our air samples via the XRF machine
  
## Day 12:
 * Created the prototype for the pitot tube holder and attachments to the vacuum
 * Went to Lowes and purchased necessary materials
   * Used cups, hot glue, the pitot tube and filter holderprototypes, pvc pipe and other connector to create prototype
   https://formufit.com/pages/pvc-pipe-size-dimensions-chart
   
## Day 13: 
 * Work on tactile button switch 
 * Wiring it with LED to see if we can get it to work
 * Messed around with previous prototype
 * https://learn.adafruit.com/adafruit-arduino-lesson-6-digital-inputs/push-switches
 * https://learn.adafruit.com/adafruit-arduino-lesson-6-digital-inputs/arduino-code
 * https://learn.adafruit.com/adafruit-arduino-lesson-6-digital-inputs/breadboard-layout
 * https://www.arduino.cc/en/Tutorial/Button
 
## Day 14
 * Went to target to get a Black and Decker cordless lithium battery powered vacuum.
 * This isn't the best thing for the experimetn considering it runs on a battery
 * Went to lowes to get some connecters for our apparatus, shoutout to Raffi.
 * We went back to Target and got a Bissel vacuum.
 
 
## Day 15
 * We put together our apparatus.
 * When hooked up to the vacuum, we think we were getting good measurements.
   * When we put on a filter, or something that covered up the air, we were getting nans for our velocity
    * How do fix?????




# Week 2 (05/28/2018 - 06/01/2018):

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
 Humidity [What is humidity](http://www.edinformatics.com/math_science/what_is_humidity.htm)
     
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
  
   * The filters we have are 4.5 cm roughly, would 8 of them to amount to the 15 cm sized filter
  * Thinking about attaching a cone to the end of the pitot tube hose and then the pitot tube hose to the vacuum with a filter in front of pitot
  * Probably will need ball flow meter, possibly a manometer if we need density
   * Whilst we could calculate density somehow, it is confusing because there are different equations for dry air and humid but Dr.Rhoads said that humid air doesn't really matter
  * Tested out the vacuum; I think it works?? 
   * Measuring the velocity at around 100 mph
   
## Day 10

Possible relevant article [PIXE and XRF analysis of atmospheric aerosols from a site in the West area of Mexico City](https://www.sciencedirect.com/science/article/pii/S0168583X13007581)

Also this one, [Simultaneous PIXE and XRF elemental analysis of atmospheric aerosols](https://www.researchgate.net/publication/271226028_Simultaneous_PIXE_and_XRF_elemental_analysis_of_atmospheric_aerosols)

Also this! [Potassium as a Marker in Air Particulate Matter After Crop Residue Burning Events in Patiala, India](https://www.researchgate.net/publication/257164864_Potassium_as_a_Marker_in_Air_Particulate_Matter_After_Crop_Residue_Burning_Events_in_Patiala_India)

Learned how to use the XRF in Saints Center-
  * Many questions were raised regarding things to do/ things we need
    * What are our filters made of? How do we minimize contaminating the filter? How do we maximize the measurements we take? 
  * Should get our own hard drive// can we collect raw data? 
  
Ideas of 3D printing a filter holder
http://www.hi-q.net/products/filter-holders/combination-cartridge-paper-holders/default.html


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
        
