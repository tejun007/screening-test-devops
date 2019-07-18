#!/usr/bin/env bash
docker build --tag screening-test-backend:latest ./backend/Dockerfile
docker push tejunlee007/screening-test-backend
