#!/bin/bash
rm downloads/*
docker build -t yt .
docker run -v $(pwd)/downloads:/root/youtube/downloads yt $1