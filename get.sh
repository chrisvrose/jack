while true
do
if [ "$1" == "3"  ];
then
python3 get_message.py # Keeping on and restart in case of an error
else
python get_message.py
fi
echo "Restarting in 15 seconds. Press CTL+C to cancel"
sleep 5
done
