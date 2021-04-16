# squirrel-project
IEOR E4501 Final Project - Xiao Huang(xh2488), Hui Chen(hc3255)

## Description 
This is a Django-based project which keeps track of all the known squirrels in the central park, New York City. There are five views available in total, respectively shows:
- Squirrels' location on a map
- A list of all squirrels and a button that navigate users to add new squirrels
- Detailed information of each squirrel
- A form to add new squirrels
- Some general statistics of squirrels

## Group name and section 
Project Group 13, Section: Wednesday 7pm - 9pm

## UNI
UNIs:[xh2488, hc3255]

## Deploy link
http://x-catwalk-308822.ue.r.appspot.com

## Installation Guidance
1. pip install -r requirements.txt
2. python3 manage.py migrate
3. python3 manage.py import_squirrel_data <csv_file_path>\
(The csv can be found in the folder as well)
4. python3 manage.py runserver
5. python3 manage.py export_squirrel_data <export_path>\
(Used to export data)
