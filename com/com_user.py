
def get_user(request):
    username = request.COOKIES.get("username")
    return username

class User(object):
    def __init__(self, username):
        self.username = username

