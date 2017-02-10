# Jack

#### NOTE: Reading the code is about as tedious as catching a whale with a fishing pole. Most of the things needed to run the bot is here. Unless you're wanna know the code. Then, you're probably going to read that in just a few seconds.



Jack is a indev bot forked from a previous project.
Indev, so I might add anything I wish.


A server PC is required to run these scripts, so yes, be sure to have one lying around. Basically, anything with access to the internet and can execute python3 scripts.


## Files to care about

ALL. I add only files that are required.


## How do I get set up?

1. Install python (v3) and download/clone jack to your workplace.

2. Run `pip install -r requirements.txt`. This will install all dependencies. If you get an error like pip is not installed whatever blah, use `pip3 install -r requirements.txt`. If you're in Windows, run the `setup.py` file. _Note: Needs Administrator Command Prompt in Windows. Prefix `sudo` (Or `sudo -H` if asked to) in Linux._

## Usage

###Scripts###

#### messages.py
**syntax:** `python messages.py`

Using prop.json and feeds.json, the name and custom responses will be used whenever a message with the format '*name*, *command/question*' is sent to it. 
Otherwise, Cleverbot will be used for responses. 
You can also use its `processMsg(string msg,string conversation_id)` to send messages.
If you'd like to use a message to reply with cleverbot, use `processMsg(string question,string conversation_id, 1)`. The 1, tells the script to fetch and use cleverbot's answer.
Also, it fetches magnet links of defined sources from 'feeds.json'.

#### screen.sh
**syntax:** `./screen.sh`

Creates a `screen` session that can be detached by CTL+A+D and reattached by `screen -r jack`

#### res.sh
**syntax:** `./res.sh

Sets up an infinite loop that exits only if the bot exits with a status code '0'. Useful to battle network issues.

#### res.bat

Refer above.

#### et.py and cbot.py

They are used internally by `messages.py` to provide functionality. I used different files so as to be able to differentiate between code.

###Other kinda important files###

#### prop.json

Well, it contains three things, the bot's name, custom responses, and the lines that are invoked when the user enters an invalid code. Handle with care, don't break.

#### feeds.json

Contains information for interpreting '*name*, get me *episode* of *show*'.

### Things to know

* refresh_token.txt contains the OAuth 2.0 token that lets the bot sign in as your given (or provided) user. Delete it, but you'll have to login again.

* The prop.json can be edited to insert new responses to commands/questions

* Sorry for the commit names. We are trying our best to sound more professional :(.

* I have no idea what's going on