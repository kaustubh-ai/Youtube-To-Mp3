# YouTube Video to mp3 Converter

Converts the YouTube videos stored in your playlist to mp3 files (best used for songs!)

### Table of Contents
1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [Usage](#usage)
4. [Contribute](#contribute)

***

<a name="installation"/>

## Installation

**Installation with pip:**  Type this in the terminal:<br/>
`pip install dizzy-dj`

.........................................................................................................................................................................................................................................................
<a name="motivation"/>
## Project Motivation
You know the drill---You find a great song on YouTube, and wish there was an mp3 for offline listening. Well, wishes do come true!

<a name="usage"/>
## Usage
Here's a sample usage demonstration:
```
from dizzydj import Downloader

# 'Music' is the playlist name
# Make sure to add the 'r' for chromedriver.exe path
# '320' is the music quality in kbps

obj = Downloader.Downloader('email@gmail.com', 'Music', r'path/to/chromedriver.exe', '320')
# Enter password when prompted
obj.download()
``` 
Download chromedrive.exe from [this](https://chromedriver.chromium.org/downloads) link.<br/>
Check your chrome version from [this](https://support.chall.com/hc/en-us/articles/200336349-How-do-I-determine-what-version-of-Google-Chrome-I-m-using-) link.

***

## Contribute

1.  Fork the repository from Github
2.  Clone your fork

`git clone https://github.com/yourname/DizzyDJ.git`

3.  Add the main repository as a remote

`git remote add upstream https://github.com/kaustubh-ai/DizzyDJ.git`

4.  Create a pull request!
