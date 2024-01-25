class ConfigFile:
    SECRET_KEY = "JUVHG80RLROTTN13WQM4GBS2JCBO3XU90RM606U5VHO3YJ762T"
    ALGORITHM = "HS256"
    FAKE_USERS_DB = {
                        "testuser": {
                            "username": "testuser",
                            "password": "testpassword"
                        }
                    }
    ORIGINS =  [
                    "http://localhost",
                    "http://localhost:8080", 
                    "http://localhost:3000",  
                ]
