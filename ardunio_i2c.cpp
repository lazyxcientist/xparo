#include <Wire.h>

const int ledPIn = 13;

void setup(){
    Wire.begin(0x8); // join I2C bus with address #8 as slave

    Wire.onReceive(receiveEvent); // register event
    pinMode(ledPin, OUTPUT);
    digitalWrite(ledPin, LOW);
}

void loop(){
    // put your main code here, to run repeatedly:
}

void receiveEvent(int howMany){
    while(Wire.available()){
        char c = Wire.read();
        Classification_fun(c);
    }
}


void Classification_fun(char data){
    if (data == 'a'){
        // write code for action 1
    }else if (data == 'b'){
        // write code for action 2
    }else if (data == 'c'){
        /* code */
    }else{

    }
}