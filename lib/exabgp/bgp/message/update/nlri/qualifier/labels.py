# encoding: utf-8
"""
labels.py

Created by Thomas Mangin on 2012-07-08.
Copyright (c) 2009-2013 Exa Networks. All rights reserved.
"""

from struct import pack

# ======================================================================= Labels
# RFC 3107

class Labels (object):
	biggest = pow(2,20)

	def __init__ (self,labels):
		self.labels = labels
		packed = []
		for label in labels:
			# shift to 20 bits of the label to be at the top of three bytes and then truncate.
			packed.append(pack('!L',label << 4)[1:])
		# Mark the bottom of stack with the bit
		if packed:
			packed.pop()
			packed.append(pack('!L',(label << 4)|1)[1:])
		self.packed = ''.join(packed)
		self._len = len(self.packed)

	def pack (self):
		return self.packed

	def __len__ (self):
		return self._len

	def json (self):
		if self._len > 1:
			return '"label": [ %s ]' % ', '.join([str(_) for _ in self.labels])
		else:
			return ''

	def __str__ (self):
		if self._len > 1:
			return ' label [ %s ]' % ' '.join([str(_) for _ in self.labels])
		elif self._len == 1:
			return ' label %s' % self.labels[0]
		else:
			return ''

Labels.NOLABEL = Labels([])
