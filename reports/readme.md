


## Website Requests

[Download Link](https://raw.githubusercontent.com/GSA/site-scanning-analysis/refs/heads/main/reports/website-requests.csv)

Issues: 

- suspected meta redirect = redirect=TRUE and has a value in pageviews field
- SSL = primary scan status code of invalid_ssl_cert, ssl_protocol_error, ssl_version_cipher_mismatch
- 404 = 404_test=TRUE
- www-required = status_code = 4xx or 5xx (e.g. 399<x<600) AND www_status_code = 2xx
- www-forbidden = initial_domain and initial_base are the same value AND www_status_code = 4xx or 5xx AND status_code=2xx.


## Report Legends 

#### USWDS
* Semantic version - count of uswds_semantic_version has a value (is not blank)
* v1.x - count of uswds_semantic_version begins with v1
* v2.x - count of uswds_semantic_version begins with v2
* v3.x - count of uswds_semantic_version begins with v3
* banner - count of uswds_banner_heres_how=TRUE
* usa-class - count of uswds_usa_class_list has a value (is not blank)



