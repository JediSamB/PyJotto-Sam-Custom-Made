import random
# Medium Word List

jotto_word_list_Medium = ['scuba', 'memes', 'latte', 'sunny', 'happy', 'silly',
                          'eerie', 'llama', 'needs', 'books,' 'offer', 'issue',
                          'added', 'seems', 'allow', 'tools', 'weeks', 'looks',
                          'apply', 'error', 'occur', 'rooms', 'upper', 'goods',
                          'inner', 'foods', 'array', 'doors', 'roots', 'feels',
                          'keeps', 'teeth', 'meets', 'essay', 'loose', 'seeds',
                          'woods', 'seeks', 'asset', 'boost', 'arrow', 'peers',
                          'pools', 'boots', 'deeds', 'apple', 'teens', 'assay',
                          'booth', 'tooth', 'loops', 'feeds', 'weeds', 'utter',
                          'heels', 'hooks', 'alley', 'beers', 'reefs', 'alloy',
                          'goose', 'roofs', 'oddly', 'needy', 'moose', 'fools',
                          'attic', 'geese', 'cooks', 'moods', 'moons', 'annum',
                          'reels', 'looms', 'woody', 'reeds', 'erred', 'otter',
                          'deems', 'geeks', 'abbey', 'beech', 'annex', 'hoops',
                          'goofy', 'booty', 'abbot', 'annoy', 'asses', 'moody',
                          'roost', 'cools', 'hoods', 'booze', 'httpd', 'https',
                          'jeeps', 'ellos', 'leech', 'booms', 'illus', 'roomy',
                          'beets', 'soooo', 'noose', 'noone', 'peels', 'allot',
                          'seers', 'peeps', 'zooms', 'affix', 'seedy', 'sooty',
                          'allay', 'upped', 'moors', 'booby', 'seeps', 'weedy',
                          'adder', 'beeps', 'allen', 'goons', 'geeky', 'alles',
                          'udder', 'leery', 'nooks', 'loons', 'leeks', 'gooey',
                          'cells', 'blood', 'green', 'speed', 'fully', 'happy',
                          'calls', 'floor', 'carry', 'trees', 'sleep', 'tells',
                          'steel', 'walls', 'stood', 'sorry', 'falls', 'proof',
                          'sheet', 'sweet', 'hills', 'funny', 'wheel', 'worry',
                          'fleet', 'shoot', 'breed', 'sheep', 'flood', 'bills',
                          'gonna', 'balls', 'rally', 'sells', 'wells', 'steep',
                          'rolls', 'marry', 'queen', 'silly', 'mills', 'knees',
                          'ferry', 'sheer', 'shook', 'villa', 'kills', 'fatty',
                          'lobby', 'puppy', 'sunny', 'pizza', 'polls', 'hobby',
                          'pulls', 'gotta', 'belly', 'halls', 'buddy', 'wanna',
                          'freed', 'bloom', 'dolls', 'hurry', 'fills', 'bells',
                          'gamma', 'sweep', 'troop', 'pills', 'fuzzy', 'creek',
                          'greed', 'cheek', 'petty', 'cheer', 'greet', 'spoon',
                          'wills', 'penny', 'steer', 'motto', 'hello', 'scoop',
                          'bulls', 'muddy', 'creed', 'groom', 'cello', 'stool',
                          'witty', 'curry', 'savvy', 'messy', 'jelly', 'creep',
                          'della', 'bleed', 'malls', 'folly', 'comma', 'sleek',
                          'buggy', 'dummy', 'poppy', 'queer', 'merry', 'rabbi',
                          'tally', 'ebook', 'watts', 'jolly', 'paddy', 'mummy',
                          'bully', 'furry', 'dizzy', 'hilly', 'gloom', 'brood',
                          'berry', 'dunno', 'daddy', 'riffs', 'frees', 'broom',
                          'brook', 'bunny', 'teddy', 'butts', 'spool', 'sheen',
                          'matte', 'buffs', 'outta', 'crook', 'gulls', 'kitty',
                          'jazzy', 'kamma', 'cuffs', 'lotto', 'gully', 'yells',
                          'nanny', 'hulls', 'yummy', 'posse', 'terra', 'tolls',
                          'aloof', 'foggy', 'masse', 'greek', 'gills', 'filly',
                          'pussy', 'citta', 'spoof', 'tummy', 'tonne', 'kneel',
                          'freer', 'nutty', 'jetty', 'putty', 'flees', 'steed',
                          'mommy', 'henna', 'swoop', 'delle', 'giddy', 'parry',
                          'piggy', 'afoot', 'tabby', 'potty', 'soooo', 'puffs',
                          'lorry', 'fella', 'sassy', 'soggy', 'puffy', 'stoop',
                          'fussy', 'drool', 'femme', 'holly', 'hells', 'runny',
                          'baggy', 'mamma', 'mecca', 'sills', 'manna', 'sleet',
                          'kappa', 'hadde', 'sneer', 'sloop', 'hubby', 'spook',
                          'fells', 'cotta', 'caddy', 'fossa', 'harry', 'cette',
                          'terry', 'lemma', 'swoon', 'mossy', 'metta', 'hippy',
                          'latte', 'galls', 'bossa', 'canny', 'tarry', 'telly',
                          'lotta', 'dolly', 'belle', 'whoop', 'doggy', 'ditto',
                          'sappy', 'hippo', 'comms', 'tutti', 'myrrh', 'lossy',
                          'lasso', 'three', 'breed', 'still', 'small', 'shall',
                          'staff', 'press', 'stuff', 'cross', 'agree', 'glass',
                          'guess', 'skill', 'shell', 'grass', 'dress', 'spell',
                          'gross', 'smell', 'brass', 'chess', 'skull', 'drill',
                          'bless', 'stiff', 'cliff', 'grill', 'bliss', 'spill',
                          'dwell', 'chill', 'stall', 'swell', 'bluff', 'abyss',
                          'gloss', 'troll', 'melee', 'yahoo', 'taboo', 'sniff',
                          'spree', 'fluff', 'truss', 'floss', 'quell', 'quill',
                          'snuff', 'ascii', 'radii', 'knoll', 'chaff', 'soooo',
                          'amiss', 'payee', 'puree', 'whiff', 'rupee', 'crass',
                          'gruff', 'levee', 'twill', 'atoll', 'amass', 'skiff',
                          'swiss', 'scott', 'loess', 'weeds', 'hiatt', 'krill',
                          'trill', 'scoff', 'emcee', 'knell', 'upped', 'undid',
                          'agate', 'goods', 'sculp', 'fadge', 'faked', 'fecal',
                          'algid', 'cadge', 'chafe', 'there', 'these', 'alums',
                          'apron', 'arson', 'aport', 'aunts', 'marts', 'mason',
                          'molas', 'molts', 'mourn', 'muton', 'nomas', 'punas',
                          'salon', 'pouts', 'prams', 'prats', 'praus', 'proas',
                          'sural', 'tonus', 'toras', 'torus', 'tramp', 'tunas',
                          'tauon', 'tolan', 'tolar', 'tolas', 'stupa', 'turps',
                          'swind', 'winds', 'trams', 'sport', 'spout', 'sprat',
                          'spurn', 'spurt', 'sputa', 'stump', 'stoma', 'tonal',
                          'trans', 'tolus', 'toman', 'solum', 'stour', 'swamp',
                          'likes', 'lakes']


jotto_word_picked_Medium = random.choice(jotto_word_list_Medium)
true_loop = True
jotto_guesses_count_Medium = 0
while true_loop == True:
    jotto_number_of_letters_correct_Medium = 0
    guessed = False
    while guessed != True:
        jotto_guess_Medium = input("Guess A Five letter Word\n")
        jotto_guess_list_Medium = list(jotto_guess_Medium)
        jotto_word_picked_list_Medium = list(jotto_word_picked_Medium)

        if list(jotto_guess_Medium) == int:
            print("No numbers are allowed you cheater lol jkjk!!")

        if len(jotto_guess_Medium) != 5:
            print("Your input can only be a max of 5 letters!!! And also No less than five letters, Please, Just pick a valid and real five letter word!! Thank You!!!")
            break
        else:
            if 'a' in jotto_guess_list_Medium and 'a' in jotto_word_picked_list_Medium:
                jotto_number_of_letters_correct_Medium += 1
            if 'b' in jotto_guess_list_Medium and 'b' in jotto_word_picked_list_Medium:
                jotto_number_of_letters_correct_Medium += 1
            if 'c' in jotto_guess_list_Medium and 'c' in jotto_word_picked_list_Medium:
                jotto_number_of_letters_correct_Medium += 1
            if 'd' in jotto_guess_list_Medium and 'd' in jotto_word_picked_list_Medium:
                jotto_number_of_letters_correct_Medium += 1
            if 'e' in jotto_guess_list_Medium and 'e' in jotto_word_picked_list_Medium:
                jotto_number_of_letters_correct_Medium += 1
            if 'f' in jotto_guess_list_Medium and 'f' in jotto_word_picked_list_Medium:
                jotto_number_of_letters_correct_Medium += 1
            if 'g' in jotto_guess_list_Medium and 'g' in jotto_word_picked_list_Medium:
                jotto_number_of_letters_correct_Medium += 1
            if 'h' in jotto_guess_list_Medium and 'h' in jotto_word_picked_list_Medium:
                jotto_number_of_letters_correct_Medium += 1
            if 'i' in jotto_guess_list_Medium and 'i' in jotto_word_picked_list_Medium:
                jotto_number_of_letters_correct_Medium += 1
            if 'j' in jotto_guess_list_Medium and 'j' in jotto_word_picked_list_Medium:
                jotto_number_of_letters_correct_Medium += 1
            if 'k' in jotto_guess_list_Medium and 'k' in jotto_word_picked_list_Medium:
                jotto_number_of_letters_correct_Medium += 1
            if 'l' in jotto_guess_list_Medium and 'l' in jotto_word_picked_list_Medium:
                jotto_number_of_letters_correct_Medium += 1
            if 'm' in jotto_guess_list_Medium and 'm' in jotto_word_picked_list_Medium:
                jotto_number_of_letters_correct_Medium += 1
            if 'n' in jotto_guess_list_Medium and 'n' in jotto_word_picked_list_Medium:
                jotto_number_of_letters_correct_Medium += 1
            if 'o' in jotto_guess_list_Medium and 'o' in jotto_word_picked_list_Medium:
                jotto_number_of_letters_correct_Medium += 1
            if 'p' in jotto_guess_list_Medium and 'p' in jotto_word_picked_list_Medium:
                jotto_number_of_letters_correct_Medium += 1
            if 'q' in jotto_guess_list_Medium and 'q' in jotto_word_picked_list_Medium:
                jotto_number_of_letters_correct_Medium += 1
            if 'r' in jotto_guess_list_Medium and 'r' in jotto_word_picked_list_Medium:
                jotto_number_of_letters_correct_Medium += 1
            if 's' in jotto_guess_list_Medium and 's' in jotto_word_picked_list_Medium:
                jotto_number_of_letters_correct_Medium += 1
            if 't' in jotto_guess_list_Medium and 't' in jotto_word_picked_list_Medium:
                jotto_number_of_letters_correct_Medium += 1
            if 'u' in jotto_guess_list_Medium and 'u' in jotto_word_picked_list_Medium:
                jotto_number_of_letters_correct_Medium += 1
            if 'v' in jotto_guess_list_Medium and 'v' in jotto_word_picked_list_Medium:
                jotto_number_of_letters_correct_Medium += 1
            if 'w' in jotto_guess_list_Medium and 'w' in jotto_word_picked_list_Medium:
                jotto_number_of_letters_correct_Medium += 1
            if 'x' in jotto_guess_list_Medium and 'x' in jotto_word_picked_list_Medium:
                jotto_number_of_letters_correct_Medium += 1
            if 'y' in jotto_guess_list_Medium and 'y' in jotto_word_picked_list_Medium:
                jotto_number_of_letters_correct_Medium += 1
            if 'z' in jotto_guess_list_Medium and 'z' in jotto_word_picked_list_Medium:
                jotto_number_of_letters_correct_Medium += 1

            if jotto_guess_Medium == jotto_word_picked_Medium:
                jotto_guesses_count_Medium += 1
                jotto_print_CorrectMedium = f"CORRECT!!! == {jotto_guess_Medium} | {jotto_number_of_letters_correct_Medium} | {jotto_guesses_count_Medium} |"
                print(jotto_print_CorrectMedium)
                print("\nThe selected word was, " +
                      jotto_word_picked_Medium + "! Great Job!!!")
                guessed = True

            elif jotto_guess_Medium != guessed:
                jotto_guesses_count_Medium += 1
                jotto_print_GuessesMedium = f"{jotto_guess_Medium} | {jotto_number_of_letters_correct_Medium} | {jotto_guesses_count_Medium} |"
                print(jotto_print_GuessesMedium)
                jotto_guess_Medium = None
                break
