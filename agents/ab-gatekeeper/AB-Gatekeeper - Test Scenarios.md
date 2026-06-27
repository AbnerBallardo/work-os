# AB-Gatekeeper - Test Scenarios

Version: v1.1  
Owner: VP Technology / Acting CIO  
Status: Pilot test pack  
Applies To: AB-Gatekeeper validation before team rollout  
Runtime Sources:

* [AB-Gatekeeper - Agent Instructions.md](AB-Gatekeeper%20-%20Agent%20Instructions.md)
* [AB-Gatekeeper - Project Context Register.md](AB-Gatekeeper%20-%20Project%20Context%20Register.md)

Design Reference: [AB-Gatekeeper - Copilot Agent Vision.md](AB-Gatekeeper%20-%20Copilot%20Agent%20Vision.md)

---

## 1. Purpose

Validate that AB-Gatekeeper behaves correctly before broad team usage.

The test pack checks:

* Intent classification
* C-level classification
* TC routing
* Subject keyword consistency
* Spanish / English output
* Email body structure
* Word-ready committee brief format
* Output compression and length control
* Special-case validation
* Do-not-send behavior

---

## 2. Pass Criteria

The agent passes pilot validation when:

| Metric | Minimum Target |
|---|---:|
| Subject format accuracy | 90% |
| Correct intent classification | 85% |
| Correct C-level classification | 85% |
| Correct TC routing | 85% |
| Correct language handling | 95% |
| Word Paste Mode compliance for full committee briefs | 90% |
| Full committee brief length within one-page target | 90% |
| Special-case mandatory field detection | 100% |
| Do-not-send detection for empty updates | 80% |

Special-case approval scenarios must pass before the agent is used for real approval emails.

---

## 3. Test Scenario Format

For each test, capture:

```text
Scenario ID:
Input:
Expected output type:
Expected format mode:
Expected subject:
Expected language:
Expected C-level:
Expected TC routing:
Expected special-case rule:
Pass / fail:
Notes:
```

---

## 4. Scenario Pack

### T-001 - C1 Delivery Delta in Spanish

Input:

```text
Prepara correo para Abner. Ya conoce el tema de Banca Movil. Solo quiero informar que la salida paso de viernes a lunes por una dependencia menor, sin impacto al cliente. Necesito que este enterado.
```

Expected:

| Field | Expected |
|---|---|
| Output type | Email |
| Language | Spanish |
| Subject | ABG &#124; FYI &#124; C1 &#124; DELIVERY &#124; Banca Movil - Cambio de fecha sin impacto al cliente |
| C-level | `C1` |
| TC routing | `TC0` |
| Special case | None |

---

### T-002 - C2 Architecture Decision in English

Input:

```text
Prepare this in English. We need Abner to approve the recommended architecture option for the interoperability latency remediation. There are two options: tune current flow or redesign the integration boundary. Recommendation is redesign because tuning does not solve structural scaling.
```

Expected:

| Field | Expected |
|---|---|
| Output type | Email |
| Language | English |
| Subject | ABG &#124; DECISION &#124; C2 &#124; ARCH &#124; Interoperability - Approve latency remediation option |
| C-level | `C2` |
| TC routing | `TC2` |
| Special case | None |

---

### T-003 - C3 New Initiative

Input:

```text
Preparar correo para Abner sobre una nueva iniciativa de tokenizacion que nunca hemos revisado con el. Necesitamos su aprobacion para iniciar discovery.
```

Expected:

| Field | Expected |
|---|---|
| Output type | Email |
| Language | Spanish |
| Subject | ABG &#124; DECISION &#124; C3 &#124; ENG &#124; Tokenizacion - Aprobar inicio de discovery |
| C-level | `C3` |
| TC routing | `TC1` or `TC2` depending on cross-domain impact |
| Special case | None |

---

### T-004 - Do Not Send Empty FYI

Input:

```text
Prepara correo para decirle a Abner que seguimos trabajando en el analisis y no hay cambios ni riesgos nuevos.
```

Expected:

| Field | Expected |
|---|---|
| Output type | Do-not-send recommendation |
| Language | Spanish |
| Reason | No change in decision, action, awareness, risk, ownership, timeline, or escalation path |
| Alternative | Convert to short async update only if sender insists |

---

### T-005 - TRA Approval Missing URL

Input:

```text
Prepara correo para pedir aprobacion de TRA-123. Lo reviso Maria de Seguridad. Necesitamos aprobacion antes del viernes.
```

Expected:

| Field | Expected |
|---|---|
| Output type | Clarification request |
| Language | Spanish |
| Subject | Not finalized |
| C-level | `C2` |
| TC routing | `TC1` unless material risk / cross-domain |
| Special case | `SC-001` |
| Missing field | TRA document URL |

---

### T-006 - TRA Approval Complete

Input:

```text
Prepara correo para Abner. Solicitud: aprobar TRA-123 para el proyecto Pagos. URL: https://contoso.sharepoint.com/sites/security/TRA-123. Lo reviso Maria Perez de Seguridad y esta conforme. Se necesita aprobacion antes del viernes para continuar con salida a produccion.
```

Expected:

| Field | Expected |
|---|---|
| Output type | Approval email |
| Language | Spanish |
| Subject | ABG &#124; DECISION &#124; C2 &#124; SEC &#124; TRA-123 - Aprobar evaluacion de riesgo para Pagos |
| C-level | `C2` |
| TC routing | `TC1` unless material exposure |
| Special case | `SC-001` |
| Required CC | Maria Perez / Security reviewer |

---

### T-007 - Vulnerability Extension Missing Mitigation

Input:

```text
Necesito correo para pedir aprobacion de extension de vulnerabilidad CVE-2026-1234 en Plataforma X. Critica. Fecha actual vence manana, nueva fecha propuesta 15 de junio. Lo reviso Seguridad.
```

Expected:

| Field | Expected |
|---|---|
| Output type | Clarification request |
| Language | Spanish |
| C-level | `C3` because critical severity |
| TC routing | `TC2` or `TC3` depending exposure |
| Special case | `SC-002` |
| Missing fields | Security reviewer name, reason for extension, compensating controls / interim mitigation, remediation owner |

---

### T-008 - Vulnerability Extension Complete

Input:

```text
Draft in English. Request Abner approval to extend remediation for CVE-2026-1234 and scanner finding VULN-889 on Core Payments. Severity high. Current deadline May 30, requested new deadline June 14. Reason: vendor patch dependency. Interim mitigation: WAF rule deployed and enhanced monitoring enabled. Remediation owner: Juan Lopez. Security reviewer: Ana Torres, reviewed and agreed on May 24.
```

Expected:

| Field | Expected |
|---|---|
| Output type | Approval email |
| Language | English |
| Subject | ABG &#124; DECISION &#124; C2 &#124; SEC/PROD &#124; Vulnerabilities - Approve remediation deadline extension for Core Payments |
| C-level | `C2` |
| TC routing | `TC1` or `TC2` depending materiality |
| Special case | `SC-002` |
| Required CC | Ana Torres / Security reviewer |

---

### T-009 - Production Risk

Input:

```text
Preparar correo. Hay incremento de errores en mobile despues del release. Impacto todavia bajo, SRE esta revisando. Necesito que Abner sepa y apruebe activar war room si sube el impacto.
```

Expected:

| Field | Expected |
|---|---|
| Output type | Risk / blocked email |
| Language | Spanish |
| Subject | ABG &#124; RISK &#124; C1 &#124; PROD/SRE &#124; Mobile - Incremento de errores post-release |
| C-level | `C1` |
| TC routing | `TC1`; increase if material impact |
| Special case | None |

---

### T-010 - Committee Triage

Input:

```text
Tenemos conflicto entre Data, Engineering y Delivery por la secuencia de una entrega regulatoria. Nadie puede resolverlo localmente. Necesitamos decision de priorizacion.
```

Expected:

| Field | Expected |
|---|---|
| Output type | Technology Committee triage |
| Language | Spanish |
| C-level | `C2` |
| TC routing | `TC2` |
| Full brief required | Yes, after acceptance |

---

### T-011 - Information Only Committee Candidate

Input:

```text
Quiero llevar al comite un update de avance del proyecto porque completamos el 60% del plan.
```

Expected:

| Field | Expected |
|---|---|
| Output type | Redirect / convert to async |
| Language | Spanish |
| C-level | `C1` or `C2` depending project |
| TC routing | `TC0` |
| Full brief required | No |

---

### T-012 - Mixed Language Notes, Spanish Default

Input:

```text
Need email para Abner. The blocker is vendor capacity, pero el correo puede ser en espanol. Necesitamos que escale con proveedor porque el equipo local ya no puede resolver.
```

Expected:

| Field | Expected |
|---|---|
| Output type | Email |
| Language | Spanish |
| Subject | ABG &#124; ESCALATION &#124; C2 &#124; VENDOR &#124; [Project] - Escalar capacidad del proveedor |
| C-level | `C2` |
| TC routing | `TC2` if cross-domain / material |

---

### T-013 - Accepted Committee Brief in Word Paste Mode

Input:

```text
El topic ya fue aceptado para Technology Committee como TC2. Preparar brief en espanol para copiar a Word.

Tema: secuencia de entrega regulatoria entre Data, Engineering y Delivery.
Decision requerida: priorizar estabilizacion de datos regulatorios antes de dos entregas de producto.
Por que importa: si no se prioriza, el reporte regulatorio de junio queda en riesgo y los equipos seguiran compitiendo por la misma capacidad.
Recomendacion: priorizar el trabajo regulatorio por dos semanas y mover una entrega de producto al siguiente ciclo.
Alternativas: mantener plan actual o agregar capacidad temporal.
Riesgos: retraso de producto, agotamiento de capacidad, exposicion regulatoria.
Owner: Data Owner.
Deadline: decision esta semana.
```

Expected:

| Field | Expected |
|---|---|
| Output type | Full committee brief plus proposed decision-log entry |
| Format mode | Word Paste Mode |
| Language | Spanish |
| C-level | `C2` |
| TC routing | `TC2` |
| Full brief required | Yes, already accepted |
| Length | One-page target; maximum 900 words |
| Formatting | No Markdown tables, code fences, HTML, bold, italics, heading marks, or decorative separators |
| Compression | Maximum two alternatives, three trade-offs, and three risks / constraints |

---

## 5. Pilot Review Log

| Scenario ID | Pass / Fail | Issue Found | Fix Required | Retest Date |
|---|---|---|---|---|
| T-001 |  |  |  |  |
| T-002 |  |  |  |  |
| T-003 |  |  |  |  |
| T-004 |  |  |  |  |
| T-005 |  |  |  |  |
| T-006 |  |  |  |  |
| T-007 |  |  |  |  |
| T-008 |  |  |  |  |
| T-009 |  |  |  |  |
| T-010 |  |  |  |  |
| T-011 |  |  |  |  |
| T-012 |  |  |  |  |
| T-013 |  |  |  |  |
