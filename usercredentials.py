class Usercredentials:

    """docstring for ."""

    def __init__(self,username,password):
        self.username = username
        self.password = password

        def saveuser(self):
            '''
            docstring
            '''
            User.userlist.append(self)
