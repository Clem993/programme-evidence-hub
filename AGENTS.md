# Working on this demonstrator

Keep the scientific scenario illustrative. The source pack contains synthetic programme material; client discovery documents and statements of work do not belong in this repository.

Edit `app.js`, `styles.css`, `src/index.template.html`, and the canonical JSON files. Build with `python3 tools/build.py`, then check with `python3 tools/build.py --check`. Include regenerated files in the same commit. Preserve the ability to open `index.html` directly without network access.

Keep role simulation distinct from production authentication. The complete dataset is embedded in the downloadable HTML.

For ticket changes, check both the JSON data and `DEFAULT_STATE` in `app.js`. Browser state persists until Reset is used.

Validate changed behaviour with the relevant dashboard interaction. Do not add external services, credentials, dependencies, or public deployment as a side effect of a routine edit.
