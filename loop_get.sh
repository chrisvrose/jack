#!/bin/bash
#Poor man's restart script
while true
do
python3 get_message.py # Replace with python if required
echo "Waiting for 15 seconds. Press CTL+C to cancel"
sleep 15
done
