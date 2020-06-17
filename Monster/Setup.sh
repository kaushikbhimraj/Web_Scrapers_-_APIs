
#! bin/bash

echo installing homebrew...
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

nano ~/.bash_profile
source ~/.bash_profile

echo Check to see homebrew is running...
brew doctor

brew search python
brew install python3

echo Creating python3 environment...
python3.7 -m venv my_env
source my_env/bin/activate

echo Load file dependencies...
sudo pip3 install requests
sudo pip3 install bs4
sudo pip3 install nltk

echo Congrats installation finished successfully.
