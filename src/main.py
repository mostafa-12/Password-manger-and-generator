from colorama import Fore
import password_manager
import encryption
import pwinput

def main():
    print(Fore.RED,"""
        .....   ......   .....    .....   .....    .....   ......   .....    .....   .....    .....    .
        .....   ......   .....    ....... .....    .....  .......   ......   .....   .....    ..... .  .
    ....................................................................................................
    .....   ......   ..... .  .....   .....    .....   ......   .....   ......   .....    ......  ......
    .....   .......  .....    .....   ..... .  ...=#@@@@#=... . .....    ..... . ...... . ......   .....
        .....   ......  .......   .....   ....=%%%%%%%%%%%%%%=...   .....    .....   .....    .....    .
        .....   ......   .....    .....   ..*%%%%%%#++++*%%%%%%*.  ...... .  .....   .....    .....    .
    ..... . ......   .....    .....   ....-%%%%%-...   ....-%%%%%-....   .....   ..... .  .....    .....
    .....   ......   .....    .....   ...-%%%%=.....   ......-%%%%-..    .....  ......    ......   .....
        ..... . ......  ......    ..... .#%%%-.    .....   ...:%%%#.......   .....   .....    .....    .
        .....   ........ .....    ..... -%%%*..    .....   ....+%%%=.....    .....   .....    .....  . .
    ....................................*%%%:...................%%%*....................................
    ..... . ......   .....    .....   ..#%%%.  .....   ...... . %%%#.    .....   .....  . .....    .....
    .....   ......   .....  . .....  ...#%%%.  .....   .......  %%%#.    .....   .....    .....    .....
        .....   ......   .....    ..:+%@%%%%@@@@@@@@@@@@@@@@@@@@%%%%@%+:.   ...... . .....    .....  . .
      . .....   ......   ......   .*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#    .....   .....    .....    .
    ..............................=%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%=..............................
    .....   ......   .....   .....=%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%=....   .....    ......   .....
    ..............................=%%%%%%%%%%%%%%%%*....*%%%%%%%%%%%%%%%%=..............................
     .  .....   ......   .....   .=%%%%%%%%%%%%%%%=..... -%%%%%%%%%%%%%%%=.  .....   .....    .....  . .
        .....   ....... ......    =%%%%%%%%%%%%%%%:..... :%%%%%%%%%%%%%%%=   .....   .....    .....  . .
    .....  .......   .....    ....=%%%%%%%%%%%%%%%%.   ..%%%%%%%%%%%%%%%%=....   .....    ..... .  .....
    .....   ......   .....    ....=%%%%%%%%%%%%%%%%%.  .%%%%%%%%%%%%%%%%%=....   .....    .....  . .....
        .....   ......   .....    =%%%%%%%%%%%%%%%%%....%%%%%%%%%%%%%%%%%=.  .....   .....  . .....    .
        .....   ......   .....    =%%%%%%%%%%%%%%%%%....%%%%%%%%%%%%%%%%%=   ......  ......   .....    .
    ..............................=%%%%%%%%%%%%%%%%%*..*%%%%%%%%%%%%%%%%%=..............................
    .....   ......   ......   ....=%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%=....   .....    .....    .....
    .....   ......   .....    ....=%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%=....   .....   ......    .....
     .. .....  .......   .....  . .#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#    ......  .....    .....    .
        .....   ......   .....    ..:*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*-.    .....   .....    .....  . .
    ....................................................................................................
    """)
    print(Fore.GREEN,"Welcome to Password-Manger-Generator",end="")
    encryption.creatKeyIfNot()
    while True :
        print(Fore.GREEN,"What do you want ? :)\n 0-exit\n 1- only generate password\n 2- Create an account and save your password secrets \n 3- Login \n 4-creat fast url token => ",end="")
        choice = input()

        if choice == "0":
            exit()
        elif choice == "1" :
            print("enter the length of the password ('default value is 8 and we don't recommend less than that') : ",end="")
            length = input()
            if len(length) == 0 :
                print(password_manager.generatePassword())
            else:
                length = int(length)
                print(password_manager.generatePassword(length))
                print("*"*50)
        
        
        
        elif choice == "2":

            print(Fore.GREEN,"user name : ",end="")
            userName = input()    
            

            accPassword = pwinput.pwinput(prompt =f"{Fore.GREEN}Password : " )

            person = password_manager.creatAccount(userName,accPassword)

            print(Fore.GREEN,"want to add password ?! (yes or no ,(y,n))",end="")

            des = input()
            try:
                if des.lower() == "yes" or  des.lower() == "y":
        
                    print(Fore.RED,"enter site-mail-password")
                    passwordItems = input().split("-") 
                    password = {"site": passwordItems[0], "mail" : passwordItems[1], "password" : passwordItems[2]}
                    person = password_manager.addPass(person,password)

                
                elif des.lower() == "no" or  des.lower() == "n":
                    pass
                else:
                    print("please enter valid input")
                    raise ValueError
                person = encryption.hashing(person)
                person = encryption.Encrypt(person)
                password_manager.saveUser(person)
                
                print(Fore.BLUE,"See later pro 🙌")                
                 
            except Exception as err:
                print(err)

        elif choice == "3":
            
            print(Fore.GREEN,"account's name : ",end="")
            userName = input()    
            
            accPassword = pwinput.pwinput(prompt =f"{Fore.GREEN}Password : " )
            
            user = password_manager.loadUser(userName,accPassword)
            user = encryption.Decrypt(user)
            if not user :
                print("user name or password is wrong please check your data and try again")
                continue

            while True:
                print(Fore.BLUE,f"Hello {userName}\nwhat do you want \n0-exit\n1-show all passwords\n2-add password \n3-delete password\n=> ",end="")
                choice = input()
                if choice == "0":
                    exit()
                elif choice == "1":
                    
                    print(Fore.BLUE,user.showInfo())
                elif choice == "2":
                    print(Fore.RED,"enter site-mail-password")
                    passwordItems = input().split("-") 
                    password = {"site": passwordItems[0], "mail" : passwordItems[1], "password" : passwordItems[2]}
                    user = password_manager.addPass(user,password)
                elif choice == "3":
                    print(Fore.RED,"enter site-mail-password")
                    passwordItems = input().split("-") 
                    password = {"site": passwordItems[0], "mail" : passwordItems[1], "password" : passwordItems[2]}
                    password_manager.removePass(user,password)
                else:
                    print(Fore.RED,"Invalid input, please try again with enter a valid input")
                    continue
        elif choice == "4":
            print(password_manager.generateToken())
            print("*" * 50)
        else:
            print("please enter valid input :| ")
            continue



if __name__ == "__main__":
    main()