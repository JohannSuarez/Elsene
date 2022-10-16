
# Elsene
A webapp for downloading audio from YouTube videos.


Live implementation: johanns.xyz/elsene

# Prerequisites
Elsene uses youtube-dl and Python3 in the background. The Python3 packages
are listed in requirements.txt. The app is containerized 
and so all its prerequsites will
be included with the built image.

# Setting up and deploying

```
git clone git@github.com:JohannSuarez/Elsene.git
```


Run this command to build the docker image.

```
docker build -t ytmp3 .
```
