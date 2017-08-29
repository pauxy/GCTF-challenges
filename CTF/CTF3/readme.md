# DEAD BABE IS DEAD

## Question Text

HELP!!I CANT OPEN THIS FILE:((
I NEED IT FOR AN ASSIGNMENT ;_;

Created by paux

## Setup Guide
1. upload files

## Distribution
image for "decrypt"
- flag.jpg 

## Solution

This is a relatively simple picture recovery challenge, where i change 7 bytes of a jpg header file, disabling it from being opened. This can be solved by using "hexeditor" on linux to edit the front 7 bytes from "de ad ba be 15 de ad" to "ff d8 ff e0 00 10 4a" will enable you to be able open the file and seeing the image with the flag.

## Recommended Reads
