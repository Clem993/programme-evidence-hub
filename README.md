# Programme Evidence Hub Demonstrator

Version 0.2.3. An interactive demonstration of programme evidence, decision rationale, source provenance, and human review.

The dashboard uses a fictional antibody programme with seven illustrative source artefacts and 24 evidence claims. All programme details, scientific findings, and organisations are illustrative. No real company or programme data is included.

## Open the dashboard

Download the repository using **Code → Download ZIP**, extract it, and open **index.html** in your browser. The dashboard contains its styling, application logic, configuration, data, and downloadable source artefacts. It does not need a package installation, API key, database, or internet connection.

Alternatively, run the supplied local server from the repository folder:

```bash
python3 serve_demo.py
```

The server binds to the local computer and opens the dashboard in a browser. Stop it with Ctrl+C. The supplied macOS and Windows launchers open the HTML file directly.

## Included functionality

- Programme overview and Decision Workspace, with rationale, evidence, outstanding actions, and review records.
- Source Registry, with metadata, file checksums, owners, illustrative access policies, ingestion status, and terminology mappings.
- Evidence Explorer, with claim-level retrieval traces, source locations, ontology concepts, and human review status.
- Four role views, derived from the visible policy configuration.
- Signals and Suggestions, with ticket opening dates, due dates, days open, and resolution times.
- Golden-question evaluation, with expected and retrieved evidence, omissions, false positives, citation correctness, and human disposition.
- Handover exports, the architecture diagram, and the module-to-capability mapping.

See [DEMO_SCRIPT.md](DEMO_SCRIPT.md) for the demonstration sequence.

## Edit and rebuild

The repository includes editable source files alongside the generated dashboard. Python 3.9 or later is required to rebuild it; the build uses the Python standard library.

| File or folder | Purpose |
| --- | --- |
| `app.js` | Application behaviour, rendering, ticket logic, and browser state |
| `styles.css` | Dashboard styling |
| `src/index.template.html` | Page structure and build placeholders |
| `config/role_access_policy.json` | Canonical role policy |
| `data/programme_data.json` | Canonical illustrative programme and evidence data |
| `sources/` | Seven synthetic source artefacts |
| `src/embedded_resources.json` | Resources embedded in the dashboard |
| `schema/programme_evidence_schema.json` | Illustrative data schema |
| `tools/build.py` | Builds the HTML, YAML policy export, and file manifest |
| `index.html` | Generated, self-contained dashboard |

After editing the source files, rebuild and check the generated outputs:

```bash
python3 tools/build.py
python3 tools/build.py --check
```

Commit the edited source files and the regenerated `index.html`, `config/role_access_policy.yaml`, and `manifest.json` together. Direct edits to generated files are overwritten on the next build.

The build checks the seven source artefacts against their recorded SHA-256 checksums and byte counts. If a source changes, review it and update its registry record deliberately before rebuilding.

Ticket ages use calendar days and the browser's date. The initial ticket dates also appear in `DEFAULT_STATE` in `app.js`; update those defaults alongside the JSON data when changing the initial scenario. Saved browser state takes precedence. Use **Reset** to restore the current defaults.

## Demonstration boundaries

Role selection and source gating demonstrate policy behaviour within the browser. All embedded data can be inspected by someone who receives the HTML file; the role selector does not authenticate users or provide server-enforced access control.

Interactions are saved in that browser's local storage. Users have independent state, and there is no shared database or central audit log. Retrieval traces, evaluation cases, and suggested actions are predefined illustrative examples. No live retrieval service or language model is called.

This repository stores the demonstrator. Publishing a hosted website is a separate action and requires an appropriate audience and access configuration.

## Repository preparation

The repository includes a self-contained dashboard, editable source files, and a synthetic source pack. Downloadable data and policy exports match the active dashboard configuration, including ticket opening dates and policy version 1.0.1. The presentation uses a neutral visual identity, and document properties have been cleared. The application has independent browser state for this version.
