from flask import Flask, render_template

server = Flask('todolist')


@server.get("/")
def home():
    return render_template('home.html')


@server.get("/about")
def about():
    return render_template('about.html')


#create a contact page

@server.get("/contact")
def contact():
    return render_template('contact.html')





            
server.run(debug= True)





#start the server
server.run(debug=True)