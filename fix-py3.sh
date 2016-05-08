#!/bin/bash
COMMITIA=`git log -1 | grep "commit"`
COMMITIB=`cat conv_commit`
if [ "$COMMITIA" = "$COMMITIB" ]; then
   echo "Updated. Use the -py3 appended files"
else
   cp -v get_message.py get_message-py3.py
   sed -i -e 's/\"python /\"python3 /g' get_message-py3.py
   cp -v script.py script-py3.py
   sed -i -e 's/\"python /\"python3 /g' script-py3.py
   git log -1 | grep commit > conv_commit
   echo "Converted and/or updated"
fi

