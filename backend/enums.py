import enum

class UserRole(enum.Enum):
    ADMIN = "Admin"
    CUSTOMER = "Customer"

    
class OrderStatus(enum.Enum):
    PENDING = "Pending"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"