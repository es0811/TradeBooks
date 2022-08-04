Project Readme

1. Tech Stack Used
  Backend: Python Flask
  Front End: HTML, CSS, Javascript, Bootstrap
  Database: PostgreSQL (V 14)

2. Setup of PostgreSQL
  1. Download pgAdmin for PostgreSQL from the link below:
  https://www.pgadmin.org/download/
  2. Install pgAdmin. You might also be prompted to provide a default password.
  3. Copy the postal_codes.csv file to C drive. The schema uses this file path to import the postal codes.
  4. Select the ‘PSQL tool’ under ‘Tools’ located under toolbar.
  5. Copy the schema ‘schema.sql’ which is located in the sql folder of the project to the ‘PSQL tool’ and this will run the schema and generate the database named ‘bookworld’


3. Setting up virtual environment
  1. Open the cmd prompt and run the command: pip install virtualenv
  2. Make sure that python is installed
  3. Create the virtual environment using:
  virtualenv --python C:\Path\To\Python\python.exe env
  Here, you need to provide path to the python.exe file which is generally located in ‘C:\Users\%username%\AppData\Local\Programs\Python\Python37\python.exe’
  This will create a virtual environment named env
  4. Activate the virtual environment using ‘.\env\Scripts\activate’
  5. Navigate to the folder ‘TradeBooks’ where the project is located.
  6. Next, we need to install all the flask-based packages.
  Run the command: pip install -r requirements.txt
  7. Run the flask application using the command ‘flask run’.
  8. The details on the command prompt will provide the server address of the hosted webserver as shown below:
  ‘Running on http://127.0.0.1:5000 (Press CTRL+C to quit)’
  9. Use any web browser and navigate to the address above.


Explanation of the Application:
This application allows book readers to sell and buy books online.
Firstly, the user has to register themselves using the register option.
The user has to login and upon successfull login, the user will be directed to the dashboard.
On the dashboard, the user will be able to see statistics about the number of books bought, sold, and listed.
The user can list new books. Details related to the book will be needed here (the title, the author as well as the price at which the user intends to sell the book.)
The user can also search for books. The books can be searched by title or by the genre.
