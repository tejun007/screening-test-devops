#!/usr/bin/env bash
git add .
git commit -m "merge dev to master"
git push origin master

docker push tejunlee007/screening-test-backend:latest
