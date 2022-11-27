#!/usr/bin/env python3
# Priblizne reseni rovnice x = cos(x) pulenim intervalu

from math import cos

# Nastavime pozadovanou presnost
epsilon = 1e-10

# funkce x - cos(x) musi mit na krajich intervalu (xmin, xmax) opacna znamenka
xmin = 0
xmax = 1

while xmax - xmin > epsilon:
	xstred = (xmax + xmin)/2
	fxstred = xstred - cos(xstred)
	# Stale musime udrzovat opacna znamenka na krajich intervalu!
	if fxstred > 0:
		xmax = xstred
	else:
		xmin = xstred
print("Reseni rovnice je mezi ", xmin, " a ", xmax)
