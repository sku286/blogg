# blogg
CREATING the project python project:
 1. Install required Python(3.7,always try to go with latest version)

 2. Install virtual environment using "pip"
            pip install virtualenv
			
 3. Create the project directory
			mkdir blogdir
			cd blogdir
			
 4. Create a virtualenv to isolate our package dependencies locally
			virtualenv blogging
			blogging\Scripts\activate     # On Linux use `source blogging/bin/activate`

 5. Install Django and Django REST framework into the virtualenv
			pip install django
			pip install djangorestframework

 6. Set up a new project with a single application
			django-admin startproject blogg .  # Note the trailing '.' character
			cd blogg
			django-admin startapp sblogg
			
			

USING PyCharm:
 1. Open Pycharm and select the project directory "e.g: blogg" to open.
 2. Set the Python Interpretor. Load virtual environment in python Interpretor.
    1) Goto File > Settings 
	2) Goto Project and tab Project Interpretor
	3) In project Interpretor select the directory where there is virtual environment.
	      e.g: E:\PythonWDir\blogdir\blogging\Scripts\python.exe
		  

SETTING Github with pycharm:
 1. Install github on system and create github account.
 2. Create local git repository i.e: .git file will appear in your directory
 4. Add files/directory on local git by selecting the file and "right click"
    Then select Git> Add, add git commit comment.
 4. Goto "VCS" on pycharm
 5. Then Select "Import into version Control" > "Share project on Github"
