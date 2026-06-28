# DeltaSIB Reference Notes

Source file: `C:\Users\Mr.Saeedi\Desktop\DeltaSIB.pdf`

The PDF is image-based and appears to be a Persian product brochure for DeltaSIB Accounting System. These notes extract product capabilities that are useful for our own comprehensive accounting platform.

Important: DeltaSIB is a market and feature reference, not a product design blueprint. We should learn from the capabilities, but the user experience, architecture, naming, workflows, and interface style must be designed independently.

## Positioning

DeltaSIB is presented as an ISP accounting system around RADIUS-based authentication, subscriber accounting, reseller management, reporting, and web-based administration.

## Capabilities To Consider

### Deployment and Access

- Linux server deployment
- Web-based admin and user panels
- Auto installer style setup
- Browser-based operation without special client software

### Network and Authentication

- RADIUS-centered authentication
- Router/NAS support, including MikroTik, Cisco, Huawei BRAS, and similar devices
- Authentication protocols such as PAP, CHAP, MS-CHAPv1, MS-CHAPv2
- MPPE support for PPP-style secure connections
- Active Directory integration
- Automatic user creation for Active Directory users on first connection

### Access Control

- Fine-grained admin permissions
- Reseller permissions with many configurable limits
- VISP-level access separation
- Restrict what each reseller can do, such as charging only, creating users only, or managing selected user data

### Subscriber Management

- User status history
- Custom user statuses
- Service lifecycle management
- Time-based connection restrictions by day and hour
- Static IP management
- Centralized IP management
- Static IP cost control
- Customer self-service registration
- Automatic username creation
- User notification by SMS

### Billing and Charging

- Credit balance management
- Online credit purchase
- Online service purchase and renewal
- Service change from user portal
- Expired or low-credit user redirection to renewal/payment pages
- Separation of base traffic from extra traffic/time
- Gift, installment, attachment, extra credit, IP, and other service tabs
- Promotional one-day services
- Smart discounts for marketing
- Separate send/receive accounting coefficients
- Per-destination or per-site traffic rating support through router features such as ISG

### Reseller and VISP

- Unlimited reseller/operator hierarchy
- Tree-structured reseller management
- VISP, reseller, center, service class, server, and user levels
- Reseller credit control
- Reseller internet credit packages
- Reseller self-service credit purchase
- Fixed profit margin packages
- Multi-level commission model:
  - charger commission
  - supporter commission
  - reseller commission
- Share percentage distribution through reseller tree
- Separate payment gateways or bank accounts per reseller

### Logging and Audit

- Change log per program section
- Admin/user activity tracing
- Follow-up logs for support and accountability

### Usage and Reports

- Hourly usage recording
- Hourly usage charts
- Online users
- Service usage reports
- Reseller sales reports
- URL reporting for visited sites
- URL reports by user, top site, and daily views

### URL Reporting

DeltaSIB describes a URL-Reporting module that reports websites visited by users.

Important product claims:

- Works without forcing traffic through a proxy
- Uses the user's own IP
- Avoids internet speed drop
- Can work with any number of routers/NAS devices
- Can be used across different cities or network segments

For our platform, this maps to the Traffic Attribution module. We should design it as a collector-based feature that ingests flow/NAT/DNS/router data instead of relying on proxy interception.

## Product Lessons

- Reseller hierarchy and commission logic are not optional for a serious ISP accounting system.
- URL/destination reporting must be designed as a first-class module from the beginning.
- The system should support several network service types, not only VPN.
- User self-service and payment redirection reduce operator workload.
- Change logs and permission boundaries are core accounting features, not extras.

## What Not To Copy

- Do not copy the old desktop-like tabbed UI.
- Do not copy screen layouts, visual style, naming, or interaction patterns.
- Do not make a clone of DeltaSIB workflows.
- Do not build URL reporting as a black-box feature; design it as a transparent attribution pipeline.
- Do not couple billing, RADIUS, reseller finance, and reporting into one monolithic module.

## How To Use This Reference

Use this document only as a checklist of market-proven ISP accounting capabilities. Each accepted capability should be redesigned for our platform as a modern, API-first, auditable module with clean admin, reseller, and customer experiences.
