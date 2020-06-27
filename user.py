class User:

    """docstring for ."""

    def __init__(self,user_name,password):
        self.user_name = user_name
        self.password = password

        def save_user(self):
            '''
            docstring
            '''
            User.user_list.append(self)
