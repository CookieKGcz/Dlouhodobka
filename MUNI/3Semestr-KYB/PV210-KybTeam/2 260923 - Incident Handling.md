- Martin Laštovička
## Cyber threat landscape
- ENISA Cyber threat landscape report
	- Annual report on the state of cybersec within the EU
	- from their own Cyber threat Intelligence
	- Identifies
		- prime threats
		- major trends observed with respect to threats
		- threat actors
		- attacks techniques
	- Describes relevant mitigation measures and recommendations
- Phishing remains a primary initial intrusion vector
## Incident Handling Phases
![[Pasted image 20260923102528.png | 400]]
### Incident report
- Communication channels: Web, email, phone, verbal, message from IDS, CSIRT own activity
- may come from within and outside of the org
- CSIRT must define how to report incident
### Registration
- Report inserted into incident handling system
- Spam filters
	- BRUH, automatic reports often falls into spam
- Assign incident ID
- Assign person who proceeds within the incident triage
### Triage
- Initial assessment of the report
- Incident verification
- Check if you have mandate to solve the incident
- Check for duplicates
- Accept / decline report and further steps
	- Incident classification
	- Incident prioritization
		- based on classif. and targeted system/customer
	- Incident assignment
		- allocate number of incident handlers
### Incident Resolving
#### Data Analysis
- Collect data
	- Monitoring systems, log files, setups and configs
- An incident can result in a real legal case -> proper collection needed (checksum the data...)
- Data from third parties
	- prob wont help
- Analyze the data
	- Goal is to come up with a solution for the incident
#### Resolution Research
- Timeliness of reaction
#### Action Proposed
- set of concrete and practical tasks for each party
- The task must be understandable
	- lang and tech knowledge
#### Action Performed
- Were all actions really carried out?
- Monitor the progress
#### Eradication and Recovery
- Ensure all systems went back online
- Get confirmation from each party that their operations are back to normal
### Closure
- Main findings and recommendations
- Final classifications
- Archiving
### Post analysis
- Not every incident is worth analyzing
- proposal for improvement

## Report Triage
- Goals: initial assessment of the report, verification, classification, prioritization, assignment
- ![[Pasted image 20260923105149.png | 420]]
## Incoming Report Processing
### Incident Report
- "Origin" of all incidents
- Comes from various sources in various formats
- Both manually and automatically
