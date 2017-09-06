# Where_Is_It

## Question Text



i realised there was suspicious traffic on my network.. it seems like someone is trying to communicate through it? help me find out what it is?<br>Thanks!

Created by paux



## Setup Guide

1. upload files



## Distribution

pcap file with network traffic
- notpatrick.pcap

## Solution


1.	look through file and you will notice a bunch of tcp packets `86-122`
2.	you will notice that the last few bits is the message sent
3. 	piecing all the packet returns the flag.

or 

follow stream!

## Recommended Reads

