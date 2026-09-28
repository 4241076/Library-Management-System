class Member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email

    def display(self):
        print("Member ID: ", self.member_id, "\nName: ", self.name, "\nEmail: ", self.email)
