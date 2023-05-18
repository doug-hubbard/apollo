FROM python
RUN pip3 install pytube

RUN mkdir -p /root/youtube
RUN mkdir -p /root/youtube/downloads
WORKDIR /root/youtube
ADD app /root/youtube

ENTRYPOINT ["python", "-u", "download.py"]