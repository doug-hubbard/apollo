FROM python
#RUN pip3 install pytube

RUN mkdir -p /root/youtube
RUN mkdir -p /root/youtube/downloads
WORKDIR /root/youtube
RUN git clone -b fix_throttling https://github.com/davidegazze/pytube.git
RUN pip install ./pytube
ADD app /root/youtube

ENTRYPOINT ["python", "-u", "download.py"]