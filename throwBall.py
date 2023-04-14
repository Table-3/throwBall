import meArm
import time

arm = meArm.meArm()
arm.begin(block=0, address=0x70) # block address of motor controller

#wait to start
time.sleep(2)

arm.gotoPoint(-80.0, 140.0, 105.0)#bottom sitting postition
#later we can comment this out as you can adjust the start position in your meArm code
time.sleep(3)

arm.gotoPoint(30, 190, -75) # goes backwards left or right (slow)

time.sleep(1) #ADJUST depending on speed of me arm

arm.goDirectlyTo(-65.0, 200.0, -70.0) #go foreward (fast) toward goal

time.sleep(3)

#if needed add another gotoPoint if your meArm is hitting the net


