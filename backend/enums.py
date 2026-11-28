import enum

class UserRole(enum.StrEnum):
    ADMIN = "Admin"
    CUSTOMER = "Customer"

    
class OrderStatus(enum.StrEnum):
    PENDING = "Pending"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"
    
class MenuCategory(enum.StrEnum):
    MAINDISH = "MainDish"
    SWALLOW = "Swallow"
    SNACKS = "Snacks"
    DRINKS = "Drinks"