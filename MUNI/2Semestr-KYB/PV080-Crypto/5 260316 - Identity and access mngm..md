## Identity
- Subset of attributes associated with a given individual, which uniquely identifies that individual within a given set
- multiple identities of an individual (diff. environments)
- partial identity is associated with given context, role.
## Human to human
- How do we identify known person?
	- Name, Look, Photo, Voice, Common friend..
- Unknown?
	- Official (gov) documents, Passport, ID, Driving license, SSN
## Digitalization of attributes of identity
- email address nicknames, cell phone num., elec. fingerprints, passwords, PINs, access cards
- Verification of such attributes? -> by other subject or official institution..
## Attributes for identification
- Domain - work environment, school/unis, medical, state institutions...
- Functional - locality, social group, biological
- Temporal
	- Permanent-given - sex, eye color, parents, date of births,...
	- Permanent-gained - qualification, behavior,...
	- Permanent-situational - address, marital status,...
	- Transitional - location, hairstyle, dress style,...
## Methods of authentication
- Something we know
	- Passwords, PINs, phrases,...
- Something we have
	- token, card, cell phone
- Something we are
	- Biometrics
- Somewhere we are - recent dimension of auth.
	- Geolocation - absolute
	- Co-location - relative (proximity based)
- Combination of methods from at least two groups from above
	- Multifactor auth. (MFA)
## Strong auth.
- combination (MFA)
- SMS is bit considered as a strong auth. (aka 2nd factor)
## Password lifecycle
- ![[Pasted image 20260316102144.png|300]]
- Forced change bad -> predictability
## Attacks on passwords
- Direct attacks
	- Online passwords guessing
		- protection? - automated account locking
	- Offline passwords guessing
		- stolen database
	- Password capture
		- keyloggers, sticky notes, stolen devices, etc.

- Bypass attacks
	- password interface bypass
	- Defeating recovery mechanisms (through email)
## Password management and SSO
- Password managers and their benefits
- Single-sign-on concept and its benefits
- Storing user passwords on a server
	- salting, hashing
	- compare with use-case for password managers
## Password managers
- Help users to align with best sec practices when using passwords
	- unique password per service
	- Reasonable password complexity
	- Easy passwords rotations
- Create some new attack vector
	- Single point of failure
	- Weak master password
		- Online, offline guessing of the master password
## Recommendations for passwords
- Use unique password per service
- Use complex passwords - mixed character sets
- Or use passphrases
- If you end up re-using passwords for different services
- Use MFA on critical online services
- Use passwords managers
- Use no-password authentication
## Challenge-respoonse protocols for auth.
- Based on random numbers
	- req. good source of randomness
- Based on sequence numbers
	- req. initialization of a seq.
- Based on timestamps
	- req. synch. of tokens and servers

## Biometrics
- Two modes of deployment:
	- Authentication (verification) = verify whether person is who s/he claims to be.
		- 1:1 comparison
	- Identification = determine identity of person
		- 1: many = search through database

- Biometrics are not secrets
	- must be combined with other factors for auth.
- Not suitable for remote auth.
- Biometrics of a same person are never 100% same
	- some level of threshold needs to be considered

## Biometrics - enrolment process
- Failure to enroll (FTE)
- Failure to capture (FTC)
- "Features" of a given type of biometrics
	- Arches, loops, relative location, distance between
- Matching score
	- never 100% match with a template

## Biometrics - verification process
- ![[Pasted image 20260316105009.png|400]]
- yellow = False acceptance rate (FAR)
- and FRR
## Characteristics and criteria of biometrics
- universality - do all users have it?
- Distinguishability - enough diff. for a set of users?
- Ease-of-sampling - compare dna with fingerprints
- Cost - includes time for processing, storage, HW/SW needed
- User acceptance - did fingerprints improve cell phones sec?
- Attack-resistance - how easy is it to circumvent the system?
## Excursion with two prominents...
### Minutiae
- = ridge characteristics, identify specific points on a fingerprint
- ![[Pasted image 20260316105518.png|400]]
### Fingerprint characteristics
- ![[Pasted image 20260316105605.png| 400]]
- ![[Pasted image 20260316105659.png|400]]
- ![[Pasted image 20260316110135.png|400]]
### Fingerprint auth.
- ![[Pasted image 20260316110208.png|400]]
### Fingerprint readers
- Sensor types:
	- Optical
		- 2D pic.
		- oldest
	- Capacitive
		- arrays of tiny capacitors circuits
		- material matters
	- Ultrasonic
		- usually in-display sensors
	- Thermal and many more...
- Smartphone readers
	- Partial scanning
	- liveness still an issue
	- In-screen fingerprint technology
## Attacks and liveness detection
- Attacks
	- Latent fingerprints, replay attacks, fake features
- Liveness detection
	- Testing the finger reaction to sensor stimuli
	- Measurement of:
		- Temp
		- Skin resistance
		- Pulse/blood flow
## Automated face recognition
- Statistical
	- Eigenface, PCA, LDA, ...
- Neural networks
	- Face API, DeepFace, FindFace, FaceNet
## Challenges in face recognition
- Illumination
- Pose
- Environment
	- Background
- Aging
- Feature occlusion
	- hats, glasses, hair
- Image quality
## Face impersonation
- Fooling deep-neural-networks-based face recognition systems
	- over 90% success rate
	- The principle is more general
## Commercial vs. forensic use/purpose/built
- Commercial
	- Low precision
	- Enrollment can be repeated
	- Only extracted characteristics saved
	- Fast and automatic
	- cheap
- Forensic
	- High precision
	- Enrollment just once
	- Full biometric data saved
	- Slower, expert interventions often necessary
	- costly
# After authentication/id -> Authorization
## Authorization
- Whether a requested privilege or resource access should be granted to the requesting entity/identity
- Which goes first, authentication or authorization?
- Default-deny principle
- Least privileges principle
- Authorization based on roles (RBAC)
## Access control intro
- models:
	- Role based access control - after AuthN, a user is given role with assigned permissions
	- Mandatory - defined by sys admin
	- Discretionary -defined by resource owners
## Identity management (IdM)
- framework of policies and technologies for ensuring that the proper people in an enterprise have the appropriate access to technology resources.
## PKI in the light if IdM
- usage of assym keys to identify services/servers
- standards for sys certs (X509)
## SAML
- Sec assertion markup language
- XML-based standard for exchanging AuthN and AuthZ data
- Use sec tokens, that contains assertions
- used to implement SSO
### SAML - Service provider request
- ![[Pasted image 20260316113927.png|400]]
## SPML
- Service provisioning markup language
- Used to setup user services/interfaces
- Provisioning requests contain required information for given service
- Helps automating provisioning/deprovision process

- In connection with SAML creates env. for IdM (mngm from one place!)

## FreeIPA
- integrated sec information managment solution combing Linux, 389 Dir server, MIT kerberos, NTP, DNS, Dogtag certificate system, SSSD and others
- ... more in presentation


## Least privilage
- Def:
	- "The principle of least privilege states that a person or system should be granted the minimal access necessary complete their purpose"
## Default deny
- unless explicitly permitted, access is not allowed
- ![[Pasted image 20260316114456.png|300]]
## Standards and regulations for Identity M.
- NIST
	- https://pages.nist.gov/800-63-3/sp800-63-3.html
- EU diractives
	- eIDAS READY
### NIST SP 800-63 "Digital Identity Guidelines"
- 2017
- Identity Assurance Level (IAL) (63A)
- Authenticator Assurance Level (AAL) (63B)
- For federated systems also Federation Assurance Level (FAL) (63C)