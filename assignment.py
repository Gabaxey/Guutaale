def Add_contac():
    name = input("please inter your name ")
    number  = input("please inter your number ")
    email = input("please inter your email")
    #step2 list
    contact_list = [name , number , email]

    # Add Contact 
    while True :

        print ("\n===================Contact Managment System ===================")
        print ("Add contaact ")
        print ("Remove Contact ")
        print ("Show Contact ")
        print ("Exit")
        user_input =input('choice')

    #  if Statment for Adding contact to list 
        if user_input == '1':
            print("add contact ")
        elif user_input == '2':
            print("Remove contact ")
        elif user_input == '3':
            print("show  contact ")
        elif user_input == '4':
            print("Exit ")
            

    #step1
        name = input("please inter your name ")
        number  = input("please inter your number ")
        email = input("please inter your email")

        #step2 list
        contact_list = [name , number , email]


        #step3 
        tuple_ = ('name' , 'number' , 'email')

        #step4 
        dict_ ={
            tuple_[0]:contact_list[0],
            tuple_[1]:contact_list[1],
            tuple_[2]:contact_list[2]

        }
        print('----------contact----------')
        print('name' , dict_[tuple_[0]])
        print('number', dict_[tuple_[1]])
        print('email' ,dict_[tuple_[2]])

# add contact 
# remove contact 
#  show contact 
#  quit 