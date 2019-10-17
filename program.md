# Stytra hackathon!

### Hackathon program

- **Day 1**: tutorials
  - GUI programming in Python - the PyQt library
  - Stytra nitty-gritties
  - Version control with github - a recap
  - unit testing
 
 - **Day 2 - 3**: coding
 
 - **Day 3**: presentations
 


### Final projects

List of potential projects, together with the topics they cover.

**1. Create new experiment / Documentation!**
   
   Parts of stytra are still quite un-documented and obscure and it would be important to fix this. Also, if would be very convenient to make little video tutorials for things like adjusting tracking parameters, calibrating, etc. The protocol class, protocol runner, and stimuli should have a more detailled introductory documentation, and the experience of starting a new experiment from scratch should be documented as well.
   
   People: 1.Elena, 1.Miguel
    
**2. Automatic fish detection**

   Andreas developed a (convolutional neural network-based) automatic fish features detector. It would be cool to use this approach to automatically place the ROI for the tail/eyes tracking. Crawling the J:/experiments folder should provide quite a lot of training data (an example notebook that extracts that exists)
    - Stytra core internals/tracking modules, neural networks (keras?)
    
   1.Diego, 1.You, 2.Ot
    
**3. Stimulus / experiment replay**

   For some analyses (for example, event-triggered averaging such as the behavior receptive fields of Andreas' paper) it would be useful to have in stytra the possibility of "play back" exactly the stimulus that was shown during an experiment. Also, controlling randomness in expoeriments could enable some interesting analysis (e.g. if every run of the coherence experiment is exactly reproducible)
    - Stytra core internals/stimulation modules. Approachable if you have written a few of your own stimuli.
    
   Luigi, Vilim 

**4. Clean up names and coordinate systems**

   There are still errors and inconsistencies in stytra reference frames of fish and stimuli, and stimuli attributes and arguments names. Making all of this more consistent would be very important.
    - Stytra stimulation and tracking modules
    1.Olga, 1.Tugce

**5. Experiment browser**

   A little GUI that allows a user to open a folder with stytra experiments inside, have a look (and potentially fix) metadata,  load and overview data from the experiment and easily discard failed experiments. Ot should have already something to work with. 
   Three modules: for freely-swimming, eye-tracking and tail tracking should provide nice previews. Thinking about how to make a generic 1-D plot for protocol runs.
    - Python GUI design, Stytra metadata
    1.Ot, 2.Hagar, 2.Elena

**6. Main GUI improvements** 
Create full user interface movie thorugh screen grabbing, calibration interface, hardare / settings window (pool with 9)
    1.Hagar 1.Virginia

**7. Coordinate system optimization**
   Is there a way of specifying stimulus dimensions in visual field angles instead of absolute screen centimeters? 
    - Stytra calibration, stimulation modules
    Kata
