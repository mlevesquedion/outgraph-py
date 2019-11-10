#!/bin/bash

python3 outmind.py valid.outline png
diff valid.png reference.png
