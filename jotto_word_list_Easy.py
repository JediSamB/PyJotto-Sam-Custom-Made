import random
# Easy Word List

jotto_word_list_Easy = ['brown', 'brown', 'acids', 'store', 'shelf', 'eight', 'found',
                        'wreck', 'naked', 'plant', 'bronx', 'place', 'areas', 'craft',
                        'combs', 'hiked', 'snake', 'waste', 'check', 'spark', 'lacey',
                        'bream', 'tenth', 'ideal', 'acted', 'syncs', 'crank', 'items',
                        'cabin', 'songs', 'viper', 'notch', 'miles', 'masks', 'redid',
                        'abide', 'abled', 'ached', 'agile', 'ailed', 'alcid', 'alike',
                        'alkie', 'badge', 'bagel', 'baked', 'baled', 'beach', 'belch',
                        'bield', 'biked', 'black', 'bleak', 'cable', 'caged', 'caked',
                        'chalk', 'chela', 'chide', 'chief', 'child', 'chile', 'decaf',
                        'decal', 'faced', 'felid', 'fidge', 'field', 'filed', 'seals',
                        'flake', 'fleck', 'flick', 'gable', 'gelid', 'flied', 'glade',
                        'glide', 'haled', 'hiked', 'ideal', 'laced', 'leach', 'liked',
                        'their', 'world', 'altos', 'atoms', 'autos', 'lamps', 'loans',
                        'lotus', 'louma', 'loups', 'lours', 'louts', 'lumps', 'lunar',
                        'manor', 'manos', 'manus', 'mauls', 'mauts', 'moats', 'molar',
                        'monas', 'moral', 'moras', 'morns', 'morts', 'moult', 'mount',
                        'mural', 'nopal', 'norms', 'opals', 'orals', 'palms', 'panto',
                        'pants', 'parol', 'parts', 'porns', 'ports', 'pours', 'proms',
                        'pumas', 'punto', 'punts', 'purls', 'puton', 'qualm', 'quant',
                        'quart', 'quota', 'ramps', 'ratos', 'roams', 'roans', 'roast',
                        'roman', 'romps', 'rotas', 'rotls', 'roups', 'roust', 'routs',
                        'rumps', 'santo', 'sapor', 'slump', 'smalt', 'smart', 'smolt',
                        'snarl', 'snort', 'snout', 'slant', 'stamp', 'stomp', 'storm',
                        'squat', 'tarns', ]

jotto_word_picked_Easy = random.choice(jotto_word_list_Easy)
true_loop = True
jotto_guesses_count_Easy = 0
while true_loop == True:
    jotto_number_of_letters_correct_Easy = 0
    guessed = False
    while guessed != True:
        jotto_guess_Easy = input("Guess A Five letter Word\n")
        jotto_guess_list_Easy = list(jotto_guess_Easy)
        jotto_word_picked_list_Easy = list(jotto_word_picked_Easy)

        if list(jotto_guess_Easy) == int:
            print("No numbers are allowed you cheater lol jkjk")

        if len(jotto_guess_Easy) != 5:
            print("Your input can only be a max of 5 letters!! And also No less than five letters, Please, Just pick a valid and real five letter word!!! Thank You!")
            break
        else:
            if 'a' in jotto_guess_list_Easy and 'a' in jotto_word_picked_list_Easy:
                jotto_number_of_letters_correct_Easy += 1
            if 'b' in jotto_guess_list_Easy and 'b' in jotto_word_picked_list_Easy:
                jotto_number_of_letters_correct_Easy += 1
            if 'c' in jotto_guess_list_Easy and 'c' in jotto_word_picked_list_Easy:
                jotto_number_of_letters_correct_Easy += 1
            if 'd' in jotto_guess_list_Easy and 'd' in jotto_word_picked_list_Easy:
                jotto_number_of_letters_correct_Easy += 1
            if 'e' in jotto_guess_list_Easy and 'e' in jotto_word_picked_list_Easy:
                jotto_number_of_letters_correct_Easy += 1
            if 'f' in jotto_guess_list_Easy and 'f' in jotto_word_picked_list_Easy:
                jotto_number_of_letters_correct_Easy += 1
            if 'g' in jotto_guess_list_Easy and 'g' in jotto_word_picked_list_Easy:
                jotto_number_of_letters_correct_Easy += 1
            if 'h' in jotto_guess_list_Easy and 'h' in jotto_word_picked_list_Easy:
                jotto_number_of_letters_correct_Easy += 1
            if 'i' in jotto_guess_list_Easy and 'i' in jotto_word_picked_list_Easy:
                jotto_number_of_letters_correct_Easy += 1
            if 'j' in jotto_guess_list_Easy and 'j' in jotto_word_picked_list_Easy:
                jotto_number_of_letters_correct_Easy += 1
            if 'k' in jotto_guess_list_Easy and 'k' in jotto_word_picked_list_Easy:
                jotto_number_of_letters_correct_Easy += 1
            if 'l' in jotto_guess_list_Easy and 'l' in jotto_word_picked_list_Easy:
                jotto_number_of_letters_correct_Easy += 1
            if 'm' in jotto_guess_list_Easy and 'm' in jotto_word_picked_list_Easy:
                jotto_number_of_letters_correct_Easy += 1
            if 'n' in jotto_guess_list_Easy and 'n' in jotto_word_picked_list_Easy:
                jotto_number_of_letters_correct_Easy += 1
            if 'o' in jotto_guess_list_Easy and 'o' in jotto_word_picked_list_Easy:
                jotto_number_of_letters_correct_Easy += 1
            if 'p' in jotto_guess_list_Easy and 'p' in jotto_word_picked_list_Easy:
                jotto_number_of_letters_correct_Easy += 1
            if 'q' in jotto_guess_list_Easy and 'q' in jotto_word_picked_list_Easy:
                jotto_number_of_letters_correct_Easy += 1
            if 'r' in jotto_guess_list_Easy and 'r' in jotto_word_picked_list_Easy:
                jotto_number_of_letters_correct_Easy += 1
            if 's' in jotto_guess_list_Easy and 's' in jotto_word_picked_list_Easy:
                jotto_number_of_letters_correct_Easy += 1
            if 't' in jotto_guess_list_Easy and 't' in jotto_word_picked_list_Easy:
                jotto_number_of_letters_correct_Easy += 1
            if 'u' in jotto_guess_list_Easy and 'u' in jotto_word_picked_list_Easy:
                jotto_number_of_letters_correct_Easy += 1
            if 'v' in jotto_guess_list_Easy and 'v' in jotto_word_picked_list_Easy:
                jotto_number_of_letters_correct_Easy += 1
            if 'w' in jotto_guess_list_Easy and 'w' in jotto_word_picked_list_Easy:
                jotto_number_of_letters_correct_Easy += 1
            if 'x' in jotto_guess_list_Easy and 'x' in jotto_word_picked_list_Easy:
                jotto_number_of_letters_correct_Easy += 1
            if 'y' in jotto_guess_list_Easy and 'y' in jotto_word_picked_list_Easy:
                jotto_number_of_letters_correct_Easy += 1
            if 'z' in jotto_guess_list_Easy and 'z' in jotto_word_picked_list_Easy:
                jotto_number_of_letters_correct_Easy += 1

            if jotto_guess_Easy == jotto_word_picked_Easy:
                jotto_guesses_count_Easy += 1
                jotto_print_CorrectEasy = f"CORRECT!!! == {jotto_guess_Easy} | {jotto_number_of_letters_correct_Easy} | {jotto_guesses_count_Easy} |"
                print(jotto_print_CorrectEasy)
                print("\nThe selected word was, " +
                      jotto_word_picked_Easy + "! Great Job!!!")
                guessed = True

            elif jotto_guess_Easy != guessed:
                jotto_guesses_count_Easy += 1
                jotto_print_GuessesEasy = f"{jotto_guess_Easy} | {jotto_number_of_letters_correct_Easy} | {jotto_guesses_count_Easy} |"
                print(jotto_print_GuessesEasy)
                jotto_guess_Easy = None
                break
