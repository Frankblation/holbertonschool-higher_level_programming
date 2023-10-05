#!/usr/bin/python3
"""Rectangele that inherates base g"""
from base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """inherates class base g"""
    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
