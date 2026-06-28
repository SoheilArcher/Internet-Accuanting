# API Outline

The API should be versioned from the beginning.

Base path:

```text
/api/v1
```

## Auth

- POST `/auth/login`
- POST `/auth/logout`
- GET `/auth/me`
- POST `/auth/change-password`

## Platform Owner

- GET `/owner/dashboard`
- GET `/owner/tenants`
- POST `/owner/tenants`
- GET `/owner/tenants/{id}`
- PATCH `/owner/tenants/{id}`
- GET `/owner/tenants/{id}/health`
- GET `/owner/tenants/{id}/reports`
- POST `/owner/tenants/{id}/impersonation-sessions`
- POST `/owner/tenants/{id}/feature-overrides`

## Licensing

- GET `/licenses`
- POST `/licenses`
- GET `/licenses/{id}`
- PATCH `/licenses/{id}`
- POST `/licenses/{id}/activate`
- POST `/licenses/{id}/renew`
- POST `/licenses/{id}/suspend`
- POST `/licenses/{id}/expire`
- GET `/licenses/{id}/features`
- PATCH `/licenses/{id}/features`

## Admin

- GET `/admin/dashboard`
- GET `/admin/audit-logs`
- GET `/admin/users`
- POST `/admin/users`
- PATCH `/admin/users/{id}`

## Customers

- GET `/customers`
- POST `/customers`
- GET `/customers/{id}`
- PATCH `/customers/{id}`
- GET `/customers/{id}/wallet`
- GET `/customers/{id}/services`
- GET `/customers/{id}/invoices`

## Customer Portal

- GET `/portal/dashboard`
- GET `/portal/services`
- POST `/portal/services/{id}/renew`
- POST `/portal/services/{id}/buy-traffic`
- POST `/portal/wallet/charge`
- GET `/portal/invoices`
- GET `/portal/payments`
- GET `/portal/tickets`
- POST `/portal/tickets`
- POST `/portal/tickets/{id}/messages`
- PATCH `/portal/profile`

## Plans

- GET `/plans`
- POST `/plans`
- PATCH `/plans/{id}`
- DELETE `/plans/{id}`

## Billing

- GET `/invoices`
- POST `/invoices`
- GET `/invoices/{id}`
- POST `/invoices/{id}/issue`
- POST `/invoices/{id}/void`
- GET `/payments`
- POST `/payments/manual`
- POST `/payments/gateway-callback/{gateway}`

## Services

- GET `/services`
- POST `/services`
- GET `/services/{id}`
- POST `/services/{id}/renew`
- POST `/services/{id}/suspend`
- POST `/services/{id}/resume`
- POST `/services/{id}/sync`

## Resellers

- GET `/resellers`
- POST `/resellers`
- GET `/resellers/{id}`
- PATCH `/resellers/{id}`
- GET `/resellers/{id}/customers`
- GET `/resellers/{id}/reports/sales`
- GET `/resellers/{id}/credit`
- POST `/resellers/{id}/credit-adjustments`
- GET `/resellers/{id}/price-rules`
- POST `/resellers/{id}/price-rules`
- GET `/resellers/{id}/commission-rules`
- POST `/resellers/{id}/commission-rules`
- GET `/resellers/{id}/allowed-plans`
- PATCH `/resellers/{id}/allowed-plans`
- GET `/resellers/{id}/tickets`

## Integrations

- GET `/integrations`
- POST `/integrations`
- POST `/integrations/{id}/test`
- POST `/integrations/{id}/sync`

## Attribution

- GET `/attribution/sessions`
- GET `/attribution/sessions/{id}`
- GET `/attribution/lookup-subscriber`
- GET `/attribution/lookup-public-endpoint`
- GET `/attribution/subscribers/{id}/destinations`
- GET `/attribution/url-report`
- GET `/attribution/top-destinations`
- GET `/attribution/daily-destinations`
- POST `/attribution/import/radius`
- POST `/attribution/import/nat`
- POST `/attribution/import/flows`
- POST `/attribution/reports`
- GET `/attribution/reports/{id}`

Access rule:

Tenant users can access session and usage reports only when they do not expose subscriber destinations. Destination, URL, NAT forensic, and public endpoint attribution APIs are owner-only by default.

## Support

- GET `/tickets`
- POST `/tickets`
- GET `/tickets/{id}`
- POST `/tickets/{id}/messages`
- POST `/tickets/{id}/close`

## Reseller Finance

- GET `/resellers/{id}/credit-packages`
- POST `/resellers/{id}/credit-purchases`
- GET `/resellers/{id}/commissions`
- POST `/resellers/{id}/commission-rules`
- GET `/resellers/{id}/gateway-accounts`
- POST `/resellers/{id}/gateway-accounts`
