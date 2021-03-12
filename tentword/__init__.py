__version__ = '0.0.5'

from prettytable import PrettyTable
import random
import csv
from random import randint

WORD_FILE = 'tent-words.csv'

# fil   = open(WORD_FILE)

content = """word ,definition,TV-SHOW-Line,TV-Show-Details
Bragging,excessively proud and boastful talk about one's achievements or possessions,Its not bragging if its true,Suits season 2 : sucker punch
Chaos,complete disorder and comfusion,Chaos isn’t a pit. Chaos is a ladder,Game Of Thrones season 3 : The Climb
Hustled,push roughly,Oh man I'm being hustled,Two and Half Men season-1 episode-2: BIG FLAPPY BASTARDS
chores,a routine task,she still counts on me to do a few chores,Two and Half Men season-1 episode-2: BIG FLAPPY BASTARDS
reconciliation,to restore to friendship or harmony,It leaves the door open for you know reconciliation,Two and Half Men season-1 episode-2: BIG FLAPPY BASTARDS
errand,a short trip to fulfill some small business,Jake I have to run a quick errand,Two and Half Men season-1 episode-2: BIG FLAPPY BASTARDS
nausea,sensation of unease and discomfort,Unfortunately the feeling is nausea,Two and Half Men season-1 episode-2: BIG FLAPPY BASTARDS
reciprocated,to give and take mutually,Unprompted but reciprocated by yours truly,Two and Half Men season-1 episode-2: BIG FLAPPY BASTARDS
crapping,rubbish,screaming crapping birds in his house,Two and Half Men season-1 episode-2: BIG FLAPPY BASTARDS
to lure,tempt (a person or animal) to do something,We're gonna throw the bait out the window to lure the birds out of the house,Two and Half Men season-1 episode-2: BIG FLAPPY BASTARDS
aviary,a large cage  building or enclosure for keeping birds in,I'll put it on the market,Two and Half Men season-1 episode-2: BIG FLAPPY BASTARDS"""


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

    p = random.randint(1, words_count-1)

    current_content = content_list[p]
    current_content_list = current_content.split(',')

    word            = current_content_list[0]
    meaning         = current_content_list[1]
    usage           = current_content_list[2]
    tv_show_details = current_content_list[3]

    word_table.add_row([word, meaning, usage, tv_show_details])

    # print(word_table)

    return word_table



def _get_random_word_with_tv_show_line():
    content_list = _get_content_list()
    words_count = len(content_list) - 1

    p = random.randint(1, words_count)

    current_content = content_list[p]
    current_content_list = current_content.split(',')
    info={
        "word":current_content_list[0],
        "meaning":current_content_list[1],
        "dialogue":current_content_list[2],
        "tv_show":current_content_list[3]
    }

   # print(word_table)

    return info   

def get_word():
    """Reverse the content

    :param url: content
    :type content: str
    :returns: Response int
    :rtype: int
    """
    return _get_random_word_with_tv_show_line()


def print_word():
    """Reverse the content

    :param url: content
    :type content: str
    :returns: Response int
    :rtype: int
    """
    print(_print_random_word_with_tv_show_line())
     
    