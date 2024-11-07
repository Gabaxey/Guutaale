#y =[1,2,3]
#x = list(y)
#print(x)

#x= '12+9' 
#y = eval(x)
#print(type(y))

#x = '3'
#change = int(x)
#print (type (change))

#x = 40
#change = float(x)
#print(type (change))

#x = 40
#change = str(x)
#print(type(change))

#L = ( 1, 2, 3 ,4)
#t = list(L)
#print(type(t))

#l = ([(1, 'a'), (2, 'b')])
#d = dict(l)
#print(type(d))
#print(d)
#chr(65)
# saar/ jibaar
#x = 5
#y = 3
#print(x**y)

#modulus
#x =21
#y =2
#print(x%y)
# floor
#x = 17
#y =2
#print(x/y)

# comparision
#a = 10
#b = 5
#print(a >= b)

# logical operators
#x = 0 
#y = 20
#s = 30
#b = 30
#if  x == y and s == b :
 #   print( 'waaa isku mid' )
#else:
#    print('isku mid maaha')

# identity 
#x = 6 
#y = 5 
#print(x is not y)

# membership trou or  false
#x = ("qaro" , "cambo")
#y = "qaro" 
#print(y not in x)
            #list
        #sclicing
#fruite = ['abaayo', 'hooyo' , 'habirir']
#print(fruite[-1])  
#       loop through list
#fruite = ['abaayo', 'hooyo' , 'habirir']
#for index , x in enumerate(fruite):
#    print(index,x)
#       check if item exists
#fruite = ['abaayo', 'hooyo' , 'habirir']
#if 'apple' in fruite:
 #   print ("haa wuu ku jiraa")
#else:
    #print("maya kuma jiro")
#print(len(fruite))
                                # how to add item in list
#fruit2 = [ "ani" , "adi"]
#fruite.insert( 0 ,fruit2) 
#fruite,extend(fruit2) 
#print(fruite+fruit2) 
    # HOW TO REMOVE ITEM LIST
#fruite = ['abaayo', 'hooyo' , 'habirir']
#fruite.remove('hooyo')
#removeItem = fruite.pop()
#print(removeItem)
#print(fruite)
# reverse Item List
#fruite = ['abaayo', 'hooyo' , 'habirir']
#fruite.reverse()
#print(fruite)
    # sorted item
#num = [  4 ,7, 5 , 6,3 ,10,8,9,2,1]
#num.sort() 
#sortednumber =sorted(num)
#print(sortednumber)
#print(num)

  #  max ,min , sum

#num = ['abaayo', 'hooyo' , 'habirir'] 
#num_str = " , ".join(num)
#print(num_str)

# int convert x to an integer

# x = int('5')
# badel= str(x);
# print(type(badel))

# #  convert y to floating-point 
# y = float('5.3')
# change = float(y)
# print(change )
# # str convert x to string 
# x = int (3)
# y = str(x)
# print(y)
# #  eval (str)evaluates a string expression
# z = str('9+6')
# c = eval(z)
# print(c)

# #  tuble
# x = tuple([1,2,3])
# y = list(x)
# print(y)

# # list
# x=list((1,2,3))
# y= tuple(x)
# print(y)

# x=dict([(1,'a' ), (2, 'b') ])
# # y=tuple(x)
# print(x)
# #  convert chr
# x = chr(65)
# print(x)

# #  convert ord 
# y = ord('A')
# print(y)

# # convert hex 
# y = hex(255)
# print(y)
# # oct convert 
# x = oct(8)
# print ()

                                            # practical
# pin_one =5432
# if pin_one<5432:
#     print("welcome ")
# else:
#     print("qalad")

num=90
if num%2==0:
    print("dhaban")
else:
    print('ksisi')

for x in range(1,6):
 print(x)
                                    # --------------------------------------


                                    # Fucntion  initialize an empty list to store item 

# 
# store=[]
# def add_item():
#     item1=input("enter item1: ")
#     item2=input("enter item2: ")
#     item3=input("enter item3: ")
#     store.append(item1)
#     store.append(item2)
#     store.append(item3)
#     print (store)

#                                                       #  Fucntion calling  
# add_item()

# #  using parameter 
# def add_item(item1,item2):
#     # item1=input("enter item1: ")
#     store =  [item1,item2]
#     print(store)
# add_item('saliid', 'bur')


store = []
def add_item(store):
    item = 'bariis'
    store = [item]
    print(store)

add_item(store)