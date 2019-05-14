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
  gripper.write(50);

  top.attach(TOP) ;
  top.write(80);

  bottom.attach(BOTTOM) ;
  bottom.write(90);

  base.attach(BASE) ;
  base.write(90);

  Serial.setTimeout(50);
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
      angle=angle<5?5:angle;
      top.write(angle) ; 
      break  ; 
       
    case 2 :
      angle=angle<5?5:angle;
      bottom.write(angle) ; 
      break ; 
      
    case 1 :
      angle=angle<5?5:angle;
      base.write( angle ) ;
      break ;
    }
  }

void loop()
{
  String command = Serial.readString() ;
  control( command );
}
