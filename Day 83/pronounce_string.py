import pyttsx3


def pronounce_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    text_to_pronounce = """
Kishan: Good morning teachers. Myself Kishan Panchal, and he is my Group Partner Jaymin Darji.
Kishan: We are working on Fresh Mart, an E-commerce Platform for Online Grocery Shopping. We plan to sell various groceries, including vegetables, fruits, rice, wheat, and dals.
Kishan: Talking about the existing system, there are limitations such as limited scalability, lack of personalization, inefficient search functionality, etc.
Kishan: Moving to the proposed system, we are adding functionalities like review and rating, advanced search functionality, etc.
Kishan: We'll use the following technologies to make our project run smoothly. In the front end, we'll use React.js (a JavaScript library) and Tailwind CSS (a CSS framework) for styling. On the backend, we'll use Node.js (JavaScript runtime) and Express.js (Node.js framework). For the database, we'll use MongoDB.
Kishan: In our project, there will be two types of users - Admin and User/Customer.
Kishan: Talking about the Admin role, the admin can perform roles such as user management, product management, system maintenance, etc.
Kishan: Users can perform roles like searching for products, adding items to the cart, etc.
Kishan: Talking about the use case diagram, it shows the interaction between an actor (user/admin) and the functionality.
Kishan: Admin functionalities include login, managing users, products, payments, etc.
Kishan: User functionalities include registering, logging in, searching for items, managing the cart, etc.
Further information will be provided by my group partner Jaymin Darji.
Jaymin: Itna to Kishan ne bola, me kya bolu. Chaliye marks de dijiye, aur is ko khatam karte hai.
"""

    pronounce_text(text_to_pronounce)
