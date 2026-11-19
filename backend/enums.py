import enum

class UserRole(enum.Enum):
    ADMIN = "admin"
    CUSTOMER = "customer"

    
class OrderStatus(enum.Enum):
    PENDING = "Pending"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"