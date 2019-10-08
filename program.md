# Stytra hackathon!

### Hackathon program

- **Day 1**: tutorials
  - GUI programming in Python - the PyQt library
  - Stytra nitty-gritties
  - Version control with github - a recap
 
 - **Day 2 - 3**: coding
 
 - **Day 3**: presentations
 


### #TODOs and potential projects

List of potential projects, together with the topics they cover.

**1. Documentation!**
   
   Parts of stytra are still quite un-documented and obscure and it would be important to fix this. Also, if would be very convenient to make little video tutorials for things like adjusting tracking parameters, calibrating, etc.
    - Broad understanding of the commented code; acting skills for the video recording
    
**2. Automatic fish detection**

   Andreas developed a (convolutional neural network-based) automatic fish features detector. It would be cool to use this approach to automatically place the ROI for the tail/eyes tracking
    - Stytra core internals/tracking modules, neural networks (keras?)
    
**3. Stimulus / experiment replay**

   For some analyses (for example, event-triggered averaging such as the behavior receptive fields of Andreas' paper) it would be useful to have in stytra the possibility of "play back" exactly the stimulus that was shown during an experiment.
    - Stytra core internals/stimulation modules

**4. Clean up names and coordinate systems**

   There are still errors and inconsistencies in stytra reference frames of fish and stimuli, and stimuli attributes and arguments names. Making all of this more consistent would be very important.
    - Stytra stimulation and tracking modules

**5. Experiment browser**

   A little GUI that allows a user to open a folder with stytra experiments inside, have a look (and potentially fix) metadata,  load and overview data from the experiment and easily discard failed experiments. Ot should have already something to work with
    - Python GUI design, Stytra metadata

**6. Create full experiment movie**

   For explanatory purposes (presentations, supplementary materials, etc) it would be useful to have an easy way of generating little videos of the full experiment (live stimulus, camera video, and live traces for tail/eyes/position)
    - Stytra core internals, PyQt 

**7. Parameters GUI improvements**

   Stytra parameter windows could help some fixes and improvements!
    - Stytra parameterization, lightparams library, PyQt GUI design

**8. Angular units support**

   Is there a way of specifying stimulus dimensions in visual field angles instead of absolute screen centimeters? 
    - Stytra calibration, stimulation modules

**9. Improve calibration user interface**

   The calibration procedure for the freely swimming fish could be made more intuitive, with step-by-step instructions on the GUI itself.
    - Stytra calibration, PyQt GUI design

**10. Improve replay user interface**
   
   We still have some hope that the replay tool to adjust the stimulus parameters might prove useful in the future - and you could help making this possible!
    - Topics/requirements: Stytra video display, PyQt GUI design
    
**11. Implement you new Stytra experiment?**

