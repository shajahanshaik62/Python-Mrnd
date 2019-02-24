__author__ = 'Kalyan'

notes = '''
1. Read instructions for the function carefully and constraints carefully.
2. Try to generate all possible combinations of tests which exhaustively test the given constraints.
3. If behavior in certain cases is unclear, you can ask on the forums
'''
from placeholders import *

# Convert a sentence which has either or to only the first choice.
# e.g we could either go to a movie or a hotel -> we could go to a movie.
# note: do not use intermediate lists (string.split), only use string functions
# assume words are separated by a single space. you can use control flow statements
# So sentence is of form <blah> either <something> or <somethingelse> and gets converted to <blah> <something>
# if it is not of the correct form, you just return the original sentence.
def prune_either_or(sentence):
    if sentence == None:
        return  None
    if "either or" in sentence:
        return sentence
    if (" either " in sentence and " or " in sentence) and "either or" not in sentence:
        b = (sentence.replace("either ", ""))
        ser = b.find(" or")
        return (b[:ser])
    elif sentence == None:
        return None
    else:
        return sentence

def test_prune_either_or_student():
    assert "we could go to a movie" == prune_either_or("we could either go to a movie or a hotel")
    assert "i want shirt" == prune_either_or("i want either shirt or tshirt")
    assert "i have seen tajmahal" == prune_either_or("i have seen tajmahal")
    assert "we want chicken" == prune_either_or("we want either chicken or mutton")
    assert "either system or pc" == prune_either_or("either system or pc")
    assert "Two mythical cities eitheron and oregon" == prune_either_or("Two mythical cities eitheron and oregon")


# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_prune_either_or_server():
    servertests = pytest.importorskip("unit5_server_tests")
    servertests.test_prune_either_or(prune_either_or)
