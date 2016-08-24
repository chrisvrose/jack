# Jack

#### NOTE: Reading the code is about as tedious as catching a whale with a fishing pole. Most of the things needed to run the bot is here. Unless you're wanna know the code. Then, you're probably going to read that in just a few seconds.



Jack is a indev bot forked from a previous project.
Indev, so I might add anything I wish.


A server PC is required to run these scripts, so yes, be sure to have one lying around.


## Files to care about

Most of them are required,as they are part of the project files


## How do I get set up?

1. Setup python. Sorry, no explanation on that, as there are so many different ways to do so. If you're on Windows, **do not forget** to add python and pip, etc to the PATH during installation

2. Download the code with git:
    * By git:
`git clone https://bitbucket.org/tose-project/tose-app` (Recommended)
    * By downloading src: [Click here and then 'Download Repository'](https://bitbucket.org/tose-project/tose-app/downloads). Extract it.

3. Run `pip install -r requirements.txt`. This will install all dependencies. If you get an error like pip is not installed whatever blah, use `pip3 install -r requirements.txt`. If you're in Windows, run the `setup.py` file. _Note: Needs Administrator Command Prompt in Windows. Prefix `sudo` (Or `sudo -H` if asked to) in Linux._

## Usage

###Scripts###

#### res.sh
**syntax:** `./res.sh`

This script is for *drum roll* Linux users who'd like to keep the bot running. It will restart the bot if it crashes.

Note : It counts keyboard interrupts as a crash, and allows a 20 second gap where if CTL+C is pressed again, it will quit

Recommendation : `screen [-S *session name*] ./res.sh`

This will keep the service separated, and you can attach back to it later if you detach by using `CTL+A+D`. Refer to [screen manual](https://www.gnu.org/software/screen/manual/screen.html) for help.

#### res.bat
No syntax as per needed.

Windows equivalent of the `res.sh` file.

#### get_message.py
**syntax:** `python get_message.py`

Using prop.json, the name and custom responses will be used whenever a message with the format '*name*, *command/question*' is sent to it. 
Otherwise, Cleverbot will be used for responses. 
You can also use its `processMsg(string msg,string conversation_id)` to send messages.
If you'd like to use a message to reply with cleverbot, use `processMsg(string question,string conversation_id, 1)`. The 1, tells the script to fetch and use cleverbot's answer.

###Other files###

#### prop.json

Well, it contains three things, the bot's name, custom responses, and the lines that are invoked when the user enters an invalid code. Handle with care, don't break

### Things to know

* refresh_token.txt contains the OAuth 2.0 token that lets the bot sign in as your given (or provided) user. Delete it, but you'll have to login again.

* The prop.json can be edited to insert new responses to commands/questions

* Sorry for the commit names. We ae trying our best to sound more professional :(.


### Debian-based Linux Version Issues

Yeah, it is something in Debian-based distributions (probably others too) that python has `real big` issues. In there, `python` stands for Python v2.7, which basically trashes our project.

Ubuntu especially, is no exception (Ubuntu being the platform it is also tested on). You will notice this as "syntax" issues.

Hence, if such occurs, run with `python3` and not `python`


### Who do I talk to? ###

If you happen to find a bug (highly likely with these noob grade scripts), create an issue [here](https://bitbucket.org/tose-project/tose-app/issues).

If you have a question, do the same thing as above.


* Repo owner, any admin or developer.
* ~~Other community or team contact~~
