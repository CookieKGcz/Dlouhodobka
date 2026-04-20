## Elementary taxonomy
- ==Asset== (resource): information, software, hardware and computing and communications services
- ==Vulnerability== (weakness): specific system characteristics, design flaws, implementation flaws, deployment or configuration issues
- ==Security policy==: specification of the design intent of a system's rules and practices - what is, and is not (supposed to be) allowed
## Steps in security
1. Risk assessment execution
2. _Security policy definition_
3. Security architecture design
4. Security mechanism - design and implementation
5. Monitoring of security related events
- loopback to step #1
## Security policy should:
- specify assets requiring protection;
- specific users allowed to access specific assets,
	- and the allowed means of access;
- security services to be provided; and
- system controls that must be in place.
## Security policy:
- _aims to minimize_ (manage) risks;
	- risk analysis is therefore crucial, as is
	- identification of assets;
- presents strategies (high-level concepts??) how to achieve the aims using security services and controls;
- should clearly tell what and how should security services and controls achieve;
- is usually written is a standard human language (often with some recommended vocab. and structure)
## Bell-LaPadula confidentiality policy (model)
- State machine based multilevel security policy, originally for military applications
- Gives a state transition model with access control rules that use security labels on objects and clearances for subjects.
	- Top secret > Secret > Confidential > Public
- Simple security property: subject at a given security level may bot read an object at a higher security level. (NRU = No read up)
- -property: subject at a given security level may not write to any object at a lower security level. (NWD = No write down)
## Microsoft Windows OS example (part of CAPP):
- “Any other systems with which the TOE communicates are assumed to be under the same management control and operate under the same security policy constraints.
- The TOE is applicable to networked or distributed environments only if the entire network operates under the same constraints and resides within a single management domain.
- There are no security requirements that address the need to trust external systems or the communications links to such systems.
### Translation ??
- System disconnected from networks (at different security level), disabled media drives, etc
- Level of protection appropriate for an assumed non-hostile and well-managed user community
- The profile is not intended to be applicable to circumstances in which protection is required against determined attempts by hostile and well funded attackers to breach system security.
- CAPP does not fully address the threats posed by malicious system development or administrative personnel.
## Relevant taxonomy recap
- Threat: combination of circumstances and entities that might harm assets
- Attack is the deliberate execution of one of more steps intended to cause a security violation
	- Attacks exploit vulnerabilities
- Countermeasures and controls:
	- support and enforce security policies,
	- include operational and management processes, os enforcement by software monitors and related access control measures, and sec. mechanisms.
## Risk, Risk assessment
- Risk is expected loss due to harmful future events, and
- is relative to the identified set of assets and over a fixed time period.
- Risk depends on:
	- threat agents,
	- probability of an attack, and
	- expected losses on the case
- Risk assessment involves analyzing these factors in order to estimate risk.
## What is risk?
- R = T * V * C
	- T - threat information
	- V - existence of vulnerabilities
	- C - cost or impact of a successful attack -asset value.
- R = P * C
	- P = T * V
		- Probability that a threat agent takes an action that successfully exploits vulnerability
## Approaches to risk assessment
- Quantitative risk assessment = compute numerical estimates of risk.
	- units
	- Annual Loss Expectancy (ALE) $\sum_{i=1}^{n}{Fi \times Ci}$
	- suited for incidents that occur regularly
- Qualitative risk assessment = qualitative rating and comparative reasoning.
	- Typically using 3-5 levels of scale.
	- Practical risk assessment
	- Risk score  = probability score/level * impact score/level
## Risk rating/score set
- ![[Pasted image 20260413104649.png|400]]
## Risk assessment - final notes
- Details of recommended/considered controls (safeguards) vary
- Desired state = where risks to defined assets would not cause any harm bigger than what the organization is willing to accept/tolerate.
- Risk assessment will hardly ever assess all foreseeable risks.

## ISO/IEC 27000
- Family of information sec. standards focused on security management
- Also known for ISMS ´Information Security Management System
### ISO/IEC 27000 PDCA
- Plan:
	- Establish ISMS policy, objectives, processes and procedures relevant to managing risk and improving information security to deliver results in accordance with an organization's overall policies and objectives
- Do:
	- Implement and operate the ISMS policy, controls, processes, and procedures.
- Check:
	- Assess and, where applicable, measure process performance against ISMS policy, objectives, and practical experience and report the results  to management for review.
- Act:
	- Take corrective and preventive actions, based on the results of the internal ISMS audit and management review or other relevant information, to achieve continual improvement of the ISMS

## IT (security) audit
1. Audit planning
2. Documentation and checks of controls/safeguards
3. Selection of compliance test and their execution
4. Selection and execution of special tests
5. Overall assessment of the system

- Internal audit - department independent of the IT division
## Business continuity planning (BCP)
- Deals with preventative and reactive recovery actions to enable organization's activities before and during disaster recovery
- The organization going on ´having all essential functions of the organization provided when critical problems/events arise - earthquake, floods, COVID....
- Disaster recovery - practice aiming to recover or have ongoing operations of vital systems and technology infrastructures after a serious disruptive event
## Disaster recovery
- Recovery Point Objective (RPO) = maximum target period where data might be lost (permanently) from an IT service due to major incident.
- Recovery Time Objective (RTO) = target time and service level at  which a service must be restored after a disaster to avoid unacceptable consequences of a break in business continuity.
