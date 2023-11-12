#!/usr/bin/python3
"""for Review class."""

from models.base_model import BaseModel


class Review(BaseModel):
	"""Class showing a Review."""
	place_id = ""
	user_id = ""
	text = ""
