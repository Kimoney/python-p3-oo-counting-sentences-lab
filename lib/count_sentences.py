#!/usr/bin/env python3
import re

class MyString:

  def __init__(self, value=""):
    self.value = value

  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, value):
    if isinstance(value, str):
        self._value = value
    else:
      print("The value must be a string.")

  def is_sentence(self):
    if self.value.endswith("."):
      return True
    else:
      return False
    
  def is_question(self):
    if self.value.endswith("?"):
      return True
    else:
      return False
    
  def is_exclamation(self):
    if self.value.endswith("!"):
      return True
    else:
      return False
  
  def count_sentences(self):
    # use regular expression to split the sentences using a specifc pattern
    sentences = re.split(r'(?<=[.!?]) +', self.value)
    # remove empty strings from the list 
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    return len(sentences)
 

do = MyString("How comes... Eh!!!! Now this is crazy. People have to stop. Now!! Wow..")
print(do.value)
print(do.count_sentences())
  
