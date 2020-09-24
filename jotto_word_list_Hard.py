import random
# Hard Word List

jotto_word_list_Hard = ['brick', 'jumpy', 'spitz', 'scuzz', 'japps',
                        'oxide', 'fjord', 'nymph', 'waltz', 'gucks'
                        'proxy', 'pixel', 'vozhd', 'treck', 'exact',
                        'vibex', 'xylem', 'quick', 'staph', 'xylem',
                        'apter', 'arete', 'eater', 'etape', 'pater',
                        'peart', 'perea', 'prate', 'taper', 'curse',
                        'belga', 'bilge', 'blade', 'calif', 'cebid',
                        'ceiba', 'clade', 'debag', 'ileac', 'jibed',
                        'gleba', 'kibla', 'gadje', 'hacek', 'fiche',
                        'laked', 'laich', 'laigh', 'flack', 'omens',
                        'coped', 'lingo', 'chiel', 'hadji', 'fable',
                        'filch', 'amort', 'amour', 'ampul', 'arums',
                        'arvos', 'larum', 'loams', 'loran', 'lotas',
                        'lovat', 'lumas', 'lunas', 'lunts', 'malts',
                        'marls', 'muons', 'muras', 'plans', 'plant',
                        'plasm', 'parvo', 'plats',  'plots', 'plums',
                        'polar', 'praos', 'prost', 'pruta', 'psalm',
                        'ovals', 'notal', 'notum', 'novas', 'nurls',
                        'poult', 'ramus', 'rants', 'salvo', 'solan',
                        'strop', 'strum', 'talus', 'tamps', 'sutra',
                        'tranq', 'tours', 'runts', 'taros', 'traps',
                        'supra', 'spals', 'jemmy', 'jemma', 'gemmy',
                        'strap', 'tarps', 'trona', 'turns', 'scala',
                        'ulnas', 'ulpan', 'ultra', 'ulvas', 'unapt',
                        'unarm', 'valor', 'vamps', 'ulnar', 'vapor',
                        'varus', 'vatus', 'vault', 'vaunt', 'volar',
                        'volta', 'volts', 'ulans', 'splat', 'sorta',
                        'soman', 'sault', 'savor', 'sonar', 'talon',
                        'slurp', 'solar', ]


jotto_word_picked_Hard = random.choice(jotto_word_list_Hard)
true_loop = True
jotto_guesses_count_Hard = 0
while true_loop == True:
    jotto_number_of_letters_correct_Hard = 0
    guessed = False
    while guessed != True:
        jotto_guess_Hard = input("Guess A Five letter Word\n")
        jotto_guess_list_Hard = list(jotto_guess_Hard)
        jotto_word_picked_list_Hard = list(jotto_word_picked_Hard)

        if list(jotto_guess_Hard) == int:
            print("No numbers are allowed you cheater lol jkjk")

        if len(jotto_guess_Hard) != 5:
            print("Your input can only be a max of 5 letters!! And also No less than five letters, Please, Just pick a valid and real five letter word!!! Thank You!")
            break
        else:
            if 'a' in jotto_guess_list_Hard and 'a' in jotto_word_picked_list_Hard:
                jotto_number_of_letters_correct_Hard += 1
            if 'b' in jotto_guess_list_Hard and 'b' in jotto_word_picked_list_Hard:
                jotto_number_of_letters_correct_Hard += 1
            if 'c' in jotto_guess_list_Hard and 'c' in jotto_word_picked_list_Hard:
                jotto_number_of_letters_correct_Hard += 1
            if 'd' in jotto_guess_list_Hard and 'd' in jotto_word_picked_list_Hard:
                jotto_number_of_letters_correct_Hard += 1
            if 'e' in jotto_guess_list_Hard and 'e' in jotto_word_picked_list_Hard:
                jotto_number_of_letters_correct_Hard += 1
            if 'f' in jotto_guess_list_Hard and 'f' in jotto_word_picked_list_Hard:
                jotto_number_of_letters_correct_Hard += 1
            if 'g' in jotto_guess_list_Hard and 'g' in jotto_word_picked_list_Hard:
                jotto_number_of_letters_correct_Hard += 1
            if 'h' in jotto_guess_list_Hard and 'h' in jotto_word_picked_list_Hard:
                jotto_number_of_letters_correct_Hard += 1
            if 'i' in jotto_guess_list_Hard and 'i' in jotto_word_picked_list_Hard:
                jotto_number_of_letters_correct_Hard += 1
            if 'j' in jotto_guess_list_Hard and 'j' in jotto_word_picked_list_Hard:
                jotto_number_of_letters_correct_Hard += 1
            if 'k' in jotto_guess_list_Hard and 'k' in jotto_word_picked_list_Hard:
                jotto_number_of_letters_correct_Hard += 1
            if 'l' in jotto_guess_list_Hard and 'l' in jotto_word_picked_list_Hard:
                jotto_number_of_letters_correct_Hard += 1
            if 'm' in jotto_guess_list_Hard and 'm' in jotto_word_picked_list_Hard:
                jotto_number_of_letters_correct_Hard += 1
            if 'n' in jotto_guess_list_Hard and 'n' in jotto_word_picked_list_Hard:
                jotto_number_of_letters_correct_Hard += 1
            if 'o' in jotto_guess_list_Hard and 'o' in jotto_word_picked_list_Hard:
                jotto_number_of_letters_correct_Hard += 1
            if 'p' in jotto_guess_list_Hard and 'p' in jotto_word_picked_list_Hard:
                jotto_number_of_letters_correct_Hard += 1
            if 'q' in jotto_guess_list_Hard and 'q' in jotto_word_picked_list_Hard:
                jotto_number_of_letters_correct_Hard += 1
            if 'r' in jotto_guess_list_Hard and 'r' in jotto_word_picked_list_Hard:
                jotto_number_of_letters_correct_Hard += 1
            if 's' in jotto_guess_list_Hard and 's' in jotto_word_picked_list_Hard:
                jotto_number_of_letters_correct_Hard += 1
            if 't' in jotto_guess_list_Hard and 't' in jotto_word_picked_list_Hard:
                jotto_number_of_letters_correct_Hard += 1
            if 'u' in jotto_guess_list_Hard and 'u' in jotto_word_picked_list_Hard:
                jotto_number_of_letters_correct_Hard += 1
            if 'v' in jotto_guess_list_Hard and 'v' in jotto_word_picked_list_Hard:
                jotto_number_of_letters_correct_Hard += 1
            if 'w' in jotto_guess_list_Hard and 'w' in jotto_word_picked_list_Hard:
                jotto_number_of_letters_correct_Hard += 1
            if 'x' in jotto_guess_list_Hard and 'x' in jotto_word_picked_list_Hard:
                jotto_number_of_letters_correct_Hard += 1
            if 'y' in jotto_guess_list_Hard and 'y' in jotto_word_picked_list_Hard:
                jotto_number_of_letters_correct_Hard += 1
            if 'z' in jotto_guess_list_Hard and 'z' in jotto_word_picked_list_Hard:
                jotto_number_of_letters_correct_Hard += 1

            if jotto_guess_Hard == jotto_word_picked_Hard:
                jotto_guesses_count_Hard += 1
                jotto_print_CorrectHard = f"CORRECT!!! == {jotto_guess_Hard} | {jotto_number_of_letters_correct_Hard} | {jotto_guesses_count_Hard} |"
                print(jotto_print_CorrectHard)
                print("\nThe selected word was, " +
                      jotto_word_picked_Hard + "! Great Job!!!")
                guessed = True

            elif jotto_guess_Hard != guessed:
                jotto_guesses_count_Hard += 1
                jotto_print_GuessesHard = f"{jotto_guess_Hard} | {jotto_number_of_letters_correct_Hard} | {jotto_guesses_count_Hard} |"
                print(jotto_print_GuessesHard)
                jotto_guess_Hard = None
                break
