import datetime

# Client Class representing customer for Security Agency
class Client:

    def __init__(self, name=None, phone=None, email=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.registered_on = datetime.datetime.now()
        
        # Guards Associated with a Client (1 to many relationship)
        self.guards = []


# Pricing Class for Charges of Security Guard
class Pricing:
    # Attributes with default values
    def __init__(self):
        self.day = 500
        self.week = 3000
        self.month = 10000


# SecurityGuard Class representing a security person alongwith charges
class SecurityGuard:

    def __init__(self, name=None, phone=None, email=None, gender=None, security_rating=None, pricing=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.gender = gender
        self.security_rating = security_rating
        
        # Pricing Associated with a Security Guard
        self.pricing = pricing


# ServiceRequest Class representing a request raised by client having options as a response with status management
class ServiceRequest:

    def __init__(self, requested_by=None):
        self.requested_by = requested_by
        self.requested_on = datetime.datetime.now()
        # 0 for pending, 1 for approved, 2 for rejected
        self.status = 0 
        
        # list of 3 security guards to choose from
        self.options = []
 