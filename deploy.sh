#!/usr/bin/env bash
docker-compose up -d
docker-compose ps
docker-compose down --volumes
docker-compose push
