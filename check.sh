#!/bin/bash
python -m black magic_ssg/
read -p "Press enter to execute flaske 8"
python -m flake8 magic_ssg/
read -p "Press enter to exit the system"