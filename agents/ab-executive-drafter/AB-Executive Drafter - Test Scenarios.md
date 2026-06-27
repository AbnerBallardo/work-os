# AB-Executive Drafter - Test Scenarios

Version: v1.2
Owner: VP Technology / Acting CIO
Status: Pilot test pack
Applies To: AB-Executive Drafter validation before team rollout
Runtime Sources:

* [AB-Executive Drafter - Agent Instructions.md](AB-Executive%20Drafter%20-%20Agent%20Instructions.md)
* [AB-Executive Drafter - Recipient Playbook.md](AB-Executive%20Drafter%20-%20Recipient%20Playbook.md)

---

## 1. Purpose

Validate that AB-Executive Drafter behaves correctly before broad team usage.

The test pack checks:

* Recipient selection
* Communication state classification
* Channel decision
* Internal `EXEC` subject format
* Clean visible subject format
* Visible subject excludes recipient names and internal tags
* Spanish / English output
* Recipient-specific framing
* Executive compression
* Technical-to-executive translation
* Abner review gate
* Do-not-send behavior
* Sensitive-context generalization
* Minimum thinking-input detection

---

## 2. Pass Criteria

The agent passes pilot validation when:

| Metric | Minimum Target |
|---|---:|
| Internal subject format accuracy | 90% |
| Visible subject quality | 90% |
| Visible subject excludes recipient names and internal tags | 100% |
| Correct recipient selection | 90% |
| Correct communication state classification | 85% |
| Correct channel recommendation | 85% |
| Correct language handling | 95% |
| Recipient-specific framing quality | 85% |
| Executive compression compliance | 90% |
| Abner review detection for high-exposure drafts | 90% |
| Do-not-send detection for weak or unsafe drafts | 80% |
| Sensitive-context generalization | 100% |
| Minimum thinking-input detection | 100% |

Sensitive-context and missing-input scenarios must pass before the agent is used for real stakeholder-facing drafts.

---

## 3. Test Scenario Format

For each test, capture:

```text
Scenario ID:
Input:
Expected output type:
Expected recipient:
Expected communication state:
Expected recommended channel:
Expected internal subject:
Expected visible subject:
Expected language:
Expected Abner review gate:
Expected send readiness:
Pass / fail:
Notes:
```

---

## 4. Scenario Pack

### TS-001 - Luis Alfredo Strategic Alignment

Input:

```text
Preparar un email para Luis Alfredo. Tema: necesitamos mantener la secuencia del programa Valinor aunque hay presion por adelantar entregables. Recomendacion: proteger la fase de estabilizacion y mostrar avance con el hito del viernes. Owner: Raul. Fecha: viernes.
```

Expected:

| Field | Expected |
|---|---|
| Output type | Email |
| Recipient | `LUIS` |
| Communication state | `ALIGN` |
| Recommended channel | `Email` |
| Language | Spanish |
| Internal subject | EXEC &#124; LUIS &#124; ALIGN &#124; Valinor - Confirm sequencing guardrail for Friday milestone |
| Visible subject | `Valinor - Mantener secuencia hasta el hito del viernes` |
| Required framing | Strategic implication, recommendation, guardrail, owner, next visible signal |
| Compression | Maximum 5 lines before the ask; one recommendation, owner, and date |
| Abner review gate | Not required unless additional exposure is present |
| Send readiness | `Ready` |

---

### TS-002 - Sebastian Visible Progress Inform

Input:

```text
Preparar un update informativo para Sebastian. Ya cerramos el primer hito de mejoras WIFI en edificios. No requiere accion de su lado. Proxima senal: reporte de cobertura el jueves. Owner: Infraestructura.
```

Expected:

| Field | Expected |
|---|---|
| Output type | Email |
| Recipient | `SEBASTIAN` |
| Communication state | `INFORM` |
| Recommended channel | `Email` |
| Language | Spanish |
| Internal subject | EXEC &#124; SEBASTIAN &#124; INFORM &#124; WIFI Improvements - Avance y proxima senal visible |
| Visible subject | `WIFI Improvements - Avance y proxima senal visible` |
| Required framing | Current status, business-facing impact, no action required, owner, next visible signal |
| Compression | Short status plus one next visible signal |
| Abner review gate | Not required |
| Send readiness | `Ready` |

---

### TS-003 - Technical Incident Notes to Sebastian

Input:

```text
Convertir estas notas tecnicas en email para Sebastian: hubo aumento de errores en mobile despues del release, causa probable en integracion, rollback parcial listo, SRE monitoreando, impacto acotado, proximo update 6pm, owner Victor.
```

Expected:

| Field | Expected |
|---|---|
| Output type | Email |
| Recipient | `SEBASTIAN` |
| Communication state | `INFORM` unless intervention is required |
| Recommended channel | `Email`; use `Call` if exposure or urgency is high |
| Language | Spanish |
| Internal subject | EXEC &#124; SEBASTIAN &#124; INFORM &#124; Mobile Banking - Contencion de errores post-release |
| Visible subject | `Mobile Banking - Contencion de errores post-release` |
| Required framing | Business / customer impact, containment, owner, next update |
| Removed detail | Deep technical cause and internal process detail |
| Abner review gate | Recommended if exposure is high |
| Send readiness | `Ready` or `Abner review recommended` |

---

### TS-004 - Luis Alfredo Regional Dependency Support

Input:

```text
Draft in English for Luis Alfredo. We need support to unblock a regional dependency for the Data Platform. Decision needed by Friday. Recommended path is to confirm the regional owner and sequence the local delivery after that dependency is explicit.
```

Expected:

| Field | Expected |
|---|---|
| Output type | Email or channel recommendation if facts are incomplete |
| Recipient | `LUIS` |
| Communication state | `ESCALATE` |
| Recommended channel | `Email` if framing is approved; `Call` if the regional dependency is sensitive |
| Language | English |
| Internal subject | EXEC &#124; LUIS &#124; ESCALATE &#124; Data Platform - Confirm regional dependency owner by Friday |
| Visible subject | `Data Platform - Confirm regional dependency owner by Friday` |
| Required framing | Structural implication, required support, date, trade-off, owner |
| Abner review gate | Recommended because it requests structural support |
| Send readiness | `Abner review recommended` |

---

### TS-005 - Weak Sebastian Update

Input:

```text
Revisar este email para Sebastian: "Hola, te cuento que seguimos revisando el tema con varias areas. Hay algunos puntos pendientes y luego te contamos mas."
```

Expected:

| Field | Expected |
|---|---|
| Output type | Do-not-send recommendation |
| Recipient | `SEBASTIAN` |
| Communication state | Not finalized |
| Recommended channel | `No communication` until useful signal exists |
| Language | Spanish |
| Internal subject | Not finalized |
| Visible subject | Not finalized |
| Reason | No clear change, owner, timeline, ask, or business relevance |
| Required correction | Add what changed, why it matters, what is being asked, owner, and next visible signal |
| Send readiness | `Do not send` |

---

### TS-006 - Joint Recipient Request

Input:

```text
Necesito un correo conjunto para Luis Alfredo y Sebastian sobre un retraso en una entrega visible. Hay impacto local, pero tambien necesitamos proteger la secuencia regional. Owner: Delivery. Nueva fecha: viernes.
```

Expected:

| Field | Expected |
|---|---|
| Output type | Joint recipient recommendation |
| Recipient | Recommend whether one joint message is appropriate |
| Communication state | `ALIGN` or `ESCALATE` depending severity |
| Recommended channel | `Email` only if one shared narrative is safe; otherwise `Call` or two tailored drafts |
| Language | Spanish |
| Internal subject | If joint is appropriate, EXEC &#124; LUIS/SEBASTIAN &#124; [State] &#124; [Topic] - [Ask or signal]; otherwise separate `LUIS` and `SEBASTIAN` subjects |
| Visible subject | Clean topic-first subject without `EXEC` tags |
| Required framing | Explain trade-off between strategic sequencing and local business visibility |
| Abner review gate | Recommended |
| Send readiness | `Abner review recommended` |

---

### TS-007 - Spanish Notes, English Output

Input:

```text
User asks for English output. Notas: Sebastian necesita saber que el incidente esta contenido, el impacto al cliente fue bajo, Victor es owner, siguiente actualizacion 6pm, no requiere accion de su lado.
```

Expected:

| Field | Expected |
|---|---|
| Output type | Email |
| Recipient | `SEBASTIAN` |
| Communication state | `INFORM` |
| Recommended channel | `Email` |
| Language | English |
| Internal subject | EXEC &#124; SEBASTIAN &#124; INFORM &#124; [Topic] - Containment and next update at 6pm |
| Visible subject | `[Topic] - Containment and next update at 6pm` |
| Required framing | Plain-language status, business impact, containment, owner, next update |
| Abner review gate | Not required unless exposure is high |
| Send readiness | `Ready` |

---

### TS-008 - Sensitive Internal Interpretation

Input:

```text
Preparar email para Luis Alfredo. Contexto: el area esta resistiendo el cambio y no quieren asumir responsabilidad. Necesitamos que Luis Alfredo intervenga para ordenar el tema. Decision antes del viernes. Owner: Abner.
```

Expected:

| Field | Expected |
|---|---|
| Output type | Channel recommendation plus corrected framing |
| Recipient | `LUIS` |
| Communication state | `ESCALATE` |
| Recommended channel | `Call` before email unless Abner has approved the written framing |
| Language | Spanish |
| Internal subject | EXEC &#124; LUIS &#124; ESCALATE &#124; [Topic] - Align decision rights before Friday |
| Visible subject | `[Topic] - Alinear derechos de decision antes del viernes` |
| Required framing | Generalize sensitive interpretation into decision rights, alignment, owner, timeline |
| Removed detail | Political labels and unverified attribution |
| Abner review gate | Recommended |
| Send readiness | `Abner review recommended` or `Do not send` if facts are unverified |

---

### TS-009 - Subject Only

Input:

```text
Crear solo un subject para un email a Sebastian. Tema: PLIN SLA, riesgo de incumplimiento, necesitamos visibilidad ejecutiva y proxima actualizacion manana.
```

Expected:

| Field | Expected |
|---|---|
| Output type | Subject only |
| Recipient | `SEBASTIAN` |
| Communication state | `INFORM` unless action is needed |
| Recommended channel | Not applicable |
| Language | Spanish visible subject; internal tags in English |
| Internal subject | EXEC &#124; SEBASTIAN &#124; INFORM &#124; PLIN SLA - Riesgo de incumplimiento y proxima actualizacion |
| Visible subject | `PLIN SLA - Riesgo de incumplimiento y proxima actualizacion` |
| Required output | `Internal subject:`, `Visible subject:`, and `Reason:` only |
| Send readiness | Not applicable |

---

### TS-010 - Wrong Recipient / No Stakeholder Relevance

Input:

```text
Preparar correo para Luis Alfredo sobre un update interno: el equipo termino una reunion de seguimiento, no hay decision, no hay riesgo, no hay cambio de fecha y no hay accion requerida.
```

Expected:

| Field | Expected |
|---|---|
| Output type | Do-not-send recommendation |
| Recipient | `LUIS` requested, but should challenge fit |
| Communication state | Not finalized |
| Recommended channel | `No communication` or internal team update |
| Language | Spanish |
| Internal subject | Not finalized |
| Visible subject | Not finalized |
| Reason | No decision-useful signal for Luis Alfredo |
| Required correction | Add a real decision, risk, owner, timeline, stakeholder implication, or keep it internal |
| Send readiness | `Do not send` |

---

### TS-011 - No-Email Channel Decision

Input:

```text
Necesito mandar un correo a Luis Alfredo y Sebastian. Hay tension entre areas, no esta claro quien decide, hay tres opciones posibles, y queremos que ambos se alineen hoy antes de comunicar nueva fecha.
```

Expected:

| Field | Expected |
|---|---|
| Output type | Channel recommendation |
| Recipient | `LUIS/SEBASTIAN` or separate pre-alignment audiences |
| Communication state | `ALIGN` |
| Recommended channel | `Call` or `Meeting`, not email |
| Language | Spanish |
| Internal subject | Optional only if a follow-up email is needed after alignment |
| Visible subject | Optional only if a follow-up email is needed after alignment |
| Reason | Multiple decisions, unclear decision rights, and active tension require synchronous alignment |
| Send readiness | `Do not send` until alignment occurs |

---

### TS-012 - Missing Thinking Inputs

Input:

```text
Preparar un email para Sebastian sobre el proyecto nuevo. Queremos que este enterado.
```

Expected:

| Field | Expected |
|---|---|
| Output type | Needs-inputs response |
| Recipient | `SEBASTIAN` |
| Communication state | Not finalized |
| Recommended channel | Not finalized |
| Language | Spanish |
| Internal subject | Not finalized |
| Visible subject | Not finalized |
| Required questions | What changed? Why does it matter? What is being asked? |
| Send readiness | `Needs inputs` |

---

### TS-013 - Compression Review

Input:

```text
Revisar este email para Luis Alfredo: contiene cinco parrafos de historia del proyecto, detalles tecnicos de integracion, tres recomendaciones posibles, dos owners y varias fechas tentativas. El mensaje real es que recomendamos mantener la secuencia actual hasta el hito del viernes. Owner: Raul.
```

Expected:

| Field | Expected |
|---|---|
| Output type | Review plus compressed corrected draft |
| Recipient | `LUIS` |
| Communication state | `ALIGN` |
| Recommended channel | `Email` if facts are complete |
| Language | Spanish |
| Internal subject | EXEC &#124; LUIS &#124; ALIGN &#124; [Topic] - Mantener secuencia hasta hito del viernes |
| Visible subject | `[Topic] - Mantener secuencia hasta hito del viernes` |
| Required correction | Reduce to one recommendation, one owner, one date, and maximum three bullets |
| Send readiness | `Ready` or `Needs inputs` if topic/date is incomplete |

---

## 5. Pilot Review Log

| Scenario ID | Pass / Fail | Issue Found | Fix Required | Retest Date |
|---|---|---|---|---|
| TS-001 |  |  |  |  |
| TS-002 |  |  |  |  |
| TS-003 |  |  |  |  |
| TS-004 |  |  |  |  |
| TS-005 |  |  |  |  |
| TS-006 |  |  |  |  |
| TS-007 |  |  |  |  |
| TS-008 |  |  |  |  |
| TS-009 |  |  |  |  |
| TS-010 |  |  |  |  |
| TS-011 |  |  |  |  |
| TS-012 |  |  |  |  |
| TS-013 |  |  |  |  |
