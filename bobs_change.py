Python 3.3.5rc2 (v3.3.5rc2:ca5635efe090, Mar  2 2014, 14:20:24) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
>>> bobs_change(49)
sorry, bob,you don't have enough
>>> ================================ RESTART ================================
>>> 
>>> bobs_change(90)
40
>>> bobs_change(60)
10
>>> ================================ RESTART ================================
>>> 
>>> bobs_change(60)
10
>>> ================================ RESTART ================================
>>> 
>>> bobs_change (90)
40
>>> ================================ RESTART ================================
>>> 
>>> bobs_change(132)
82
>>> ================================ RESTART ================================
>>> 
>>> run_tests()
Trying:
    bobs_change(80)
Expecting:
    30
ok
Trying:
    bobs_change(132)
Expecting:
    82
ok
Trying:
    bobs_change(50)
Expecting:
    0
ok
Trying:
    bobs_change(40)
Expecting:
    Sorry Bob, you don't have enough
**********************************************************************
File "H:\computing\problems\p01.1\bobs_change.py", line 23, in __main__
Failed example:
    bobs_change(40)
Expected:
    Sorry Bob, you don't have enough
Got:
    sorry, bob,you don't have enough
2 items had no tests:
    __main__.bobs_change
    __main__.run_tests
**********************************************************************
1 items had failures:
   1 of   4 in __main__
4 tests in 3 items.
3 passed and 1 failed.
***Test Failed*** 1 failures.
>>> ================================ RESTART ================================
>>> 
>>> bobs_change(90)
40
>>> bobs_change(80)
30
>>> run_tests()
Trying:
    bobs_change(80)
Expecting:
    30
ok
Trying:
    bobs_change(132)
Expecting:
    82
ok
Trying:
    bobs_change(50)
Expecting:
    0
ok
Trying:
    bobs_change(40)
Expecting:
    Sorry Bob, you don't have enough
ok
2 items had no tests:
    __main__.bobs_change
    __main__.run_tests
1 items passed all tests:
   4 tests in __main__
4 tests in 3 items.
4 passed and 0 failed.
Test passed.
>>> 
