# Udacity-Movie-Trailer-Final-Project
Udacity Full Stack Web Developer Movie Trailer Project.

Project dynamically creates web page that displays users favorite Movies, including the ability to display movie trailer, poster art, global gross boxoffice receipts, and story line.

fresh_tomatoes.py
Using python, javascript, and html fresh_tomatoes.py uses objects passed in by entertainment_center.py to create/write/open an html that displays Movie object content.

entertainment_center.py
Uses fresh_tomatoes.py and media.py to create several instances of Movie objects that assign movie title, storyline, gross global receipts, poster art, and youtube trailer. Objects are passed into fresh_tomatoes method open_moves_page() via list.

media.py
creates Movie object class and includes show_trailer() method definition. Movie object creates space in memory for object and all passed in attributes. show trailer uses webbrowser library to display objects trailer in browser.
