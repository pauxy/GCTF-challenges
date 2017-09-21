#include "DigiKeyboard.h"

void setup() {
  pinMode(1, OUTPUT);
  char l[]={'.','-','-',' ','.',' ','.','.',' ','.','-','.',' ','-','.','.',' ','-','-','.','-',' ','.','.','-',' ','.',' ','.','.','.',' ','-',' ','.','.',' ','-','-','-',' ','-','.',' ','.','.','.',' ','.','-',' ','.','-','.',' ','.',' ','.','-','-',' ','.',' ','.','.',' ','.','-','.',' ','-','.','.'};
  char i[]={'I',' ','h','a','v','e',' ','a',' ','t','o','p',' ','s','e','c','r','e','t',' ','m','e','s','s','a','g','e',' ','f','o','r',' ','y','o','u',' ','a','n','d',' ','o','n','l','y',' ','y','o','u','!',' ','p','l','e','a','s','e',' ','k','e','e','p',' ','i','t',' ','a',' ','s','e','c','r','e','t'};
  cmd();
  DigiKeyboard.println("notepad");
  DigiKeyboard.delay(300);
  for(int z = 0; z < 73; z++){
    if(l[z]=='.'){
       blinks(50);DigiKeyboard.print(i[z]);
    }else if(l[z]=='-'){
      blinks(550);DigiKeyboard.print(i[z]);
    }else{
    delay(400);DigiKeyboard.print(i[z]);
    }
    delay(50);
  }
  DigiKeyboard.println();
  DigiKeyboard.println("Heres the thing");
  DigiKeyboard.println("PWokHvOGw3sRaV1hEC0qSakL1vSImr0T9UeQdvE/TfA=");
  DigiKeyboard.println("Bye Frien");
}
void cmd() {
  DigiKeyboard.delay(450);
  DigiKeyboard.sendKeyStroke(0, MOD_GUI_LEFT);
  DigiKeyboard.delay(700);
  DigiKeyboard.println("cmd");
  DigiKeyboard.delay(1300);
  }
void blinks(int i){
  digitalWrite(1, HIGH);  
  delay(i);             
  digitalWrite(1, LOW);   
  delay(100); 
} 

void loop() {
}
