# Jack

#### NOTE: Highly alpha-grade stuff here. Tread carefully. Code held together by cobwebs.

#### Requirements : `hangups`, `chatterbot`, `feedparser`, `psycopb2`

Jack is a indev bot forked from a previous project.

Server required to run the python3 script. For all this, this project is essentially a complicated if then else program. :|
Or Heroku, along with the PostgreSQL plugin,

## Files to care about

ALL. I add only files that are required.
Except for those suffixed with .old, do whatever you want with them.


## How do I get set up?

1. Install python (v3.6) and download/clone jack to your workplace.

2. Run `pip install -r requirements.txt`. This will install all dependencies. If you get an error like pip is not installed whatever blah, use `pip3 install -r requirements.txt`. If you're in Windows, run the `setup.py` file. _Note: Needs Administrator Command Prompt in Windows. Prefix `sudo` (Or `sudo -H` if asked to) in Linux._

OR

1. Attach to heroku.


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
**syntax:** `./res.sh`

Sets up an infinite loop that exits only if the bot exits with a status code '0'. Useful to battle random timeouts that occur during the way.


#### l33tx.py, leetx.py and cbot.py

Used internally by `messages.py` to provide functionality.
leetx.py is a generalized search function modified from the pyleetx module from the pypi repo (now broken), which has been patched up to work properly.
l33tx.py provides for the specifiv search functions and is used by messages.py
cbot.py is specifically for usage with the bot's awake state, where it will attempt to (and sometimes fail) make conversation.

###Other kinda important files###

#### prop.json

Well, it contains three things, the bot's name, custom responses, and the lines that are invoked when the user enters an invalid code. Handle with care, don't break.

#### feeds.json

Contains information for interpreting '*name*, get me *episode* of *show*'.

#### database.db

Created only if not on Heroku. Otherwise uses the PostgreSQL server present.
Contains the speech database of `chatterbot`.
Remove it to reset Jack's progress in learning how to make conversations.

#### Procfile

If you wish to use Heroku, the Procfile has been defined for usage with a single worker.

### Things to know

* refresh_token.txt contains the OAuth 2.0 token that lets the bot sign in as your given (or provided) user. Delete it, but you'll have to login again.

* The prop.json can be edited to insert new responses to commands/questions

* Sorry for the commit names. We are trying our best to sound more professional :(.

* I have no idea what's going on
