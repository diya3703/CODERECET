#define trigPin 9
#define echoPin 10
#define buzzerPin 8 

void setup() {
    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);
    pinMode(buzzerPin, OUTPUT);
    Serial.begin(9600);
}

void loop() {
    long duration;
    int distance;

    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);

    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);

    duration = pulseIn(echoPin, HIGH);
    distance = duration * 0.034 / 2;

    Serial.print("Distance: ");
    Serial.print(distance);
    Serial.println(" cm");

    if (distance < 20) { // You can change the detection range
        digitalWrite(buzzerPin, HIGH); // Buzzer on
    }
    else {
        digitalWrite(buzzerPin, LOW); // Buzzer off
    }

    delay(200);
}