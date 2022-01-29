import click

from . import (
    utils,
    urban,
    google
)

@click.group()
@click.option('--index', '-i', 'index', type=bool, is_flag=True, help='search result index to display.')
@click.option('--google', '-g', 'goog', type=bool, is_flag=True, help='use google search instead.')
def urb(goog, index): #pylint: disable=unused-argument
    pass

@urb.command("define")
@click.option('--google', '-g', 'goog', type=bool, default=False, is_flag=True)
@click.option('--index', '-i', 'index', type=int, default=0, required=False)
@click.argument("word")
def define(word, goog, index):
    try:
        if goog:
            definition = google.define(word)
            utils.print_goog(definition[0], index)
        else:
            definition = urban.define(word)
            utils.print_urb(definition[:index + 1][-1])
    except IndexError:
        print('\nno definitions found for this word :(')

# @urb.command("greet")
# @click.option('--formal', '-f', 'formal', type=bool, default=False, is_flag=True)
# @click.argument('name')
# def greet(name: str, formal = False):
#     if formal:
#         click.echo(f"Goodbye {name}")
#     else:
#         click.echo(f"Bye {name}")

def main():
    urb(obj={})

if __name__ == "__main__":
    main()