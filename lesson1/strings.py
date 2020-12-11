
def say_hello_to(name):
    print "Hello " + name
    print "--------------"


def say_my_name_times(name, times):
    print (name + " ") * times
    print "--------------"


def your_name_too_long(name):
    if len(name) > 5:
        print name + " - is a very long name"
    else:
        print name + " - is a short name"
    print "--------------"


def multiply(num1, num2):
    print num1 * num2


say_hello_to("Robert")
say_my_name_times("Robert", 3)
your_name_too_long("Robert")
multiply(-5, 6)
