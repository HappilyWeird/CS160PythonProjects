int pot_val;
int max_val = 1010;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(A1, INPUT);
  pinMode(12, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(4, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  pot_val = analogRead(A1);
  Serial.print("The value of the potentiometer is: ");
  Serial.println(pot_val);
  delay(1000);
  if (pot_val > max_val) {
    digitalWrite(4, HIGH);
  }
   else {
    digitalWrite(4, LOW);
  }
       if (pot_val > max_val * 2 / 3) {
        digitalWrite(8, HIGH);
      }
       else {
       digitalWrite(8, LOW);
     }
    if (pot_val > max_val/3) {
    digitalWrite(12, HIGH);
  }
   else {
    digitalWrite(12, LOW);
  }
}
