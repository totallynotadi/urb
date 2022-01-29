from typing import List
import os

import pyfiglet
from sklearn.manifold import trustworthiness

from .google import GoogleDefinition
from .urban import UrbanDefinition


def print_urb(definition: UrbanDefinition):
    print(pyfiglet.figlet_format(definition.word, font='cybermedium'))

    def format_def(_def):
        if any([str(i) in _def.strip()[:3] for i in range(10)]):
            _def = '• ' + _def.strip()[3:]
        return _def

    def format_eg(_eg):
        # print(_eg.strip())
        _eg = _eg.strip()
        truth = [str(i) in _eg.strip()[:3] for i in range(10)]
        if any(truth):
            truth_index = _eg.index(str(truth.index(True)))
            # print(truth_index)
            while _eg[truth_index] != ' ':
                truth_index += 1
            # print(truth_index)
            _eg = _eg[truth_index:].strip()
        # print(_eg)
        return _eg

    print(
        '\n'.join(
            list(
                map(
                    format_def, definition.definition.split('\n')
                )
            )
        )
    )
    # print(f"{definition.definition}")

    lines = definition.example.split('\n')
    if 'example' in lines[0].lower():
        definition.example = '\n'.join(lines[1:])
    print('\nexample ─\n')
    print(
        '\n'.join(
            map(
                format_eg, lines
            )
        )
    )
    # print(f"\nexample - \n\n{definition.example}")

    try:
        print(f"\nauthor - {definition.author} | 👍 {definition.thumbs_up} | 👎 {definition.thumbs_down}")
    except AttributeError:
        print(f"\nauthor - {definition.author} :)")


def print_goog(definition: GoogleDefinition, index: int = 0):
    print(pyfiglet.figlet_format(definition.word, font='cybermedium').strip(), '\n')
    
    if definition.phonetic is not None:
        print(definition.phonetic)

    if definition.origin is not None:
        print(f"\norigin - \n{definition.origin}\n")

    if index > len(definition.meanings):
        index = 0
    if index != 0:
        index += 1
        definition.meanings = [definition.meanings[:index - 1][-1]]
    for meaning in definition.meanings:
        print(meaning.part_of_speech)
        print((len(meaning.definition) + int((os.get_terminal_size().columns - len(meaning.definition)) / 2)) * "─")
        print(meaning.definition)
        if meaning.example is not None:
            print(meaning.example, "\n")
