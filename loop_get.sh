#!/bin/bash
#Poor man's restart script
# Run with screen -S [Some name] to help
while true
do
python3 get_message.py # Replace with python if required
echo "Waiting for 15 seconds. Press CTL+C to cancel"
sleep 15
done
