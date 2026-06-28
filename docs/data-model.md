# Data Model

This is the first-pass domain model. It should evolve through migrations.

## Identity and Access

- users: login identity for admins, resellers, and customers
- roles: named permission groups
- permissions: granular actions
- user_roles: role assignment
- audit_logs: immutable operational history

## Tenancy and Licensing

- tenants: licensed operator workspaces
- tenant_domains: optional domains or hostnames for each tenant
- licenses: purchased license, start date, expiry date, status, plan, limits
- license_features: enabled/disabled feature flags per license
- tenant_owner_access: platform-owner access records and reason/audit metadata
- tenant_settings: branding, locale, currency, invoice settings, network defaults

Important rule:

Every business record must belong to a tenant unless it is explicitly platform-owned. Platform owner users can inspect tenants through audited owner access, but tenant users cannot cross tenant boundaries.

## Customers

- customers: profile, status, contact details, owner/reseller
- customer_contacts: phones, emails, messaging handles
- customer_documents: optional identity or contract files
- customer_notes: internal support and sales notes

## Resellers

- resellers: reseller profile linked to a user/customer identity
- reseller_credit_limits: credit rules and allowed debt
- reseller_price_rules: custom plan prices
- reseller_commissions: commission or profit calculation records

## Catalog

- plans: sellable service definitions
- plan_prices: time-based and reseller-specific prices
- plan_limits: traffic, duration, speed, device count
- add_ons: extra traffic, days, speed, static IP, support packages

## Accounting

- wallets: balance per customer/reseller
- ledger_entries: append-only financial movements
- invoices: issued bills
- invoice_items: line items for plans, add-ons, discounts, tax
- payments: received payments and gateway references
- refunds: refund records
- adjustments: manual corrections with required reason

## Services

- services: purchased service instance
- service_events: create, renew, suspend, resume, expire, delete
- service_usage_snapshots: periodic usage records
- service_credentials: external usernames or subscription identifiers

## Integrations

- integration_accounts: Marzban, MikroTik, FreeRADIUS, payment, SMS
- nodes: external service nodes and servers
- nas_devices: RADIUS/MikroTik NAS definitions
- provisioning_jobs: queued external actions and retry state
- external_mappings: local entity to external system ids

## Attribution

- radius_sessions: subscriber session start/stop, assigned IP, NAS, port, session id
- radius_session_attributes: raw RADIUS attributes for traceability
- nat_mappings: private source IP/port to public source IP/port over a time window
- flow_records: source, destination, ports, protocol, bytes, packets, timestamps
- dns_observations: optional subscriber or resolver DNS lookups
- url_report_entries: normalized destination report rows for user-facing reports
- destination_enrichment: ASN, country, organization, category, reputation
- attribution_queries: audited lookups performed by admins
- attribution_results: immutable result snapshots for official reports

Important rule:

RADIUS sessions identify the subscriber and assigned IP. NAT/flow records identify the destination. Both are required for reliable source-to-destination reporting.

Destination-level attribution records are platform-sensitive. They may be collected for all tenants, but normal tenant roles must not be able to query destination history unless a license feature and explicit owner policy allow it.

## Reseller Commission

- reseller_trees: parent/child reseller hierarchy
- reseller_credit_packages: reseller purchasable credit packages
- reseller_commission_rules: charger, supporter, and reseller commission percentages
- reseller_commission_entries: calculated commission per payment or sale
- reseller_gateway_accounts: payment gateway or bank account assignment per reseller

## Support

- tickets: support requests
- ticket_messages: conversation history
- notifications: messages sent or queued

## User Manager

- portal_sessions: customer portal sessions
- portal_tokens: temporary portal login or magic links
- wallet_charge_requests: customer wallet charge attempts
- service_renewal_requests: customer renewal attempts
- service_addon_purchases: traffic, time, speed, static IP add-ons
- customer_portal_audit_logs: customer self-service actions

## Reseller Control

- reseller_allowed_plans: plans each reseller can sell
- reseller_allowed_regions: NAS, node, or city restrictions
- reseller_limits: customer, service, debt, and credit limits
- reseller_sales_access: permission flags for sales and support actions
- reseller_price_lists: custom plan prices
- reseller_settlements: payable commission and settlement batches
