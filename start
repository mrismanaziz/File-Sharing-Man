#!/usr/bin/bash
#
# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

# Attemp to Terminate and Remove previous session
if [ ! -d .git ]; then
    git clone https://github.com/mrismanaziz/File-Sharing-Man -b master tmp_git
    mv tmp_git/.git .
    rm -rf tmp_git
fi

# start
python3 main.py
