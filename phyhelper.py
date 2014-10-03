#!/usr/bin/env python
#-*- coding: utf-8 -*-
from sympy import *
class ULM:
  ### Set up the known data ###
  # x => actual position
  # xo => original position
  # t => actual time
  # to => original time
  # v => speed
  def __init__ (self, x, xo, t, to, v):

    # Initializate variables
    self.xo = int(xo) if xo != "?" else Symbol('xo')
    self.x = int(x) if x != "?" else Symbol('x')
    self.to = int(to) if to != "?" else Symbol('to')
    self.t = int(t) if t != "?" else Symbol('t')
    self.v = int(v) if v != "?" else Symbol('v')

    # Set the position and speed equations
    self.position = Eq(self.x,self.v/(self.t-self.to))
    self.speed = Eq(self.v,(self.x-self.xo)/(self.t-self.to))

  # Solve the equation
  def find_values (self, what, second):
    # Try to solve the equation
    try:
      result = solve([self.position, self.speed], [what, second], dict=True)

      # Beautify the result
      fr = []
      for k in result:
        fr.append(k[what])
      return ", ".join(map(str,fr))
    except:
      return False

  def find_value (self, what):
    # Try it first with the position equation
    result = solve(self.position, what)
    if not result:
      # Now do it with the speed equation
      result = solve(self.speed, what)
    # Return
    return result

class UALM:
  ### Set up the known data ###
  # x => actual position
  # xo => original position
  # t => actual time
  # to => original time
  # v => actual speed
  # vo => original speed
  # a => acceleration
  def __init__ (self, x, xo, t, to, v, vo, a):
    self.x = x
    self.xo = xo
    self.t = t
    self.to = to
    self.v = v
    self.vo = vo
    self.a = a


print "Welcome to PhyHelper. I'm gonna ask you a few questions."
correct = False
while correct == False:
  kind = raw_input("Is the motion an uniform linear motion or an uniformly accelerated linear motion? (ULM/UALM): ")
  if kind == "ULM" or kind == "UALM":
    correct = True

print "I'm going to ask you for the variables of the motion. If a variable is unknown, just type '?'."
# If it's a ULM
if kind == "ULM":
  xo = raw_input("Value of the original position (integer/?) ")
  x = raw_input("Value of the current position (integer/?) ")
  to = raw_input("Value of the original time (integer/?) ")
  t = raw_input("Value of the current time (integer/?) ")
  v = raw_input("Value of the uniform speed (integer/?) ")
  
  # Create ULM
  u = ULM(x, xo, t, to, v)

  ccontinue = True
  # We are going to repeat this forever until it breaks
  while True:
    # What symbol do we want to find?
    sym = raw_input("Enter the symbol that you'd like to find (x, xo, t, to or v): ")
    # Find another symbol (any undefined one)
    cvars = dict(x=u.x, xo=u.xo, t=u.t, to=u.to, v=u.v)
    other = False
    for key, value in cvars.iteritems():
      if key == sym:
        # Oops, it's the one we're trying to find so let's skip it
        continue
      # Is it a symbol?
      if isinstance(value, Symbol):
        other = value
        break
      # No luck yet

  # Now other = another symbol that we can use
  # EXCEPTION: if there's no "other", it means there
  # are no more unknown values, so it's a normal equation and we
  # have to use u.find_value(u.something) instead, so we keep
  # other as False

  # Is "sym" a real symbol?
  symreal = False
  for key in cvars:
    if sym == key:
      symreal = True
  if not symreal:
    print "The symbol %s doesn't exist!" % sym
  else:
    if isinstance(cvars[sym], Symbol):
      R = u.find_values(cvars[sym], other) if other else u.find_value(cvars[sym])
      print "Values of %s: %s" % (sym, R)
    else:
      print "Value of %s: %s" % (sym, cvars[sym])

"""
    elif sym == "xo":
      if isinstance(u.xo, Symbol):
        R = u.find_values(u.xo, other) if other else u.find_value(u.xo)
        print "Values of xo: %s" % R
      else:
        print "Value of xo: %s" % u.xo
    elif sym == "t":
      if isinstance(u.t, Symbol):
        R = u.find_values(u.t, other)
        print "Values of t: %s" % R
      else:
        print "Value of t: %s" % u.t
    elif sym == "to":
      if isinstance(u.to, Symbol):
        R = u.find_values(u.to, other)
        print "Values of to: %s" % R
      else:
        print "Value of to: %s" % u.to
    elif sym == "v":
      if isinstance(u.v, Symbol):
        R = u.find_values(u.v, other)
        print "Values of v: %s" % R
      else:
        print "Value of v: %s" % u.v
    else:
      print "Unknown symbol!"

    # Continue?
    keep = raw_input("Find another symbol? (y/n) ")
    if keep == "n":
      break
"""

