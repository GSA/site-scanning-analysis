## Requests for Websites

## Invalid SSL 

* Websites [on this list](https://github.com/GSA/site-scanning-analysis/blob/main/reports/website-requests/invalid-ssl.csv) cannot be scanned because of an invalid SSL certificate.

## IPv6 

* Websites [on this list](https://github.com/GSA/site-scanning-analysis/blob/main/reports/website-requests/ipv6.csv) do not have the AAAA DNS record necessary to support IPv6.

## Media Type 

* Websites [on this list](https://github.com/GSA/site-scanning-analysis/blob/main/reports/website-requests/media_type.csv) do not report a media type (formerly known as MIME type), making analysis of the file that loads more difficult.  

## 20+ Third Party Services 

* Websites [on this list](https://github.com/GSA/site-scanning-analysis/blob/main/reports/website-requests/third-party-services.csv) trigger an unusually large number (20+) of third party services on page load, with possible performance and privacy implications.  

## Missing Viewport Tag

* Websites [on this list](https://github.com/GSA/site-scanning-analysis/blob/main/reports/website-requests/viewport.csv) do not have a viewport meta tag, resulting in mobile visitors seeing a version of the webpage intended for desktop visitors.  

## Required `www.`

* Websites [on this list](https://github.com/GSA/site-scanning-analysis/blob/main/reports/website-requests/www-required.csv) will only load if the www is included, resulting in a failed visitor experience if the `www.` is left off.

## Unsupported `www`

* Websites [on this list](https://github.com/GSA/site-scanning-analysis/blob/main/reports/website-requests/www-unsupported.csv) will not load if `www.` is included, resulting in a failed visitor experience if `www.` is included.  



----------------------

Details on the methodologies for these scans can be found [here](https://github.com/GSA/site-scanning-documentation/blob/main/pages/scan_steps.md), and the complete Site Scanning dataset, with further analysis of each website can be found [here](https://digital.gov/guides/site-scanning/data/).  
