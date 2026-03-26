# Smoke Test — SecurityBI Forensic MCP (Cursor)

Casos reales verificados contra el scope **Local** (`https://test-securitybi-securitybi-forensic-api-ok.melioffice.com`).
Ejecutar en orden: cada sección es independiente, pero los IDs de transacción provienen de los resultados de los queries de usuario.

---

## Setup

Copiar la entrada `securitybi-forensic-test` de `cursor-mcp-config-example.json` al archivo `~/.cursor/mcp.json` (global) o `.cursor/mcp.json` (sólo este proyecto). No se necesita token: el dominio `melioffice.com` no requiere autenticación.

---

## Datos de referencia

| Producto | user_id | transaction_id | fecha |
|---|---|---|---|
| login | 184003413 | xB4P02IiXDgHGdPB | 2025-04-30 |
| recovery | 614553877 | 768YI6YLzFkIUrAB | 2025-11-14 |
| reauth | 3000735211 | b7e60af5-4df2-4dc3-863d-829fc90581c9 | 2025-11-18 |
| factors | 184003413 | 8FJhEBfYVpGwEs6u | 2026-02-19 |
| ito | 2600207067 | 2600207067+2025-11-25 | 2025-11-25 |
| screenlock | 1260076131 | d6828e16-4c03-4949-a5ce-1ed96ff24521-19a5678f7f6 | 2025-11-05 |
| asa | 105889189 | bc5e5791-e18e-4ac9-99c4-dfba24a85366 | 2025-11-19 |
| sessions | 184003413 | 977e7adf-f7bb-4473-8261-4bfec46d9ed6 | 2026-03-15 |

---

## LOGIN

### 1. Summary
**Prompt:** `Get the login summary for user 184003413`

**Resultado esperado:**
```
total_events: 39
latest_event_date: 2026-03-15
unique_devices: 3
active_days: 17
successful_logins: 33
```

---

### 2. Events by date
**Prompt:** `Get login events for user 184003413 on 2025-07-03`

**Resultado esperado:** 2 registros
```
TRACKING_ID: 5KK5cMXoKLw1y1Rv  FLAG_GRANTED_TX: 0  ATO_RISK: low  POLICY: 2FA-high
TRACKING_ID: psAD4SUX4DL23UGz  FLAG_GRANTED_TX: 0  ATO_RISK: low  POLICY: trusted_device
```

---

### 3. Events by range
**Prompt:** `Get login events for user 184003413 between 2025-01-01 and 2025-07-10`

**Resultado esperado:** `total_records: 33`

---

### 4. Events recent (last 180 days)
**Prompt:** `Get recent login events for user 184003413`

**Resultado esperado:** `total_records: 39`, registro más reciente `TX_DATE: 2026-03-15`

---

### 5. Transaction by ID
**Prompt:** `Get forensic details for login tracking xB4P02IiXDgHGdPB on 2025-04-30`

**Resultado esperado:**
```
cust_id: 184003413
flag_granted_tx: 0
ato_risk: low
authentication_policy: trusted_device
tracking_history: [challenge_creation_enter_password, user_identified_N/A, challenge_completion_email]
```

---

## RECOVERY

### 6. Summary
**Prompt:** `Get the recovery summary for user 614553877`

**Resultado esperado:**
```
total_events: 3
approved_transactions: 2
finished_transactions: 2
transactions_with_login_post_recovery: 2
```

---

### 7. Events by date
**Prompt:** `Get recovery attempts for user 614553877 on 2025-11-14`

**Resultado esperado:** 3 registros
```
[0] TRACKING: 768YI6YLzFkIUrAB  RESOLUTION: APPROVED  elapsed: 5 min
[1] TRACKING: hXJpk2JR4l1CkrDY  RESOLUTION: APPROVED  elapsed: 3 min
[2] TRACKING: pXZsMwowm3f73ZaU  FLAG_FINISHED: 0  (no terminó)
```

---

### 8. Transaction by ID
**Prompt:** `Get forensic details for recovery tracking 768YI6YLzFkIUrAB on 2025-11-14`

**Resultado esperado:**
```
recovery_type: AUTH_FACTOR
recovery_resolution: APPROVED
recovery_resolution_reason: APPROVED_BY_RECOVERY_SYNC
completed_elements: PHONE_VALIDATION
declined_elements: ENTER_PASSWORD, EMAIL_VALIDATION
risk_level: MEDIUM
```

---

## REAUTH

### 9. Summary
**Prompt:** `Get the reauth summary for user 3000735211`

**Resultado esperado:**
```
OPERATION_ID: change_email_bridge
RISK: MID
APPLIED_RULES: [LastReauthenticationRule]
SCORED: 1  OPEN: 1  CLOSED: 0
```

---

### 10. Events by date
**Prompt:** `Get reauth sessions for user 3000735211 on 2025-11-18`

**Resultado esperado:** 6 sesiones
```
[0] d802e741  change_email_bridge        REAUTH_COMPLETED  COMPLETED: SCREEN_LOCK, PHONE_VALIDATION
[1] b7e60af5  change_email_bridge        NOT_CLOSED        RULE: ReauthTokenRule
[2] 76467d4b  phone-validation-enroll    REAUTH_COMPLETED  RISK: HIGH
[3] f6d6530e  phone-validation-enroll    NOT_CLOSED        RULE: ReauthTokenRule
[4] d857d2fb  phone-validation-ajax      NOT_REQUIRED
[5] 44cf9c3e  change_account_limits      REAUTH_COMPLETED  RULE: RiskApiRule
```

---

### 11. Transaction by ID
**Prompt:** `Get forensic details for reauth b7e60af5-4df2-4dc3-863d-829fc90581c9 on 2025-11-18`

**Resultado esperado:**
```
REAUTH_STATUS: NOT_CLOSED
STATUS: CONTINUE
APPLIED_RULES: [ReauthTokenRule]
OPERATION_ID: change_email_bridge
DETACHED_ID: ef7d266c-be6a-493d-ac24-a3757668ec84
```

---

## FACTORS

### 12. Events by date (no_data esperado)
**Prompt:** `Get factors events for user 184003413 on 2025-09-12`

**Resultado esperado:** `no_data: true` — respuesta 200 sin error.

---

### 13. Events recent
**Prompt:** `Get recent factors events for user 184003413`

**Resultado esperado:** `total_records: 40`, recursos: `face`, `phone`, `qr-token`, `totp`

---

### 14. Transaction by ID
**Prompt:** `Get forensic details for factors match transaction 8FJhEBfYVpGwEs6u on 2026-02-19`

**Resultado esperado:**
```
event: start_match
resource: face
context_flow: login
result: success
face_declinable: true
pol_transaction_id: kSxPu7okNaJyXSyq
```

---

## ITO

### 15. Events by date
**Prompt:** `Get ITO transactions for user 2600207067 on 2025-11-25`

**Resultado esperado:**
```
INCOMING_ID: 2600207067+2025-11-25
LABEL: VERIFIED
TAG: RECHAZADO
KYC_ENTITY_TYPE: company
SIT_SITE_ID: CBT
```

---

### 16. Transaction by ID
**Prompt:** `Get forensic details for ITO incoming 2600207067+2025-11-25 on 2025-11-25`

**Resultado esperado:** mismo registro que el by_date. `total_records: 1`.

---

## SCREENLOCK

### 17. Summary
**Prompt:** `Get the screenlock summary for user 1260076131`

**Resultado esperado:**
```
OS_CONFIG: BIOM-FB-FACE
TOTAL: 10
TOTAL_SUCCESS: 8
SUCCESS_BIOMETRICS: 8
NOT_SUCCESS: 2
```

---

### 18. Events by date
**Prompt:** `Get screenlock events for user 1260076131 on 2025-11-05`

**Resultado esperado:**
```
ID: d6828e16-4c03-4949-a5ce-1ed96ff24521-19a5678f7f6
OS_CONFIG: PPP-NO-BIOM
METHOD_USED: PPP
RESULT: SUCCESS
DEVICE: XIAOMI 21051182G / ANDROID 13
FACETEC_STATUS: ENABLED
```

---

### 19. Events by range
**Prompt:** `Get screenlock events for user 1260076131 between 2025-10-01 and 2025-11-30`

**Resultado esperado:** `total_records: 10` — coincide exactamente con el TOTAL del summary.

---

### 20. Transaction by ID
**Prompt:** `Get forensic details for screenlock event d6828e16-4c03-4949-a5ce-1ed96ff24521-19a5678f7f6 on 2025-11-05`

**Resultado esperado:** incluye campo `EVENT_DATA` con JSON completo:
```
flow_id: app-screen-lock
elapsed_time: 9
fraud_data.has_risk: true
fraud_data.result: no_data
strategy_id: security_slogan_mla
enrollment_status: enabled
```

---

## ASA

### 21. Summary
**Prompt:** `Get the ASA summary for user 105889189`

**Resultado esperado:**
```
total_events: 1
latest_event_date: 2025-11-19
authorizations: 1
cases_created: 1
reports_submitted: 1
ato_confirmed: 1 (implícito en preventive_actions_applied: 1)
```

---

### 22. Events by date
**Prompt:** `Get ASA authorizations for user 105889189 on 2025-11-19`

**Resultado esperado:**
```
AUTHORIZATION_ID: bc5e5791-e18e-4ac9-99c4-dfba24a85366
ORIGIN: panic_button
REPORT_TYPE: ATO_COMPLAINT
ATO_CONFIRMED_FLG: 1
USER_ATO_PROFILE: MEDIUM
CASE_ID: 417301486
EXPERIENCE_TYPE: PIXSINGLETRANSFERMLB
USER_ALERT: TRANSFERS
```

---

### 23. Transaction by ID
**Prompt:** `Get forensic details for ASA authorization bc5e5791-e18e-4ac9-99c4-dfba24a85366 on 2025-11-19`

**Resultado esperado:** mismo registro que el by_date. `total_records: 1`.

---

## SESSIONS

### 24. Events by date
**Prompt:** `Get sessions for user 184003413 on 2026-03-15`

**Resultado esperado:**
```
DETACHED_ID: 977e7adf-f7bb-4473-8261-4bfec46d9ed6
TYPE: WEB
msl_tx: 4gNTIVETuJGAHVlw   ← correlaciona con login tracking
is_new_device: true
completed_elements: [email_validation]
ip: 179.41.154.182
```

---

### 25. Events by range
**Prompt:** `Get sessions for user 184003413 between 2026-03-01 and 2026-03-24`

**Resultado esperado:** 2 sesiones
```
[0] 1b0172bb  2026-03-11  DELETE_TYPE: DELETED-WEB  MOTIVE: device-browser-unsafe.devices-core
[1] 977e7adf  2026-03-15  activa (DATE_DELETED: null)
```

---

### 26. Transaction by ID
**Prompt:** `Get forensic details for session detached ID 977e7adf-f7bb-4473-8261-4bfec46d9ed6 on 2026-03-15`

**Resultado esperado:**
```
USER_ID: 184003413
authentication_reliability: SECURE
ato_planning_profile: applies
device_profile_session: armor.<fingerprint>
login_type: EXPLICIT
business_flow: login
```

---

## Tests de error esperado (capability negativa)

Estos tests aplican **solo si se deploya el branch `feature/reengineering-tools-quantity`** con las 5 tools genéricas consolidadas. En la versión deployada actual (31 tools product-específicas) no aplican.

### 27. Range no soportado — factors
**Prompt:** `Get factors events for user 184003413 between 2025-01-01 and 2025-12-31`

**Resultado esperado:** `ToolError: Product 'factors' does not support date range queries. Products that support this: login, recovery, reauth, screenlock, asa, sessions.`

---

### 28. Recent no soportado — ito
**Prompt:** `Get recent ITO transactions for user 2600207067`

**Resultado esperado:** `ToolError: Product 'ito' does not support last 180 days queries.`

---

### 29. Summary no soportado — sessions
**Prompt:** `Get the sessions summary for user 184003413`

**Resultado esperado:** `ToolError: Product 'sessions' does not support summary queries.`

---

## Cross-product verification

### 30. Correlación login ↔ sessions
**Prompt:** `For user 184003413: get the login summary, then get the session created on 2026-03-15 and confirm the detached_id and msl_tx match`

**Resultado esperado:**
- login `get_user_summary` → `latest_event_date: 2026-03-15`
- sessions `get_user_events_by_date` → `msl_tx: 4gNTIVETuJGAHVlw` = TRACKING_ID del login más reciente del summary
- Ambos comparten `DETACHED_ID: 977e7adf-...`

---

### 31. Correlación reauth ↔ recovery
**Prompt:** `For user 614553877 on 2025-11-14: show the recovery attempts, then check if there's reauth activity that day`

**Resultado esperado:**
- recovery `get_user_events_by_date` → 3 intentos, `COMPLETED_FACTORS: PHONE_VALIDATION`
- reauth `get_user_events_by_date` → `no_data: true` (el usuario hizo recovery directo, no reauth)
