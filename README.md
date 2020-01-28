# YouTube Video to mp3 Converter

Converts the YouTube videos stored in your playlist to mp3 files (best used for songs!)

### Table of Contents
1. [Project Motivation](#motivation)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Contribute](#contribute)

***

<a name="motivation"/>

## Project Motivation

You know the drill---You find a great song on YouTube, and wish there was an mp3 for offline listening. Well, wishes do come true!

***

<a name="installation"/>

## Installation

**Installation with pip:**  Type this in the terminal:<br/>
`pip install dizzy-dj`

***

<a name="usage"/>

## Usage

Here's a sample usage demonstration:
```
from dizzydj import Downloader


playlist = 'https://www.youtube.com/playlist?list=PL__7grx6zYyDAIzTQ5tWVv2SZjvgzLziN'
chrome_path = 'path\\to\\chromedriver.exe'
quality = '320'
rename = True

# 'playlist' is the playlist name
# 'chrome_path' is the chromedriver.exe path
# '320' is the music quality in kbps
# 'rename' is for renaming files or not

obj = downloader.Downloader(playlist, chrome_path, quality, rename)
obj.download()
``` 

Download `chromedrive.exe` from [this](https://chromedriver.chromium.org/downloads) link.<br/>
Check your chrome version from [this](https://support.chall.com/hc/en-us/articles/200336349-How-do-I-determine-what-version-of-Google-Chrome-I-m-using-) link.

***

## Contribute

1.  Fork the repository from Github
2.  Clone your fork

`git clone https://github.com/yourname/DizzyDJ.git`

3.  Add the main repository as a remote

`git remote add upstream https://github.com/kaustubh-ai/DizzyDJ.git`

4.  Create a pull request!
