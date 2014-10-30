#!/bin/bash
celery -A tasks -S caerus.CaerusScheduler --max-interval=5 -l DEBUG beat
