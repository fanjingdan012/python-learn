import random
import shutil
import os
def randomFileName():
	return str(random.randint(1,999999999))

while True:
	print "*"*40
	print "101 Python Coding Ground for Kids"
	print "*"*40
	print "[+] Options : \n\t1. Create file\n\t2. Read a file\n\t3. Delete File\n\t4. Run file:"
	try:
		userinput1 = input("Choose an option:")
		print("Your selected choise is "+str(userinput1)) #will remove

		if userinput1 == 1:
			fname = randomFileName()
			print "Creating a file with name :"+fname
			w = open(fname,'w')
			userinput2 = str(raw_input("Write your content ( use enter to finish entering):"))
			print "Your entry :" + str(userinput2) #will remove
			w.write(userinput2)
			w.close()
			print "[+] Options : \n\t1. Public file\n\t2. Private file"
			userinput3 = input("Enter choice:")
			print "Your input :"+str(userinput3) #will remove
			if userinput3 == 1:
				try:
					shutil.move(fname,"public/"+fname)
					print "Successfully moved the file in public directory"
				except:
					print "That was an unpected move"
			elif userinput3 == 2:
				try:
					shutil.move(fname,"private/"+fname)
					print "Successfully moved the file in private directory"
				except:
					print "That was an unexpected move"

		if userinput1 == 2:
			userinput4 = input("Enter file name:")
			userinput5 = input("What type of file was it : \t1. Public \t2. Private")
			if userinput5 == 1:
				w = open("public/"+str(userinput4),'r')
				x = w.readlines()
				w.close()
				print "Your file contents:"+str(x)
			elif userinput5 == 2:
				w = open("private/"+str(userinput4),'r')
				x = w.readlines()
				w.close()
				print "Your file contents:"+str(x)

		if userinput1 == 3:
			userinput6 = raw_input("Enter the file name you want to delete:")
			userinput7 = input("Enter the type of file \t1. Public \t2. Private:")
			if userinput7 == 1:
				cmd = 'rm public/'+userinput6
				os.system(cmd)
			elif userinput7 == 2:
				cmd = 'rm private/'+userinput6
				os.system(cmd)
			else:
				cmd = 'rm '+userinput6
				os.system(cmd)


		if userinput1 == 4:
			userinput8 = input("Enter file name:")
			userinput9 = input("Enter the type of file \t1. Public \t2. Private:")
			if userinput9 == 1:
				w = open("public/"+str(userinput8),'r')
				x = w.readlines()
				w.close()
				x = ''.join(x).strip()
				print str(x)
				y = eval(str(x))
				print(y)

		if userinput1 == 5:
			x = os.listdir("public")
			print "Now printing contents of public directory"
			for i in x:
				w = open("public/"+str(i),'r')
				print(w.readlines())
				w.close()

			x = os.listdir("private")
			print "Now printing contents of public directory"
			for i in x:
				w = open("private/"+str(i),'r')
				print(w.readlines())
				w.close()
	except IOError:
		print("Could not read or open the file")
	except Exception as exc:
		print("An error occured")
exit
