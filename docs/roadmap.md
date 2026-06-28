# Roadmap

## Phase 1: Foundation

- Project structure
- FastAPI app
- PostgreSQL migrations
- Authentication
- Roles and permissions
- Audit logs
- Tenant model
- Platform owner model
- License model
- Feature gates

## Phase 2: Accounting Core

- Customers
- Wallets
- Ledger entries
- Invoices
- Payments
- Manual adjustments
- Basic reports
- Tenant isolation across all accounting records

## Phase 3: Service Management

- Plans
- Service lifecycle
- Expiration handling
- Suspend/resume workflows
- Usage snapshots

## Phase 4: Marzban Integration

- Marzban account setup
- User provisioning
- Subscription link storage
- Traffic and expiry sync
- Error handling and retries

## Phase 5: Reseller System

- Reseller login
- Credit management
- Custom prices
- Reseller-owned customers
- Reseller reports
- Reseller tree hierarchy
- Reseller credit packages
- Multi-level commission rules
- Separate reseller payment gateways
- Reseller sales access control
- Reseller ticket visibility
- Reseller settlement reports

## Phase 6: User Manager and Support

- Customer portal
- Service renewal by customer
- Wallet charge by customer
- Invoice payment by customer
- Ticket creation by customer
- Ticket reply workflow
- ISP support assignment
- SLA and support reports

## Phase 7: Network Integrations

- FreeRADIUS accounting
- MikroTik/NAS management
- Session tracking
- IP attribution

## Phase 8: Traffic Attribution

- RADIUS session ingestion
- IBSng import compatibility
- DeltaSIB-style URL reporting
- MikroTik Traffic Flow ingestion
- NAT log ingestion
- NetFlow/IPFIX collector design
- Subscriber destination report
- Top sites and daily URL reports
- Public IP/port/time lookup
- Retention and access policy
- Owner-only destination report enforcement

## Phase 9: SaaS Operations

- License purchase and activation
- One-year license renewal
- Tenant suspension on expiry
- Owner dashboard
- Tenant health report
- Audited owner access to tenant workspace
- Feature gates per license

## Phase 10: Automation and Notifications

- Renewal reminders
- Debt reminders
- Payment notifications
- Auto suspend/resume
- SMS/Telegram/Email providers

## Phase 11: Production Hardening

- Backup strategy
- Monitoring
- Rate limits
- Secret management
- Deployment playbooks
- Security review
