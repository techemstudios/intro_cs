##def get_formatted_name(first, last):
##    """Generate a neatly formatted full name."""
##    full_name = first + " " + last
##    return full_name.title()

### New version of function
### (adding a third argument, 'middle')


# edit made before a fail test: adding a middle name parameter
##def get_formatted_name(first, middle, last):
##    """Generate a neatly formatted full name."""
##    full_name = first + " " + middle + " " + last
##    return full_name.title()


# edit after a fail test: making the middle name paramter optional
##def get_formatted_name(first, middle='', last):
##    """Generate a neatly formatted full name."""
##    if middle:
##        full_name = first + " " + middle + " " + last
##    else:
##        full_name = first + " " + last
##    return full_name.title()

# edit after this file failed: making the middle name paramter optional
# (moving the empty default value for the middle parameter to the
# end of the parameter list
def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = first + " " + middle + " " + last
    else:
        full_name = first + " " + last
    return full_name.title()
