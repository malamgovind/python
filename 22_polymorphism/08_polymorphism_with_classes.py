class India:
    
    def capital(self):
        print("New Dilhi")

class Japan:

    def capital(self):
        print("Tokyo")


for country in [India(), Japan()]:
    country.capital()