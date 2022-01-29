import argparse

import googletrans
import pyfiglet

from ..urb import urban

# TO-DO
#
# tts lib combining pyttsx3 and gTTS (currently using pyttsx3)
# translate error handling when no internet (for urb api too)
#
# define
# random
# say
# translate
# translate and say (using options together)

parser = argparse.ArgumentParser()

parser.add_argument('term',
                    type=str,
                    help='the word to be searched')

parser.add_argument('-def', '--define',
                    help='get the definition for a word',
                    action='store_true')

parser.add_argument('-r', '--random',
                    help='feeling lucky? define a random word',
                    action='store_true')

parser.add_argument('-s', '--say',
                    help='listen to the pronounciation of a word',
                    action='store_true')

translation_group = parser.add_argument_group('translation', 'translate text among languages (can be customized using the helper args for this action)')
translation_group.add_argument('-t', '--translate',
                               help='translate a word to english',
                               action='store_true')

# translation halper args
translation_group.add_argument('from',
                               type=str,
                               help='specify the source language to translate from')

translation_group.add_argument('to',
                               type=str,
                               help='specify the destination language to translate to')

translation_group.add_argument('-d', '--detect',
                               type=str,
                               help='detect whichlanguge the term is in')

translation_group.add_argument('-l', '--list',
                               help='list all language codes for reference',
                               action='store_true',)

args = parser.parse_args()

GTRANS = googletrans.Translator()

def print_def(definition: urban.UrbanDefinition):
    print(pyfiglet.figlet_format(definition.word, font='cybermedium'))

    print(definition.definition)

    print(f"\nexample - \n{definition.example}")

    print(f"\nauthor - {definition.author} | 👍 {definition.thumbs_up} | 👎 {definition.thumbs_down}\n")

if args.translate:
    dest = None
    src = None
    if args.to is not None and args.to in list(googletrans.LANGUAGES.keys()) + list(googletrans.LANGCODES.keys()):
        dest = args.to
    else:
        dest='en'
    from_src = args.__dict__['from']
    if from_src is not None and from_src in list(googletrans.LANGUAGES.keys()) + list(googletrans.LANGCODES.keys()):
        dest = from_src
    else:
        src='auto'
    print(dest)
    print(src)
    result = GTRANS.translate(args.term, dest=dest, src=src)
    print(result.text)

if args.define:
    definitions = urban.define(args.term)
    if len(definitions) <= 0:
        print('urb: [define] no results found :(')
    else:
        print_def(definitions[0])

if args.random:
    definition = urban.random()
    print_def(definition)

if args.say:
    pass

def detect(text):
    lang = GTRANS.detect(text).lang
    return googletrans.LANGCODES[lang]
if args.detect:
    print(f"\nthis text is in {detect(args.term)}")
