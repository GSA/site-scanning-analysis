# Execution Context Destroyed Experiment

## Goal

The goal of this experiment was to better understand which websites end up with
the error `execution_context_destroyed` for their primary scan, and how often.

## Method

To get day-by-day scan results, we used daily local backups of the postgres
database. In total, nine backups were made over the course of two weeks.

After each backup was acquired, we then updated and ran a script based on the
template included in this directory.

## Findings

The `over_time.csv` file in the directory contains every target URL that wound
up with the the error `execution_context_destroyed` for their primary scan at
least once across the nine daily database backups that were analyzed. It also
includes each target URL's primary scan status for every run.

For example, here is the primary scan status of the target URL `srs.ntis.gov`
over the course of the nine days we conducted the experiment:

- day 1: execution_context_destroyed
- day 2: completed
- day 3: execution_context_destroyed
- day 4: unknown_error
- day 5: completed
- day 6: completed
- day 7: execution_context_destroyed
- day 8: execution_context_destroyed
- day 9: execution_context_destroyed

Below is a list of target URLs that consistently got this error across all nine
days:

```csv
asap.gov
bms.fiscal.treasury.gov
cmdp.epa.gov
ecos-training.fws.gov
ecos.fws.gov
esp-ebz-ext-wc-f5.lanl.gov
fis.fws.gov
fpdss.fws.gov
gsaglobalsupply.gsa.gov
learner.pnl.gov
library.doi.gov
nccd.cdc.gov
nncamstrn.ornl.gov
pwm.grantsolutions.gov
researchtoreality.cancer.gov
review.rcfl.gov
rnc.lbl.gov
search-origin.cdc.gov
search.cdc.gov
servicedesk.edc.usda.gov
soarproto.airports.faa.gov
tenuretrack.nih.gov
usmcservmart.gsa.gov
www.ncep.noaa.gov
```
