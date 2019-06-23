# Request module and json module

import requests
import json

def get_course_data(api):		#First api for get course data
	response=requests.get(api)	#get the data from api
	course_data=response.json()	#convert the data in json
	course_json_file=open("courses_data.json","w")	# new file made and this file in data write
	string_data=json.dumps(course_data)				# convert the string_data use of dumps
	course_json_file.write(string_data)				# write the string_data
url="http://saral.navgurukul.org/api/courses"
get_course_data(url)								#Api calling

# for all course list  print
course_list = []
def get_courses():
	courseDataJsonFile=open("courses_data.json","r")
	data1=courseDataJsonFile.read()
	dict_data=json.loads(data1)
	inside_data=dict_data["availableCourses"]
	count=0
	for index in inside_data:
	    course_name = index["name"]
	    course_id = index["id"]
	    course_list.append(course_id)
	    print str(count)+" ",course_name,course_id
	    count=count+1
get_courses()

#	here is print of all course list we can use in one course id
user_input=input("enter your choice to anyone id:-")
user_id=course_list[user_input]

def exersice_fun(api2): 	# again api use for excersice
	exersice_data=requests.get(api2)
	excersiceData=exersice_data.json() 
	json_file1=open("exercises_id.json","w")
	string_data=json.dumps(excersiceData)
	json_file1.write(string_data)
	json_file1.close()
url2=url+"/"+str(user_id) + "/" +"exercises"
exersice_fun(url2) 		#api calling

#childExcersice
def getChildExersice():
	course_json_file=open("exercises_id.json","r")
	data1=course_json_file.read()
	dict_data1=json.loads(data1)
	inside_data=dict_data1["data"]
	return inside_data
inside_data=getChildExersice()

#this function parantchildexcersice and childexcers
def childExerciseData():
	child_list=[]
	count=0
	if inside_data!=[]:
		if get_courses!=[]:
			for index in inside_data:
				child_list.append(index["id"])
				print count,"parentChldExercise:",index["name"],index["id"]
				inside_data1= index["childExercises"]
				count1=0
				for index1 in inside_data1:
					print "\t""\t",count1, "childExersice:",index1["name"],index1["id"]
					count1=count1+1
				count=count+1
			return child_list
child_list=childExerciseData()

#this functon use in childExcersice and slug
slug_list=[]
def child_exersice(user_childExersice):
	childExercises=0
	for index in inside_data: 
		count=0
		childExercises=child_list[user_childExersice]
		if childExercises==index["id"]:
			slug_list.append(index["slug"])
			print str(count),index["name"]
			child_ex = index["childExercises"]
			count1=count+1
			for index1 in child_ex:
				slug_list.append(index1["slug"])
			 	print str(count1),index1["name"],index1["id"]
			 	count1 = count1+1
		count=count+1
	return slug_list

slug_input=input("enter the childExercise which slug you want:")
slug_list=child_exersice(slug_input)

# here is all print slug list which exsercise of slug you want so you can choose here
user_slug=input("enter your slug_index")
get_slug=slug_list[user_slug]

def child_fun(api3):	#again api  for content 
	exersice_data=requests.get(api3)
	exersiceData=exersice_data.json()
	json_file1=open("slug_id.json","w")
	string_data=json.dumps(exersiceData)
	json_file1.write(string_data)
	json_file1.close()
	if get_slug!=None:
		if slug_list[user_slug] != []:
			course_json_file=open("slug_id.json","r")
			data1=course_json_file.read()
			dict_data1=json.loads(data1)
			inside_data=dict_data1["content"]
			print inside_data
url3="http://saral.navgurukul.org/api/courses"+"/"+str(user_id)+"/"+"exercise"+"/"+"getBySlug?slug="+str(get_slug)
child_fun(url3)		#api calling		

# this loop for privios, next and up 
while True:
	user_choice=raw_input("enter the what u want previous,next,up,exit we have 3 option we can use enter your choice /p,/n,/up,:")
	user=user_slug+1
	if user_choice=="n" :	#next Part
		num=1
		user=user_slug+num
		if user<len(slug_list): 
			get_slug=slug_list[user]		
			url3=url+"/"+str(user_id)+"/"+"exercise"+"/"+"getBySlug?slug="+str(get_slug)
			child_fun(url3)
			print (url3)
		else:
			print " "
			print " aage apke pas page nahi hai"
			print "app up ka use kr sakte ho"
			print " "
			continue
		child_fun(url3)
		user_slug=user_slug+1
	elif user_choice=="p": 		#privious Part
		user2=user_slug-1
		if user_slug==0:
			print "no there is no page"
			break
		get_slug=slug_list[user2]		
		url3=url+"/"+str(user_id)+"/"+"exercise"+"/"+"getBySlug?slug="+str(get_slug)
		child_fun(url3)
		print url3
		user_slug=user_slug-1
	elif user_choice == "up":	#up Part
		up=1
		get_courses()
		user_input=input("enter your choice to anyone id:-")
		user_id=course_list[user_input]
		child_list=childExerciseData()
		print child_list
		slug_input=input("enter the childExercise which slug you want:")
		slug_list=child_exersice(slug_input)
		print slug_list
		get_slug=slug_list[user_slug]		
		print get_slug
		url3=url+"/"+str(user_id)+"/"+"exercise"+"/"+"getBySlug?slug="+str(get_slug)
		child_fun(url3)
		print url3
		up=up+1
	else:
		print " "
		print "THIS IS invalid input print again valid input"
		continue




# 