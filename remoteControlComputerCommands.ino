#include <IRremote.hpp>
 
// Define sensor pin
const int IR_RECEIVE_PIN = 4;

void setup(){
  // Serial Monitor @ 9600 baud
  Serial.begin(9600);
  // Enable the IR Receiver
  IrReceiver.begin(IR_RECEIVE_PIN, ENABLE_LED_FEEDBACK);
}
 
void loop(){
  //IR reciever
  if (IrReceiver.decode()){
      	//Serial.println(IrReceiver.decodedIRData.decodedRawData, HEX);
        switch(IrReceiver.decodedIRData.decodedRawData){
          case 0xBC43FF00: //shut down
          	Serial.println("a");
            delay(1000);
            break;
          case 0xBF40FF00: //restart
          	Serial.println("b");
            delay(1000);
            break;
          case 0xBB44FF00: //log out
            Serial.println("c");
            delay(1000);
            break;
          case 0xF609FF00: //open cmd
            Serial.println("d");
            delay(1000);
            break;
          case 0xE619FF00: //nuke
            Serial.println("e");
            delay(1000);
            break;
          case 0xBA45FF00: //
            Serial.println("f");
            delay(1000);
            break;
          case 0xB946FF00: //
            Serial.println("g");
            delay(1000);
            break;
          case 0xB847FF00: //
            Serial.println("h");
            delay(1000);
            break;
        }
    IrReceiver.resume();
  
  }
}

