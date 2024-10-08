import tornado.web
import db

class UserHandler(tornado.web.RequestHandler):
    def get(self):
        connection = db.get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        self.render("index.html", users=users)

class CreateUserHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("create_user.html")
    
    def post(self):
        name = self.get_argument("name")
        email = self.get_argument("email")
        age = self.get_argument("age")
        connection = db.get_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (name, email, age) VALUES (%s, %s, %s)", (name, email, age))
        connection.commit()
        self.redirect("/users")

class EditUserHandler(tornado.web.RequestHandler):
    def get(self, user_id):
        connection = db.get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        self.render("edit_user.html", user=user)
    
    def post(self, user_id):
        name = self.get_argument("name")
        email = self.get_argument("email")
        age = self.get_argument("age")
        connection = db.get_connection()
        cursor = connection.cursor()
        cursor.execute("UPDATE users SET name = %s, email = %s, age = %s WHERE id = %s", (name, email, age, user_id))
        connection.commit()
        self.redirect("/users")

class DeleteUserHandler(tornado.web.RequestHandler):
    def get(self, user_id):
        connection = db.get_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        connection.commit()
        self.redirect("/users")
