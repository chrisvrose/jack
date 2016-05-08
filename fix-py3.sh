
COMMITID1 = `git log -1 | grep commit`
COMMITID2 = `cat conv_commit`
if[ COMMITID1 != COMMITID2 ]
then
    cp get_message.py get_message-py3.py
    sed -i -e 's/\"python /\"python3 /g' get_message-py3
    cp script.py script-py3.py
    sed -i -e 's/\"python /\"python3 /g' script-py3
    git log -1 | grep commit > conv_commit
    echo "Converted and/or updated"
else
    echo "Already Updated"
fi
