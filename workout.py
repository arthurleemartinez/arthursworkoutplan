#THIS IS A SCHEDULE-BASED PROGRAM 
#This program is a simple tool that can be used to create an optimal workout and sleep schedule for up to one month!
#It will also give you a detailed ratings portfolio and rate your workout on a scale of 1-100
#Ratings data was generated using calculations derived from data at https://www.bodybuilding.com/exercises/finder/?muscleid=1
#Users will choose how many days of planning they need, as well as select from a choice of parameters regarding which muscles they want to train.
#Follow-up research on a group of elite Norwegian powerlifters also showed better results with more frequent training. Subjects taking part in the study – 13 men and 3 women – were assigned to one of two groups. They all followed the exact same workout routine, but with one important difference. Group one trained three times each week. Group two did the same volume of work, but over six weekly sessions. Study subjects training three times a week simply performed twice as many sets in each workout 
#Even though the total weekly training volume was the same, it was the guys training each muscle group three times a week who saw the greatest gains in both size and strength.
#The 3-day group performed one set of each exercise three times a week. The 1-day group performed three sets of each exercise once per week.

#Import Python Modules:
import math
from random import *
import time
import datetime
import weekday

#Initialize program and generic user interface
print "Current date and time: " , datetime.datetime.now()
print "Current weekday: "datetime.datetime.today().weekday()
user_weight = raw_input("Please Enter Your Weight")

#The 3-day group performed one set of each exercise three times a week. 
sets = 1

def choose_exercises(muscle_areas, day((week))
	if  

def choose_muscleareas(muscle_areas, day):
     for in range(1, 31, [1])
     rca1 = random.choice(muscle_areas)
     rca2 = random.choice(muscle_areas)
     if rca2 == rc1:
          rca2 = random.choice(muscle_areas) 
def Day_plan(muscle_areas, choose_exercises):
     for in range(1, 31, [1])
     rca1 = random.choice(muscle_areas)
     rca2 = random.choice(muscle_areas)
     if rca2 == rc1:
          rca2 = random.choice(muscle_areas) 
	
def muscle_groups(day_of_month, choose_muscle_areas):
	day_of_month = 0
	while day_of_month +=1:
	     day_of_month =<30       	
#There are 7 days in a week, and the index starts at 0 (Monday)	
week = [“Monday”, “Tuesday”, “Wednesday”, “Thursday”, “Friday”, “Saturday”, “Sunday”]
#Function that turns the value returned by weekday module into a variable
def day(week):
	day =  datetime.datetime.today().weekday()
#This is a list of all the popularly trained muscle groups
muscle_areas = [“Chest”, “Biceps”, “Abdominals”, “Lats”, “Triceps”, “Forearms”, “Shoulders”, “Middle Back”, “Calves”,  “Hamstrings”,  “Quadriceps”,  “Traps”,  “Lower Back”,  “Glutes”, “Abductors”, “Adductors”]
#Exercise dictionary that referrences midly obfuscated ratings provided by bodybuilding.com
Chest_exercises: {
	“Dumbbell Bench Press” : 9.200341
	”Pushups” : 9.205362346
	”Dumbbell Flyes” : 9.1043562
	“Incline Dumbbell Bench Press” : 9.100678
	“Medium-Grip Barbell Bench Press” : 9.090678
	“Chest Dips” : 9.000567
}

Biceps_exercises: {
	“Incline Hammer Curls” : 9.5006794
	”Wide-Grip Standing Barbell Curl” : 9.30003245
	”Spider Curl” : 9.200004576
	”EZBar Curl” : 9.10004576
	”Hammer Curls” : 9.1000234
	”Zottman Curl” : 9.1000045672
	”Concentration Curls” : 9.0000036421
	”Barbell Curl” : 9.00074721
	“Dumbbell Bicep Curl” : 8.900034612
}

Abdominals_exercises: {
	“One-Arm Medicine Ball Slam” : 9.12341
	”Landmine180s” : 9.50000235
	”Plank” : 9.3000004578
	”Elbow to Knee” : 9.100000568
	”Plate-Twist” : 9.000003467
	”Bottom’s Up” : 9.300000346
}

Lats_exercises: {
	“Weighted Pull Ups” : 9.50000436, 
	”Pullups” : 9.2000235
	”Chin-Up” : 9.10000012
	”Wide-Grip Pull-Up” : 8.90000395
	”Close-Grip Front Lat Pulldown” : 8.80000001
	”Shotgun Row” : 8.8000001
}

Triceps_exercises: {
	“Dips - Triceps Version” : 9.40000012
	”Decline EZ Bar Triceps Extension” : 9.300012
	”Dumbbell Floor Press” : 9.300003461
	”Close-Grip Barbell Bench Press” : 9.10041325
	”Triceps Pushdown - V-Bar Attachment” : 9.100311
	”Weighted Bench Dip” : 9.100003
	”Push-Ups - Close Triceps Position” : 9.00000346
	”Close-Grip Barbell Bench Press” : 9.100046
}

Forearms_exercises: {
	“Seated Palm-Up Barbell Wrist Curl” : 8.700046
	”Seated One-Arm Dumbbell Palms-Up Wrist Curl : 9.00034
	”Wrist Roller” : 9.100325
	”Palms-Up Barbell Wrist Curl Over A Bench” : 9.40235
	”Wrist RotationswithStraight Bar” : 9.500162
}

Shoulders_exercises: {
	“Single-Arm Linear Jammer” : 9.50007
	”Side Laterals to Front Raise” : 9.50005
	”Standing Palm-In One-Arm Dumbbell Press” : 9.40003
	”Power Partials” : 9.10005
	”Seated Dumbbell Press” : 9.10002
	”Side Laterals to Front Raise” : 9.5060012
	”Standing Palm-In One-Arm Dumbbell Press” : 9.40001
	”One-Arm Side Laterals” : 9.10105
}

Middle_Back_exercises: {
	“T-Bar RowwithHandle" : 9.50060024
	”Reverse Grip Bent-Over Rows” : 9.200054221
	”One-Arm Long Bar Row” : 9.000861
	”One-Arm Dumbbell Row” : 9.0001
	”Seated Cable Rows” : 8.800761
}

Calves_exercises: {
	“Smith Machine Calf Raise” : 9.20071
	”Standing Calf Raises” : 9.008
	”Standing Dumbbell Calf Raise” : 8.8088
	”Seated Calf Raise” : 8.70777
	”Rocking Standing Calf Raise” : 8.707777
	”Standing Barbell Calf Raise” : 8.20222
}

Hamstrings_exercises: {
	“Lying Leg Curls” : 8.9004 
	”Barbell Deadlift” : 9.40004
	”Leg Curl” : 8.5011
	”Romanian Deadlift With Dumbbells” : 9.41
}

Quadriceps_exercises: {
	“Barbell Full Squat” : 9.400014
	”Leg Press” : 9.600235
	”Rope Jumping” : 9.200235
	”Step Mill” : 9.100145
}

Traps_exercises: {
	“Smith Machine Shrug” : 9.201255
	”Dumbbell Shrug”: 8.70014
	”Barbell Shrug”: 8.4
	”Standing Dumbbell Upright Row”: 8.70071
}

Lower_Back_exercises: {
	“Axle Deadlift” : 9.10012
	”Deficit Deadlift” : 9.4001245
	”Hyperextensions (Back Extensions)” : 9.1001245
}

Glutes_exercises: {
	“Butt Lift (Bridge)” : 8.80001	   
	”One-Legged Cable Kickback” : 9.000111
	”Kneeling Squat” : 8.6
}

Adductors_exercises: {
	“Thigh Adductor” : 9.0004555
	”GroinandBack Stretch” : 7.100101

}

Abductors_exercises: {
	“Thigh Abductor” : 8.200501
	”Hip Circles (prone)” :9.20015556
}
#Abductors and Adductors are not a sufficient component of a 3 group workout
def addabdcorrect():
	
