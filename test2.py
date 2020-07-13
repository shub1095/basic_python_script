import os
import subprocess

def main():
	git_repo = os.getenv("GIT_REPO_PATH", "/Users/saket/work/shubham/basic_python_script")

	response = subprocess.check_output("git diff --cached --name-only", shell = True)
	# if not response:
	# 	exit(1)
	response = response.decode("utf-8").split('\n')

	email = subprocess.check_output("git config user.name", shell = True).decode("utf-8")
	usrname = subprocess.check_output("git config user.email", shell = True).decode("utf-8")

	if email or usrname:
		exit(1)
	else:
		print(email)
		print(usrname)


	for item in response:
		if item:
			file_path = git_repo + "/" + item
			file = open(file_path, "rt")
			data = file.read()
			#words = data.split()
			print(data)


	
if __name__=="__main__":
    main()
