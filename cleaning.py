def cleaning_tweet(string):
    for ch in string:
        if(ch >= 'a' and ch <='z'):
            print(ch)
        
string = "#he@ll^o"
string2 = ''
cleaning_tweet(string)