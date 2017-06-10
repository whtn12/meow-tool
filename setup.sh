#!/bin/bash

echo  [*]-------------------------------[*]
echo  [-]Sometimes love isnt enough  to [-]
echo  [-]run a script                   [-]
echo  [-]There are requirements  hhh    [-]
echo  [*]-------------------------------[*]
sleep 2
echo  Let s check wether you have pip sweethearts
sleep 2
if (pip); then
	echo  Oh yea  yes you have buddy 
	echo  Now lets generate a list of the requirements and create what we need
	sleep 2
	pip freeze > requirements.txt
	sleep 2
	clear	
	echo  --->And Voila xD
	ls requirements.txt
	sleep 1
	echo  ----> Look buddy we need to install this lol
	sudo pip install -r requirements.txt
	sleep 1
	clear
	echo   Everything is installed my friend :
	echo   We had a good conversation but I need to go 
	echo   Im taking my requirements.txt file with me
	sleep 2 
	rm -f requirements.txt
else
echo  Install pip for god sake ...
fi		
