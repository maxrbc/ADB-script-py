import os
import subprocess as s

## getcwd gives you already the current working directory 
pwd_current = os.getcwd()
out1 = os.popen("pwd ").read()
print out1

########################################################
##
##	Max R. Berrios 
##

# reduce the amount of un handle process to 0 
# and use less shell like struct that an be turn 
# against us later . 
output3 = s.check_output(['adb' , 'shell' , 'getprop'])
for opt in output3.split("\n"):
	if not ":" in i:
	continue

	tmp = i.strip("\r[]").split(":")
	opt = tmp[0].strip().strip("[]")
	resp = tmp[1].strip().strip("[]")
	
	if "product.brand" in opt:
		brand = resp
	elif "product.model" in opt:
		model = resp
##
##
########################################################

output1 = os.popen("adb shell getprop | grep product.brand").read()
output2 = os.popen("adb shell getprop | grep product.model").read()



output1 = output1.replace("[", "")
output1 = output1.replace("]", "")
output1=output1.split()
#print output1[1]


## Python is dynamic you do not need to 
## define them to used them just init 
## them before

directory = "LOL"
folder = "OLO"

## here i change to model and product since i have them already in diferent 
## variables 
if "samsung" in str(output1[1]).lower():
	print "Samsung S6"
	folder="Samsung S6"
	directory ="/storage/emulated/legacy"
elif "motorola" in str(output1[1]).lower():
	print "Motorola"
	folder="Moto"
	directory ="/storage/emulated/legacy"
elif "google" in str(output1[1]).lower():
	print "nexus found"
	folder = "Nexus"
	directory= "/storage/sdcard0"

## both directory and folder are strings you do not need to re-cast them 
pull_command="adb pull "+directory+"/Attribute-data/ '/home/larsip-ubuntu-2/Downloads/data-char/script-data/"+folder+"' "		

#print pull_command
os.system(pull_command)
print "completed"
