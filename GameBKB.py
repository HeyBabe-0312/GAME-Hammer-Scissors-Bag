import speech_recognition
import pyttsx3
from random import randint

AI_mouth = pyttsx3.init()
while True:
	print ("Enter what you want to choose [Hammer(Búa), Scissors(Kéo), Bag(Bao)]: ")
	voices = AI_mouth.getProperty('rate')
	AI_mouth.setProperty('rate', 123)
	voices = AI_mouth.getProperty('voices')
	AI_mouth.setProperty('voice', voices[1].id)
	AI_mouth.say("Enter what you want to choose: ")
	AI_mouth.runAndWait()

	player=input()
	print("[--------------VS--------------]")
	print("> You choose   : " + player)
	AI_mouth.say("You choose " + player)
	AI_mouth.runAndWait()

	robot= randint(0,2)

	if robot == 0:
		robot="Hammer"
	elif robot == 1:
		robot="Scissors"
	else:
		robot="Bag"

	print ("> Sophia choose: " + robot)
	print("[--------------VS--------------]")
	AI_mouth.say("I'm choose " + robot)
	AI_mouth.runAndWait()

	if player==robot:
		res="1"
	elif player=="Hammer":
		if robot=="Scissors":
			res="2"
		else:
			res="0"
	elif player=="Scissors":
		if robot=="Hammer":
			res="0"
		else:
			res="2"
	elif player=="Bag":
		if robot=="Hammer":
			res="2"
		else:
			res="0"
	else:
		res="3"

	if res=="1":
		print ("$$$ Result: Draw !!")
		print ("Sophia: Ohh shitt ... we draw. Do you want to determine whether you win or lose again? (Y/N)")
		AI_mouth.say("Ohh shitt ... we draw. Do you want to determine whether you win or lose again? (Yes or No)")
		AI_mouth.runAndWait()
		yes=input()
		if yes == "N":
			print ("Sophia: We have yet to determine the winner. See you next time... You seem tired now !!! You should relax ... It was fun today, sir")
			AI_mouth.say("We have yet to determine the winner. See you next time... You seem tired now. You should relax ... It was fun today, sir")
			AI_mouth.runAndWait()
			break
		elif yes == "Y":
			print ("Sophia: Alright, this time, I won't draw anymore ... Let's play now")
			AI_mouth.say("Alright, this time, I won't draw anymore ... Let's play now")
			AI_mouth.runAndWait()
		else:
			print ("Sophia: You are only selected (Y/N). Try again !!!")
			AI_mouth.say("You are only selected (Y/N). Try again !!!")
			AI_mouth.runAndWait()
			yes=input()
			if yes == "N":
				break
			elif yes == "Y":
				continue
			else:
				print ("Sophia: You are so muddy. Let's have a rest !!!")
				AI_mouth.say("You are so muddy. Let's have a rest !!!")
				AI_mouth.runAndWait()
				yes=input()
				break
	elif res=="0":
		print ("$$$ Result: Lose !!!")
		print ("Sophia: Yeahh... Yesssss, I beat you. Do you want to revenge me hahaha (Y/N)")
		AI_mouth.say("Yeahh... Yesssss, I beat you. Do you want to revenge me hahaha (Yes or No)")
		AI_mouth.runAndWait()
		yes=input()
		if yes == "N":
			print ("Sophia: You still lost to me hahaha. Bye bye loser ... Just kidding haha haha. You seem tired now !!! You should relax ... It was fun today, sir")
			AI_mouth.say("You still lost to me hahaha. Bye bye loser ... Just kidding haha haha. You seem tired now. You should relax ... It was fun today, sir")
			AI_mouth.runAndWait()
			break
		elif yes == "Y":
			print ("Sophia: Alright, this time, I still keep winning you hahaaa... Come on")
			AI_mouth.say("Alright, this time, I still keep winning you hahaaa... Come on")
			AI_mouth.runAndWait()
		else:
			print ("Sophia: You are only selected (Y/N). Try again !!!")
			AI_mouth.say("You are only selected (Y/N). Try again !!!")
			AI_mouth.runAndWait()
			yes=input()
			if yes == "N":
				break
			elif yes == "Y":
				continue
			else:
				print ("Sophia: You are so muddy. Let's have a rest !!!")
				AI_mouth.say("You are so muddy. Let's have a rest !!!")
				AI_mouth.runAndWait()
				yes=input()
				break	
	elif res=="2":
		print ("$$$ Result: Win !!!")
		print ("Sophia: Ohh nooo... huhuhu, Why am I losing, you're so lucky. Let's continue now (Y/N)")
		AI_mouth.say("Ohh nooo... huhuhu, Why am I losing, you're so lucky. Let's continue now (Yes or No)")
		AI_mouth.runAndWait()
		yes=input()
		if yes == "N":
			print ("Sophia: I will not submit... If there is a next time I will definitely win. But you seem to be tired now !!! You should relax ... It was fun today, sir")
			AI_mouth.say("I will not submit... If there is a next time I will definitely win. But you seem to be tired now. You should relax ... It was fun today, sir")
			AI_mouth.runAndWait()
			break
		elif yes == "Y":
			print ("Sophia: Alright, don't be confident. This time I will prove you're just lucky... Choose carefully, sir")
			AI_mouth.say("Alright, don't be confident. This time I will prove you're just lucky... Choose carefully, sir")
			AI_mouth.runAndWait()
		else:
			print ("Sophia: You are only selected (Y/N). Try again !!!")
			AI_mouth.say("You are only selected (Y/N). Try again !!!")
			AI_mouth.runAndWait()
			yes=input()
			if yes == "N":
				break
			elif yes == "Y":
				continue
			else:
				print ("Sophia: You are so muddy. Let's have a rest !!!")
				AI_mouth.say("You are so muddy. Let's have a rest !!!")
				AI_mouth.runAndWait()
				yes=input()
				break
	else:   		
		print ("$$$ Error: No result !!!")
		print ("Sophia: You are only selected (Hammer,Scissors,Bag). Try again now !!!")
		AI_mouth.say("You are only selected (Hammer,Scissors,Bag). Try again now !!!")
		AI_mouth.runAndWait()
