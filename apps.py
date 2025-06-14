from turtle import title
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

all_images=[]

@server.get("/gallery")
def gallery():
    return render_template("gallery.html", all_images=all_images)

@server.post("/addImage")
def add_image():
    image_url = request.form.get("image")
    all_images.append(image_url)
    return redirect(url_for("gallery"))



#--------------Online Store---------

all_products = [
    {
        "title": "Toothpaste",
        "price":  9,
        "image":"https://m.media-amazon.com/images/I/612MXu5fFoL._SX466_.jpg"
    },
    {
        "title": "Mints",
        "price": 4 ,
        "image":"https://m.media-amazon.com/images/I/81p9PcPsffL._AC_UL480_FMwebp_QL65_.jpg"
    },
    {
            "title": "floss",
            "price":4,
            "image":"https://m.media-amazon.com/images/I/31hTE829EOL._SX300_SY300_QL70_FMwebp_.jpg"
    },
    {
            "title": "Tooth brushes",
            "price": 5,
            "image":"https://m.media-amazon.com/images/I/71hcRuTJYeL.__AC_SX300_SY300_QL70_FMwebp_.jpg"
    },
    {
            "title": "whitening strips",
            "price": 20,
            "image":"https://m.media-amazon.com/images/I/81I12YXEuPL._AC_SX679_.jpg"
    },
    {
            "title":"mouth wash",
            "price": 6,
            "image":"https://m.media-amazon.com/images/I/71R1J7lz6zL._AC_SY879_.jpg"
    },
    {
            "title":"water pick",
            "price":48,
            "image":"https://m.media-amazon.com/images/I/61LVwSVLvyL._AC_SX679_.jpg"
    },
    {       "title":" tongue scraper",
            "price": 10,
            "image":"https://m.media-amazon.com/images/I/71rHWCneOfL._SX466_.jpg"
}

]

cart_list= []

@server.get("/catalog")
def catalog():
    return render_template("catalog.html", all_products=all_products)

@server.post("/addtoCart")
def add_to_cart():
    title = request.form.get("title")
    cart_list.append(title)
    return redirect(url_for("catalog"))

@ server.get("/cart")
def cart():
    """ 
    We have the title on the cart_list
    but we need all the data of each product, not just the titles


    we get the title,
    we find the product for that title
    we send the list of prods instead of just the titles
    """
    cart_prods =[]
    for title in cart_list:
        for prod in all_products:
            if prod["title"]==title:
                #found the match
                cart_prods.append(prod)





    return render_template("cart.html", cart_prods=cart_prods)





server.run(debug=True)