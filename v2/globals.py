"""Seems to be required to get UnitRegistry to work across files"""
from pint import UnitRegistry, Quantity
unit = UnitRegistry()
Q = unit.Quantity
