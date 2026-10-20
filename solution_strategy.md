# Programme Evidence Hub prototype solution strategy, v0.2.3

All programme details, scientific findings, and organisations are illustrative. No real company or programme data is included.

## Purpose

Demonstrate how a bounded programme and governance gate can be supported by a thin knowledge layer over mixed-format source artefacts, while keeping scientific judgement and decision ownership with named humans.

## Technical pattern

The prototype uses authoritative source artefacts, a Source Registry, terminology mappings, a versioned role policy, atomic evidence claims, retrieval traces and a role-specific programme overview. The application does not require source migration or comprehensive FAIR remediation before decision value can be tested.

## Governance pattern

`config/role_access_policy.json` is the canonical governance object. Evidence visibility requires an allowed scientific domain, an allowed classification and explicit role membership. Registry metadata remains discoverable, while the underlying artefact is gated where the role does not have permission. Decision approval remains human-only. This is a client-side policy simulation. The HTML includes all demonstration data and provides no server-enforced access control.

## Evaluation pattern

Golden questions are paired with an SME-defined expected evidence set and exact locators. The prototype reports recall, precision, omissions, false positives, citation correctness and human disposition separately. This avoids treating fluent output as evidence of decision quality.

## Pilot boundary

One illustrative antibody programme; one candidate-nomination gate; seven heterogeneous source artefacts; twenty-four evidence claims; four user roles; three deterministic suggestion rules; six golden evaluation questions.
