def validate_user_creation(data):
    required_fields = ['name', 'email', 'password']
    return all(field in data and data[field] for field in required_fields)

def validate_user_update(data):
    required_fields = ['name', 'email']
    return all(field in data and data[field] for field in required_fields)

def validate_login(data):
    required_fields = ['email', 'password']
    return all(field in data and data[field] for field in required_fields)
