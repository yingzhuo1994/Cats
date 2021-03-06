"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    >>> ps = ['short', 'really long', 'tiny']
    >>> s = lambda p: len(p) <= 5
    >>> choose(ps, s, 0)
    'short'
    >>> choose(ps, s, 1)
    'tiny'
    >>> choose(ps, s, 2)
    ''
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    # END PROBLEM 1
    n = 0
    for s in paragraphs:
        if select(s):
            if n == k:
                return s
            n += 1
    return ''



def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    # END PROBLEM 2
    def check_topic(s):
        s1 = remove_punctuation(s)
        s2 = lower(s1).split()
        for w in topic:
            if w in s2:
                return True
        return False
    return check_topic

def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    >>> accuracy("12345", "12345") # Returns 100.0
    100.0
    >>> accuracy("a b c", "a b c")
    100.0
    >>> accuracy("a  b  c  d", "b  a  c  d")
    50.0
    >>> accuracy("a b", "c d e")
    0.0
    >>> accuracy("Cat", "cat") # the function is case-sensitive
    0.0
    >>> accuracy("a b c d", " a d ")
    25.0
    >>> accuracy("abc", " ")
    0.0
    >>> accuracy(" a b \tc" , "a b c") # Tabs don't count as words
    100.0
    >>> accuracy("abc", "")
    0.0
    >>> accuracy("cats.", "cats") # punctuation counts
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    # END PROBLEM 3
    cwords = 0
    a, b = len(typed_words), len(reference_words)
    for k in range(min(a, b)):
        if typed_words[k] == reference_words[k]:
            cwords += 1
    if a == 0:
        return 0.0
    return cwords/a*100


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    # END PROBLEM 4
    n = len(typed)
    return (n/5)/(elapsed/60)


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    >>> abs_diff = lambda w1, w2, limit: abs(len(w2) - len(w1))
    >>> autocorrect("cul", ["culture", "cult", "cultivate"], abs_diff, 10)
    'cult'
    >>> autocorrect("cul", ["culture", "cult", "cultivate"], abs_diff, 0)
    'cul'
    >>> autocorrect("wor", ["worry", "car", "part"], abs_diff, 10)
    'car'
    >>> first_diff = lambda w1, w2, limit: 1 if w1[0] != w2[0] else 0
    >>> autocorrect("wrod", ["word", "rod"], first_diff, 1)
    'word'
    >>> autocorrect("inside", ["idea", "inside"], first_diff, 0.5)
    'inside'
    >>> autocorrect("inside", ["idea", "insider"], first_diff, 0.5)
    'idea'
    >>> autocorrect("outside", ["idea", "insider"], first_diff, 0.5)
    'outside'
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    # END PROBLEM 5
    dic = {}
    for w in valid_words:
        if user_word == w:
            return w
        dic[w] = diff_function(user_word, w, limit)
    # print(dic)
    if min(dic.values()) <= limit:
        return min(dic, key=dic.get)
    else:
        return user_word



def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    # assert False, 'Remove this line'
    if start == goal:
        return 0
    elif limit == 0:
        return 1
    if len(start) == 0:
        return len(goal)
    if len(goal) == 0:
        return len(start)
    if start[0] == goal[0]:
        return shifty_shifts(start[1:], goal[1:], limit)
    else:
        return 1 + shifty_shifts(start[1:], goal[1:], limit-1)
    # END PROBLEM 6

def same_num(s, g):
    allz = []
    for k in range(len(s)):
        z = []
        for i in range(len(g)):
            try:
                if g[i] == s[k]:
                    k += 1
                    z.append(s[i])
            except:
                break
        allz.append(z)
    num = max([len(e) for e in allz])
    for e in allz:
        if len(e) == num:
            return e

def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL.
    >>> pawssible_patches('place', 'wreat', 100)
    5
    """
    # assert False, 'Remove this line'
    # print(start, goal, limit)
    if start == goal:
        return 0
    elif limit == 0:
        return 1

    if len(goal) == 0 or len(start) ==0: # Fill in the condition
        # BEGIN
        "*** YOUR CODE HERE ***"
        return max(len(goal), len(start))
        # END

    elif start[0] == goal[0]: # Feel free to remove or add additional cases
        # BEGIN substitute
        "*** YOUR CODE HERE ***"
        return pawssible_patches(start[1:], goal[1:], limit)
        # END

    else:
        "*** YOUR CODE HERE ***"
        add_diff =  pawssible_patches(start, goal[1:], limit - 1) + 1# Fill in these lines
        remove_diff = pawssible_patches(start[1:], goal, limit - 1) + 1
        substitute_diff = pawssible_patches(start[1:], goal[1:], limit - 1) + 1
        return min(add_diff, remove_diff, substitute_diff)

def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    # assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server.
    >>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
    >>> typed = ['I', 'have', 'begun']
    >>> prompt = ['I', 'have', 'begun', 'to', 'type']
    >>> print_progress({'id': 1, 'progress': 0.6})
    ID: 1 Progress: 0.6
    >>> report_progress(typed, prompt, 1, print_progress) # print_progress is called on the report
    ID: 1 Progress: 0.6
    0.6
    >>> report_progress(['I', 'begun'], prompt, 2, print_progress)
    ID: 2 Progress: 0.2
    0.2
    >>> report_progress(['I', 'hve', 'begun', 'to', 'type'], prompt, 3, print_progress)
    ID: 3 Progress: 0.2
    0.2
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    k = 0
    while k < len(typed) and typed[k] == prompt[k]:
        # print(typed[k], prompt[k])
        k +=1
    ratio = k / len(prompt)
    send({'id': user_id, 'progress': ratio})
    return ratio
    # END PROBLEM 8

# from doctest import *
# run_docstring_examples(report_progress, globals(), True)

def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    time_interval=[]
    for n in range(len(times_per_player)):
        t =[]
        for k in range(len(times_per_player[n])-1):
            t.append(times_per_player[n][k+1] - times_per_player[n][k])
        time_interval.append(t)
    return game(words, time_interval)
    # END PROBLEM 9

# p = [[1, 4, 6, 7], [0, 4, 6, 9]]
# words = ['This', 'is', 'fun']
# game = time_per_word(p, words)

def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    player_indices = range(len(all_times(game)))  # contains an *index* for each player
    word_indices = range(len(all_words(game)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    word_record=[]
    for _ in player_indices:
        word_record.append([])
    k = 0
    for words in all_words(game):
        for t in player_indices:
            n = t + 1
            while n < len(all_times(game)):
                if all_times(game)[t][k] > all_times(game)[n][k]:
                    break
                n += 1
            if n == len(all_times(game)):
                # print(words)
                word_record[t].append(words)
                break
        k += 1
    return word_record


    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)
