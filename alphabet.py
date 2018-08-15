#-*- encoding: utf-8 -*-
import sys
import string
import pdb
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

def is_hangul(ch):
  if len(ch) > 1: return False
  elif ch >= '가' and ch <= '힣': return True
  return False

def is_hanja(ch):
  if len(ch) > 1: return False
  elif ch >= '一' and ch <= '龥': return True
  return False

def is_punctuation(ch):
  if ch == ' ' or ch == ',' or ch == '"' or ch == '.' or ch == '-' or ch == "'" or ch == ";" or ch == "!" or ch == "?" or ch == "·":
   return True
  else:
   return False

def is_extended_punctuation(ch):
  if is_punctuation(ch) or ch == '“' or ch == u'：' or ch == u'？' or ch == '”' or ch == u'！' or ch == u'．' or \
     ch == u'，' or ch == u'《' or ch == u'》' or ch == '…' or ch == u'。' or ch == u'♪ ': 
     return True
  else:
     return False

def is_all_hanja(line):
  for ch in line:
    if is_hanja(ch) or is_num(ch) or is_extended_punctuation(ch):
      continue
    else:
      return False
  return True

def is_alphanum(ch):
  if is_num(ch) or is_alpha(ch):
    return True
  return False

def is_english(ch):
  if is_alphanum(ch) or is_punctuation(ch):
    return True
  return False

def is_num(ch):
  if ch >= '0' and ch <= '9':
    return True
  return False

def is_alpha(ch):
  if ch >= 'A' and ch <= 'Z':
    return True
  if ch >= 'a' and ch <= 'z':
    return True
  return False

def has_hangul(text):
  for ch in text:
    if is_hangul(ch):
      return True
  return False

def has_alpha(text):
  for ch in text:
    if is_alpha(ch):
      return True
  return False

def has_alphanum(text):
  for ch in text:
    if is_alphanum(ch):
      return True
  return False

def is_all_english(text):
  for ch in text:
    if not is_english(ch):
      return False
  return True

def has_hanja(text):
  for ch in text:
    if is_hanja(ch):
      return True
  return False

def len_hangul(text):
  len = 0
  for ch in text:
    if is_hangul(ch):
      len += 1
  return len

def len_alpha(text):
  len = 0
  for ch in text:
    if is_alpha(ch):
      len += 1
  return len

# write test code against regression
if __name__ == "__main__":
  print 'is_all_hanja(u"한자") ' + str(is_all_hanja(u"한자"))
  print 'is_all_hanja(u"中国话") ' + str(is_all_hanja(u"中国话"))
  print 'is_hanja(u"中国话한자") ' + str(is_hanja(u"中国话한자"))
