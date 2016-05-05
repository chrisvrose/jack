# Tose-app

#### NOTE: Before running, read through the first few commented lines in each main file. It provides insight on syntax and purpose.
#### New NOTE: Forget the previous note. Just read this README. Those comments are likely outdated.

Tose-app is a bot that periodically checks for new episodes and publishes a link, and other details.

/TODO: Insert more bullshit text here.


## Files to care about

/TODO: Rename files meaningfully

* manager.py
* script.py
* send_message.py

Optional files:

* dump.py
* argsparse.py


## How do I get set up?

1. Install python 3.5.x [from here](https://www.python.org/downloads/release/python-351/) [Scroll down to the end] {No, this isn't backwards-compatible with python 2.7}

2. Download the code with git:
    * By git:
`git clone https://bitbucket.org/tose-project/tose-app` (Recommended)
    * By downloading src: [Click here and then 'Download Repository'](https://bitbucket.org/tose-project/tose-app/downloads). Extract it.

3. In terminal (Linux/OS X) or command line (Windows), navigate to the root of the folder using `cd` _Note: Needs Administrator Command Prompt in Windows. Prefix `sudo` in Linux._

4. Run `pip install -r requirements.txt`. This will install all dependencies. If you get an error like pip is not installed whatever blah, use `pip3 install -r requirements.txt`

5. Profit!


## Usage

/TODO: More bs

### manager.py
**syntax:** `python manager.py --add <serie> -s [X]X -e [Y]Y`

Example: `python manager.py --add The Flash -s 2 -e 19`

This is the main file. Almost always, this is the only script you'll ever need to run. Manages shows and seasons and episodes and stuff pre-search. Time `6 a.m. - 7 a.m. (IST` have been hard-coded in this file. Change variables `startTime` and `endTime` as required (Won't need to, mostly)


### script.py
**syntax:** `python script.py <serie> -s [X]X -e [Y]Y`

Example: `python script.py The Flash -s 2 -e 19`

Actually searches Kickass Torrents, get results and pick one. Run this for _1-time search-and-send_ Then runs send_message.py to send hangouts messages.

### send_message.py
**syntax:** `python send_message.py <message>`

Example: `python send_message.py "Hello There"`

Send message using Hangouts. Used by script.py to send links. Recipient is (currently) hard-coded in script. Edit with any text editor and change the value of `CONVERSATION_ID`


### Things to know

* The queue of pending episodes are stored in `data.js` in json format, which is automatically generated if it doesn't exist. Feel free to edit it, just maintain the structure.

* refresh_token.txt contains the OAuth 2.0 token that lets the bot sign in as 'Tose App' user into Google. _Do. Not. Delete. Ever._

* The non-essential folder is non essential. You may delete it, but why waste energy? Let it be.

* Don't mind the lazy commit descriptions.


### Who do I talk to? ###

If you happen to find a bug (highly likely with these alpha grade scripts), [create an issue here](https://bitbucket.org/tose-project/tose-app/issues).

If you have a question, do the same thing as above.

Bug a developer:

* Repo owner, any admin or developer.
* ~~Other community or team contact~~