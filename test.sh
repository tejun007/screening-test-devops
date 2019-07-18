#!/usr/bin/env bash
pip install --trusted-host pypi.python.org -r ./backend/requirements.txt
pytest ./backend
