
#define BLYNK_TEMPLATE_ID "TMPL2R363TnU1"
#define BLYNK_TEMPLATE_NAME "Distance Measure 2"
#define BLYNK_AUTH_TOKEN "axcuhbKgW9sD2gcFgfhfYcFHHLYd4YGI"
#define BLYNK_PRINT Serial


#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>
#define trig D5   // Trig pin
#define echo D6 
#define trig1 D4
#define echo1 D7


char auth[] = BLYNK_AUTH_TOKEN;
char ssid[] = "Invisible";
char pass[] = "#A1B2C3#";

 
 BLYNK_WRITE(V2)
{
  digitalWrite(D0, param.asInt());
}

 
void setup()
{
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
  pinMode(trig1, OUTPUT);
  pinMode(echo1, INPUT);
  pinMode(D0, OUTPUT);
  Serial.begin(9600);
  Blynk.begin(auth, ssid, pass, "blynk.cloud", 80);
}

void loop()
{ 
  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);
  int t = pulseIn(echo, HIGH);
  int distance = t*0.034/2;
  Blynk.virtualWrite(V0, distance);

  digitalWrite(trig1, LOW);
  delayMicroseconds(2);
  digitalWrite(trig1, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig1, LOW);
  t = pulseIn(echo1, HIGH);
  distance = t*0.034/2;
  Blynk.virtualWrite(V1, distance);
  Blynk.run();
}
