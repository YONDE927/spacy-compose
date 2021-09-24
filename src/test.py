#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import spacy
import pandas as pd

nlp = spacy.load('ja_ginza')

txt = 'M1チップでSpacyが動きますように。' 

doc = nlp(txt)

def test_doc():
    assert doc.text == txt

def test_ginza1():
    assert doc[2] == 'チップ'

def test_ginza1():
    assert doc[2].dep_ == 'obl'  