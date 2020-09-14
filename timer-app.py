import datetime
import os
import time

def main():

	MINUTES = 25
	MINUTE_TO_SECONDS = 60
	SLEEP_TIME = 5 * MINUTE_TO_SECONDS
	total = 0
	work = 0
	isWork = False
	fileName = input("Enter file name: ")
	
	while True:
		command = input("Enter start command: ")
		while True:
			if command == "start work":
				isWork = True
				print("Starting timer for work")
				break
			elif command == "start study":
				print("Starting timer for study")
				break
			else:
				print("command not recognised")

		timeLeft = MINUTES * MINUTE_TO_SECONDS
		while timeLeft > 0:
			time.sleep(SLEEP_TIME)
			timeLeft -= SLEEP_TIME
			print(str(timeLeft / 60) + " minutes left")

		print("Work Bracket Done!")
		os.system("open jobs-done.mp3")
		total += 1
		with open(fileName, "a+") as f:
			if isWork:
				work += 1
				f.write("work\n")
				isWork = False
			else:
				f.write("study\n")

if __name__== "__main__":
 	main()