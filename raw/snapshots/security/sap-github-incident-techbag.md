<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://www.thetechbag.com/blog/sap-suspicious-activity-github-development-systems -->
<!-- fetched_at: 2026-11-28 07:12:08 -->
<!-- sha256: d88c5fd916d0de99cb343c7d4e6887d0ce03f030e3a1531eff2b4e97123c7f3d -->

SAP cyber incident: GitHub, signing keys, customer data | TechBag

Explore TechBag → Menu

The TechBag Journal Subscribe

The TechBag Journal Subscribe
SAP confirms suspicious activity: press report GitHub curbs, signing keys replaced

Illustration: The TechBag Journal
SAP confirmed on Friday 27 November that it had identified suspicious activity and had immediately taken steps to protect its customers and secure its services. “Based on our investigation to date, we have found no evidence of unauthorized access to customer business data,” the company said in a statement to The Record. “We will continue to strengthen our security to provide the secure and resilient environment our customers depend on.” 1 SAP did not say what the activity was, when it was detected or which parts of the company it touched. 2 Its own news site, news.sap.com, carried no post about it when we last checked.
Almost everything else in the coverage comes from German press reports built on SAP’s internal communications and people inside the company. For an SAP customer the useful question is narrower than “was SAP hacked?”: can the corrections and updates my systems take from SAP still be trusted, and what can I check myself? We separate what SAP has said from what has been reported, explain what a signing key does in SAP’s own delivery chain, and set out the checks SAP’s documents already describe.
27 Nov
SAP’s statement: no evidence so far of unauthorised access to customer business data
SAP, via The Record

3
steps Handelsblatt reports: GitHub access restricted, automated development stopped, signing keys replaced
Handelsblatt, via heise

1 week+
how long SAP has been dealing with the incident, Der Spiegel reports
Der Spiegel

8 Dec
SAP’s next Security Patch Day, held on the second Tuesday of each month
SAP

01 What SAP has said, and what others report
SAP’s statement has three parts. It identified suspicious activity. It acted at once: dpa quotes SAP as saying it had “unverzüglich die notwendigen Maßnahmen ergriffen, um seine Kunden zu schützen und die Sicherheit seiner Dienste zu gewährleisten”, which we translate as “immediately taken the necessary measures to protect its customers and ensure the security of its services”. And, so far, it has found no evidence that anyone reached customer business data. 1 2
Der Spiegel broke the story on the evening of 26 November, citing internal communications and people familiar with the matter. As The Record summarises Spiegel’s report, the attackers went for SAP’s software development environment on GitHub and obtained employee authentication tokens that let them copy and modify source code. dpa, which saw parts of SAP’s internal communication, reported that SAP had told staff several days earlier about suspicious activity in “the platform for developer productivity and software delivery GitHub” (our translation of dpa’s German) and asked them to check whether they needed to change their login details. Handelsblatt, citing people in the company, reported that SAP restricted access to GitHub, stopped automated processes in software development and replaced signing keys (“Signaturschlüssel ausgetauscht”). 1 2 3 On 27 November Spiegel added that SAP has been dealing with the incident for more than a week and that several authorities are now involved. 4
SAP has confirmed two things; GitHub, the tokens and the replaced keys come from press reports
Each claim about SAP’s incident, who makes it, and its status, 26 and 27 November 2026
Show table Hide table Claim Who says it Status
Suspicious activity identified; steps taken at once to protect customers and secure services SAP, statement of 27 Nov Confirmed by SAP
No evidence, so far, of unauthorised access to customer business data SAP, statement of 27 Nov Confirmed by SAP
The activity was in SAP’s development systems on GitHub dpa, from SAP’s internal notice; Der Spiegel Reported
Employee authentication tokens let the attackers copy and modify source code Der Spiegel, as summarised by The Record Reported
Staff were told days earlier to check whether to change their login details dpa, from SAP’s internal notice Reported
GitHub access restricted; automated development processes stopped; signing keys replaced Handelsblatt, citing company sources Reported
Internal code name “Project Granite” Der Spiegel Reported
The attackers may have used agentic AI Der Spiegel, citing internal sources (via heise) Reported
More than a week in progress; several authorities involved Der Spiegel, 27 Nov Reported
Whether altered code reached any customer No one has said Not known

Source: SAP via The Record and dpa/heise; Der Spiegel; Handelsblatt via heise · as of 27 November 2026, 7:30pm IST
The TechBag Journal
02 What sits behind a developer’s GitHub login
In general terms, a company’s development environment on GitHub holds three things: its source code, in repositories; the automated pipelines that build, test and package that code for release; and the secrets those pipelines use, such as tokens and keys that let a build reach other systems. SAP has not described its own setup, so that is a general description, not a report about SAP. 1Password, which disclosed on 25 November that one employee’s GitHub account was used to push code to its backend, said its CI/CD system “contains infrastructure related secrets in order for our product to work”. 10
SAP has written down what it treats as reachable from a compromised build machine. On 29 April 2026 several of its open-source npm packages were compromised with malware, which SAP said could lead to “the potential exfiltration of information, including credentials”. Its HotNews Security Note 3747787, released that day at 19:30 UTC, told anyone affected to isolate the developer machine or CI/CD runner and to “Assume that all secrets reachable from an infected system are compromised”. 8 The Record notes that it is unclear whether the April and November incidents are connected; SAP has not said. 1
In April, SAP told anyone hit to treat every secret on a build machine as stolen, GitHub tokens first
Secrets SAP listed as compromised if a system was infected, Security Note 3747787, 29 April 2026
Show table Hide table Kind of secret What SAP listed
Code hosting and packages SSH keys, GitHub tokens and grants, npm tokens, GitHub Actions secrets, personal access tokens
Cloud accounts AWS, Azure and GCP credentials, including machine identity network endpoints
Deployment tools Kubernetes, Docker, Terraform, Helm, Ansible and FileZilla secrets
Everything else on the machine Password manager credentials, environment variables, AI and MCP tool secrets, messaging apps, crypto wallets, VPN configurations
Other clean-up Remove injected workflow branches; clean IDE configurations; delete unauthorised GitHub repositories; pin exact package versions

Source: SAP, FAQ on the Mini Shai Hulud npm supply chain attack (Q2 2026), quoting Security Note 3747787 · as of 27 November 2026, 7:30pm IST
The TechBag Journal
That list explains why the steps Handelsblatt describes go together. A token taken from one developer opens whatever that developer can reach on GitHub; a pipeline that may have been touched is stopped so that nothing new is built from it until it is checked; and a key that may have been exposed is replaced. That is our reading of the reported steps, not SAP’s explanation of them, which it has not given. 3
03 What a signing key does for an SAP customer
SAP customers do not take SAP’s software on trust; their systems check a signature. SAP began delivering every SAP Note, the correction files customers apply to their ABAP systems, with a digital signature, and explained why in plain words: “The SAP Notes files can get maliciously modified and the customer unknowingly can upload the maliciously modified SAP Notes files into their ABAP systems.” Since 1 January 2020, downloading and uploading SAP Notes has stopped working unless the Note Assistant (transaction SNOTE) is set up for signed Notes. “All SAP Notes downloaded through SAP ONE Support Launchpad are digitally signed SAR files.” 5
The check runs on the customer’s own server. “The Note Assistant tool will use the SAPCAR utility on the application server to verify the digital signature of the uploaded SAP Note,” SAP wrote; if SAPCAR is not at the required patch level, “the digital signature verification fails and the files are not extracted.” 5 The same check guards upgrades: SAP’s Software Update Manager stops on an archive whose signature does not verify, with the error “Signer is not known or not trusted”. 6
A signed SAP Note is unpacked only if its signature checks out on the customer’s own server
How a digitally signed SAP Note reaches an ABAP system, as SAP documents it, 2017 to 2026
01 SAP signs
Each SAP Note is delivered as a SAR archive carrying SAP’s digital signature.

02 Customer downloads
The Note Assistant (SNOTE) fetches or uploads the signed archive.

03 SAPCAR verifies
SAPCAR, on the customer’s application server, checks the signature against a trusted signer.

04 Unpack or refuse
A valid file is extracted; a failed check means “the files are not extracted”.

Source: SAP Community post on digitally signed SAP Notes (2017); SAP Knowledge Base Articles 2788793 and 3771224 · as of 27 November 2026, 7:30pm IST
The TechBag Journal
04 Two software makers, one route in, one week
SAP’s is the second incident in three days at a software company reported to run through GitHub. On 25 November 1Password disclosed that an attacker who gained access to one employee’s corporate GitHub account copied source code from private repositories, reached its CI/CD system and pushed malicious code to backend services, which then downloaded account records for “a subset of our users”. It had begun investigating on 19 November. 10 Two weeks earlier, from 10 November, Aikido Security counted 4,837 hijacked GitHub accounts opening pull requests in 61,764 repositories to plant a stealer of CI secrets. 11 The Journal read the 1Password case in full in our analysis of 26 November , and the April npm attack on SAP’s packages in our account of the three npm worm waves .
Within three days, 1Password and SAP both disclosed incidents reported to run through GitHub
Dated events in developer-side incidents at software companies, 29 April to 27 November 2026
29 Apr 2026 SAP npm packages poisoned
10 Nov 2026 GitHub accounts hijacked
19 Nov 2026 1Password investigates
25 Nov 2026 1Password discloses
26 Nov 2026 Der Spiegel reports SAP
27 Nov 2026 SAP confirms
Show table Hide table Date Event Detail
29 Apr 2026 SAP npm packages poisoned HotNews Security Note 3747787 released at 19:30 UTC
10 Nov 2026 GitHub accounts hijacked Aikido: 4,837 accounts opened pull requests in 61,764 repositories
19 Nov 2026 1Password investigates Signs that an employee’s GitHub account was accessed
25 Nov 2026 1Password discloses Code pushed to the backend; account records taken; vaults not
26 Nov 2026 Der Spiegel reports SAP 20:14 CET: an incident in SAP’s development systems, “Project Granite”
27 Nov 2026 SAP confirms Suspicious activity; no evidence of access to customer business data

Source: SAP FAQ (Q2 2026); Aikido Security (12 Nov); 1Password (25 Nov); Der Spiegel (26 Nov); SAP via The Record (27 Nov) · as of 27 November 2026, 7:30pm IST
The TechBag Journal
The two companies’ disclosures differ in what they confirm. 1Password set out the route itself: one GitHub account, private code, the CI/CD system and the backend. SAP has confirmed suspicious activity and its conclusion about customer data, and left the route to others to report. 1 10
05 What an SAP customer checks now
SAP has asked customers to do nothing specific about this incident. Its own documents already describe the checks that matter if a supplier’s signing keys or build systems are in question, and SAP’s security team said in April where further information comes from: “Please ensure you are subscribed to our HotNews notifications.” 8 SAP publishes security fixes as SAP Security Notes on its Security Patch Day, the second Tuesday of every month, and recommends implementing them “at a priority”; the next falls on 8 December. 9
Four checks an SAP customer can run today, built on SAP’s own documents
Steps for SAP ABAP system owners, from SAP’s Security Notes page, FAQ and Knowledge Base, as of 27 November 2026
Step 1 of 4

Watch SAP’s own channels
Subscribe to HotNews notifications and read the Security Notes list in SAP for Me. In April, SAP pointed customers to exactly these for further information, not to press reports.

Back Next

Source: SAP Security Notes & News; SAP FAQ (Q2 2026); SAP Community (2017); SAP KBAs 2788793 and 3771224 · as of 27 November 2026, 7:30pm IST
The TechBag Journal
When we last checked, SAP had published no statement that signed files or customer systems were affected, and no instruction to customers about new signing keys. Either would change the checks above, and either would come from SAP, through the channels in the first step.
Sources
The Record (Recorded Future News): Software giant SAP confirms cyber incident amid reports of source code breach (SAP statement in English) — 27 November 2026
heise online: SAP: IT-Vorfall in Entwicklungssystemen (SAP statement via dpa; Handelsblatt report; in German) — 27 November 2026
Der Spiegel: »Project Granite«: SAP wird Opfer von Hackerangriff (paywalled; in German) — 26 November 2026
Der Spiegel: Was wir über den IT-Vorfall bei SAP wissen – und was nicht (paywalled; in German) — 27 November 2026
SAP Community (SAP): Enable Note Assistant to Support Digitally Signed SAP Notes — 12 September 2017
SAP Knowledge Base Article 3771224: SAPCAR error in signature verification (error 60), SSF_API_UNKNOWN_SIGNER (public preview) — read 27 November 2026
SAP Knowledge Base Article 2788793: SNOTE: Installed SAPCAR version does not support verification of signed archives (public preview) — read 27 November 2026
SAP Global Security & Cloud Compliance: FAQ, Mini Shai Hulud npm Developer Package Supply Chain Attack (Security Note 3747787) — Q2 2026
SAP Support: SAP Security Notes & News (Security Patch Day, second Tuesday of every month) — read 27 November 2026
1Password: Update on a security incident involving 1Password’s backend systems — 25 November 2026
Aikido Security: wfx-loot campaign pushes CI secret stealer to tens of thousands of repositories — 12 November 2026
CERT-In, Directions under section 70B(6) of the IT Act, 2000 (six-hour reporting) — 28 April 2022
MeitY: commencement notification under the DPDP Act, G.S.R. 843(E) (copy on MediaNama) — 13 November 2025
Show all 13 sources Disclosure. TechBag is a software reseller: it earns when companies buy through it, including from vendors named here. The analysis is TechBag’s own; no vendor paid for or saw this piece before publication. Facts are labelled reported, TechBag count or our view. How the Journal works .

Share this piece LinkedIn WhatsApp X X Email Copy link

Keep reading

Security CERT-In: tampered payment records hit government service providers, not only banks 27 November 2026 · 3 min
Security Meetsmore: logins to 201 accounts in 48 minutes, then up to 366,850 records leaked 27 November 2026 · 2 min
Security 1Password: one employee’s GitHub account led to stolen customer records, not vaults 26 November 2026 · 9 min
