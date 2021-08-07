#!/usr/bin/env python3

import sys
from collections import Counter

class Person(object):

	def __init__(self,name,grade):
		self.name=name
		self.grade=grade

	def get_details(self):

		return self.name


class Student(Person):


	def __init__(self, name, grade, branch, year):
		Person.__init__(self, name, grade)
		self.branch = branch
		self.year = year

	def get_details(self):
		return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)
	@property
	def get_grade(self):
		'''
		return student's grade in F/P mode
		'''
		Pass=0
		Fail=0
		for i in self.grade:
			if i=='D':
				Fail+=1
			else:
				Pass+=1
		return "Pass:{}, Fail:{}".format(Pass,Fail)
		
			
			
		


class Teacher(Person):

	def __init__(self, name, grade, papers):
		Person.__init__(self, name, grade)
		self.papers = papers

	def get_details(self):
		return "{} teaches {}".format(self.name, ','.join(self.papers))
	@property
	def get_grade(self):
		'''
		counter class count students' grades in A,B,C,D group
		'''
		c = Counter(self.grade)
		c1=c.most_common()
		
		return c1



if sys.argv[1]=='teacher':
		l=Teacher('',sys.argv[2],'').get_grade
		for i in range(len(l)):
			print("{}:{}".format(l[i][0],l[i][1]),end='')
			if i!=len(l)-1:
				print(", ",end='')
elif sys.argv[1]=='student':
		str=Student('',sys.argv[2],'','').get_grade
		print(str)

	




