from selenium import webdriver
from pages.login_page import LoginPage
import time

def func(x):
    return x+1;
def add(x,y):
    return x+y;
# Tests
def test1():
    assert func(3)==4  # This should pass

def test2():
    assert func(3)==5  # This should fail

def test3():
    assert add(3,5)==8 # This should pass

def test4():
    assert add(4,5)==76 # This should fail

