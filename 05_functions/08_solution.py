def multiKeywords(**kargs):
    for key, value in kargs.items():
        print(f"{key}: {value}")
        
multiKeywords(name = "Hirdesh", branch = "CSE")