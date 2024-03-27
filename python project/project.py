class user:
    def __init__(self,name,rollno,email,password):
        self.name=name
        self.rollno=rollno
        self.email=email
        self.password=password
class reguser:
    def __init__(self):
        self.reg_user={}
        self.cur_user=None
    def register(self):
        name=input()
        rollno=int(input())
        email=input()
        password=int(input())
        if not name or not rollno or not email or not password:
            print("enter details")
            return
        conf_pass=int(input())
        if password != conf_pass:
            print("invalid ")
            return
        self.reg_user[rollno]=user(name,rollno,email,password)
        print("registration successful",name)
    def login(self):
        rollno=int(input())
        password=int(input())
        if rollno in self.reg_user and self.reg_user[rollno].password==password:
            self.cur_user=rollno
            print("user logged in")
        else:
            print("invalid rollno or password")

    def displaydet(self):
        if self.cur_user:
            print("details")
            print("name",user.name)
            print("rollno",user.rollno)
            print("email",user.email)
            #print("password",user.password)
        else:
            print("no user log in")
    def logout(self):
        if self.cur_user:
            print("\nlogging out user:",self.reg_user[self.cur_user].nsme)
            self.cur_user=None
        else:
            print("no user logged in")
    def mainmenu(self):
        while True:
            print("\nmain menu")
            print("1.Register")
            print("2.login")
            print("3.display details")
            print("4.logout")
            print("5.exit")
            ch=input("enter choice:")
            if ch=='1':
                self.register()
            elif ch=='2':
                self.login()
            elif ch=='3':
                self.displaydet()
            elif ch=='4':
                self.logout()
            elif ch=='5':
                print("existing prgm")
                break
            else:
                print("invalid choice.try again")

if __name__ == "__main__":
    registration_system = reguser()
    registration_system.mainmenu()


















            
            
        
