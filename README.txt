1) This project is implemented using Python 2.7.10 and Django web framework and Mysql database.
2) Install Django 1.9.5
3) Setup mysql. Create database "stocks". 
4) To create mysql tables, got to directory using command line /stock-prediction/stockprediction/.
	run the following commands:
	a) "python manage.py makemigrations"
	b) "python manage.py migrate"
	this will create the mysql tables in the database "stocks".
5) to Run the sytem server:
	a) Navigate to directory /stock-prediction/stockprediction/
	b) Run the command "python manage.py runserver"




Directory structure:

Stock-Prediction - Main folder


--> Scripts (Folder containing all the data collection python scripts)
	historical.py- Python script to fetch historical data and store in db
	current.py-    Python script to fetch current data and store in db
	stock_list.txt- List of stocks implemented in the system


--> Stockprediction


----------stockprediction
		This folder is the main base directory in the system. It contains the most important .py files like:
			settings.py Contains main settings for system. Go and put your mysql password here.
			urls.py it has main URL mapping of the system. Maps all the urls to their URIs.
----------Manage.py: It is main file in the system.
	

----------Templates- Contains all of the HTML templates of the system.
		index.html
		base.html
		news.html
		search.html
		login.html
		and all other html templates for graph plots.

----------Static- Contains all the static files for the system like images, Javascript files, CSS files, fonts.
 
----------stockapp- main App in our system.
	 	Models.py- This script makes the mysql tables for this app.
		urls.py- maps urls of this app
		views.py Contains all the functions to create views on the webpage.

----------track- new app to let user track his favourite stocks or remove them.
		urls.py
		views.py

----------User- App to let user login and show user home page
		urls.py
		views.py


		
