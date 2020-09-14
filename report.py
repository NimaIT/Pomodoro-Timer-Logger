import datetime
import os
import time

def main():
	
	total = 0
	totalStudy = 0
	totalWork = 0
	files = files = os.listdir('.')

	for f in files:
		if len(f.split('.')) > 1 and f.split('.')[1] == "txt":
			file = open(f, "r")
			content = file.readlines()

			for line in content:
				if line == "study\n":
					total += 1
					totalStudy += 1
				elif line == "work\n":
					total += 1
					totalWork += 1

	studyHours = (totalStudy * 25) // 60
	studyMinutes = (totalStudy * 25) % 60
	workHours = (totalWork * 25) // 60
	workMinutes = (totalWork * 25) % 60
	totalHours = (total * 25) // 60
	totalMinutes = (total * 25) % 60

	reportStudy = "Total time spent studying: " + str(studyHours) + "hr " + str(studyMinutes) + "m"
	reportWork = "Total time spent working: " + str(workHours) + "hr " + str(workMinutes) + "m"
	reportTotal = "Total time: " + str(totalHours) + "hr " + str(totalMinutes) + "m"
	print(reportStudy)
	print(reportWork)
	print(reportTotal)

	makeDirectory = input("Move all logs into a new folder? (y/n): ")
	if makeDirectory == "y":
		directory = str(datetime.datetime.today()).split()[0]

		with open("reportlog.txt", "a+") as reportFile:
			reportFile.write(reportStudy + "\n")
			reportFile.write(reportWork + "\n")
			reportFile.write(reportTotal + "\n")

		os.system("mkdir " + directory)
		for f in files:
			if (len(f.split('.')) > 1) and (f.split('.')[1] == "txt"):
				os.system("mv " + f + " " + directory)

		print("All files log moved to folder: " + directory)






if __name__== "__main__":
 	main()