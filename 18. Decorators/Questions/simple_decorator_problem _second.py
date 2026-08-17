def login_required(func):

    def wrapper(*args, **kwargs):
        print("Checking login...")
        func(*args, **kwargs)

    return wrapper


@login_required
def dashboard():
    print("Welcome to your dashboard!")
    
dashboard()