#-*- coding: utf-8 -*-

import copy
import collections

class cAction:
	def __init__(self,Name):
		self.Name = Name
		self.PosCondiction 		= ()
		self.NegCondiction 		= ()
		self.PosEffect			= ()
		self.NegEffect			= ()
		self.Available			= True
		self.ActionCooltime 	= 0
		self.curCooltime		= 0
		self.actionTime 		= 0

	def addPosCondition(self, _PosCondition):
		if type(_PosCondition) == tuple :
			self.PosCondiction 	= _PosCondition
		elif type(_PosCondition) == list :
			self.PosCondiction 	= tuple(_PosCondition)
		else:
			print "data error"

	def addNegCondition(self, _NegCondition):
		if type(_NegCondition) == tuple :
			self.NegCondiction 	= _NegCondition
		elif type(_NegCondition) == list :
			self.NegCondiction 	= tuple(_NegCondition)
		else:
			print "data error"

	def addPosEffect(self, _Effect):
		if type(_Effect) == tuple :
			self.PosEffect 	= _Effect
		elif type(_Effect) == list :
			self.PosEffect 	= tuple(_Effect)
		else:
			print "data error"

	def addNegEffect(self, _Effect):
		if type(_Effect) == tuple :
			self.NegEffect 	= _Effect
		elif type(_Effect) == list :
			self.NegEffect 	= tuple(_Effect)
		else:
			print "data error"

	def setActionCooltime(self, _ActionCooltime):
		self.ActionCooltime = _ActionCooltime 

	def setUsed(self):
		self.Available = False
		self.curCooltime = self.ActionCooltime

	def runCooltime(self):
		self.curCooltime -= 1
		if( self.curCooltime <= 0):
			self.Available = True
			self.curCooltime = 0

	def reduceCooltime(self, _time):
		self.curCooltime -= _time
		if( self.curCooltime <= 0):
			self.Available = True
			self.curCooltime = 0

	def setActionTime(self, _time):
		self.actionTime = _time

	def getPosCondition(self):
		return self.PosCondiction

	def getNegCondition(self):
		return self.NegCondiction

	def getPosEffect(self):
		return self.PosEffect

	def getNegEffect(self):
		return self.NegEffect

	def IsAvailable(self):
		return self.Available

	def getName(self):
		return self.Name

	def getActionTime(self):
		return self.actionTime

class cState:
	def __init__(self, distance, position, abnormal, stance):
		self.distance = distance
		self.stance = stance
		self.position = position
		self.abnormal = abnormal
		self.property = []

	def removeProperty(self, _rmProperty):
		try:
			self.property.remove( _rmProperty)
		except ValueError:
			pass

	def addProperty(self, _addProperty):
		self.property.append(_addProperty)

	def printProperty(self):
		print "-----------"
		print "Distance : " 	+ str(self.distance)
		print "Stance : " 		+ str(self.stance)
		print "Position : " 	+ str(self.position)
		print "Abnormal : " 	+ str(self.abnormal)
		print "Property : " 	+ str(self.property)
		print "-----------"

	def applyPosEffect(self, _Effect):
		if _Effect == 'backPosition':
			self.position = 'backPosition'
		elif  _Effect == 'frontPostition':
			self.position = 'frontPostition'
		elif  _Effect == 'longDistance':
			self.distance = 90
		elif  _Effect == 'shortDistance':
			self.distance = 30
		elif _Effect == 'normal':
			self.abnormal = 'normal'
		elif _Effect == 'stun':
			self.abnormal = 'stun'
		elif _Effect == 'kneel':
			self.abnormal = 'kneel'
		elif _Effect == 'down':
			self.abnormal = 'down'
		elif _Effect == 'air1':
			self.abnormal = 'air1'
		elif _Effect == 'air2':
			self.abnormal = 'air2'
		elif  _Effect == 'hide':
			self.stance = 'hide'
		elif  _Effect == 'blade':
			self.stance = 'blade'
		else:
			self.addProperty(_Effect)

	def applyNegEffect(self, _Effect):
		self.removeProperty(_Effect)

	def applyEffects(self, _action):
		for iEffect in _action.getPosEffect():
			self.applyPosEffect(iEffect)
		for iEffect in _action.getNegEffect():
			self.applyNegEffect(iEffect)

	def IsMatchedCondition(self, _Condition):		
		if _Condition == 'backPosition':
			if self.position == 'backPosition':
				return True
		elif  _Condition == 'frontPostition':
			if self.position == 'frontPostition':
				return True
		elif  _Condition == 'longDistance':
			if self.distance >=85:
				return True
		elif  _Condition == 'shortDistance':
			if self.distance < 37:
				return True
		elif  _Condition == 'normal':
			if self.abnormal == 'normal':
				return True
		elif  _Condition == 'stun':
			if self.abnormal == 'stun':
				return True
		elif  _Condition == 'kneel':
			if self.abnormal == 'kneel':
				return True
		elif  _Condition == 'down':
			if self.abnormal == 'down':
				return True
		elif  _Condition == 'air1':
			if self.abnormal == 'air1':
				return True
		elif  _Condition == 'air2':
			if self.abnormal == 'air2':
				return True
		elif  _Condition == 'hide':
			if self.stance == 'hide':
				return True
		elif  _Condition == 'blade':
			if self.stance == 'blade':
				return True
		else:
			for iProperty in self.property:
				if _Condition == iProperty:
					return True
		return False

	def IsMatchedConditions(self, _conditions):
		if type(_conditions) == tuple:
			for iCondition in _conditions:
				if self.IsMatchedCondition(iCondition) == False:
					return False
			return True
		else:
			print "type error"
			return False



arrText = [
['leaf1',		140,		5,		['longDistance'],						['backPosition'],				[]],
['jamib1',		70,			3,		['longDistance','backPosition'],		['hide','shortDistance'],		[]],
['chuckchu',	50,			20,		['hide','shortDistance'],				['blade','stun'],				[]],
['hot_Wind',	150,		5,		['stun','shortDistance'],				['air1'],						[]],
['amyun',		100,		8,		['air1','shortDistance'],				['air2'],						[]],
['bomb',		180,		1,		['air2','shortDistance'],				['air2','bomb_flag'],			[]],
['spider',		120,		40,		['air2','shortDistance'],				['down','longDistance'],		[]],
['fire',		100,		1,		['down','bomb_flag'],					['down'],						['bomb_flag']]
]

class cEnvironment:
	def __init__(self):
		self.State 		= cState(90,'frontPostition','normal','blade')
		self.Actions	= []
		self.applyActionContext()
		self.Tick 		= 0

	def applyActionContext(self):
		for iArrText in arrText:
			self.Actions.append(cAction(iArrText[0]))
			self.Actions[-1].setActionCooltime(iArrText[1])
			self.Actions[-1].setActionTime(iArrText[2])
			self.Actions[-1].addPosCondition(iArrText[3])
			self.Actions[-1].addPosEffect(iArrText[4])
			self.Actions[-1].addNegEffect(iArrText[5])

	def getActionByName(self, _Name):
		for iAction in self.Actions:
			if iAction.getName() == _Name:
				return iAction
		else:
			return False

	def IsPossibleActionByName(self, _ActionName):
		if self.getActionByName(_ActionName) is not False:
			return self.State.IsMatchedConditions(self.getActionByName(_ActionName).getPosCondition())
		else:
			return False

	def getUsedAction(self):
		temp = []
		for iAction in self.Actions:
			if iAction.IsAvailable() == False:
				temp.append(iAction.getName())
		return temp

	def getPossibleAction(self):
		temp = []
		for iAction in self.Actions:
			if iAction.IsAvailable() == True:
				if self.State.IsMatchedConditions(iAction.getPosCondition()) == True:
					temp.append(iAction.getName())
		return temp

	def applyAction(self, _ActionName, bUsed = False, bApplyActionTime = False, bWriteLog == False):
		action = self.getActionByName(_ActionName)
		if bApplyActionTime is True:
			for iAction in self.getUsedAction():
				self.getActionByName(iAction).reduceCooltime(action.getActionTime())
		if bUsed is True:
			action.setUsed()		
		self.State.applyEffects(action)

	def printState(self):
		self.State.printProperty()


class Queue:
	def __init__(self):
		self.elements = collections.deque()

	def empty(self):
		return len(self.elements) == 0

	def put( self, x):
		self.elements.append(x)

	def get(self):
		return self.elements.popleft()



frontier = Queue()
frontier.put(cEnvironment())

def run(bPrint = False):
	if frontier.empty() == False:
		current = frontier.get()
		possibleAction = current.getPossibleAction()
		print possibleAction	
		for iAction in possibleAction:
			next = copy.deepcopy(current)		
			next.applyAction(iAction,bUsed = True, bApplyActionTime = True)
			if bPrint == True:
				next.printState()
			frontier.put(next)

run()
run()
run()
run()
run()
run()
run()
run()
run()
run()








'''
step1 = []
for iAction in possibleAction:
	step1.append(copy.deepcopy(initial))
	step1[-1].applyAction(iAction)

print step1
'''

















		
