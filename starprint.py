# craete function which can print star in traingle shape
def starprint():
    for i in range(1, 6):
        for j in range(1, i+1):
            print("*", end=" ")
        print()
starprint()

#create function which can print star in recatngle shape

def starprint_rec():

    for i in range(1, 6):
        for j in range(1, 6):
            print("*", end=" ")
        print()
starprint_rec()

#create function name heart_shape which can print star in heart shape.
def heart_shape():
    for row in range(6):
        for col in range(7):
            if (row == 0 and col % 3 != 0) or (row == 1 and col % 3 == 0) or (row - col == 2) or (row + col == 8):
                print("*", end="")
            else:
                print(end=" ")
        print()
heart_shape()

# create crud function for mongo db using flask.
# create function for create data in mongo db.
def create_data():
    # create object of mongoengine class
    user = User(name="sagar", email="test")
    # save data in mongo db
    user.save()
    return f'{user} : data saved'
def update_data():
    # update data in mongo db
    user = User.objects(name="sagar").update(name="sagar", email="test")
    return f'{user} : data updated'
def delete_data():
    # delete data in mongo db
    user = User.objects(name="sagar").delete()
    return f'{user} : data deleted'
def read_data():
    # read data from mongo db
    user = User.objects(name="sagar")
    return f'{user} : data read'

# create list of odd number from 1 to 100
def odd_list():
    odd = []
    for i in range(1, 100):
        if i % 2 != 0:
            odd.append(i)
    return odd
# create list of even number from 1 to 100
def even_list():
    even = []
    for i in range(1, 100):
        if i % 2 == 0:
            even.append(i)
    return even

# create function for fibonacci series
def fibonacci():
    a = 0
    b = 1
    for i in range(10):
        print(a)
        c = a + b
        a = b
        b = c
fibonacci()









