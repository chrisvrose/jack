#!/bin/bash
# Please note that you can use the screen res.sh command to be able to work properly

result=1
while [ $result -ne 0 ]; do
  python3 messages.py
  result=$?
  if [ $result -ne 0 ]; then
    echo "Not sure if crashed or quit by ctl+c. Press ctl+c to quit"
    sleep 20
  else
    echo "Graceful shutdown - Exiting"
  fi
done
