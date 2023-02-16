import random
import string
import sqlite3

class User:
    """Represents a user that buys a cinema ticket"""
    def __init__(self, name):
        self.name = name
        
    def buy(self, seat, card):
        """Buys a Ticket if the card is valid"""
        if seat.is_free():
            if card.validate(price = seat.get_price()):
                seat.occupy()
                ticket = Ticket(user = self, price = seat.get_price, seat_number=seat.seat_id)
                ticket.to_pdf
                return "Purchase was successful!!"
            else:
                return "There was a problem with your card"
        else:
            return "The seat chosen is already occupied"
    
class Seat:
    """Represents a cinema seat that can taken by a user"""
    database = "cinema.db"
    
    def __init__(self, seat_id):
        self.seat = seat_id
    
    def get_price(self):
        """Get the price of a specified seat"""
        # Connect to the database
        connection = sqlite3.Connection(self.database)
        # Create a cursor
        cursor = connection.cursor()
        # create a query/sql statement
        query = "SELECT price FROM seat WHERE seat_id = ?"
        # Execute our query
        cursor.execute(query, [self.seat_id])
        # get price from database and store in variable
        price = cursor.fetchall()[0][0]
        return price
    
    def is_free(self):
        """Check in the database if a specified seat if taken or not"""
        # Connect to the database
        connection = sqlite3.Connection(self.database)
        # Create a cursor
        cursor = connection.cursor()
        # create a query/sql statement
        query = "SELECT taken FROM seat WHERE seat_id = ?"
        # Execute our query
        cursor.execute(query, [self.seat_id])
        # fetch results
        result = cursor.fetchall()[0][0]
        # checkif seat is taken or not
        if result  == 0:
            return True
        else:
            return False
    def occupy(self):
        """Changes the value of taken in the database from 0 to 2 if the seat is free"""
        if self.is_free():
            # Connect to the database
            connection = sqlite3.Connection(self.database)
            # Create a cursor
            cursor = connection.cursor()
            # create a query/sql statement
            query = "UPDATE seat SET taken = ? WHERE = ?"
            # Execute our query
            cursor.execute(query, [1, self.seat_id])
            # Commit changes to the database
            connection.commit()
            # Close the db connection
            connection.close()
          
       
    

class Card:
    """Represents a bank card needed to finalize a seat purchase"""
    database = "cinema.db"
    
    def __init__(self, type, number, cvc, holder):
        self.holder =holder
        self.cvc = cvc
        self.number = number
        self.type = type
        
    def validate(self,price):
        """Checks if card is valid and has balance, subtracts price from balance"""
        # Connect to the database
        connection = sqlite3.Connection(self.database)
        # Create a cursor
        cursor = connection.cursor()
        # create a query/sql statement
        query = "SELECT balance FROM card WHERE number = ? AND cvc = ?"
        # Execute our query
        cursor.execute(query, [self.number, self.cvc])
        # get price from database and store in variable
        result = cursor.fetchall()
        
        if result:
            balance = result[0][0]
            if balance >= price:
                query = "UPDATE card SET balance = ? WHERE number = ? AND cvc = ?"
                cursor.execute(query, [balance - price, self.number, self.cvc])
                connection.commit()
                connection.close()

class Ticket:
    def __init__(self, user, price, seat_number):
        self.user = user
        self.price = price
        self.id = "".join([random.choice(string.ascii_letters) for i in range(8)])
        self.seat_number = seat_number
        
    def to_pdf(self):
        pass
    
name = input("Enter your full names: ")
seat_id = input("Preffered seat number: ")
card_type = input("Your card type: ")
card_number = int(input("Your Card number: "))
card_cvc = int(input("Your card cvc: "))
card_holder = input("Card holder name")

user = User(name)

seat = Seat(seat_id)

card = Card(card_type,  card_number, card_cvc, card_holder)

print(user.buy(seat,card))