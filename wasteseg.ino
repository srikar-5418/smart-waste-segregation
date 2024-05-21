#include <Servo.h>
#define step1 5
#define dir1 4
#define step2 3
#define dir2 2
Servo myservo1,myservo2,dir; 

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(step1,OUTPUT);
  pinMode(dir1,OUTPUT);
  pinMode(step2,OUTPUT);
  pinMode(dir2,OUTPUT);

  dir.attach(9);
  myservo1.attach(10);
  myservo2.attach(11);
  dir.write(90);
  myservo1.write(90);
  myservo2.write(90);

}

//dir HIGH- clockwise, LOW- anti-clockwise

//Horizontal Right- dir1-HIGH dir2-HIGH
//Horizontal Left - dir1-LOW  dir2-LOW
//Vertical top    - dir1-LOW  dir2-HIGH
//Vertical bottom - dir1-HIGH dir2-LOW
//Top Right       - dir1-LOW
//Bottom Left     - dir1-HIGH
//Top Left        -           dir2-HIGH
//Bottom Right    -           dir2-LOW

void loop() {
  // put your main code here, to run repeatedly:
  while(Serial.available())
  {
    int c=Serial.readString().toInt();
    Serial.println(c);
    int m=450;
    switch(c)
    {
    case 0:
    {
      //E-Waste
      //Left
      digitalWrite(dir1,LOW);
      digitalWrite(dir2,LOW);
      move(m);

      //Top Movement
      digitalWrite(dir1,LOW);
      digitalWrite(dir2,HIGH);
      move(m);

      ld();
      delay(1000);
      norm();

      //Bottom Movement
      digitalWrite(dir1,HIGH);
      digitalWrite(dir2,LOW);
      move(m);

      //Right Movement
      digitalWrite(dir1,HIGH);
      digitalWrite(dir2,HIGH);
      move(m);
      break;
    }
    case 1:
    {
      //food
      //Right Movement
      digitalWrite(dir1,HIGH);
      digitalWrite(dir2,HIGH);
      move(m);

      //Bottom Movement
      digitalWrite(dir1,HIGH);
      digitalWrite(dir2,LOW);
      move(m);
      
      rd();
      delay(1000);
      norm();
      //Top Movement
      digitalWrite(dir1,LOW);
      digitalWrite(dir2,HIGH);
      move(m);

      //Left
      digitalWrite(dir1,LOW);
      digitalWrite(dir2,LOW);
      move(m);
      break;
    }
    case 2:
    {
      //glass
      //Left
      digitalWrite(dir1,LOW);
      digitalWrite(dir2,LOW);
      move(m);

      //Bottom Movement
      digitalWrite(dir1,HIGH);
      digitalWrite(dir2,LOW);
      move(m);

      ld();
      delay(1000);
      norm();

      //Top Movement
      digitalWrite(dir1,LOW);
      digitalWrite(dir2,HIGH);
      move(m);

      //Right Movement
      digitalWrite(dir1,HIGH);
      digitalWrite(dir2,HIGH);
      move(m);
      break;
    }
    case 3:
    {
      //leaf
      //Right Movement
      digitalWrite(dir1,HIGH);
      digitalWrite(dir2,HIGH);
      move(m);

      //Bottom Movement
      digitalWrite(dir1,HIGH);
      digitalWrite(dir2,LOW);
      move(m);

      rd();
      delay(1000);
      norm();
      
      //Top Movement
      digitalWrite(dir1,LOW);
      digitalWrite(dir2,HIGH);
      move(m);

      //Left
      digitalWrite(dir1,LOW);
      digitalWrite(dir2,LOW);
      move(m);break;
    }
    case 4:
    {
      //medical
      //Right Movement
      digitalWrite(dir1,HIGH);
      digitalWrite(dir2,HIGH);
      move(m);

      //Top Movement
      digitalWrite(dir1,LOW);
      digitalWrite(dir2,HIGH);
      move(m);

      rd();
      delay(1000);
      norm();

      //Bottom Movement
      digitalWrite(dir1,HIGH);
      digitalWrite(dir2,LOW);
      move(m);

      //Left
      digitalWrite(dir1,LOW);
      digitalWrite(dir2,LOW);
      move(m);
      break;
    }
    case 5:
    {
      //metal
      //Left
      digitalWrite(dir1,LOW);
      digitalWrite(dir2,LOW);
      move(m);

      //Bottom Movement
      digitalWrite(dir1,HIGH);
      digitalWrite(dir2,LOW);
      move(m);

      ld();
      delay(1000);
      norm();

      //Top Movement
      digitalWrite(dir1,LOW);
      digitalWrite(dir2,HIGH);
      move(m);

      //Right Movement
      digitalWrite(dir1,HIGH);
      digitalWrite(dir2,HIGH);
      move(m);
      break;
    }
    case 6:
    {
      //paper
      //Left
      digitalWrite(dir1,LOW);
      digitalWrite(dir2,LOW);
      move(m);

      //Bottom Movement
      digitalWrite(dir1,HIGH);
      digitalWrite(dir2,LOW);
      move(m);

      ld();
      delay(1000);
      norm();

      //Top Movement
      digitalWrite(dir1,LOW);
      digitalWrite(dir2,HIGH);
      move(m);

      //Right Movement
      digitalWrite(dir1,HIGH);
      digitalWrite(dir2,HIGH);
      move(m);break;
    }
    case 7:
    {
      //plastic
      //Top Movement
      digitalWrite(dir1,HIGH);
      digitalWrite(dir2,LOW);
      move(m);

      td();
      delay(1000);
      norm();

      //Bottom Movement
      digitalWrite(dir1,LOW);
      digitalWrite(dir2,HIGH);
      move(m);
      break;
    }
    case 8:
    {
      //textile
      //Right Movement
      digitalWrite(dir1,HIGH);
      digitalWrite(dir2,HIGH);
      move(m);

      //Bottom Movement
      digitalWrite(dir1,HIGH);
      digitalWrite(dir2,LOW);
      move(m);

      rd();
      delay(1000);
      norm();
      
      //Top Movement
      digitalWrite(dir1,LOW);
      digitalWrite(dir2,HIGH);
      move(m);

      //Left
      digitalWrite(dir1,LOW);
      digitalWrite(dir2,LOW);
      move(m);break;
    }
    case 9:
    {
      //wood
      //Right Movement
      digitalWrite(dir1,HIGH);
      digitalWrite(dir2,HIGH);
      move(m);

      //Bottom Movement
      digitalWrite(dir1,HIGH);
      digitalWrite(dir2,LOW);
      move(m);

      rd();
      delay(1000);
      norm();


      
      //Top Movement
      digitalWrite(dir1,LOW);
      digitalWrite(dir2,HIGH);
      move(m);

      //Left
      digitalWrite(dir1,LOW);
      digitalWrite(dir2,LOW);
      move(m);
      break;
    }
  }
  }

}

void move(int l)
{
  for(int x = 0; x < l; x++) {
        digitalWrite(step1,HIGH);
        digitalWrite(step2,LOW); 
        delayMicroseconds(1000);    // by changing this time delay between the steps we can change the rotation speed
        digitalWrite(step1,LOW);
        digitalWrite(step2,HIGH); 
        delayMicroseconds(1000); 
      }
      //delay(300);
}

void ld()
{
  dir.write(180);
  delay(1000);
  myservo1.write(0);
  myservo2.write(180);
}
void norm()
{
  myservo1.write(90);
  myservo2.write(90);
  delay(1000);
  dir.write(90);
}
void rd()
{
  dir.write(180);
  delay(1000);
  myservo1.write(180);
  myservo2.write(0);
}
void td()
{
  dir.write(90);
  delay(1000);
  myservo1.write(30);
  myservo2.write(150);
}