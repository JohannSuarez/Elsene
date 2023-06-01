FROM python:3.10

# set the working directory
WORKDIR /app

# install dependencies
COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt
# youtube-dl needs to be installed.
RUN apt update
RUN apt install -y ffmpeg
#RUN curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
RUN pip install --upgrade --force-reinstall "git+https://github.com/ytdl-org/youtube-dl.git"

RUN chmod a+rx /usr/local/bin/youtube-dl

# copy the scripts to the folder
COPY . /app

# start the server
CMD ["make", "run"]
