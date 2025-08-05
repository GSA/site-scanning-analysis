


## Website Requests

[Download Link](https://raw.githubusercontent.com/GSA/site-scanning-analysis/refs/heads/main/reports/website-requests.csv)

Issues: 

- suspected meta redirect = redirect=TRUE and has a value in pageviews field
- SSL = primary scan status code of invalid_ssl_cert, ssl_protocol_error, ssl_version_cipher_mismatch
- 404 = 404_test=TRUE
- www-required = status_code = 4xx or 5xx (e.g. 399<x<600) AND www_status_code = 2xx
- www-forbidden = initial_domain and initial_base are the same value AND www_status_code = 4xx or 5xx AND status_code=2xx.
