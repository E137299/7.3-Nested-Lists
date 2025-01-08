from main import *

def test_update_list():
    assert update_list([['tooth paste', 'q-tips', 'milk'],['milk', 'candy', 'apples'],['planner', 'pencils', 'q-tips']], 1, 1, "peppers") == [['tooth paste', 'q-tips', 'milk'],['milk', 'peppers', 'apples'],['planner', 'pencils', 'q-tips']]
    assert update_list([['tooth paste', 'q-tips', 'milk'],['milk', 'candy', 'apples'],['planner', 'pencils', 'q-tips']], 0, 1, "floss") == [['tooth paste', 'floss', 'milk'],['milk', 'candy', 'apples'],['planner', 'pencils', 'q-tips']]

def test_view_list():
    assert view_list([['tooth paste', 'q-tips', 'milk'],['milk', 'candy', 'apples'],['planner', 'pencils', 'q-tips']],0) == ['tooth paste', 'q-tips', 'milk']
    assert view_list([["a","b","c"],["d","e","f"],["g","h","j"]],1) == ["d","e","f"]

def test_view_item():
    assert view_item([['tooth paste', 'q-tips', 'milk'],['milk', 'candy', 'apples'],['planner', 'pencils', 'q-tips']],2,0) == "planner"
    assert view_item([["a","b","c"],["d","e","f"],["g","h","j"]],1,0) == "d"

def test_all_in_one():
    assert all_in_one([['tooth paste', 'q-tips', 'milk'],['milk', 'candy', 'apples'],['planner', 'pencils', 'q-tips']]) == ['tooth paste', 'q-tips', 'milk', 'candy', 'apples','planner', 'pencils', 'q-tips']
    assert all_in_one([["a","b","c"],["d","e","f"],["g","h","j"]]) == ["a","b","c","d","e","f","g","h","j"]

def test_count_item():
    assert count_item([['tooth paste', 'q-tips', 'milk'],['milk', 'candy', 'apples'],['planner', 'pencils', 'q-tips']], "milk") == 2
    assert count_item([["a","b","c"],["d","e","f"],["g","h","j"]],"z") == 0

def test_drink_more_milk():
    assert drink_more_milk([['tooth paste', 'q-tips', 'milk'],['milk', 'candy', 'apples'],['planner', 'pencils', 'q-tips']]) == [['tooth paste', 'q-tips', 'milk'],['milk', 'candy', 'apples'],['planner', 'pencils', 'q-tips', 'milk']]
    assert drink_more_milk([["a","b","c"],["d","e","f"],["g","h","j"]]) == [["a","b","c","milk"],["d","e","f","milk"],["g","h","j","milk"]]

def test_add_a_cookie():
    assert if_add_a_cookie([['tooth paste', 'q-tips', 'milk'],['milk', 'candy', 'apples'],['planner', 'pencils', 'q-tips']]) == [['tooth paste', 'q-tips', 'milk and cookies'],['milk and cookies', 'candy', 'apples'],['planner', 'pencils', 'q-tips']]
    assert if_add_a_cookie([["a","b","c"],["d","e","f"],["g","h","j"]]) == [["a","b","c"],["d","e","f"],["g","h","j"]]

def test_reverse_lists_and_items():
    assert reverse_lists_and_items([['tooth paste', 'q-tips', 'milk'],['milk', 'candy', 'apples'],['planner', 'pencils', 'q-tips']]) == [['q-tips','pencils','planner'],['apples','candy','milk'],['milk','q-tips','tooth paste']]
    assert reverse_lists_and_items([["a","b","c"],["d","e","f"],["g","h","j"]]) == [["j","h","g"],["f","e","d"],["c","b","a"]]
