# Copyright (c) 2025, dox buisness and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class DoxSettings(Document):
	pass

@frappe.whitelist()
def update_settings(doc,method=None):
	settings_mapping = {
		"System Settings": {
			"system_language": "language",
			"date_format": "date_format",
			"time_format": "time_format",
			"number_format": "number_format",
			"first_day_of_the_week": "first_day_of_the_week",
			"float_precision": "float_precision",
			"currency_precision": "currency_precision",
			"rounding_method": "rounding_method",
			"apply_strict_user_permissions": "apply_strict_user_permissions",
			"enable_two_factor_auth": "enable_two_factor_auth",
			"allow_login_using_mobile_number": "allow_login_using_mobile_number",
			"allow_login_using_user_name": "allow_login_using_user_name",
			"email_footer_address": "email_footer_address",
			"welcome_email_template": "welcome_email_template",
			"reset_password_template": "reset_password_template",
			"backup_limit": "backup_limit",
			
		},
		"Global Defaults": {
			"default_currency": "default_currency",
			"hide_currency_symbol": "hide_currency_symbol",
			"disable_rounded_total": "disable_rounded_total",
			"disable_in_words": "disable_in_words",
		},
		"Accounts Settings": {
			"unlink_advance_payment_on_cancellation_of_order": "unlink_advance_payment_on_cancelation_of_order",
			"allow_multi_currency_invoices_for_the_same_party": "allow_multi_currency_invoices_against_single_party_account",
			"delete_ledger_entries_on_transaction_deletion": "delete_linked_ledger_entries",
			"book_deferred_entries_based_on": "book_deferred_entries_based_on",
			"submit_journal_entries": "submit_journal_entries",
			"auto_process_deferred_accounting_entries": "automatically_process_deferred_accounting_entry",
			"create_journal_entry_for_deferred_entries": "book_deferred_entries_via_journal_entry",
			"auto_reconcile_payments": "auto_reconcile_payments",
			"overbilling_allowance": "over_billing_allowance",
			"role_for_overbilling": "role_allowed_to_over_bill",
			"role_to_bypass_credit_limit": "credit_controller",
			"accounts_frozen_till_date": "acc_frozen_upto",
			"ignore_closing_balances": "ignore_account_closing_balance",
			"role_allow_to_edit_frozen_accounts_and_entries": "frozen_accounts_modifier",
			"auto_book_asset_depreciation": "book_asset_depreciation_entry_automatically",
		},
		"Selling Settings": {
			"customer_naming_by": "cust_master_name",
			"default_sales_price_list": "selling_price_list",
			"consistent_pricing_during_sales_cycle": "maintain_same_sales_rate",
			"validate_price_against_purchasevaluation_rates": "validate_selling_price",
			"allow_negative_item_rates": "allow_negative_rates_for_items",
			"allow_editing_of_price_list_rates_in_transactions": "editable_price_list_rate",
			"calculate_bundle_price_from_its_item_rates": "editable_bundle_item_rates",
			"repeat_items_multiple_times_in_a_transaction": "auto_reconcile_payments",
			"no_reservation_on_sales_returns": "over_billing_allowance",
			"sales_order_creation_for_expired_quotations": "role_allowed_to_over_bill",
			"enable_discount_accounting": "credit_controller",
		},
		"Buying Settings": {
			"supplier_naming_style": "cust_master_name",
			"default_purchase_price_list": "selling_price_list",
			"action_for_price_inconsistencies": "maintain_same_sales_rate",
			"override_stop_action_role": "validate_selling_price",
			"consistent_pricing_during_purchase_cycle": "allow_negative_rates_for_items",
			"billing_for_rejected_quantities": "editable_price_list_rate",
			"use_transaction_date_exchange_rate": "editable_bundle_item_rates",
			"repeat_item_multiple_times_in_purchase_transactions": "auto_reconcile_payments",
			"disable_last_purchase_rate": "over_billing_allowance",
		},
		"Stock Settings": {
			"item_naming_style": "item_naming_by",
			"allow_negative_stock": "allow_negative_stock",
			"default_valuation_method": "valuation_method",
			"show_barcode_field_in_transactions": "show_barcode_field",
			"enable_stock_reservations": "enable_stock_reservation",
			"enable_serialbatch_fields": "use_serial_batch_fields",
			"allow_partial_reservations": "allow_partial_reservation",
			"auto_reserve_serial_and_batch_numbers": "auto_reserve_stock_for_sales_order_on_purchase",
			"auto_material_request_on_reorder_level": "auto_indent",
			"email_notification_for_auto_material_requests": "reorder_email_notify",
			"stock_frozen_upto": "stock_frozen_upto",
			"freeze_older_stocks_days": "stock_frozen_upto_days",
			"role_for_backdated_transactions": "role_allowed_to_create_edit_back_dated_transactions",
		},
	}
	for doctype, field_map in settings_mapping.items():
		updates = {}
		for dox_field, target_field in field_map.items():
			value = doc.get(dox_field)
			if value is not None:
				updates[target_field] = value
        
		if updates:
			frappe.db.set_value(doctype, None, updates)
			frappe.db.commit()
    