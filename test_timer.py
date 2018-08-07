#!/usr/bin/env python
# encoding: utf-8


def test_timer():
    import time
    import timer
    with timer.Timer():
        time.sleep(1)

if __name__=='__main__':
    test_timer()
