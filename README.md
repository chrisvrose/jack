# ToSE App

#### NOTE: Reading the code is about as tedious as catching a whale with a fishing pole. Most of the things needed to run the bot is here. Unless you're wanna know the code. Then, you're probably going to read that in just a few seconds.



Tose-app is a bot that periodically checks KAT for new episodes and publishes a link alongside a magnet link.
It also has the feature of giving snide replies in conversations.


A server PC is required to run these scripts, so yes, be sure to have one lying around.


## Files to care about

ALL, except wherever mentioned. Because otherwise it wouldn't be in this project.


## How do I get set up?

1. Install python 3.5.x [from here](https://www.python.org/downloads/release/python-351/) [Scroll down to the end] {No, this isn't backwards-compatible with python 2.7} or if you're running Ubuntu, `sudo apt-get install python3`.

2. Only if you are using Windows, grab git for Windows. Or, you can get SourceTree, and use the git terminal from there.

3. Download the code with git:
    * By git:
`git clone https://bitbucket.org/tose-project/tose-app` (Recommended)
    * By downloading src: [Click here and then 'Download Repository'](https://bitbucket.org/tose-project/tose-app/downloads). Extract it.

4. In terminal (Linux/OS X) or command line (Windows), navigate to the root of the folder using `cd` 

5. Run `pip install -r requirements.txt`. This will install all dependencies. If you get an error like pip is not installed whatever blah, use `pip3 install -r requirements.txt`. _Note: Needs Administrator Command Prompt in Windows. Prefix `sudo` in Linux._

6. Profit?!


## Usage

The various scripts have been documented here

### manager.py
**syntax:** `python manager.py --add <serie> -s [X]X -e [Y]Y`

Example: `python manager.py --add The Flash -s 2 -e 19`

This is the main file. Almost always, this is the only script you'll ever need to run. Manages shows and seasons and episodes and stuff pre-search. Time `6 a.m. - 7 a.m. (IST` have been hard-coded in this file. Change variables `startTime` and `endTime` as required (Won't need to, mostly)


### script.py
**syntax:** `python script.py <serie> -s [X]X -e [Y]Y`

Example: `python script.py The Flash -s 2 -e 19`

Actually searches Kickass Torrents, get results and pick one. Run this for _1-time search-and-send_ Then runs send_message.py to send hangouts messages.

### send_message.py
**syntax:** `python send_message.py <message> [conversation id]`

Example: `python send_message.py "Hello There"`
Example: `python send_message.py "Hello There" "HuGEconVERSATIONID"`
Example: `python send_message.py "Hello There" "shortconvname"`

Send message using Hangouts. Used by script.py to send links. Recipient can be selected, but its rather tedious. Edit with any text editor and change the value of `CONVERSATION_ID`.
Only for our convenience, we have added (Yea Yea Yea we know) a few constants so that we no longer need the huge cids for testing.

### get_message.py
**syntax:** `python get_message.py`

Its kinda fun to run this script as Cleverbot will repond. Use at your own discretion because if you use this, you will lose all your popularity (If you have any) in hangouts.

### Things to know

* The queue of pending episodes are stored in `data.js` in json format, which is automatically generated if it doesn't exist. Feel free to edit it, just maintain the structure.

* refresh_token.txt contains the OAuth 2.0 token that lets the bot sign in as your given (or provided) user. Delete it, but you'll have to login again.

* The non-essential folder is non essential. You may delete it, but why waste energy? Let it be.

* Sorry for the commit names. We ae trying our best to sound more professional :(.


### Debian-based Linux Version Issues

Yeah, it is something in Debian-based distributions (probably others too) that python has `real big` issues. In there, `python` stands for Python v2.7, which basically trashes our project.

Ubuntu, especially is no exception (Ubuntu being the platform it is also tested on). You will notice this as "syntax" issues, especially in the `send_message.py`.

In older versions, we used a script, but after a few fixes, you no longer will need (or be able to find) it. Run all commands with `python3` (Instead of `python`)


### Who do I talk to? ###

If you happen to find a bug (highly likely with these alpha grade scripts), [create an issue here](https://bitbucket.org/tose-project/tose-app/issues).

If you have a question, do the same thing as above.

If they don't respond, this file gives you the permission to do the following - 

1. Send message

2. Repeat until enter key is pulpy

* Repo owner, any admin or developer.
* ~~Other community or team contact~~
