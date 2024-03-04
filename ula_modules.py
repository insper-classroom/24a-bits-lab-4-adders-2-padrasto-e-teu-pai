#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

from myhdl import *


@block
def halfAdder(a, b, soma, carry):
    @always_comb
    def comb():
        soma.next = a ^ b
        carry.next = a and b
    return instances()


@block
def fullAdder(a, b, c, soma, carry):
    @always_comb
    def comb():
        carry.next = (a and b) or ((a ^ b) and c)
        soma.next = (a ^ b) ^ c

    return instances()


@block
def adder2bits(x, y, soma, carry):
    c = Signal(bool(0))
    h0 = halfAdder(x[0], y[0], soma[0], c )
    f0 = fullAdder(x[1], y[1], c, soma[1], carry)
    
    return instances()


@block
def adder(x, y, soma, carry):
    @always_comb
    def comb():
        pass

    return instances()
