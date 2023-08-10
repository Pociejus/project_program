# project_program
First Project - Program

The program is designed to simplify and accelerate the process of creating sports programs. Essentially, it's a database of exercises with visual examples that allows you to print a template for a sports program. You can populate the exercise database with new exercises or clients, as well as accumulate information about clients. The program is built using the Django framework for ease of use. There was no intention to create a website, but this project has the potential to grow.
Installation:

Copy all files from the repository.
Run the command pip install -r requirements.txt to install the necessary libraries.
In the views.py file, on line 48, you will need to specify the absolute path to the Arial.ttf file depending on the directory where you place the project.
You'll need to create your own superuser(or use mine : admin/ admin), as program creation happens through the admin panel. First, create a client by adding a new user through the admin panel. Access it by adding /admin to the base URL. The user is automatically assigned a profile.
After filling in the client's information, create a program for them without assigning a program day. Then, create program days by selecting strength and stretching exercises through the admin panel.
After saving the data, you can change the number of sets and repetitions for exercises. You can print a new program by going to the main directory and selecting the desired program. Print each day separately by clicking on each day.
You can view information about clients. The Body Mass Index (BMI) is automatically calculated, and recommendations are provided based on the BMI value. Additionally, the appropriate heart rate for cardiovascular exercises is calculated based on the client's age.
