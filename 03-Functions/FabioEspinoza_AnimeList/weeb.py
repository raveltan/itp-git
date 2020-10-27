class Weeb:
    
    def __init__(self, firstname, lastname, animes=''):
        self.first = firstname
        self.last = lastname
        self.animes = animes
    
    def print_fullname(self):
        return('{} {}'.format(self.first, self.last))
    
    def favorite_animes(self):
        animeList = []
        animeNumber = int(input("Please Enter how many shows you want to add to your list {}: ".format(self.first)))
        
        for i in range(animeNumber):
            animeList.append(input('Enter Show #{}: '.format(i+1)))
        
        self.animes += '\n '.join(animeList) 
    
    def print_animes(self):
        if self.animes == '':
            return("(Empty anime list! Please add some to your list!)")
        else:
            return(str(self.animes))
    
    def introduction(self):
        print("Hello Everyone my name is "+ self.print_fullname() + " and my favorite animes are :\n " + self.print_animes())
    
    
        
        
    