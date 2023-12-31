from . import __version__ as app_version

app_name = "med"
app_title = "Medical"
app_publisher = "worood"
app_description = "Medical App"
app_email = "worood.it@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/med/css/med.css"
app_include_js = "/assets/med/js/set_route.js"

# include js, css files in header of web template
# web_include_css = "/assets/med/css/med.css"
# web_include_js = "/assets/med/js/med.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "med/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
#doctype_js = {"Laboratory" : "public/js/laboratory.js",}
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

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "med.utils.jinja_methods",
#	"filters": "med.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "med.install.before_install"
# after_install = "med.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "med.uninstall.before_uninstall"
# after_uninstall = "med.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "med.utils.before_app_install"
# after_app_install = "med.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "med.utils.before_app_uninstall"
# after_app_uninstall = "med.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "med.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

"""doc_events = {
	"Laboratory": {
		"before_save": "med.hook.laboratory.before_save",
	},
	
}"""
doc_events = {
    "*": {
        "on_session_creation": "med.hook.analyst_role_redirection.redirect_analyst"
    }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"med.tasks.all"
#	],
#	"daily": [
#		"med.tasks.daily"
#	],
#	"hourly": [
#		"med.tasks.hourly"
#	],
#	"weekly": [
#		"med.tasks.weekly"
#	],
#	"monthly": [
#		"med.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "med.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "med.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "med.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["med.utils.before_request"]
# after_request = ["med.utils.after_request"]

# Job Events
# ----------
# before_job = ["med.utils.before_job"]
# after_job = ["med.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"med.auth.validate"
# ]

fixtures = [
    {
    	"dt": "Workspace",
    },
    {
        "dt": "Property Setter", "filters": [["module", "=", "Medical"]]
    },
    {
        "dt": "Dashboard Chart", "filters": [["module", "=", "Medical"]]
    },
    {
        "dt": "Number Card", "filters": [["module", "=", "Medical"]]
    },
    {
        "dt": "Custom Field", "filters": [["module", "=", "Medical"]]
    },
    


]

"""{
        "dt": "Workspace", "filters": [["module", "=", "Medical"]]
    },"""