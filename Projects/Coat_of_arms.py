###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################
stage.set_background("winter")


q1 = codesters.Square(100, 100, 200, 'purple')
q2 = codesters.Square(-100, 100, 200, 'blue violet')
q3 = codesters.Square(-100, -100, 200, 'dark orchid')
q4 = codesters.Square(100, -100, 200, 'blue')

s1 = codesters.Sprite("soccerball", 100, 100)
s1.set_size(2)
s2 = codesters.Sprite("cutedogg", -100, -100)
s2.set_size(0.4)
s3 = codesters.Sprite("Bed", 100, -100)
s3.set_size(0.3)
s4 = codesters.Sprite("family", -100, 100)
s4.set_size(0.3)
message1 = codesters.Text("Cami Bailey!")
message2 = codesters.Text("I put a dog my family a soccer ball and a bed",0,-220,"DarkSlateBlue")
