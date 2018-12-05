import os,glob

os.chdir('/home/praveen/Pictures/')

for file in glob.glob("*.png"):
    print(file)