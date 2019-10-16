# Stytra hackathon!

### Hackathon program

- **Day 1**: tutorials
  - GUI programming in Python - the PyQt library
  - Stytra nitty-gritties
  - Version control with github - a recap
  - unit testing
 
 - **Day 2 - 3**: coding
 
 - **Day 3**: presentations
 


### #TODOs and potential projects

List of potential projects, together with the topics they cover.

**1. Documentation!**
   
   Parts of stytra are still quite un-documented and obscure and it would be important to fix this. Also, if would be very convenient to make little video tutorials for things like adjusting tracking parameters, calibrating, etc.
    - Broad understanding of the commented code; acting skills for the video recording
    Miguel
    
**2. Automatic fish detection**

   Andreas developed a (convolutional neural network-based) automatic fish features detector. It would be cool to use this approach to automatically place the ROI for the tail/eyes tracking. Crawling the J:/experiments folder should provide quite a lot of training data (an example notebook that extracts that exists)
    - Stytra core internals/tracking modules, neural networks (keras?)
    Diego, You, Ot
    
**3. Stimulus / experiment replay**

   For some analyses (for example, event-triggered averaging such as the behavior receptive fields of Andreas' paper) it would be useful to have in stytra the possibility of "play back" exactly the stimulus that was shown during an experiment. Also, controlling randomness in expoeriments could enable some interesting analysis (e.g. if every run of the coherence experiment is exactly reproducible)
    - Stytra core internals/stimulation modules. Approachable if you have written a few of your own stimuli.
    Luigi, Vilim, 

**4. Clean up names and coordinate systems**

   There are still errors and inconsistencies in stytra reference frames of fish and stimuli, and stimuli attributes and arguments names. Making all of this more consistent would be very important.
    - Stytra stimulation and tracking modules
    Olga, Tugce

**5. Experiment browser**

   A little GUI that allows a user to open a folder with stytra experiments inside, have a look (and potentially fix) metadata,  load and overview data from the experiment and easily discard failed experiments. Ot should have already something to work with. 
   Three modules: for freely-swimming, eye-tracking and tail tracking should provide nice previews. Thinking about how to make a generic 1-D plot for protocol runs.
    - Python GUI design, Stytra metadata
    Ot, Hagar, Elena

**6. Create full user interface movie thorugh screen grabbing**
   For explanatory purposes (presentations, supplementary materials, etc) it would be useful to have an easy way of generating little videos of the full experiment (live stimulus, camera video, and live traces for tail/eyes/position)
    - Stytra core internals, PyQt 
    Hagar, You

**7. Parameters GUI improvements**
   Stytra parameter windows could help some fixes and improvements!, fixing bugs with fish id, log names etx
    - Stytra parameterization, lightparams library, PyQt GUI design
    Tugce

**8. Angular units support**
   Is there a way of specifying stimulus dimensions in visual field angles instead of absolute screen centimeters? 
    - Stytra calibration, stimulation modules
    Kata, 

**9. Improve calibration user interface**
   The calibration procedure for the freely swimming fish could be made more intuitive, with step-by-step instructions on the GUI itself.
    - Stytra calibration, PyQt GUI design
    Virginia, 

**10. Improve replay user interface**
   We still have some hope that the replay tool to adjust the stimulus parameters might prove useful in the future - and you could help making this possible!
    - Topics/requirements: Stytra video display, PyQt GUI design
    
    
**11. Improve structre of multiple session experiments (e.g. 2p)**
  Right now there is no way of assinging completed experiments togehter except by putting things in a folder or looking at multiple metadata fields (fish id and experimenter id, not fully reliable). Also 2p experiments add hunderds of entries to the database (should be easy to fix)
  - a bit of python and understanding Stytra strucutre
  Diego, 
  
**12. Portugues Panopticon**
  There is a MongoDB database where all experiments done with Stytra are recorded. A rudimentary interface built with Python/Flask exists, but is quite feature-poor and does not scale to current number of experiments. Building a new thing with modern web technologies with just a few features would be very useful
  - python (one web framework, FastAPI recommended) and willingness to deal with Web technologies (HTML, CSS, Javascript)
  Tugce, Ot
  
**13. Implement you new Stytra experiment?**
    Miguel
    
**14. Hardware interfacing class and preferences**
    Settings window for saving, format hardware etc
    Virginia, Kata, 
    
**Clippy **
