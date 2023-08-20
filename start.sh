#!/bin/bash
export PATH=${PATH}:/root/fmdev/backend/venv/bin
cd /root/fmdev/backend & \
    source /root/fmdev/backend/venv/bin/activate & \
    gunicorn --chdir /root/fmdev/backend -b 0.0.0.0:5000 "run:create_app('config')"
