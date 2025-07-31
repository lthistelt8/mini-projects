@echo off
cd /d C:\Users\luthi\OneDrive\Documents\GitHub\mini-projects

:: Display timestamp
echo ==== To-Do List Session Started ====
echo Date: %DATE%
echo Time: %TIME%
echo ================================

python tasks_list.py

pause
