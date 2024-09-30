class Anagram:
    def __init__(self,word):
        self.word = word


    def match(self,text_list):
        match_list = [text for text in text_list if sorted(text) == sorted(self.word) ]
        return match_list 
        
        
                