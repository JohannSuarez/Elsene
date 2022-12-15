

<div align="center">
    <img  src="https://i.imgur.com/lcUuRuL.png">
    <h3 align="center">Elsene</h1>
    <img src="https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square"  alt="standard-readme compliant">

</div>

A webapp for downloading audio from YouTube videos.

The frontend is a form that takes the URL of the YouTube video,
and the e-mail of the recipient to send the audio file to.

Live implementation: [johanns.xyz/elsene](https://johanns.xyz/elsene/)

# Prerequisites

For a live environment, the only true prerequisite is Docker.
The app is containerized with all its dependencies included with the built image.
Elsene uses youtube-dl and Python3 in the backend, and the Python packages
are listed in requirements.txt. 

# Setup and Deployment

Clone this repository:

```
git clone git@github.com:JohannSuarez/Elsene.git
```


In the root of the directory, prepare the environment variables
by creating a ".env" file and adding values for
**EMAIL_ADDRESS** and **EMAIL_PASS**

[ image example here ]

From the root of the repo,
run this command to build the docker image.

```
docker build -t yt2mp3 .
```

Once the image is built, we can create a container instance of the image.
By default, the app runs on port 9000. 
This example command creates a container with the its port 9000 mapped to the host's port 80.

```
docker run -p 80:9000 yt2mp3:latest
```

Add the argument "-d" to run the container in the background.



