# step1: import numpy
import numpy as np

#step 2:crete a 1-D numpy array containig
#10 random heart rate values between 80 to 150
#151 is used beacuse the upper limit is excluded
heart_rate = np.random.randint(80,151,10)

#step3:display all heart rate reading
print("heart rate for 10 minutes:")
print(heart_rate)

#step4:slice the arrayt to get the first 5 minutes
first_5_minutes = heart_rate[:5]

#display the first 5 minutes
print("\nheart rates during first 5 minutes:")
print(first_5_minutes)

#step5:calculate the maximun heart rate
maximum = np.max(heart_rate)

#step6 :calculate the minimum heart rate
minimum = np.min(heart_rate)

#step7 :calculate the average heart rate
average = np.mean(heart_rate)

#display the results
print("\nmaximum heart rate :",maximum,"BPM")
print("\nminimum heart rate :",minimum,"BPM")
print("average heart rate:",round(average,2),"BPM")

#step8:identify heart rate greater than 120 BPM
high_rate = heart_rate >120

#display the actual heart rate above 120
print("\nheart rate exceeding 120 BPM:")
print(heart_rate[heart_rate])

#step9:identify yhe minutes where heart rate exceeded 120 BPM
#numpy index starts from 0,so +1 converts it to minute number
minutes = np.where (heart_rate >120)[0]+1

#display the minute number
print("\nminutes where heart rate exceeded 120 BPM:")
print(minutes)