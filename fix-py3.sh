#!/bin/bash
COMMITIA=`git log -1 | grep "commit"`
COMMITIB=`cat conv_commit`
if [ "$COMMITIA" = "$COMMITIB" ]; then
   echo "Already updated. Use the -py3 appended files. Remove the conv_commit file to force update the py3 files."
else
   cp -v get_message.py get_message-py3.py
   sed -i -e 's/\"python /\"python3 /g' get_message-py3.py

   git log -1 | grep commit > conv_commit
   echo "Converted and/or updated"
fi


