# Copyright (c) 2025, Alwin Martis and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class TrackSale(Document):
	# begin: auto-generated types
	# ruff: noqa

	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amended_from: DF.Link | None
		from_date: DF.Date | None
	# ruff: noqa
	# end: auto-generated types


	pass
