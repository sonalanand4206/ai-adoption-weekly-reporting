# Weekly AI Tool Adoption Reporting

This notebook reports weekly active users (WAU), weekly power users (WPU), and

the power-user rate for eligible Advisory employees. It covers Quill, Atlas,

and the distinct users across available tools (`ANY`).

## Regenerate the report

Requires Python 3.10 or later. Place the supplied `data/` folder alongside

`CS_JP.ipynb`, keeping the original folder structure. From the project root,

run:

```powershell

python -m pip install pandas openpyxl
python run_report.py
```

The runner executes the notebook's code from top to bottom. The code validates the report and writes `out/weekly_tool_metrics.csv`.

You can also open `CS_JP.ipynb` in Jupyter and run all cells from top to bottom.

## Leadership takeaways

- Weekly active users across Quill and Atlas rose from 654 to 791 (+21%)
  between 9 August and 27 September, two weeks with both feeds available.
- Quill weekly active users fell from 550 to 381 between 6 and 13 September,
  while Atlas stayed close to its previous level (282 to 277). Check Quill's
  daily event volumes and feed completeness before attributing the drop to
  lower adoption.
- Atlas data was unavailable for the week starting 20 September. The combined
  figures for that week (641 active users and 231 power users) reflect Quill
  only. The report flags this week as incomplete for cross-tool comparisons.

## Data quality and reporting decisions

- HR roster: 45 employees had multiple records. I selected the latest record
  per employee before filtering to Advisory, leaving 1,507 eligible employees.
- Quill: ID normalisation changed the formatting of 8,455 source rows. The source contained 1,397 rows beyond the first occurrence of each
  exact match. Without an event ID, I treated identical generation records as
  duplicates for reporting. This changed 64 employee-week power-user
  classifications. Weekly active-user counts were unchanged.
- Atlas: The 13 September delivery replaced the 7 September delivery for the
  week ending 5 September. This excluded 518 superseded rows. Atlas metrics
  are blank for the missing week starting 20 September.
- Combined usage: `ANY` counts each employee once per week for each metric.
  Its `measured` flag is `True` only when both tools have source data.

## Next steps

- Request the missing Atlas delivery and regenerate the affected week.
- Check Quill's daily event counts for the week starting 13 September and ask
  the source owner to confirm how identical events should be handled.

## Production improvements

- Schedule the workflow after the vendor delivery deadline and alert on
  missing feeds or unexpected changes in row counts.
- Keep a record of source filenames and delivery dates so revised weeks can
  be rebuilt and traced.
- Validate the schema, unique week/tool rows and metric bounds before publishing.
  If validation fails, retain the last verified dashboard and flag it as stale.
  Show a coverage warning for weeks with a missing feed.
- Pin dependency versions and test that the report regenerates in a clean
  environment.