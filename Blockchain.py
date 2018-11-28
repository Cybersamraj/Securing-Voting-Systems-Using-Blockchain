import sys
import datetime
import hashlib


#Classes
class Block(object):
    #Properties
    block_no = 0
    data = "G"
    next = None
    hash = None
    previous_hash = 0x0
    timestamp=0

    def __init__(self, data, block_no,timestamp): #Input arguments
        self.data = data
        self.block_no = block_no
        self.timestamp = datetime.datetime.now()

    def hash(self):
        h = hashlib.sha256()
        h.update(
            str(self.block_no).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.previous_hash).encode('utf-8') +
            str(self.timestamp).encode('utf-8')
        )
        return h.hexdigest()

    def str(self):
        return "--------------"+"\nBLOCK HASH: " + str(self.hash()) + "\nBLOCK NO: " + str(self.block_no) + "\nBLOCK DATA: " + self.data + "\nTIME STAMP: " + str(self.timestamp) +"\n--------------"


class Blockchain(object):

    diff = 20
    maxNonce = 2 ** 32
    target = 2 ** (256 - diff)

    chain = []
    chain.append(Block("GENESIS", 1,0))

    def add(self, block):
        block.previous_hash = self.block.hash()
        block.blockNo = self.block.blockNo + 1
        self.block = self.block.next

    def mine(self, block):
        self.chain.append(block)


def main():
    menu()


def menu():


    print("\n\n***** WELCOME TO CYBER SAMRAJ BLOCKCHAIN VOTING DEMO *****")
    print()

    choice = input("""
                      A: LOGIN
                      B: LOGOUT

                      PLEASE ENTER YOUR CHOICE: """)

    if choice == "A" or choice == "a":
        login()

    elif choice == "B" or choice == "b":
        print("\n********* THANK YOU FOR USING OUR DEMO SYSTEM **********")
        sys.exit()

    else:
        print("PLEASE ENTER A or B")
        print("PLEASE TRY AGAIN")
        menu()


def login():
    print("\n\n************** WELCOME TO THE LOGIN SCREEN ***************")
    print()

    id=input("\n PLEASE ENTER YOU ID NUMBER:")


    if id == "1234": #Default ID
        vote()

    else:
        print("YOU HAVE ENTERED YOUR ID WRONG")
        print("PLEASE START AGAIN")
        menu()

def vote():
    print("\n\n************* WELCOME TO THE VOTING SCREEN ***************")
    print()

    yvote = input("\n WHO WOULD YOU LIKE TO VOTE FOR:\n"
               "A. JACK DOWRY\n"
               "B. KATE HOLLAND\n"
               "PLEASE ENTER YOUR CHOICE:")


    if yvote == "A" or yvote == "a" or yvote == "B" or yvote == "b":
        if yvote == "A" or yvote == "a":
            vote_name = "JACK DOWRY"
        else:
            vote_name = "KATE HOLLAND"

        print("\n--------------")
        print("VOTE RECORDED. PLEASE WAIT WHILE OTHER NODES ARE CONNECTED....")
        print("--------------")
        print("THE CURRENT BLOCKCHAIN :")

        blockchain = Blockchain()

        block = Block(vote_name, len(blockchain.chain)+1,datetime.datetime.now())
        blockchain.mine(block)

        for id in range(len(blockchain.chain)):
            print(blockchain.chain[id].str()) #Prints blockchain details

        print("LENGTH OF CHAIN: ")
        print(len(blockchain.chain)) # Prints blockchain length

        print("\n--------------")
        print("\nTHANK YOU. YOUR VOTE HAS BEEN ADDED TO THE BLOCKCHAIN.")
        print("\nNOW YOU WILL BE DIRECTED TO THE HOME SCREEN.")

        menu()

    else:
        print("YOU HAVE ENTERED AN INVALID VOTE")
        print("PLEASE TRY AGAIN")
        vote()


main()
