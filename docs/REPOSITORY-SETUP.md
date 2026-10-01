# Put the package in a public repository

Cursor accepts a public Git repository link. The submission ZIP is a transport archive;
the ZIP itself is not the repository URL.

## Using GitHub in the browser

1. Extract `spycraft-cursor-submission-0.1.0.zip` into an empty folder.
2. Create a public repository, for example `spycraft-cursor-plugin`, under your chosen account or organization.
3. Upload the extracted contents, including the hidden `.cursor-plugin` directory.
   The manifest must appear as `.cursor-plugin/plugin.json` at repository root, not under a second enclosing folder.
   If your file picker does not expose hidden files, use Git as described below.
4. Confirm the repository root contains README.md, LICENSE, mcp.json, assets/, skills/, docs/, scripts/, and .cursor-plugin/.
5. Optional: add your real repository URL to the manifest's `repository` field. This field is optional in Cursor's schema.
6. Copy the public repository URL into the Cursor publisher application.

## Using Git

From the extracted folder, replace YOUR-OWNER and YOUR-REPO with your actual values:

```sh
git init -b main
git add .
git commit -m "Prepare Spycraft Cursor plugin v0.1.0"
git remote add origin https://github.com/YOUR-OWNER/YOUR-REPO.git
git push -u origin main
```

Create the empty public repository first. `git add .` includes the hidden manifest directory.
Use your usual GitHub authentication. Never add credentials to a remote URL or commit them.

## Check before submission

Run `python3 scripts/validate.py` from the extracted folder. Then perform the client smoke
tests in docs/SUBMISSION.md. Review the proposed MIT license and publisher/logo details.

Open https://cursor.com/marketplace/publish, sign in, and apply yourself. Use
`docs/LISTING-COPY.md` for copy-ready answers. The page observed while signed out required
sign-in for the publisher application; its signed-in fields have not been inspected.

Only the plugin package is included. Do not upload the Adden backend, environment files,
private reports, or the workspace's internal PROJECT-STATUS.md.
