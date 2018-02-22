def outer():
    """Prints the value of n."""
    n = 1
    def inner():
        
        n = 2
        print(n)
    inner()
    print(n)
outer()
