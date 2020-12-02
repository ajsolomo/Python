import time
import MenorahLib

## Ideally all of this would be in MenorahLib.py
ALLDAYSOFCHANUKAH=8
AllCandles = []

class Branch:
    whichBranch = 0 # 0 is the shammos
    isBurning = False
    isCandle = False

    def __init__(self, branch):
        print("Creating new Branch object")
        self.whichBranch=branch

    def setupCandle(self, toggle = True):
        print("setupCandle for ", self.whichBranch, " to ", toggle)
        isCandle = toggle
        
    def lightCandle(self, toggle = True):
        print("lightCandle for ", self.whichBranch, " to ", toggle)
        isBurning = toggle

def turnOffMenorah():
    print("Turning off the menorah")
    #for candle in range(0, ALLDAYSOFCHANUKAH):
    #    print("Turn off candle #", candle)
    #    toggleCandle(candle, False)
    #    time.sleep(1.5)
    
    for candle in AllCandles:
        candle.lightCandle(False)
    
    return



def toggleCandle(candleIndex, onOrOffBoolean):
    print("Set candle #", candleIndex, " to ", onOrOffBoolean)
    return
###

print ("Starting menorah program")

#Setup several global variables
print("setting global variables")
TodaysDayOfChanukah=8
AllCandles.append( Branch(0) )
for i in range(1,TodaysDayOfChanukah):
    AllCandles.append( Branch(i) )


print("Put in the candles...")
# For loop to setup the candles
print("First make sure the menorah is off")
turnOffMenorah()

