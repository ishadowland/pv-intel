<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://bessxchange.com/article?slug=a-password-free-login-reached-470000-sungrow-systems-india-should-keep-track-404 -->
<!-- fetched_at: 2026-11-15 07:12:13 -->
<!-- sha256: 36f3dbbf72f8016bba81ddb3bfae4ed8154f1cc9586fb9dc34910663a7ccd6d4 -->

A Password-Free Login Reached 470,000 Sungrow Systems. India Should Keep Track | BESS Xchange

Menu

close

Green Index
Stationary Storage
Mobility Storage
Policy
Storage Tenders
Interviews
Tech & Innovation

close

Search articles, categories, and creators...

Loading story…
A security researcher
in Kassel, Germany, found a way into the administrator accounts of Sungrow’s
iSolarCloud platform without needing a password. According to the report
published by his firm, Jakkaru, the access covered about 470,000 Sungrow
systems in Europe, roughly 250,000 of them in Germany with a combined peak
output of 7.8 GW. Sungrow closed the gap within a day of being told in late
August and says its logs show no one else exploited it. Trade press took up the
story this week.

## How it worked

Marlon
Starkloff, Jakkaru’s managing director, began with an ordinary customer
account. A flaw in the login logic then took him into management accounts
belonging to installers and, from there, into Sungrow’s own administrator
accounts, according to German reporting on the write-up. With administrator
rights a person can list, change, start and stop plants in a region, including
inverters and batteries, and can push new firmware. Sungrow runs four regional
platforms, covering Europe, China, Australia and the rest of the world, and
Jakkaru says the flaw touched all four. The firm did not test the access on
live plants.

The scale
explains the alarm. Die Zeit, which checked the case independently, documented
a late-August screenshot showing the European platform carrying almost 18 GW of
instantaneous generation. Europe’s grid is designed to ride through a sudden
loss of about 3 GW, so the platform potentially reached six times that.
Starkloff considers a firmware update that shuts inverters down at a preset
time more realistic than a one-click switch-off. Germany’s cyber agency, the
BSI, said platforms that pool this much capacity must be protected, because
manipulating them could affect electricity supply. German law does not treat
inverter makers as critical-infrastructure suppliers, Polish outlet
Gramwzielone noted in its summary of the Zeit report.

## Not a first

This is not
Sungrow’s first disclosure. In 2025 Forescout researchers reported 46
vulnerabilities across Sungrow, Growatt and SMA systems, all since fixed. What
is new is the combination: administrator-level reach into a cloud, over a fleet
large enough to matter to a continental grid.

## The India connect

India has
already written cyber concerns into policy, and the Sungrow case shows what the
rules cover and what they do not. In August the Ministry of New and Renewable
Energy required that data from inverters installed under PM Surya Ghar be
stored within India, with manufacturers declaring the location of their data
centres in an undertaking to REC. Separately, the Central Electricity
Authority’s Cyber Security in Power Sector Regulations, 2026 bring large
renewable and storage assets into a formal regime from April 1, 2027, extend
obligations to vendors, and require secure, authenticated and encrypted remote
access.

Data localisation
answers where information sits. It does not answer whether the login on that
server is sound. A cloud hosted in India with the same kind of authentication
bug would pose the same risk to the Indian fleet. Deloitte India’s Santosh
Jinugu has listed insecure remote access, weak credential management and
unpatched firmware among the exposures in a solar base that leans on imported
inverters. The practical test is architectural: who can send commands or
firmware to the devices, how those actions are authenticated, and whether a
plant can keep running on local control if the vendor platform is cut off.

What developers can ask for

Ahead of the
April 2027 deadline, owners and EPCs can put four questions to inverter and
storage vendors. How does the monitoring platform authenticate administrators
and installers? Who can push firmware, and how is it signed? How quickly and
openly does the vendor disclose incidents? Can plant control run locally
without the cloud? Jakkaru’s advice to operators in Germany points the same
way: reconsider cloud connectivity and, where possible, allow it only for
firmware updates. Sungrow says it supports mandatory, verifiable security
requirements for platforms that manage distributed energy at scale. That is a
position Indian buyers can test against contract terms.
