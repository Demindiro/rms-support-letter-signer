# RMS Support letter signer

This is a simple website to sign the RMS support letter


## How it works

To add a signature, enter a (non-empty) name, an optional link and click
"Sign".

The signature is then stored in a SQL database and can be exported via
the `/export/` endpoint.


## Endpoints

- `/<lang>/`: The same page but in the given language. Defaults to English
  if empty.

- `/export/?after=date`: Returns a list of signatures in JSON format. If
  `after` is specified (which is an epoch or a date) only signatures after
  the given date are returned.
