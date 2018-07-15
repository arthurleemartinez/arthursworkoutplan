#This is a list of all the popularly trained muscle groups
muscle_areas = [“Chest”, “Biceps”, “Abdominals”, “Lats”, “Triceps”, “Forearms”, “Shoulders”, “Middle Back”, “Calves”,  “Hamstrings”,  “Quadriceps”,  “Traps”,  “Lower Back”,  “Glutes”, “Abductors”, “Adductors”]
#Exercise dictionaries that referrences midly obfuscated ratings provided by bodybuilding.com
xz = raw_input("What did you workout yesterday and the day before?")
x = muscle_areas.pop(xz)
#function that gets 3 random muscle groups that have had time to recover
def new_muscleareas(x):
  c1 = random.choice(x)
  c2 = random.choice(x)
  c3 = random.choice(x)
  while (c2 == c1):
    c2 = random.choice
    break:  
  while (c3 == d2):
    c3 = random.choice
    break:  
  todayex = [c1, c2, c3]
  return todayex
  





exercises: {
	“Dumbbell Bench Press” : 9.200341
	”Pushups” : 9.205362346
	”Dumbbell Flyes” : 9.1043562
	“Incline Dumbbell Bench Press” : 9.100678
	“Medium-Grip Barbell Bench Press” : 9.090678
	“Chest Dips” : 9.000567
	“Incline Hammer Curls” : 9.5006794
	”Wide-Grip Standing Barbell Curl” : 9.30003245
	”Spider Curl” : 9.200004576
	”EZBar Curl” : 9.10004576
	”Hammer Curls” : 9.1000234
	”Zottman Curl” : 9.1000045672
	”Concentration Curls” : 9.0000036421
	”Barbell Curl” : 9.00074721
	“Dumbbell Bicep Curl” : 8.900034612
	“One-Arm Medicine Ball Slam” : 9.12341
	”Landmine180s” : 9.50000235
	”Plank” : 9.3000004578
	”Elbow to Knee” : 9.100000568
	”Plate-Twist” : 9.000003467
	”Bottom’s Up” : 9.300000346
	“Weighted Pull Ups” : 9.50000436, 
	”Pullups” : 9.2000235
	”Chin-Up” : 9.10000012
	”Wide-Grip Pull-Up” : 8.90000395
	”Close-Grip Front Lat Pulldown” : 8.80000001
	”Shotgun Row” : 8.8000001	
	“Dips - Triceps Version” : 9.40000012
	”Decline EZ Bar Triceps Extension” : 9.300012
	”Dumbbell Floor Press” : 9.300003461
	”Close-Grip Barbell Bench Press” : 9.10041325
	”Triceps Pushdown - V-Bar Attachment” : 9.100311
	”Weighted Bench Dip” : 9.100003
	”Push-Ups - Close Triceps Position” : 9.00000346
	”Close-Grip Barbell Bench Press” : 9.100046
	“Seated Palm-Up Barbell Wrist Curl” : 8.700046
	”Seated One-Arm Dumbbell Palms-Up Wrist Curl : 9.00034
	”Wrist Roller” : 9.100325
	”Palms-Up Barbell Wrist Curl Over A Bench” : 9.40235
	”Wrist RotationswithStraight Bar” : 9.500162
	“Single-Arm Linear Jammer” : 9.50007
	”Side Laterals to Front Raise” : 9.50005
	”Standing Palm-In One-Arm Dumbbell Press” : 9.40003
	”Power Partials” : 9.10005
	”Seated Dumbbell Press” : 9.10002
	”Side Laterals to Front Raise” : 9.5060012
	”Standing Palm-In One-Arm Dumbbell Press” : 9.40001
	”One-Arm Side Laterals” : 9.10105
	“T-Bar RowwithHandle" : 9.50060024
	”Reverse Grip Bent-Over Rows” : 9.200054221
	”One-Arm Long Bar Row” : 9.000861
	”One-Arm Dumbbell Row” : 9.0001
	”Seated Cable Rows” : 8.800761
	“Smith Machine Calf Raise” : 9.20071
	”Standing Calf Raises” : 9.008
	”Standing Dumbbell Calf Raise” : 8.8088
	”Seated Calf Raise” : 8.7007
	”Rocking Standing Calf Raise” : 8.707777
	”Standing Barbell Calf Raise” : 8.20222
	“Lying Leg Curls” : 8.9004 
	”Barbell Deadlift” : 9.40004
	”Leg Curl” : 8.5011
	”Romanian Deadlift With Dumbbells” : 9.41
	“Barbell Full Squat” : 9.400014
	”Leg Press” : 9.600235
	”Rope Jumping” : 9.200235
	”Step Mill” : 9.100145
	“Smith Machine Shrug” : 9.201255
	”Dumbbell Shrug”: 8.70014
	”Barbell Shrug”: 8.4
	”Standing Dumbbell Upright Row”: 8.70071
	“Axle Deadlift” : 9.10012
	”Deficit Deadlift” : 9.4001245
	”Hyperextensions (Back Extensions)” : 9.1001245
	“Butt Lift (Bridge)” : 8.80001	   
	”One-Legged Cable Kickback” : 9.000111
	”Kneeling Squat” : 8.6
	“Thigh Adductor” : 9.0004555
	”GroinandBack Stretch” : 7.100101
	“Thigh Abductor” : 8.200501
	”Hip Circles (prone)” :9.20015556
	}

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
	”Seated Calf Raise” : 8.7007
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

print (
