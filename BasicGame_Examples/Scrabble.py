


OnePointLetters = ["a","e","i","o","u","l","n","r","s","t"]
TwoPointLetters = ["d","g"]
ThreePointLetters = ["b","c","m","p"]
FourPointLetters = ["f","h","v","w","y"]
FivePointLetters = ["k"]
EightPointLetters = ["j","x"]
TenPointLetters = ["q","z"]


def ScrabbleCalc(word):
    word_score = 0 

    for char in word: 
        if char in OnePointLetters:
            word_score += 1
        elif char in TwoPointLetters:
            word_score += 2
        elif char in ThreePointLetters:
            word_score += 3
        elif char in FourPointLetters:
            word_score += 4
        elif char in FivePointLetters:
            word_score += 5
        elif char in EightPointLetters:
            word_score += 8
        else: 
            word_score += 10 

    return word_score 


print(ScrabbleCalc('zoo'))

        
