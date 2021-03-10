__version__ = '0.0.3'

from prettytable import PrettyTable
import random
import csv
from random import randint

WORD_FILE = 'tent-words.csv'

# fil   = open(WORD_FILE)

content = """throw out, to get rid of as a useless, My wife threw me out, Two and Half Men Pilot
lawsuit,An action brought in a court of law by one party against another,suits
bluffing, try to deceive someone as to one's abilities or intentions, He's bluffing, Two and Half Men Pilot
delinquents, tending to commit crime, particularly minor crime, Suits
insane, shocking, What is wrong with you? Are you insane?, Two and Half Men Pilot
Frosted, covered with or as if with frost, 370, Two and Half Men Pilot"""

# Not used
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