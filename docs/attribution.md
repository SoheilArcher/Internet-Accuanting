# Traffic Attribution

Traffic attribution connects a subscriber to network activity over time.

## What The IBSng Sample Shows

The sample server is an IBSng-based accounting host.

Observed shape:

- PostgreSQL database named `IBSng`
- RADIUS listener on UDP `1812` and `1813`
- Apache UI under `/IBSng`
- Tables such as `users`, `normal_users`, `ras`, `ras_ports`, `connection_log`, and `connection_log_details`
- Large accounting history in `connection_log` and `connection_log_details`

Useful fields seen in RADIUS logs and IBSng tables:

- username
- user id
- NAS IP
- NAS identifier
- NAS port
- NAS port type
- called station id
- calling station id
- accounting session id
- station IP
- login time
- logout time
- success state

This is enough to know who connected, from where, through which NAS, and during which time range.

It is not enough by itself to know every destination the subscriber visited.

## Required Data Sources

### RADIUS Accounting

Required for:

- subscriber identity
- session id
- assigned IP
- NAS/router
- login and logout time
- traffic counters

Sources:

- FreeRADIUS
- IBSng import
- MikroTik RADIUS accounting
- PPPoE/Hotspot accounting

### NAT Logs

Required when subscribers share public IP addresses.

Required fields:

- timestamp
- private source IP
- private source port
- public source IP
- public source port
- protocol
- router/NAS id

Without NAT source port logs, a public IP lookup is unreliable in CGNAT environments.

### Flow Records

Required for destination reporting.

Supported future sources:

- NetFlow
- IPFIX
- sFlow
- MikroTik Traffic Flow
- firewall connection logs

Required fields:

- start time
- end time
- source IP
- source port
- destination IP
- destination port
- protocol
- bytes
- packets
- exporter/router id

### DNS Logs

Optional enrichment only.

DNS can help map destination IPs to domains, but it is not complete because of encrypted DNS, CDN sharing, browser cache, and application-level behavior.

### URL Reporting

DeltaSIB presents URL reporting as a module for seeing visited websites without forcing users through a proxy.

For our system, this should be implemented as traffic attribution rather than proxy interception:

- collect RADIUS sessions to identify the subscriber and assigned IP
- collect NAT mappings when public IPs are shared
- collect NetFlow/IPFIX/MikroTik Traffic Flow/firewall flow records
- enrich destination IPs with DNS observations where available
- keep all lookups audited and permission-controlled

The product should support reports by user, top destination, daily activity, NAS/router, and time range.

## Core Queries

### Subscriber Destinations

Input:

- subscriber id or username
- time range

Process:

1. Find RADIUS sessions overlapping the time range.
2. Get assigned IPs and session windows.
3. Match flow/NAT records inside each session window.
4. Enrich destination IPs with ASN, country, and optional DNS context.

Output:

- destination IP
- destination domain when known
- destination port
- protocol
- bytes
- packets
- first seen
- last seen
- public NAT endpoint if applicable
- NAS/router

### URL/Destination Report

Input:

- username, customer id, reseller id, NAS/router id, or IP
- time range
- optional destination/domain filter

Output:

- domain when known
- destination IP
- destination port
- protocol
- request or flow count
- upload/download bytes
- first seen
- last seen
- subscriber
- NAS/router
- confidence score

### Public Endpoint Lookup

Input:

- public IP
- public source port
- timestamp
- protocol

Process:

1. Match NAT mapping at timestamp.
2. Resolve private IP and port.
3. Match active RADIUS session for private IP.
4. Return subscriber, NAS, and session evidence.

Output:

- subscriber
- internal IP
- NAS/router
- session id
- confidence score
- evidence records

## Privacy and Compliance

Destination attribution is sensitive.

Baseline requirements:

- dedicated permission for attribution access
- immutable audit log for every lookup
- retention policy per data source
- official report snapshots
- masking for normal support users
- export watermarking

## SaaS Access Policy

In the SaaS/license model, licensed accounting buyers receive normal accounting, reseller, service, RADIUS session, and usage reports.

They must not receive destination-level subscriber reports by default.

Owner-only by default:

- visited destination reports
- URL reports
- public IP/port/time lookup
- NAT mapping lookup
- per-subscriber destination history
- destination enrichment exports

Tenant-visible by default:

- online sessions
- assigned IP
- NAS/router
- usage totals
- service traffic counters
- billing and renewal reports

Any exception must be an explicit license feature plus an audited owner policy decision.
