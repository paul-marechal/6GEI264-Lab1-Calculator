# -*- coding: utf8 -*-
"""
The calculator's core functions
"""

from .calcZeroDivision import *

class Core:
	"""Core object
	Where all the magic happens
	"""

	HISTORY_LEN = 6
	FLOAT_PRECISION = 2
	CHARACTERS = "0.123456789+-*/()"

	# Object's initialization
	def __init__(this):
		this.reset()

	def reset(this):
		this.input = ""
		this.history = list("" for i in range(this.HISTORY_LEN))

	# Add character to input
	def press(this, char):
		if char in this.CHARACTERS:
			this.input += char

	# Clear the whole input
	def clearAll(this):
		this.input = ""

	# Clear character by character
	def clear(this):
		if len(this.input) > 0:
			this.input = this.input[:-1]

	# Adds an entry to the history
	def addToHistory(this, expr):
		this.history.append(expr)
		this.history = this.history[-this.HISTORY_LEN:]

	# Evaluate the input:
	def evalInput(this):
		result = this.evalExpression(this.input)
		this.clearAll()
		return result

	# Evaluate some expression
	def evalExpression(this, expr):

		# If nothing is entered, do nothing
		if expr.strip() == "": return ""

		# Evaluating the expr
		result = None
		try:
			result = round(eval(expr), this.FLOAT_PRECISION)
		except ZeroDivisionError:
			error = "ZERO DIVISION"
			ZeroDivision.Exception(33)
		except: # Lets say the syntax is alwways at fault
			error = "SYNTAX ERROR"


		# End of story
		if result is not None:
			this.addToHistory("%s = %s" % (expr, result))
		else:
			this.addToHistory("%s > %s" % (expr, error))
		return result
