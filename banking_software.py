customer_accounts = {}
client_transactions = {}

def balance(client_transactions,name):
    """Adds the total number of transactions the client has completed"""
    return sum(client_transactions)

def available_credit(client_transactions,name):
    """Returns the available credit that the user has left"""
    return customer_accounts[name] - balance(client_transactions,name)

def check_availability(new_transaction,client_transactions,customer_accounts,name):
    """Checks if the user has enough credit to pay transactions"""
    if available_credit(client_transactions,name) - new_transaction <= 0:
    	return False
    elif available_credit(client_transactions,name) - new_transaction <= customer_accounts:
		return True

def make_transaction(new_transaction,client_transactions,customer_accounts,name):
    """This function adds a new transaction to the indicated account"""
    if check_availability(new_transaction,client_transactions,customer_accounts,name) == True:
    	client_transactions.append(new_transaction)
    return client_transactions

def statement(client_transactions,customer_accounts,name):
    """Display information about the current account and then clears transactions for new statement cycle"""
    print "Balance:", balance(client_transactions,name)
    print "Available credit:", available_credit(client_transactions,name)
    print "Transactions:"
    for i in client_transactions:
		print(i)
    client_transactions[:]=[]

import random
import sys

def main():
    """This function runs the electronic banking program."""
    print "Welcome to the Credit Card Accounts Online!"
    print ""
    while True:
    		account_limit = random.randint(500,50000)
    		print ""
		print "What would you like to do? \n 1. Create a new account \n 2. Make a new transaction \n 3. Check your statement \n 4. Quit"
		choice = input("Your choice:")
		while choice < 1 or choice > 4: #If user input is less than 1 or more than 4, continues to ask for a new choice until valid choice input
			print "Invalid choice!"
			choice = input("Your choice:")
		if choice == 1: #if condition for choosing 1
			name = raw_input("Account name: ")
			while name in customer_accounts: #checks if the name is already in the customer_accounts dictionary and returns error message if so
				print "Error: account", name ,"already exists."
				name = raw_input("Account name: ")
			customer_accounts[name] = account_limit
			client_transactions[name] = []
			print "New account created for", str(name) + ".", "Credit limit is", str(customer_accounts[name]) + "."
		if choice == 2: #if condition for choosing 2
			while not customer_accounts: #checks if there are no accounts in the customer_accounts dictoinary and returns error message
				print "Error: no account exists."
				print ""
				main()
			name = raw_input("Which account? ")
			new_transaction = input("How much is your transaction? ")
			while new_transaction < 0:
				print "Invalid transaction! Must be a positive number."
				client_transactions[name] = input("How much is your transaction? ")
			if check_availability(new_transaction,client_transactions[name],customer_accounts,name) == True:
				make_transaction(new_transaction,client_transactions[name],account_limit,name)
				print "Success! Your balance is", str(balance(client_transactions[name],name)) + ",availabile credit is", str(available_credit(client_transactions[name],name))
				print ""
			if check_availability(new_transaction,client_transactions[name],customer_accounts,name) == False:
				print "Transaction rejected. Your available credit is $" + str(customer_accounts[name]) + "."
		if choice == 3: #if condition for choosing 3
			while not customer_accounts: #test if user inputs 3 as a choice when no key or value exists in the customer_accounts dictionary
				print "Error: no account exists."
				print ""
				main()
				print ""
			name = raw_input("Which account? ")
			if name in customer_accounts and client_transactions: #if the name input is found in the customer_accounts dictionary and in the client_transactions dictionary, run calculation below
				print statement(client_transactions[name],customer_accounts,name)
			else:
				print "Error: no account exists."
				print ""
                main()
		if choice == 4:
			print "Done!"
			quit() #this function exits the program altogether

if __name__ == "__main__":
    main()
