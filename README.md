# Tose-app #

##### NOTE: Before running, read through the first few commented lines in each main file. It provides insight on syntax and purpose #####

Tose-app is a bot that periodically checks for new episodes and publishes a link. Bleh.

### Files to care about ###
##### (Rename files meaningfully later) #####

* manager.py
* script.py
* send_message.py

Optional files:

* dump.py
* argsparse.py

### How do I get set up? ###

COMING UP

* Summary of set up
* Configuration
* Dependencies
* Database configuration
* How to run tests
* Deployment instructions

### Usage ###

#### manager.py ####
This is the main file. Run with `python manager.py` to kickstart the whole thing.
Use to periodically run script.py
Manages shows and seasons and episodes and stuff pre-search.
Also, like a master file sort of thing.

#### script.py ####
Use to actually search kickass, get results and pick one.
Runs send_message.py to send hangouts message whenever required.

#### send_message.py ####
Use to send message to hangouts. Used by script.py to send links.


### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact