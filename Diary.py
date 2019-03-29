from Student import Student


class Class:
	def __init__(self, nameOfClass):
		self.nameOfClass = nameOfClass


class Diary:
	def __init__(self, *classes):
		#self.classes = {i.nameOfClass,["class":i] for i in classes}

	"""def addStudentsToClass(self, nameOfClass, *students):
		self.classes[nameOfClass].append([i] for i in students)

	def addStudentToClass(self, nameOfClass, student):
		self.classes[nameOfClass].append([student])

	def addScoreToStudent(self, nameOfClass, student):


	"""