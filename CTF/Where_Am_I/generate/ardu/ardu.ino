#include "DigiKeyboard.h"

void setup() {
  pinMode(1, OUTPUT);
  char l[]={'.','-','-',' ','.',' ','.','.',' ','.','-','.',' ','-','.','.',' ','-','-','.','-',' ','.','.','-',' ','.',' ','.','.','.',' ','-',' ','.','.',' ','-','-','-',' ','-','.',' ','.','-','.',' ','.','-','-',' ','-','.','.'};
  cmd();
  DigiKeyboard.println("notepad");
  DigiKeyboard.delay(400);
  DigiKeyboard.println("Hey friend i have a secret message for you! keep it safe!");
  DigiKeyboard.println("Heres the secret thing");
  DigiKeyboard.print("bp9SQPPssHVXgnOOkQ5k91jAfMgC0ur2jfPIwwZh8Cc");//"=" is needed here but can also be guessed when you get an error
  DigiKeyboard.delay(250);
  DigiKeyboard.println("SbCg==");//fake lol
  // why am i doing this ? i dunno
  DigiKeyboard.println("Bye Frien, dont lose it!!!!");
  
  for(int z = 0; z < 73; z++){
    if(l[z]=='.'){
       blinks(60);
    }else if(l[z]=='-'){
      blinks(550);
    }else{
    delay(600);
    }
    delay(80);
  }
  while (true){
    blinks(random(60,660));
    delay(80);
  }
}
void cmd() {
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(0, MOD_GUI_LEFT);
  DigiKeyboard.delay(850);
  DigiKeyboard.println("cmd");
  DigiKeyboard.delay(1750);
  }
void blinks(int i){
  digitalWrite(1, HIGH);  
  delay(i);             
  digitalWrite(1, LOW);   
  delay(100); 
} 

void loop() {
}
