# My_Dockerfile

A simple python flask app in which it prints “Hello, I am Yazan Daibes” when nothing is 
added to the URL path and “I am good, how about you?” when /how are you is added to
the URL path.

===============================================================================

Run Container: (Note: 5000 is flask port and it must be 5000 to run the app)
docker container run -p (The port you want. i.e.:3000):5000 -d my_simple_python_app

docker run -p 3000:5000 -d  my_simple_python_app

Test the application:
http://(VM IP):(The port you specified earlier i.e.:3000)

i.e.: http://192.168.1.70:3000/
