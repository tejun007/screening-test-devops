#!/usr/bin/env bash
docker rmi tejunlee007/screening-test-backend
docker build --tag tejunlee007/screening-test-backend:latest ./backend
