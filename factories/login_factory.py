def create_login_data(overwrites=None):
    default_values= {
        "email": "test_email@test.com",
        "pwd": "123456",
        "isValidEmail":True,
        "isValidPWD": True
        }
    
    mappings = {
        "email" : [
            {"flag":"isValidEmail", "value":"test_email@test.com"},
            {"flag":"isInValidEmail", "value":"aaa@mail.com"}  
            
        ],
        
        "pwd" : [
            
            {"flag": "isValidPWD", "value":"123456"},
            {"flag": "isInValidPWD", "value":"aaa"},
            
        ]
    } 
    
    overwrites = overwrites or {}
    login_data = {**default_values, **overwrites}
    
    for key, rules in mappings.items():
        for rule in rules:
            if login_data.get(rule["flag"]):
                login_data[key] = rule["value"]
    return login_data        