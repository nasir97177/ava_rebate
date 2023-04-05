# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "ava_rebate"
app_title = "Ava Rebate"
app_publisher = "GreyCube Technologies"
app_description = "Customization for Customer Rebate Process for Ava"
app_icon = "octicon octicon-law"
app_color = "#95ddf5"
app_email = "admin@greycube.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ava_rebate/css/ava_rebate.css"
# app_include_js = "/assets/ava_rebate/js/ava_rebate.js"

# include js, css files in header of web template
# web_include_css = "/assets/ava_rebate/css/ava_rebate.css"
# web_include_js = "/assets/ava_rebate/js/ava_rebate.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
	"Sales Invoice" : "public/js/sales_invoice.js",
	"Sales Order" : "public/js/sales_order.js",
	"Delivery Note" : "public/js/delivery_note.js",
	"Customer" : "public/js/customer.js",
	}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "ava_rebate.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "ava_rebate.install.before_install"
# after_install = "ava_rebate.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ava_rebate.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"Payment Entry": {
# 		"before_validate": "ava_rebate.api.override_set_missing_values"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"ava_rebate.tasks.all"
# 	],
# 	"daily": [
# 		"ava_rebate.tasks.daily"
# 	],
# 	"hourly": [
# 		"ava_rebate.tasks.hourly"
# 	],
# 	"weekly": [
# 		"ava_rebate.tasks.weekly"
# 	]
# 	"monthly": [
# 		"ava_rebate.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "ava_rebate.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"erpnext.accounts.doctype.payment_entry.payment_entry.get_party_details": "ava_rebate.api.get_party_details"
# }

# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "ava_rebate.task.get_dashboard_data"
# }

# fixtures = ['Party Type']
# $ bench --site mysite export-fixtures
# This file will be automatically imported when the app is installed in a new site or updated via bench update.
