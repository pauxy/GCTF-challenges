# COOKIE AGENT

## Question Text

I found this mysterious cookie secret agency site while browsing the web, please help me find out what it is about

Created by paux

## Setup Guide
1. Download tomcat
2. upload all 4 files into directory (NO SQL)

## Distribution
Distribute all the contents inside `distrib` folder to the users

## Solution

1.  when inspecting elements, you will notice that the background image is located in the directory called "more"

2.  Upon checking the directory, you will realise that there is a page called "backup.txt". This contains the java code for the jsp page

3.  The backup.txt file will also reveal that how passwords and username are read is through reading in 2 lines, the first line being username and second line being password

4.  Reading the backup.txt will reveal another file, check.txt, which contains a bunch of MD5 hashes

5.  MD5 is a rather weak hash and players can use jack the ripper to crack them.

6.  When you check the results, you will realise that two plaintexts are shown together :
```
username : root
password : roottoor
```

7.  Upon login, you will get a different screen
```
WELCOME root !
YOU ARE NOT THE AGENT IM LOOKING FOR! 
GO AWAY! 
```

8.  Upon checking backup.txt you will realise it is getting a parameter from "index.jsp" and using a function called "arrange" to get an integer which will be used to get a random string from a string array

9.  When you change the user-agent to the correct one, you will get 
```
WELCOME root !
you may be real...but you'll have to pay the required cookies to enter!
```

10. Checking again will show that the problem is with the cookie "CookieDonationBox" you can then use the chrome extension "EditThisCookie" to change it to an integer greater than 1, enabling the flag to be printed
```
WELCOME root !
Sufficiently paid!
Heres the flag "GCTF{w3_ar3_7h3_c00k13_ag3nc9}"
```


## Recommended Reads
* https://links.to.good.reads
* https://www.example.com
