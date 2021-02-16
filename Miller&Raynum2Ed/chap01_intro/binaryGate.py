from .logicGate import LogicGate

class BinaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pinA = None
        self.pinB = None

    # Commented out for future examination (method getFrom() seems to have no home here.
	# def getPinA(self):
    # 	if self.pinA == None:
	#         return int(input("Enter Pin A input for gete " + self.getLabel()+"-->"))
	# 	else:
	# 		answer = self.pinA.getFrom()
	#
	# 		return self.pinA.getFrom().getOutput()

    def getPinB(self):
        return int(input("Enter Pin B input for gate " + self.getLabel()+"-->"))

    def setNextPin(self,source):
    	if self.pinA == None:
    		self.pinA = source
    	else:
    		if self.pinB == None:
    			self.pinB = source
    		else:
    			raise RuntimeError("Error: NO EMPTY PINS")
