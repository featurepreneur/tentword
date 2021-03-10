__version__ = '0.0.3'

from prettytable import PrettyTable
import random
import csv
from random import randint

WORD_FILE = 'tent-words.csv'

fil   = open(WORD_FILE)

content = """WORD,DEFINITION,TV-SHOW-Line, TV-Show-Details
throw out, to get rid of as a useless, My wife threw me out, Two and Half Men Pilot
stay over, stay overnight, Is she staying over?, Two and Half Men Pilot
rigid, -, Rigid, 
musky, -, Your brother. He has a very musky scent,
suffocating, -, I'm not that suffocating guy you threw out of the house,
renaissance, -, A rebirth. A renaissance if you will,
bluffs, -, He always pulls his ear when he bluffs,
inherently, -, Is there something inherently wrong with,"""

def _read_csv():

    global fil
    csv_f = csv.reader(fil)

    my_csv_word = list(csv_f)

    return my_csv_word

def _read_content_string():

    content_list = content.split('\n')

    return content_list

def _get_content_list():

    # _read_csv() # may be we will fix in the upcoming versions

    return _read_content_string() 


def _print_random_word_with_tv_show_line():

    word_table = PrettyTable(['Word', 'Meaning', 'TV-SHOW-Line', 'TV-Show-Details']) 

    content_list = _get_content_list()

    words_count = len(content_list) - 1

    p = random.randint(1, words_count)

    word            = content_list[p][0]
    meaning         = content_list[p][1]
    usage           = content_list[p][2]
    tv_show_details = content_list[p][3]

    word_table.add_row([word, meaning, usage, tv_show_details])

    # print(word_table)

    return word_table

def get_word():
    """Reverse the content

    :param url: content
    :type content: str
    :returns: Response int
    :rtype: int
    """
    return _print_random_word_with_tv_show_line()