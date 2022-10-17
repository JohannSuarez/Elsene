# Elsene

A webapp for downloading audio from YouTube videos.

The frontend is a form that takes the URL of the YouTube video,
and the e-mail of the recipient to send the audio file to.

Live implementation: johanns.xyz/elsene

# Prerequisites
Elsene uses youtube-dl and Python3 in the backend. The Python3 packages
are listed in requirements.txt. The app is containerized 
so all its prerequsites will be included with the built image.

# Setting up and deploying
```
git clone git@github.com:JohannSuarez/Elsene.git
```

In the root of the directory, set up the environment variables
by creating a ".env" file, and giving it string values for
EMAIL_ADDRESS and EMAIL_PASS.

[ image example here ]

From the root of the repo,
run this command to build the docker image.

```
docker build -t ytmp3 .
```
