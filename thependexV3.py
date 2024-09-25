#The Pendex, an index of names for our beloved weed pens, provided by over 100 UIUC students
#V3: Final version, adds loop feature so you do not have to reset program. 
import random
the_pendex = ['cart' , 'pen' , 'penjamin' , 'cartington' , 'stizz' , 'yarti' , 'wax' , 'teez' , 'cartiebartie' , 'pen shapiro' , 'penjamin button' , 'weed pen' , 'penver nuggets' , 'carti b' , 'frindle' , 'johnson' , 'juul' , 'dab pen' , 'zazoo' , 'fish whistle' , 'penedict' , 'stiz' , 'stizaccino' , 'cartholomew' , 'carthick' , 'cartiana' , 'gold' , 'disposable' , 'pennifer' , 'penny' , 'penelope' , 'pendleton' , 'penjamin franklin' , 'pen simmons' , 'pen stiller' , 'pen affleck' , 'jimmy pendricks' , 'pen and jerry\'s' , 'mercedes penz' , 'bombacart' , 'death sticks' , 'el boligrafog' , 'wax' , 'penji' , 'pennifer lopez' , 'blink 182' , 'blink panther' , 'blinkerton' , 'pen 10' , 'professor pen miller' , 'pen thousand dollars' , 'penny for your thoughts' , 'jart' , 'jarty' , 'jeeter' , 'gas' , 'jawn' , 'pendeezy so sweezy' , 'cartush' , 'cartek' , 'yartek' , 'shtick' , 'magic flute' , 'rodney' , 'bart' , 'carty party' , 'cartnite' , 'thc vaporizer device' , 'little guy' , 'shmeez' , 'no no stick' , 'yart' , 'penjamin city' , 'schmerze' , 'magikart' , 'stuff']
while True:
    prompt = int(input("\nWelcome to The Pendex! Please choose one of the following options:\n\n1 if you would like to see the entire Pendex in its full glory\n2 to get a random name from The Pendex\n3 to add your own name to The Pendex\n4 to see the number of names inside The Pendex\n5 make a random sentence with a word from The Pendex\n0 quit the program\n"))
    if prompt == 1:
        print(the_pendex)
    elif prompt == 2:
        print(random.choice(the_pendex))
    elif prompt == 3:
        new_word = str(input("Please enter your name here: "))
        update = the_pendex.append(new_word)
        prompt2 = int(input("Press 1 to see the entire Pendex\nor\nPress 2 to print your name\nor\nPress 3 to see your name in a random sentence\n"))
        if prompt2 == 1:
            print(the_pendex)
        elif prompt2 == 2:
            print(new_word)
        elif prompt2 == 3:
            sentences = ['yuh i smacked the shit outta the' , 'ya better believe i took a toke of that' , 'always getting so faded off that' , 'no way a 9 dollar fifty' , 'so last week my buddy was tweaking off somadat' , 'yall ever see sum demons off da' , 'sorry, i don\'t smoke any of that' , 'me when im off the' , 'wuldif spunchbob chiefd the' , 'spoke to god once off the' , 'whenever im at wendy\'s i chief the' , 'yall ever think about life when you\'re off the' , 'i think i might be breaking the law but i cant not hit the' , 'cried once off the' , 'nearly had a complete thought but i forgot i just hit the' , 'i puff puff poofed the']
            print(random.choice(sentences) , (new_word))
        else:
            print('Invalid input.')
        
    elif prompt == 4:
            print(len(the_pendex))
    elif prompt == 5:
        sentences = ['yuh i smacked the shit outta the' , 'ya better believe i took a toke of that' , 'always getting so faded off that' , 'no way a 9 dollar fifty' , 'so last week my buddy was tweaking off somadat' , 'yall ever see sum demons off da' , 'sorry, i don\'t smoke any of that' , 'me when im off the' , 'wuldif spunchbob chiefd the' , 'spoke to god once off the' , 'whenever im at wendy\'s i chief the' , 'yall ever think about life when you\'re off the' , 'i think i might be breaking the law but i cant not hit the' , 'cried once off the' , 'nearly had a complete thought but i forgot i just hit the' , 'i puff puff poofed the'] 
        print(random.choice(sentences) , random.choice(the_pendex))
    
    elif prompt == 0:
        print('Goodbye.')
        break
    
    else:
        print("Invaid input.")
