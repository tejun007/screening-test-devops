#!/usr/bin/env bash
git config --global user.email "tejunlee007@gmail.com"
git config --global user.name "Taejun Lee"

git add .
git commit -m "merge dev to master"
git push origin master

docker push tejunlee007/screening-test-backend:latest
