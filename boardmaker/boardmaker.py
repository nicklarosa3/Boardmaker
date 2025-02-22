class makeBoard(object):
	def __init__(self,rows,columns):
		hold = []
		for i in range(rows):
			hold.append([""]*columns)
		self.board = hold
		self.rows = rows
		self.columns = columns
		self.maxentry = 0
		self.append = 2
		self.methods = { "getList": "Returns the 2D List.",
					"importList": "Import a custom 2D list instead of using constructer.",
					"printBoard": "Prints out a formatted board containing entries.",
					"changeIndex": "Edit the value of specific location: .changeIndex([x,y], change)",
					"printIndex": "Prints the value of specific location: .printIndex([x,y])",
					"getIndex": "Returns the value of specific location: .getIndex([x,y])",
					"moveIndex": "Move the value of one index to another position: .moveIndex([x,y],[x,y])",
					"switchIndices": "Switch the values of two indices: .switchIndices([x,y],[x,y])",
					"removeIndex": "Removes the given index",
					"clearBoard": "Clears the entire board",
					"helpAll": "List all methods contained in makeBoard class.",
					"helpMethod": "Print function of specific method within makeBoard class: .helpMethod(method)"}
					
	def getList(self):
		return(self.board)
	def importList(self,new_list):
		hold = list()
		if isinstance(new_list, list):
			pass
		else:
			print("Argument must be 2 dimensional list")
			return
		for row in new_list:
			if isinstance(row,list):
				pass
			else:
				print("Argument must be a 2 dimensional list")
				return
		for row in new_list:
			if len(row) > self.columns:
				print("New list cannot require more space than is available.\nRows: {0}, Columns: {1}".format(self.rows,self.columns))
				return
		if len(new_list) > self.rows:
			print("New list cannot require more space than is available.\nRows: {0}, Columns: {1}".format(self.rows,self.columns))
			return
		
		self.clearBoard()
		
		self.board = new_list
		self.rows = len(new_list)
		self.columns = len(new_list[0])
		self.append = 2
	def printBoard(self):
		columns = self.columns
		rows = self.rows
		hold = self.board
		
		maxlength = 0
		for row in range(0,len(hold)):
			for space in range(0, len(hold[row])):
				current_length = len(str(hold[row][space]))
				if current_length > maxlength:
					maxlength = current_length
				else:
					continue
					
		maxlength = maxlength + 4
		
		def linetop():
			for space in range(columns-1):
				print(" "+"_"*maxlength+" ",end=""),
			print(" "+"_"*maxlength)
			for space in range(columns-1):
				print("|" + " "*maxlength + "|",end=""),
			print("|" + " "*maxlength + "|")
			
		def linebottom():
			for space in range(columns-1):
				print("|" + "_"*maxlength + "|",end=""),
			print("|" + "_"*maxlength + "|")
				
		print("")
		linetop()
		
		for row in range(0,len(hold)):
			for space in range(0,len(hold[row])):
				if (space+1) % columns == 0:
					append = maxlength - len(str(hold[row][space]))
					if append % 2 == 0:
						append1 = int(append/2)
						append2 = int(append/2)
					else:
						convert = append+1
						append1 = int((convert/2)-1)
						append2 = int(convert/2)
					l = (("|") + (" "*append1) + ("{}".format(hold[row][space])) + (" "*append2) + ("|"))
					print(l)
					if (row+1) == rows:
						linebottom()
						continue
					else:
						linebottom()
						linetop()
				else:
					append = maxlength - len(str(hold[row][space]))
					if append % 2 == 0:
						append1 = int(append/2)
						append2 = int(append/2)
					else:
						convert = append+1
						append1 = int((convert/2)-1)
						append2 = int(convert/2)
					l = (("|") + (" "*append1) + ("{}".format(hold[row][space])) + (" "*append2) + ("|"))
					print(l,end="")
		print("")
		
	def printIndex(self, xylist):
		hold = self.board
		x = xylist[0]
		y = xylist[1]
		re = hold[x][y]
		print(re)
	def getIndex(self, xylist):
		hold = self.board
		x = xylist[0]
		y = xylist[1]
		re = hold[x][y]
		return(re)
	def changeIndex(self,xylist,change):
		hold = self.board
		x = xylist[0]
		y = xylist[1]
		hold[x][y] = change
		if len(change) > self.maxentry:
			place = len(change) - self.maxentry
			self.maxentry = len(change)
			self.maxlength = 4+self.maxentry
			for row in range(0,len(hold)):
				for col in range(0,len(hold[row])):
					if x == row and y == col:
						continue
					else:
						self.append += place
		self.board = hold
	def removeIndex(self, xylist):
		hold = self.board
		x = xylist[0]
		y = xylist[1]
		hold[x][y] = ''
		self.board = hold
	def switchIndices(self, xylist_one, xylist_two):
		hold = self.board
		x_one = xylist_one[0]
		y_one = xylist_one[1]
		hold_one = hold[x_one][y_one]
		x_two = xylist_two[0]
		y_two = xylist_two[1]
		hold_two = hold[x_two][y_two]
		hold[x_one][y_one] = hold_two
		hold[x_two][y_two] = hold_one
		self.board = hold
	def moveIndex(self, xylist, xylist_target):
		hold = self.board
		x_one = xylist[0]
		y_one = xylist[1]
		hold_one = hold[x_one][y_one]
		x_target = xylist_target[0]
		y_target = xylist_target[1]
		hold[x_target][y_target] = hold_one
		hold[x_one][y_one] =  ""
		self.board = hold
	def clearBoard(self):
		hold = self.board
		for row in range(0,len(hold)):
			for space in range(0,len(hold[row])):
				hold[row][space] = ""
		self.board = hold
	def addRow(self, amt):
		hold = self.board
		try:
			amt = int(amt)
		except ValueError:
			print("Argument must be integer")
			return
		for i in range(amt):
			self.rows = self.rows + 1
			hold.append([""]*self.columns)
		self.board = hold
	def removeRow(self, amt):
		hold = self.board
		try:
			amt = int(amt)
		except ValueError:
			print("Argument must be integer")
			return
		for i in range(amt):
			hold.pop()
			self.rows = self.rows - 1
		self.board = hold
	def addColumn(self, amt):
		hold = self.board
		try:
			amt = int(amt)
		except ValueError:
			print("Argument must be integer")
			return
		for i in range(amt):
			self.columns = self.columns + 1
			for row in range(0,len(hold)):
				place = hold[row]
				place.append("")
				hold[row] = place
		self.board = hold
	def removeColumn(self, amt):
		hold = self.board
		try:
			amt = int(amt)
		except ValueError:
			print("Argument must be integer")
			return
		for i in range(amt):
			self.columns = self.columns - 1
			for row in range(0, len(hold)):
				place = hold[row]
				place.pop()
				hold[row] = place
		self.board = hold
	def helpAll(self):
		methods = self.methods
		print("")
		for method in methods:
			print("{}: {}".format(method,methods[method]))
			print("")
	def helpMethod(self, specific):
		methods = self.methods
		print("")
		for method in methods:
			if method == specific:
				print("{}: {}".format(method,methods[method]))
				break
			else:
				continue
		else:
			print("Method not found")
		print("")
		

def toBoard(new_list):
	if isinstance(new_list, list):
		pass
	else:
		print("Argument must be 2 dimensional list")
		return
	for row in new_list:
		if isinstance(row,list):
			continue
		else:
			print("Argument must be a 2 dimensional list")
			return
	check = len(new_list[0])
	for row in new_list:
		if len(row) != check:
			print("Argument must not be jagged")
			return
		else:
			continue
	rows = len(new_list)
	columns = len(new_list[0])
	new_board = makeBoard(rows,columns)
	new_board.importList(new_list)
	return new_board
		
		
		
		
		
		
