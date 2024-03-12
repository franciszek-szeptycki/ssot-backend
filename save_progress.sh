#!/bin/bash

# save requirements
pip freeze > /home/franciszek/Desktop/own-projects/nirvana2/requirments.txt

# save .env
cp /home/franciszek/Desktop/own-projects/nirvana2/.env /home/franciszek/Desktop/own-projects/nirvana2/.env.example

git add .
git commit -m "$1"