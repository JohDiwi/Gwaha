# TDD or test driven development is the software development practice in which the developers 
# write test codes first before wrtitting the actual code 
# These tests defined the desired specification of the code and set standard what code should do
# The essence of this is to ensure that the code meets the requirements and works as intended 

# Function that add two numbers in python 
import unittest

class BankAccount:
    def __init__(self, ID):
        self.ID = ID
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            raise ValueError("Withdraw amount must be positive and less than or equal to current balance")

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(123)  # Example ID

    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 0)

    def test_deposit(self):
        self.account.deposit(100)
        self.assertEqual(self.account.balance, 100)

    def test_withdrawer(self):
        self.account.deposit(100)
        self.account.withdraw(50)
        self.assertEqual(self.account.balance, 50)

    def test_withdraw_more_than_balance(self):
        self.account.deposit(100)
        with self.assertRaises(ValueError):
            self.account.withdraw(150)

    def test_withdraw_negative_amount(self):
        self.account.deposit(100)
        with self.assertRaises(ValueError):
            self.account.withdraw(-50)

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

if __name__ == "__main__":
    unittest.main()

import unittest
def add_two_numbers(x,y):
    return x+y

class TestAddTwoNumbers(unittest.TestCase):
    def test_add_two_numbers(self):
        self.assertEqual(add_two_numbers(4,6), 10)

if __name__=="__main__": # is used to check if the script is run directly by python interpreter or is 
# being imported as a module in another script
    unittest.main()


import unittest
class TestAddFunctions(unittest.TestCase):
 def Add_two_numbers(self):
    result = add(3,5)
    self.assertEqual(result,8)

import unittest

def add_numbers(a, b):
    return a + b

class TestAddition(unittest.TestCase):
# It is good practice to create this class because it allows the method of unittest.TestCase that is inbuilt 
# Method in the python. 
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_positive_and_negative_numbers(self):
        self.assertEqual(add(2, -3), -1)

    def test_add_zero_to_number(self):
        self.assertEqual(add(0, 5), 5)

    def test_add_zero_to_zero(self):
        self.assertEqual(add(0, 0), 0)

if __name__ == '__main__':
    unittest.main()

# The above operation can also be done using this method
# The disadvantage of this method is that we miss some of the functionality of unittest.TestCase 
# These methods are such as setUp and tearDown method.
import unittest

def add(a, b):
    return a + b

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-2, -3) == -5

def test_add_positive_and_negative_numbers():
    assert add(2, -3) == -1

def test_add_zero_to_number():
    assert add(0, 5) == 5

def test_add_zero_to_zero():
    assert add(0, 0) == 0

if __name__ == '__main__':
    unittest.main()

# Using unittst method
import unittest # here we import a unittest module in python that contais methods like 
                # organisin tests, runnig tests and organising results 
class TestAddFuction(unittest.Testcase): 
# unittet.Testcase is the class within unittest module in the python built-in function that has
# methods like; assertEqual, assertFalse and assert.True 
# in this case, i've created a class called TestAddFuction that inherits all methods of unittest.Testcase
  def add_two_numbers(self):
      result=add(3,5)
      self.assertEqual(result,8)

# This is the procedures with the help of code.
# write a test to check the behaviour of the code. This code should fail because the code to satisfy it
# hasn't been writte yet. This test check if the addition is correctly done

import unittest
def add(a,b): # you need to define this add function or import it from other module. 
    return a+b # you can skip these two lines and type; 
               # from (file name including corect path) import (function name, add in this case)
               # the bracket are not there 
               # This code has been defined as standaone code and are outside class block 
class TestAddition(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add(3,5), 8) # This code can also be w
if __name__=="__main__": # This line revents the top level code in the module to be executed when
                         # this code is exported into another module. 
# In Python, the __name__ variable is a special variable that holds the name of the current module
# When a Python script is diectly run, Python sets the __name__ variable for that script to '__main__
    unittest.main()

# tha main() in python. This is the conventionlly used function as the entry point to 
# executing python script   

# From class LMS the following tests were discussed 

import unittest

class BankAccount:
    def __init__(self,ID):
        self.ID=ID
        self.balance=0
    
    def withdraw(self,amount):
        if self.balance >= amount: # To withdraw, balance should be greated than amount to be withdrawn
            self.balance -=amount
            return True
        return False
    
    def deposit(self, amount):
        self.balance += amount
        return True
    
# Test if that the code will return an error when amount greater than balance is to withdrawn

class TestBankOperations(unittest.TestCase):
    def test_insuficient_funds(self):
        a=BankAccount(112)     
        a.deposit(100)
        outcome=a.withdraw(200)
        self.assertFalse(outcome)
unittest.main()
    