# Test Your Code  

As you write your own functions and classes, it is always a good idea to write tests for them. To *prove* your code works, you test it to ensure everything works as it should in response to all the input types you've designed it to receive.  

Every programmer makes mistakes, so it's a good idea to that every programmer must test their code frquently. This way, they can catch problems before users run into them.  

## What You'll Learn  

We'll learn to test our own code using Python tools found in the `unittest` module. We'll also learn how to build a **test case** and check that a set of input results in the output you want.  

We will see what a passing test looks like, as well as what a failing test looks like. A failing test can help you improve your code. We'll learn how to test your own functions and classes, and start to understand how many tests to write for a particular project.  

### Test a Function  

Let's write up some code to test (you cannot test code without any code!). Create a simple function that takes input of a first name and last name, and outputs a formatted full name.  

#### name_function.py  

```python  
def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = first + " " + last
    return full_name.title()
```  

To check that `get_formatted_name()` works, make a program that uses the function.  

The program *names.py* allows users to enter a first and last name, and then see a neatly formatted full name:  

#### names.py  

```python  
from name_function import get_formatted_name

print("Enter 'q' at anytime to quit.")

while True:
    first = raw_input("\nPlease insert a first name: ")
    if first == 'q':
        exit()
        # can use "break" here instead of exit()
        
    last = raw_input("Please insert a last name: ")
    if last == 'q':
        exit()
        # can use "break" here instead of exit()

    formatted_name = get_formatted_name(first, last)
    print("\tFormatted name: " + formatted_name + ".")
```  

After running *names.py*, we can see the names generated are correct. But, what if we wanted to modify `get_formatter_name()` to handle middle names as well? Well, when we do this, we wanted to make sure we don't break the way the function handles names that only have a first name and last name. We could test our code by running *names.py* again and enter a first and last name again, everytime we modify the function. However, you can see this can quickly get tedious.  

### Enter, `unittest` module  

Python provides an efficient way to automate the testing of a function's output, so we can always be confident the function will work given the kinds of names you write tests for.  

## Unit Tests & Test Cases  

The Python standard library holds a module called `unittest`, which provides tools for testing your code.  

A *unit test* verfies one specific aspect of a function's behavior is correct.  

A *test case* is a collection of unit tests that together prove a function is behaving as it was made to handle. A good test case considers all the possible variations of input a function could receive and includes a full range of unit tests covering all the possible ways you can use a function.  

### What a Passing Test Looks Like  

#### test_name_function.py  
```python  
import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Jimi Hendrix' work?"""
        formatted_name = get_formatted_name('jimi', 'hendrix')
        self.assertEqual(formatted_name, 'Jimi Hendrix')

unittest.main()
```  

After we run the *test_name_function.py, we'll get this output:  

#### example output for *test_name_function.py*
```  
.
----------------------------------------------------------------------
Ran 1 test in 0.004s

OK
```  

We know the test passed, because of the dot on the first line.  

This output tells us that the function `get_formatted_name()` will always work for first and last names unless we modify the function. After you modify the function, you can run this test again.  

### What a Failing Test Looks Like  

We'll modify `get_formatted_name()` so it can handle middle names. But, let's do it in a way so that it breaks the function for names with just a first and last name, like Jimi Hendrix.  

#### new version of `get_formatted_name()` which now requires a middle name argument  

```python  
def get_formatted_name(first, middle, last):
    """Generate a neatly formatted full name."""
    full_name = first + " " + middle + " " + last
    return full_name.title()
```  

This version will work for people inserting a middle name as well, but when you test it, you'll see it breaks the function for people inserting just a first and last name.  

#### example output for *test_name_function.py* having the third parameter, 'middle'  
``` 
E
======================================================================
ERROR: test_first_last_name (__main__.NameTestCase)
Do names like 'Jimi Hendrix' work?
----------------------------------------------------------------------
Traceback (most recent call last):
  File test_name_function.py", line 9, in test_first_last_name
    formatted_name = get_formatted_name('jimi', 'hendrix')
TypeError: get_formatted_name() takes exactly 3 arguments (2 given)

----------------------------------------------------------------------
Ran 1 test in 0.027s

FAILED (errors=1)
```  

We know the test failed, because of the `E` on the first line. 

The reason there is more information in the output for a failed test, is because you might need the information to find where/why the error occurred when a test fails (so you can fix it).  

#### How to Respond to a Failed Test  

Don't freak out! A failing test just means there is an error in the new code. So, **when a test fails, don't change the test.** Rather, fix the code that caused the test to fail (changes you made to the original function). --heck out the changes you just made to the function, and figure out which change(s) caused your function to break.  

For our case, the best option is to make the middle name input optional by giving it an empty default value:  

#### name_function.py where the middle name parameter is not mandatory  
```python  
def get_formatted_name(first, middle = '', last):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = first + " " + middle + " " + last
    else:
        full_name = first + " " + last
    return full_name.title()
```  

**Before running the test case**, go ahead and run this file (test before the test). You'll notice you get a *Syntax error* window with the following information.

#### Syntax error window:    
```
There's an error in your program:  
*** non-default argument follows default argument  
(name_function.py, line #)  
```  
In Python, any "non-default" argument must come after any "default" argument. To *debug*, simply place the `middle` parameter to the end of the parameter list in the function definition:  

```python  
def get_formatted_name(first, last, middle = ''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = first + " " + middle + " " + last
    else:
        full_name = first + " " + last
    return full_name.title()
```  

Now run the test case's test file.  

#### example output for *test_name_function.py* having the third parameter, 'middle'  
```  
.
----------------------------------------------------------------------
Ran 1 test in 0.065s

OK
```  
Now we have a passing test!  

***  

## Adding New Tests  

Now that you have a passing test for simple names, add another test **method** to `NamesTestCase` that provides a second case for people who inlcude a middle name:  
#### 
```python  
import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Jimi Hendrix' work?"""
        formatted_name = get_formatted_name('jimi', 'hendrix')
        self.assertEqual(formatted_name, 'Jimi Hendrix')

    def test_first_last_middle_name(self):
        """Do names like 'Marie Francis Curie' work?"""
        formatted_name = get_formatted_name('marie', 'curie', 'francis')
        self.assertEqual(formatted_name, 'Marie Francis Curie')

unittest.main()
```  



```  
.
----------------------------------------------------------------------
Ran 1 test in 0.009s

OK
```  