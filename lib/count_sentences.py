#!/usr/bin/env python3
import re

class MyString:
  def __init__(self,value=''):
    if isinstance(value, str):
      self._value = value
    else:
      print("The value must be a string.")

  @property
  def value(self):
    return self._value

  @value.setter
  def value(self,new_value):
    if isinstance(new_value,str):
      self._value = new_value
    else:
      print("The value must be a string.")

  def is_sentence(self):
    if self._value.endswith("."):
      return True
    else:
      return False

  def is_question(self):
    if self._value.endswith("?"):
      return True
    else:
      return False
  
  def is_exclamation(self):
    if self._value.endswith("!"):
      return True
    else:
      return False

  def count_sentences(self):
    sentences = re.split(r'[.!?]', self._value)
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    return len(sentences)