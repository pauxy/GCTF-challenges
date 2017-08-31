# LonelyPlanet

## Question Text

WELCOME TO YOUR NEW JOB AT THE GALATIC FEDERATION AS A UNIVERSAL TRANSLATOR FOR OUR NEW CHAT APP "LONELYPLANET" DO YOUR JOB WELL AND GET PAID PILLS DO IT BADLY AND GET FIRED.

Created by paux

## Setup Guide
1. run file "LonelyPlanet.py", enable access to port `59949`

## Distribution
text file with translations
- Translation.txt
text file describing translation.txt
- readme.txt

## Solution
1.	`nc 127.0.0.1 59949` will show that the program is running, however it has a timeout function so it would bw almost impossible to complete thr challenge by typing
2.	write a socket client program to interact with lonelyplanet
3.	split the received information and retrieve the origin language,origin text and wanted language
4.	using that, open the translation file adn load it into a list 
5.	search for original word in list and return corresponding word in wanted language

## Recommended Reads

