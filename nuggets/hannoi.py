stepCount=0
def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
	global stepCount 
	stepCount = stepCount + 1
	print("moving disk from",fp,"to",tp)

moveTower(15,"A","B","C")
print(' total steps taken is: ', stepCount)