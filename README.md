# My_Dockerfile

Run Container: (Note: 5000 is flask port and it must be 5000 to run the app)
docker container run -p (The port you want. i.e.:3000):5000 -d my_simple_python_app

docker run -p 3000:5000 -d  my_simple_python_app

Test the application:
http://(VM IP)(The port you specified earlier i.e.:3000)

i.e.: http://192.168.1.70:3000/
