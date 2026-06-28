# Comprehensive ISP Accounting Platform

An accounting and service-management platform for ISPs, VPN providers, resellers, and network operators.

This repository is the starting point for a full product, not just a Marzban wrapper. Marzban, MikroTik, FreeRADIUS, payment gateways, and notification channels are treated as integrations around a central accounting core.

Legacy products such as DeltaSIB and IBSng are treated as feature references only. This project should not become a clone of their interface, workflows, or architecture.

## Goals

- Manage customers, resellers, services, invoices, payments, wallets, and debts.
- Provision and suspend services across Marzban, MikroTik, and FreeRADIUS.
- Track usage, sessions, traffic, attribution, and service lifecycle events.
- Attribute subscriber activity by time, IP, NAS, NAT mapping, destination IP, port, protocol, ASN, and optional DNS context.
- Sell one-year accounting licenses to operators while keeping platform-owner oversight.
- Provide separate admin, reseller, and customer panels.
- Keep a clear audit trail for all financial and operational actions.

## Core Modules

- Accounting Core: ledgers, wallets, invoices, payments, adjustments, refunds.
- Customer Management: profiles, contacts, documents, tags, lifecycle state.
- Service Catalog: plans, packages, add-ons, pricing rules, discounts.
- Provisioning: Marzban, MikroTik, FreeRADIUS, node/server management.
- Attribution: RADIUS sessions, NAT logs, NetFlow/IPFIX, DNS logs, destination reports.
- Reseller System: credit limits, reseller pricing, commission, sub-customers.
- Reseller Finance: reseller credit packages, tree hierarchy, commission distribution, reseller gateways.
- Billing Automation: renewals, debt checks, suspension, reminders.
- Support: tickets, notes, customer communication history.
- Reporting: sales, revenue, debt, reseller performance, usage, active services.
- Security and Audit: roles, permissions, admin logs, API tokens.
- Licensing and Tenancy: one central platform, licensed operators, expiry, feature gates, owner oversight.
- User Manager: subscriber portal for charging, renewing, payments, and support tickets.
- ISP Manager: tenant admin tools for users, resellers, sales access, commissions, tickets, and routers.

## Tech Direction

- Backend: FastAPI
- Database: PostgreSQL
- Worker/Queue: Redis + background workers
- Frontend: Admin, reseller, and customer panels
- Deployment: Docker Compose first, Kubernetes later if needed

## Repository Layout

```text
apps/
  api/                  Backend API service
docs/
  architecture.md       System architecture
  data-model.md         Main entities and relationships
  api-outline.md        API surface
  roadmap.md            Delivery phases
infra/
  docker-compose.yml    Local development stack
```

## First Milestone

The first useful version should support:

- Platform owner dashboard
- Tenant/operator licensing
- One-year license activation and renewal
- Tenant feature gates
- Admin login and roles
- Customers
- Plans
- Wallets
- Invoices
- Payments
- Manual service creation
- Marzban integration
- RADIUS session tracking
- Traffic/NAT attribution data model
- Basic reseller panel
- Customer user manager
- Ticket creation and replies
- Reseller sales and commission control
- Audit logs

## Access Model

The platform owner keeps global access across licensed accounting instances for support, reporting, license control, and compliance. A buyer receives a tenant/operator account with nearly all accounting features.

Destination/URL attribution reports are excluded from normal buyer access by default. They remain owner-only unless explicitly enabled by policy.
