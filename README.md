# Lab 1 Submission — Problem Statement #46

## Problem Statement
**Remote Team Time-Tracking & Project Approver** — an engineering productivity platform for tracking developer hours against Jira tickets, monitoring project budget burn rates, and facilitating managerial timesheet approval workflows.

## Actors
- Remote Developer
- Engineering Manager
- Jira (external system actor)

## Use Cases
- UC-01 — Log Time Against Jira Task
- UC-02 — Submit Timesheet
- UC-03 — Review Timesheet
- UC-04 — Approve/Reject Timesheet
- UC-05 — Monitor Project Budget Burn
- UC-06 — Retrieve Jira Task Details

The UML diagram uses `UC-01 <<include>> UC-06` because retrieving Jira task details is required while logging time against a Jira task. It uses `UC-04 <<extend>> UC-03` because approval/rejection is a conditional action following review.

## Requirements Deliverables
- `requirements_table.docx` — formatted requirements table with exactly 5 FRs and 2 NFRs.
- `requirements_table.xlsx` — spreadsheet version of the same requirements table.

## UML Deliverables
- `remote_team_timesheet_use_case.drawio` — editable draw.io-compatible source file.
- `remote_team_timesheet_use_case.pdf` — PDF representation of the completed UML use-case diagram.

## Use-Case Flow Deliverables
- `use_case_flow_approve_reject_timesheet.docx` — one-page UC-04 flow specification.
- `use_case_flow_approve_reject_timesheet.pdf` — PDF export of the flow specification.

## Source Alignment
The deliverables follow Problem Statement #46 and the Lab 1 handout. The problem statement names Remote Developer and Engineering Manager; Jira is included here as the requested third actor representing the external Jira system. The requirements retain the supplied wording for FR-001 and NFR-001, while the remaining requirements are drafted to complete the required five FRs and two NFRs.

## Submission Note
No GitHub upload is claimed in this package. The files are prepared locally for submission.
