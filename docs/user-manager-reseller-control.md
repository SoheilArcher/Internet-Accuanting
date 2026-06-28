# User Manager and Reseller Control

## Goal

The system must include a complete user-facing portal and a strong ISP management layer.

The buyer of the accounting license should be able to manage subscribers, resellers, sales, credit, commissions, tickets, and service charging without needing platform-owner access.

Destination/URL attribution remains owner-only by default.

## User Manager / Customer Portal

The User Manager is the subscriber portal.

Subscribers can:

- log in with username, password, mobile OTP, or portal token
- see active services
- see remaining traffic, time, speed, and expiry
- renew service
- charge wallet
- buy traffic add-on
- buy time add-on
- pay invoices
- download receipts
- see payment history
- open support tickets
- reply to tickets
- see ticket status
- change password when allowed
- view allowed usage summaries
- receive service information by SMS/Telegram/Email

Subscribers cannot:

- see destination/URL reports
- see NAT logs
- see other subscribers
- see reseller financial data
- access admin or owner reports

## ISP Manager

The ISP Manager is the tenant/operator admin panel.

The ISP manager can:

- create and edit subscribers
- charge subscriber wallet
- create invoices
- register manual payments
- suspend, resume, renew, and expire services
- see online users
- disconnect online sessions
- manage routers/NAS devices
- manage IP pools
- manage plans and prices
- manage tickets and support staff
- manage resellers
- assign sales access
- assign reseller pricing
- assign commission percentages
- set reseller credit limits
- control reseller customers
- view reseller sales reports
- view tenant revenue and invoices

The ISP manager cannot:

- manage platform licenses
- see other tenants
- use owner-only attribution reports
- change owner-controlled feature gates

## Reseller Manager

Resellers are sales operators inside one tenant.

Resellers can be organized in a tree:

```text
ISP Manager
  Reseller A
    Sub-reseller A1
    Sub-reseller A2
  Reseller B
```

Each reseller can have:

- credit balance
- credit limit
- custom plan price
- allowed plans
- allowed service classes
- allowed NAS/regions
- allowed customer count
- allowed active service count
- commission rules
- sales percentage
- payment gateway or bank account
- support visibility rules

## Reseller Sales and Commission

The ISP manager can define how each reseller earns money.

Supported models:

- fixed margin per plan
- percentage of sale
- multi-level commission
- charger commission
- supporter commission
- reseller commission
- parent reseller share
- minimum sale price
- custom reseller price list

Commission must be calculated from immutable payment or invoice events.

Each commission entry should include:

- tenant
- reseller
- customer
- invoice
- payment
- plan/service
- gross amount
- net amount
- commission type
- commission rate
- commission amount
- calculation time
- approval status

## Ticket Management

Ticket access should follow ownership.

Subscriber:

- creates tickets
- replies to own tickets
- sees ticket status

Reseller:

- sees tickets for owned customers when allowed
- replies when permission is granted
- escalates to ISP support

ISP manager:

- sees all tenant tickets
- assigns tickets to support staff
- changes priority and status
- replies and closes tickets
- sees SLA reports

Platform owner:

- can inspect tickets for support through audited owner access

## Required Panels

### Customer Portal

- Dashboard
- My Services
- Charge/Renew
- Invoices
- Payments
- Tickets
- Profile

### ISP Admin Panel

- Dashboard
- Users
- Add User
- Online Users
- Services
- Invoices
- Payments
- Resellers
- Reseller Commissions
- Tickets
- Routers/NAS
- Reports

### Reseller Panel

- Dashboard
- My Customers
- Add Customer
- Sales
- Credit
- Commissions
- Tickets
- Reports

## Key Product Rule

The licensed buyer receives complete operational control for their ISP business: users, reseller sales, credit, invoices, tickets, routers, and service management.

The only major feature withheld by default is subscriber destination visibility.

