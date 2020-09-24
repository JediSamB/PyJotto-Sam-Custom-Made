from termcolor import colored, cprint
import sys
from colorama import init, Fore, Back, Style
import click

click.echo(u'\u22F0', nl=False)
click.echo(u"\u22F1", nl=False)
click.echo(u'\u22F0', nl=False)
click.echo(u"\u22F1", nl=False)
click.echo(u'\u22F0', nl=False)
click.echo(u"\u22F1", nl=False)
click.echo(u'\u22F0', nl=False)
click.echo(u"\u22F1", nl=False)
click.echo(u'\u22F0', nl=False)
click.echo(u"\u22F1", nl=False)
click.echo(u'\u22F0', nl=False)
click.echo(u"\u22F1", nl=False)
click.echo(u'\u22F0', nl=False)
click.echo(u"\u22F1", nl=False)

print(Fore.CYAN)
init()
click.echo.text = colored('Hello Universes', 'blue', attrs=['blink', 'bold'])
print(click.echo.text)

print("Welcome To PyJotto Made By Samuel Joseph Bruckner!!! To play Multi Player Type, '/play multiplayer'!!! To play Single Player, just select your difficulty of, Easy, Medium Or Hard!!! Be sure to type / and then play lowercase and the difficulty's first letter Uppercase!!! Thank You!!!")
while True:
    jotto_which_game = input()
    if jotto_which_game == '/play multiplayer':
        import jotto_play_Multiplayer__
        break
    elif jotto_which_game == '/play Easy':
        import jotto_word_list_Easy
        break
    elif jotto_which_game == '/play Hard':
        import jotto_word_list_Hard
        break
    elif jotto_which_game == '/play Medium':
        import jotto_word_list_Medium
        break
    else:
        print("Please check that you typed everything exactly as it says you are supposed to!!!>")
