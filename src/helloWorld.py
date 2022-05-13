def foo(name="", age=0):
    isOldEnough = age >= 18
    if isOldEnough:
        print("Old enough")
    else:
        print("Not old enough")
        
foo()