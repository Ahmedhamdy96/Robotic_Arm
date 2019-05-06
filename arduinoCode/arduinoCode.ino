#define GRIPPER 11 
#define TOP 10 
#define BOTTOM 6 
#define BASE 5 

#include <Servo.h> 

Servo gripper ; 
Servo top ; 
Servo bottom ; 
Servo base ; 

unsigned char motorToMove = 0 ; 
unsigned char angle = 0 ; 

void setup() 
{
  Serial.begin(9600) ; 
  gripper.attach(GRIPPER) ;
  top.attach(TOP) ; 
  bottom.attach(BOTTOM) ; 
  base.attach(BASE) ;    
}

void loop()
{
  String command = Serial.readString() ; 
  control( command );     
}

void control(String controlCommand )
{
    unsigned char index = controlCommand.indexOf('/') ; 
    motorToMove = controlCommand.substring( 0 , index ).toInt() ; 
    angle = controlCommand.substring(index + 1 ).toInt() ;

    switch( motorToMove ) 
    {
      case 0 : 
        break ; 
      case 4 :
        gripper.write( angle ) ; 
        break ;  
      case 3 : 
        top.write( angle ) ; 
        break ; 
      case 2 : 
        bottom.write( angle ) ; 
        break ; 
      case 1 : 
        base.write( angle ) ; 
        break ; 
    }
}
