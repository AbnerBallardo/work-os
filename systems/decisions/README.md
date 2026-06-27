# Decision Records

Version: v1.0

---

## Purpose

Store durable Work OS decisions that change system behavior, source boundaries, runtime packaging, governance mechanics, or operating rules.

---

## Admission Rules

Create a decision record only when a decision is:

* reusable,
* stable,
* structurally impactful,
* and generalizable across future Work OS maintenance.

Operational decisions stay in Work execution systems or corporate systems of record.

---

## Storage Rule

Use one file per durable decision.

Root folder:

```text
systems/decisions/
```

Use the root only for:

* `README.md`
* `Decision Record Template.md`

Use subfolders for decision records:

```text
systems/decisions/work/YYYY-MM-DD - Decision Title.md
```

---

## Routing

| Decision type | Destination |
|---|---|
| Work OS structure, source boundary, runtime architecture, or governance guardrail | `systems/decisions/work/` |
| Committee mechanics | Existing committee file first; create a decision record only if the change affects durable governance |
| Agent runtime behavior | Agent instruction file first; create a decision record only if the change affects source boundaries or reusable architecture |
| Work memory updates | `memory/work/Work - Memory.md` or a relevant case file |
| Temporary routing, task, or project decisions | Do not record unless they become durable governance |

Rule:

* Prefer the most durable existing authority file before creating a new decision record.
* Use a decision record when the decision explains why the system is structured a certain way.

---

## Template

Use `Decision Record Template.md`.
