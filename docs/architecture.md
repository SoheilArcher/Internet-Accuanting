# Architecture

## Product Shape

The platform has one accounting core and several service adapters.

The accounting core owns money, debt, wallet balance, invoices, payment records, and audit logs. Integrations such as Marzban or MikroTik should never be the source of truth for financial state.

Reference products such as DeltaSIB and IBSng are used only to identify required ISP accounting capabilities. The platform should not copy their UI, workflows, or monolithic architecture.

## SaaS and Licensing Model

The default product model is centralized SaaS with licensed operator tenants.

One platform owner operates the main system. Each buyer purchases an accounting license, usually for one year, and receives a tenant/operator workspace. The tenant manages their own customers, resellers, plans, payments, services, NAS devices, and integrations within that workspace.

The platform owner keeps global operational access for:

- license activation, suspension, renewal, and expiry
- support and troubleshooting
- platform-level reports
- audit and compliance review
- tenant configuration assistance
- backup and health monitoring

Tenant access is feature-gated by license. Most accounting and ISP features can be enabled for the tenant, but destination attribution is restricted.

## Feature Gate Rule

Normal licensed tenants must not see subscriber destination reports by default.

Allowed for tenants:

- customers
- resellers
- plans
- invoices
- payments
- wallets
- service lifecycle
- RADIUS sessions
- online users
- usage totals
- NAS and integration management
- reports that do not expose visited destinations

Owner-only by default:

- subscriber destination history
- URL reporting
- public IP/port/time attribution lookup
- NAT-to-subscriber forensic lookup
- destination enrichment reports

This separation must be enforced at the permission, API, query, and UI layers.

## Main Components

### API Service

FastAPI service that exposes admin, reseller, customer, and integration APIs.

Responsibilities:

- Authentication and session management
- Role-based access control
- CRUD workflows for customers, plans, services, invoices, payments
- Integration orchestration
- Audit logging
- Tenant isolation and license enforcement

### Database

PostgreSQL stores all business data.

Important rules:

- Financial records are append-friendly.
- Payment and ledger records should not be silently edited.
- Sensitive credentials must be encrypted or stored outside source code.
- All admin actions should produce audit records.

### Workers

Background workers handle slow or scheduled operations.

Examples:

- Service expiration checks
- Debt-based suspension
- Payment gateway callbacks
- Usage synchronization
- Notification delivery
- Integration retries

### Integration Adapters

Adapters isolate external systems from business logic.

Initial adapters:

- Marzban: VPN/proxy user provisioning and usage
- MikroTik: PPPoE/Hotspot/NAS workflows
- FreeRADIUS: authentication/accounting sessions
- Payment gateways: payment verification
- SMS/Telegram/Email: notifications

### Attribution Pipeline

The attribution pipeline answers operational questions such as:

- Which subscriber was using this IP and port at this exact time?
- Which destinations did a subscriber connect to during a time range?
- Which NAS/router handled the subscriber session?
- Which public NAT address and source port were used?

This cannot rely on accounting sessions alone. RADIUS/IBSng-style accounting tells us who was online, when, and which IP was assigned. Destination visibility requires at least one traffic source:

- NAT logs from router/firewall
- NetFlow/IPFIX/sFlow from routers
- MikroTik Traffic Flow
- Firewall connection logs
- Optional DNS logs for domain context

Recommended matching chain:

```text
subscriber -> radius_session -> assigned_ip + time_range -> nat_mapping/flow -> destination
```

If carrier-grade NAT is used, NAT source port logging is mandatory for reliable attribution.

Because destination attribution is sensitive, tenant users should only see high-level usage totals unless the platform owner grants a special policy exception.

## Panels

### Admin Panel

Full system control: accounting, customers, plans, resellers, services, reports, integrations, and security.

### Reseller Panel

Limited control over reseller-owned customers and services, based on credit and permissions.

### Customer Panel

Customer self-service: invoices, payments, active services, usage, tickets, and renewal.

## Security Baseline

- No root/password deployment assumptions.
- SSH key based deployment.
- Firewall enabled by default.
- Public services behind reverse proxy.
- Secrets outside Git.
- Audit all financial and provisioning actions.
- Treat traffic attribution as sensitive data with strict permissions, retention limits, and audit logs.
