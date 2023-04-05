const int  buttonPin = 2; 

int buttonPushCounter = 0; 
int buttonPushCounter1 = 0;   //Button presses
int buttonState = 0;          //Current state
int lastButtonState = 0;      //Previous state

void setup() {
  pinMode(buttonPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  buttonState = digitalRead(buttonPin);
  if (buttonState != lastButtonState) {
    if (buttonState == HIGH) {
      buttonPushCounter++;
    if (buttonPushCounter != buttonPushCounter1){
      Serial.println("water");  
      buttonPushCounter1++;
      };
    delay(50);
  };
};
  lastButtonState = buttonState;
}