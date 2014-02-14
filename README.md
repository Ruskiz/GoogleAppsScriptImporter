Google Apps Script Exporter/Importer
=====================================

# About
- Exporter: Export Google Apps Script information into local.
- Importer: Import local Google Apps Script into Google server(sync).

# Usage

```sh
# Exporter
$ python gas_export.py -b <OAuth2 Bearer> -f <File ID>

# Importer
$ python gas_import.py -b <OAuth2 Bearer> -f <File ID> -s <Script ID> -p <Script Local Path>
```
