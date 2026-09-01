# write a program train which has a method to book a tickect get status (no of seat )
# and get fare information of train running under indian railwats

from random import randint

class train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
    def book(self, fro, to):
        print(f"your train  ticket is booked in train no: {self.trainNo} train is running from :{fro} to {to}")
    def getstatus(self):
        print(f"trainNo :{self.trainNo} train is running on time")
    def getfare(self, fro, to):
        print(f"ticket fare for train no : {self.trainNo} from :{fro} to {to} is {randint(100, 1000)}")

ticket = train(12556)
ticket.book("rampur", "delhi")
ticket.getstatus()
ticket.getfare("rampur", "delhi")


    