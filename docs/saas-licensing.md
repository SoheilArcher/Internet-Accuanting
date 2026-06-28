# SaaS Licensing Model

## Goal

The platform is owned and operated centrally. A buyer purchases an accounting license, usually for one year, and receives access to a full accounting workspace.

The platform owner keeps global visibility and control. The buyer manages their own ISP/VPN accounting operations inside their tenant.

## Roles

### Platform Owner

The platform owner is the product operator.

Capabilities:

- create tenants
- issue licenses
- renew or suspend licenses
- see platform-wide reports
- access tenant workspaces for support
- inspect tenant health and usage
- manage feature gates
- manage backups and deployment health
- access sensitive attribution modules

### Tenant Operator

The buyer of the accounting license.

Capabilities:

- manage customers
- manage resellers
- manage plans and prices
- manage wallets, invoices, and payments
- manage services
- manage NAS/router/RADIUS integrations
- see online users
- see assigned IPs and usage totals
- run normal accounting and operational reports
- use customer and reseller panels

Restricted by default:

- destination/URL reports
- NAT forensic lookup
- public IP/port/time lookup
- per-subscriber visited destination history

### Reseller

A reseller belongs to one tenant and can manage only the customers, credit, services, and reports allowed by that tenant.

### Customer

A customer belongs to one tenant and can see only their own services, invoices, payments, tickets, and allowed usage summaries.

## License Lifecycle

1. Owner creates tenant.
2. Owner issues a license.
3. Tenant receives access for the license period.
4. System sends expiry reminders.
5. License can be renewed for another period.
6. If expired, tenant can be restricted or suspended.

Default period:

- 1 year

License states:

- draft
- active
- expiring
- expired
- suspended
- cancelled

## Feature Gates

Feature gates control what each tenant can use.

Examples:

- accounting_core
- reseller_panel
- customer_panel
- radius_accounting
- mikrotik_integration
- marzban_integration
- payment_gateways
- sms_notifications
- advanced_reports
- traffic_attribution_sessions
- traffic_attribution_destinations

Default rule:

`traffic_attribution_destinations` is disabled for tenants.

## Owner Access

The owner can access tenant data, but this access must be audited.

Each owner access event should record:

- owner user
- tenant
- reason
- start time
- end time
- actions performed
- exported reports

## Tenant Isolation

All tenant business data must be isolated by `tenant_id`.

Tenant users must never query another tenant's data. Platform owner users can query across tenants only through owner-scoped permissions and audited workflows.

## Destination Report Policy

The system may collect RADIUS, flow, NAT, and DNS data for technical and compliance reasons. However, normal tenant operators must not see destination-level subscriber activity.

Allowed tenant reports:

- online users
- session history
- assigned IPs
- total upload/download
- service usage
- billing usage
- NAS/router usage

Owner-only reports:

- visited destinations
- URL reporting
- destination domain/IP history
- public IP and port lookup
- NAT mapping to subscriber
- official attribution report exports

