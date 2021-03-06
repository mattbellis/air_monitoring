# 4/24/2019

[Contact at UC Davis](http://physics.ucdavis.edu/people/faculty/thomas-cahill) who has done *considerable* work with aerosols.
He spoke with Lauren at April APS about our work and might have a lot to share. 

It looks like he's used equipment from [DrumAir](http://www.drumair.com/) sampling consultants. They also have
information about different [analysis techniques](http://www.drumair.com/analysis) like PIGE/PIXE/SEM/XRF. 
And some [data](http://www.drumair.com/data) showing potassium. 


# 4/14/2019

[Fungal spores contribute to K in aerosols?](https://iopscience.iop.org/article/10.1088/1748-9326/10/3/034015)

[Sulfur, potassium, and phosphorus associations in aerosols from South American tropical rain forests] (https://agupubs.onlinelibrary.wiley.com/doi/pdf/10.1029/JC084iC07p03723)
Mention of Pb in aerosols. Also discussion about why these are released into the air. Should get full article!


[Combustion aerosols from potassium-containing fuels](https://www.osti.gov/etdeweb/servlets/purl/333920)

[Main particulate matter components in Saxony (Germany)](https://link.springer.com/article/10.1007/BF02987559) Should get full article!

[
REPORT
Biogenic Potassium Salt Particles as Seeds for Secondary Organic Aerosol in the Amazon](https://science.sciencemag.org/content/337/6098/1075?sid=91b1ba31-3de6-42fb-8600-94f47ba1ac4a) Should get full article!

[Condensed aerosol fire suppression](https://en.wikipedia.org/wiki/Condensed_aerosol_fire_suppression) uses potassium carbonate???






# 4/3/2019

Still getting what looks like turbulence. [This article](https://www.trutechtools.com/Measuring-Airflow-with-a-Pitot-Tube_c_253.html) mentions 

*"Accurate readings cannot be taken in a turbulent air stream. A Pitot tube should be inserted at least 8-1/2 duct diameters downstream from elbows, bends or other obstructions which create turbulence. To insure precise measurements, straightening vanes should be located 5 duct diameters upstream from the Pitot tube if used."* 




# 1/24/2019

[Interesting article](https://physicsworld.com/a/gran-sasso-lab-to-shut-down-controversial-experiments/) about how Borexino
and another experiment will be removed from Gran Sasso so they do not contaminate the water supply. 
Has some additional information about the water table there and the overhead (how much the mountain above provides
shielding). 

# 1/22/2019

To-do:
* (Bellis). Order the substrates. 
* (Cassandra). On this document take stock of where we are with the electronics and intake system. For example:
   * Are the electronics robust (do the wires still come out). 
   * Is the entire air intake system robust (could we put it outside right now and collect air for 2 hours)
   * Do we know where we would place it. 
   * Can we check the new, more precise Pitot tube? 

   Now that we've checked how the Pitot tube needs to be placed, we should record data for 1+ hours and see how stable things are. 



# 11/17/2018

The voltage seems to jump around which could potentially lead to *50%* uncertainties in the velocity measurements! We might
want to connect a wall-wart to the Arduino as that might make the voltage more stable. We should try this. 

https://www.google.com/search?q=arduino+stable+voltage+reference&oq=arduino+stable+voltage&aqs=chrome.1.69i57j0.5184j1j7&sourceid=chrome&ie=UTF-8

http://forum.arduino.cc/index.php?topic=22132.0

### More on this issue here
https://www.intorobotics.com/how-to-make-accurate-adc-readings-with-arduino/





# 11/16/2018

The biggest issue is removing and putting the pitot tubes back in
 * The styrofoam gets caught in the tube and has to get ripped out, making a new one is just harder and harder. The cork worked when we first had it in. Should we try to find something more efficient?

* Letting the vacuum run for 40ish minutes to see how both tubes together will measure

* Code looks a little off-- Using the same calculations, however not getting the same answers??
 * Pitot tube 2 seems to be a little off, the voltage is constantly reading 0 and the speeds are flucuating a lot, not at all the same speeds as pitot 1
* [Calculating the density of humid air](https://www.omnicalculator.com/physics/air-density#how-to-calculate-the-air-density)

# 11/9/2018

* Downloaded PySerial-- code will save straight to computer using python code

* Bellis printed out new substrate holders
* Used the mill to cut out holes for the holders to fit right in

* Code prints out everything - including DHT Sensor- Humidity-- Using a new sensor



# 11/3/2018

[PVC dimensions](https://formufit.com/pages/pvc-pipe-size-dimensions-chart) so we can get inside and outside measurements.


# 11/2/2018
What we need:

When printing off the ardiuno we need:

* Pitot 1 - Offset (Raw number btw 0-1023),Voltage (Converted to 0-5), Pressure_Dif, Vel/Speed
* Pitot 2 - " "
* Temperature
* Humidity
* Density
* Barometric Pressure

Things we should get:

* More pitot tubes?
* Another Barometric Pressure Sensor- This measuresbarometric pressure and temperature

* The humidity sensor - We have a DHT 22 ( i think) however it has never fully worke. It meaures temperature and humidity, we could try to find something that just measure humidity? Or find something that combines barometric pressure (is this necessary since we have differential pressure?), humidity and temperature.

How do we calculate the density of humid air- We have the density of dry air-- how much of a difference?

Another battery powered thing?

Monitor/simple laptop so we can leave her wherever without having to leave my laptop/someones personal (matt probably has an old laptop for this use laying around somewhere).

Code:

* saving straight to a computer/

https://arduino.stackexchange.com/questions/39224/write-data-on-the-computer-with-arduino




# 10/23/2018

[A review of atmospheric aerosol measurements (1999)](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.472.2091&rep=rep1&type=pdf) Might be worth reading. 

*"Tefon membrane filters
have also been used as impaction substrates. Although
these are more costly than "lm or foil substrates, they do
not require precleaning, and they are compatible with
nondestructive analytical methods such as x-ray #uorescence
analysis (XRF) or proton induced x-ray emission
(PIXE)."*

[Time series analysis of PIXE aerosol measurements](https://www.researchgate.net/publication/229285341_Time_series_analysis_of_PIXE_aerosol_measurements) Should read this as well. 

[Another article about PIXE measurements, including some time-dependence of potassium due to biomass burning](https://flore.unifi.it/retrieve/handle/2158/495658/15908/Is%20PIXE%20still%20a%20useful%20technique%20for%20the%20analysis%20of%20atmospheric%20aerosols%20The%20LABEC%20experience.pdf)

[Also this about optimizing PIXE measurements](https://inis.iaea.org/search/search.aspx?orig_q=RN:21089196)

[Read this talk about PIXE with high throughput!](http://airuse.eu/wp-content/uploads/2013/11/2014_Calzolai_CAARI_fin2.pdf)

# 10/19/18
3D Printing the pieces we need


# 10/5/18
Putting the dual intake design together!
45 Degree angles 
Using foam insulation to block the air escaping the pitot tube holes. 


# 9/28/2018
Four Lowe's runs;
 * Finally got all of the material for the dual intake design
 * Cut all of the PVC pipe and put the design together
 
  * Got the pipes to be at a 45 degree angle, do we want 60? 90? 180?
  

# 9/21/2018
A very big article but ctrl + f "substrate" and you'll find some good stuff.
https://www.epa.gov/sites/production/files/2017-01/documents/final_draft_pm2.5_speciation_guidance_1999.pdf

After doing some research, it is said that it is impossible to read two analog readings at once???
  * Whatever.. I tried it though and I got it to read two pitot tubes at once!?!
   * Need to add more code,, we will have a lot to read, what will we decide to "print"/ what will be necessary?i

Dual intake!!
  * Get more PVC (probably this weekend).
  * Get a PVC pipe that branches out two ways
  * More rubber connectors
    * How are we going to carry this? Take apart and put back together each time we measure??? Seems like a pain..
     * How long does the PVC pipe need to be to reduce the turbulence the pitot tube experiences?
     
Also, calibration of the pitot tube..:
Found some stuff, none of them make too much sense to me
https://www.canada.ca/en/environment-climate-change/services/canadian-environmental-protection-act-registry/publications/reference-method-measuring-releases-particulate/method-f.html

https://www.nist.gov/sites/default/files/documents/2017/10/31/alternate-pitot-tube-calibration-methodology.pdf

https://www.basicairdata.eu/knowledge-center/calibration/pitot-static-probe-calibrator/

*-- Bellis edit*
We might also want to get an anemometer for comparing windspeed measurements. 

https://www.amazon.com/PROSTER-Anemometer-Measurement-Thermometer-Windsurfing/dp/B00KYL3VNS?ref_=fsclp_pl_dp_2

https://www.amazon.com/Ambient-Weather-WM-4-Temperature-Psychrometer/dp/B00540I7WO?ref_=fsclp_pl_dp_5


# 9/14/2018

Dekati is a company out of Finland (but with an American distributor in Minnesota) who builds high quality
aerosol measuring devices. 

https://www.dekati.com/products/Fine%20Particle%20Measurement/DLPI

If you go to the accessories part of that, they make a spray and templates that might be used as a subtrate
on which we can collect particulate. 

*Dekati® Collection Substrate Spray

The collection substrates are often greased in impactor measurements to prevent particle bounce and blow-off from the impactor stages. The Dekati® Collection Substrate Spray is developed to grease the substrates faster and more evenly than with the traditional greasing methods. When used together with a stencil, the Dekati® Collection Substrate Spray enables an easy and fast way of applying a thin and smooth layer of grease on the collection substrates. The grease used in the spray is non-volatile also at low pressures and is therefore suitable for use in low pressure impactors, and also chemically pure enough to enable most chemical analysis to be done from the substrates. Stencils are available for 25 mm substrates that are used in the ELPI®+, High Resolution ELPI®+, High Temperature ELPI®+, ELPI®, DLPI+, DLPI and Dekati® PM10 impactors.*

Here is the American distributor

http://www.particleinstruments.com/


Here's a paper by a group that used their stuff and it talks about how to set up a good collection process. 

https://flore.unifi.it/retrieve/handle/2158/495657/15907/ED-XRF%20set-up%20for%20size-segregated%20aerosol%20sample%20analysis.pdf

Here's an older paper about particle bounce from 1992. 

https://www.tandfonline.com/doi/pdf/10.1080/02786829208959544

Things to do this fall:
  * Building two intakes
    * This will need two pitot tubes? Can the arduino read in two pitot tubes?
  * What else do we have to purchase?
    * Ball flow meter? Better vacuum?
  * Will have to calibrate the pitot tube every now and then
  * Will we use the XRF or PIXE?
  * Substrate / Substrate holder?




# Week 7 (7/2/18 - 7/6/18);
## Day 31:
  * Blistering hot day and a little humid;
   * This may in some ways affect our results, help or hinder? (not that we've gotten too much of what we want to see..)
  * Going to retry the idea of the tape on the removable piece with the white lithium grease behind the 2.5 filter, maybe it flew off into oblivion before due to the rain causing the tape to unstick
    * Sprayed about 6 inches away, a light coat that covered just enough of the surface
     * To be ran for about 30 minutes with battery
      * Didnotworkofcourse! 
  * Code is again messed up, will run samples without code until i figure out what's up
  * Ran samples with sticky side facing out behind both filters for 30 minutes each
  * Had to break after each run due to vacuum getting extremely hot
  * Tried the spray again, got too much on, spray got onto the sticky side of the tape causing it to be not sticky
  * Tried to spray again, held about 8 inches away and as lightly as possible sprayed the silicone lubricant.
   * The back of the tape did not get wet however after the 30 minutes, the tape was about half off the removable piece
   
   
 ## Day 32:
   * Another hot day!!
    * More samples to be ran today
   * Todays Goal; Get the spray to work!!
   * Tested the silicone spray on tape behind the 0.8 filter
     * Held about 8 inches away, very light spray
      * Running with no code because the code is still messed up ??????
     * Ran for 30 minutes
      * Tape fell off of course
   * Ripped off an even larger piece of tape and wrapped it around the entire removable piece.
   * Ran this with the same filter just to see if it would stay so I didn't waste a filter
    * When spraying the spray onto the tape, I sprayed a mist of spray into the air and let the mist fall onto the tape, about 10 inches away
     * The tape stayed on the piece!!
     * However I see no particulate, could be from the used filter, which probably was not the best idea
    * Tried to do again with 2.5 filter, saw no particulate again;
      * This is probably a good thing considering 2.5 microns is so small I probably should  not see it, however when running the samples with the sticky side of the kapton tape facing out, I always see particulate on the tape
       * This probably is not a good thing, probably a lot of contamination on it
       
   * How can we better our results and do this more precisely and consistently???
   
## Day 33:
  * America's 242th birthday
  
  * Redid all the wires on the arduino, should consider soldering to Perma Breadboard
    * [We have one of these](https://www.adafruit.com/product/571)
    * However DHT22 ( Temp and Humidity Sensor ) still does not work when running the code with the SD card
     * Cannot figure this out ??? Can't find anyone else with this problem as well
     
   * Code still is funky once battery is plugged in to power arduino?
    * It is either the pitot tube or the battery
     * Once you plug and unplug the pitot tube wires it goes back to normal but switches up every now and then
     
## Day 34:
  * Running the vacuum with the impactor disksas well as the vacuum pump
    * Hooked up ball flow meter to the vacuum pump, unless I am doing something wrong this pump is also way too strong for the ball flow meter. Not really sure what the point of it is
    * Didn't run anything with the code, since the code only works when it wants to
    * Ran the impactor disks using both the 0.8 filter and the 2.5 filter
     * Since the filter holder is a little bigger it was harder to get the impactor disk to be centered on the filter. The disk itself was not centered, however the whole disk was in the line of the stream flow.
      * Not even sure where the direct line of flow is but it's alright
      
    * It started to **pour** after only running for about 3 hours, so the vacuum pump didn't get to show her true potential.
     * The vacuum pump was incredibly hot, I couldn't even touch it. Don't know if that's from the sunlight?? Or if it was overheating
   * The battery thing only works when it wants to. Sometime the offset changes ?? Sometimes it doesn't even save the data. Sometimes it collects even when I have the switch turned to off??? Whatever
   
   * The DHT sensor suddenly somewhat works! Can't collect temperature or heat index from it however we can get the humidity. This way we can revisit our density equation. 
     * Can now solder everything to the perma board
     
     
## Day 36:
 *shoter day today since i put in extra hours throughut the week*
   * Isn't much left to do this week except analyze the samples and solder
    * Can't go to the SAInT Center because no one is here :/
    * Looked for solder for about 30 minutes, found 6 soldering irons and no solder
  * All info and video is on [this page](https://www.adafruit.com/product/571)


# Week 6 (6/25/18 - 6/29/18);
## Day 26:
  * 3-D printed filter holder with removable piece for that tape
  * Lots and lots and lots of sampling today
    * Used impactor filters;
     * Ran for 30 minutes with each of the two filters
      * Used the wrong side........ oops
    * Kapton tape on back of both filters for 30 minutes each
    * Carbon tape on back of both filters for 30 minutes each
  * Should try to find a different spot where one won't find us to be a nuisance
    
    
## Day 27:
  * Day at Union using ion accelerator again!
  * Realized our filters may be a little too thick to penetrate through, receiving a lot of background scattering
  * Found very small peaks of potassium on impactor disks!
    * Had our impactor all set up and ready to be used when we can
    * Should try to continue using the impactor disks
     * The filter holder with removable tape should be helpful to elimate the background we are getting due to the filter getting in the way
  * Can we possibly find double sided kapton tape?
  * https://www.kaptontape.com/Double_Sided_Polyimide_Tapes.php
  * https://www.caplinq.com/2-mil-polyimide-kapton-tape-silicone-adhesive-double-sided-pit2sd-series.html
  * If the impactor disks work, we can use the impactor itself or build another holder to hold the disks behind our own contraption
  
## Day 28: 
  * Went to SAInT Center to analyze samples that we already analyzed at Union
    * Next time: if we want to compare to go to Union after
    * Could not get too accurate of results due to the burn on the samples
    * Got a very small peak for potassium on 0.8 impactor disk, but not the 2.5, 
     * There was a peak at 2.5 but did not show on the spectrum 
    * Could not use SEM or use the XRF on the Carbon Tape
  * Thinking about adding the ball flow meter to our appartus, behind the pitot tube, need adapters
    * Went to lowes;
     * Got female adapters and more of those rubber connectors (2 of each)
     * Got wD-40:
      * Protective white lithium grease 
      * Water resistant silicone lube
    * Idea: spray on tape, place tape behind the filter and the particulate sticks to the WD-40
     * The point of WD-40 is to not leave a tacky, sticky residue, however particulate matter small enough may be able to stick to it

## Day 29:
  * Finally found an outdoor outlet
  * Placed tape on the removable piece of the filter holder, let run for an hour with the 0.8 filter
    * Used Bellis' battery power thing to charge the arduino
    * When using, there is a little on and off switch by the power source 
    * For some reason, the offset isn't calculating properly, could be because of the battery? We haven't changed the code at all
    
  * Put the ball flow meter in with our apparatus, the vacuum is too strong for it, would work better with the vacuum pump
  * Tried to utilize one of the WD-40's, the white lithium grease
   * Sprayed this on a piece of tape and placed on removable piece
  * Started pouring outside!!
    * We ran the vacuum for about 20 minutes before realizing that the vacuum was pulling in water
    * The piece of tape disappeared into oblivion
    
## Day 30:
  * Loro's last day :(
  * Had to put our apparatus back together due to it getting soaked yesterday
   * Ideas on how to run if it rains?
    * Have it held vertically somehow and have a cone/funnel thing at filter end to allow air to still flow in but block out the rain
    * ?????? Some type of cover over it
    * 
  * Cut down the PVC pipe a little, it was so long before because we experienced turbulence when the filter was too close to the pitot tube
  * Organized the lab
  * Fixed the code? There may be some issues with the pitot tube because all I had to do was plug and unplug the wires 
    * When finalizing and coming uo with a permanant and consistent setup, should solder the wires back in
  
# Week 5 (6/18/18 - 6/22/18);
## Day 21:
 * Day at Union utilizing the Ion Accelerater
 * Analyzed all 6 samples
 * The 2.5 micro meter filters had traces of titanium?
 * Both had Cl, Ca, Cr, Fe
 * The Vacuum or Air filter didn't pick up anything other than the pristine filter
   * Is the particulate matter bouncing off? Going straight through?
   * Could adding kapton tape to the back of the filter allow the particulate to stick to the tape
 
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
      * Having a filter holder with a tube-like apparatus that holds the filter onto the holder, then a 3-D printed strip of plastic or something for the Kapton tape 
  
* We tried to find a correlation between temperature changes and layering/changes in velocity; there isn't

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
    
 * Potassium!!!!!!!!!... very very very little potassium but she showed up??
 * The other day there were construction workers cutting into brick, could have been left over particles from that
 * Bricks are 20% - 30% Alumina (Al2O3) and 50% - 60% Silica (SiO2) so the Silicon could be from the brick dust/debri
     * http://www.civileblog.com/bricks/#Composition
     
 * Possible use of nine-stage aerosol impactor and vacuum pump.
 
 * Found a different code for pressure dif and..... have we been wrong?


## Day 24
  * Researched the nine-stage aerosol impactor;
    * Use with a vacuum pump thingy, these vacuums can run for a longer amount of time but do not pull in air as fast,
    * Could 24 hours with a vacuum pump give us the same results as 2 hours with our *regular* vacuum?
  * Utilizing the double sided carbon tape;
    * The carbon tape is conductive and can be used with the SEM in the SAInT Center;
     * Elimintaes X-rays coming in from the detector from the substrate
     
  * We chose a different spot to vacuum outside;
    * There was no construction going on and there was also a garden type area with flowers and dirt
  * Vacuumed for one hour with carbon tape on the back of a 0.8 micro meter filter & one hour on back of 2.5 micro meter filter
    * Also left carbon tape outside next to the vacuum for one hour
  
  * 3-D printed another filter holder, this one is extended (a little taller) and also has a plastic strip for tape
    * Can put mesh on the end of the filter holder, something to easily take on and off (Tape will be behind the filter)
     * We should 3-D print another filter holder to go over this tape-modified one to put the actual filter into
     
     
 ## Day 25
   * We used the SEM (Scanning Electron Microscope) in the SAInT Center
     * Analyzed the carbon tape that was on the filter(s)
      * Did not find anything of significance on the 2.5 Micron filter 
       * Things found on the tape from the 0.8 Micron filter were about 100 microns, could these be just from contamination?
   * Analyzed the carbon tape under the XRF as well,
     * Got a lot of data, could be from the stage that held the carbon tape, probably mostly contamination :/

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
  * Possibly buying or 3-D printing a case for the arduino;
    * Printed one that was downloaded from thingiverse; turned out to be a failure of course
    * Testing 2.5 filter;
     * Seemed to be running a little slower?
  * Seeing how long the vacuum can run for without breaking down;
    * Don't remember what micron filter we used 
    * 2 and a half hours before we had to go home

  
  
  
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
        
