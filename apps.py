from flask import Flask, render_template, request , redirect, url_for

server = Flask('todolist')


todo_list=["Get Milk","walk the dog"," get a cup of coffee"] 


@server.get("/")
def home():
    return render_template('home.html',todo_list_identifier=todo_list)


@server.post("/add")
def add_todo():
    print("Hello from/add")
    todo_item = request.form.get("todo")
    if todo_item:
        todo_list.append(todo_item)
    return redirect(url_for("home"))



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