<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://www.defconlevel.com/alert/2026-11-17-cisa-cybersecurity-advisories-siemens-simatic-icsa-26-321-08 -->
<!-- fetched_at: 2026-11-25 07:12:48 -->
<!-- sha256: 91cfa521342de87e04c4557c22c6b6c2c67ebcae7a50c138c2140e2cb570db98 -->

Siemens SIMATIC (ICSA-26-321-08) | Defcon Level

Skip to main content

Cyber Threat Official statement
At a glance
What Cyber Threat Who CISA Cybersecurity Advisories When Nov 17, 2026 at 12:00 PM UTC Statement from CISA Cybersecurity Advisories, November 17.
Summary
The products listed below contain an authentication bypass vulnerability that could allow an on-path attacker to take over the session of a legitimate user and execute arbitrary code with the privileges of the victim user. Siemens is preparing fixes and recommends specific mitigations for products where fixes are not or not yet available.
The following versions of Siemens SIMATIC are affected:
SIMATIC Batch V9.1 vers:all/* (CVE-2026-58114)
SIMATIC Information Server 2020 vers:all/* (CVE-2026-58114)
SIMATIC Information Server 2022 vers:all/* (CVE-2026-58114)
SIMATIC PCS 7 V9.1 vers:all/* (CVE-2026-58114)
SIMATIC Process Historian 2020 vers:all/* (CVE-2026-58114)
SIMATIC Process Historian 2022 vers:all/* (CVE-2026-58114)
SIMATIC WinCC Runtime Professional V17 vers:all/* (CVE-2026-58114)
SIMATIC WinCC Runtime Professional V18 vers:all/* (CVE-2026-58114)
SIMATIC WinCC Runtime Professional V19 vers:all/* (CVE-2026-58114)
SIMATIC WinCC Runtime Professional V20 vers:all/* (CVE-2026-58114)
SIMATIC WinCC Runtime Professional V21 vers:all/* (CVE-2026-58114)
SIMATIC WinCC V7.5 vers:all/* (CVE-2026-58114)
SIMATIC WinCC V8.0 vers:all/* (CVE-2026-58114)
SIMATIC WinCC V8.1 vers:all/* (CVE-2026-58114)
CVSS
Vendor
Equipment v3 7.5
Siemens
SIMATIC batch V9.1
1 Vulnerability
Weak Authentication
Background
Critical Infrastructure Sectors: Critical Manufacturing
Countries/Areas Deployed: Worldwide
Company Headquarters Location: Germany
Vulnerabilities
CVE-2026-58114
Affected systems do not properly secure their remote user authentication with the deprecated NTLM protocol. This could allow unauthenticated remote attackers, who have achieved a machine in the middle position, to relay NTLM authentication and impersonate a legitimate user. The potential impact depends on the services that are accessible, e.g. a SQL server used by WinCC.
Read More
14 Affected Products
SIMATIC batch V9.1
Product Status: known_affected
Remediations
Mitigation
No fix planned
Currently no fix is planned
SIMATIC WinCC Runtime Professional V20
Product Status: known_affected
Remediations
Mitigation
None available
Currently no fix is available
SIMATIC WinCC Runtime Professional V21
Product Status: known_affected
Remediations
Mitigation
None available
Currently no fix is available
SIMATIC WinCC V7.5
Product Status: known_affected
Remediations
Mitigation
None available
Currently no fix is available
SIMATIC WinCC V8.0
Product Status: known_affected
Remediations
Mitigation
None available
Currently no fix is available
SIMATIC WinCC V8.1
Product Status: known_affected
Remediations
Mitigation
None available
Currently no fix is available
SIMATIC Information Server 2020
Product Status: known_affected
Remediations
Mitigation
No fix planned
Currently no fix is planned
SIMATIC Information Server 2022
Product Status: known_affected
Remediations
Mitigation
No fix planned
Currently no fix is planned
SIMATIC PCS 7 V9.1
Product Status: known_affected
Remediations
Mitigation
No fix planned
Currently no fix is planned
SIMATIC Process Historian 2020
Product Status: known_affected
Remediations
Mitigation
No fix planned
Currently no fix is planned
SIMATIC Process Historian 2022
Product Status: known_affected
Remediations
Mitigation
No fix planned
Currently no fix is planned
SIMATIC WinCC Runtime Professional V17
Product Status: known_affected
Remediations
Mitigation
None available
Currently no fix is available
SIMATIC WinCC Runtime Professional V18
Product Status: known_affected
Remediations
Mitigation
None available
Currently no fix is available
SIMATIC WinCC Runtime Professional V19
Product Status: known_affected
Remediations
Mitigation
None available
Currently no fix is available
Additional Metrics
Relevant CWE: CWE-1390 Weak Authentication
CVSS Version
Base Score
Base Severity
Vector String
3.1
7.5
High
CVSS:3.1/av:N/ac:H/PR:N/ui:R/S:U/C:H/I:H/a:H
View CVE Details
Acknowledgments
Siemens ProductCERT reported this vulnerability to CISA.
General Recommendations
As a general security measure, Siemens strongly recommends to protect network access to devices with appropriate mechanisms.
Additional Resources
Terms of Use
Recommended Practices
CISA recommends users take defensive measures to minimize the risk of exploitation of these vulnerabilities. Minimize network exposure for all control system devices and/or systems, ensuring they are not accessible from the internet. Locate control system networks and remote devices behind firewalls and isolating them from business networks.
When remote access is required, use more secure methods, such as Virtual Private Networks (VPNs), recognizing VPNs may have vulnerabilities and should be updated to the most current version available. Also recognize VPN is only as secure as the connected devices.
CISA reminds organizations to perform proper impact analysis and risk assessment prior to deploying defensive measures. Several CISA products detailing cyber defense best practices are available for reading and download, including Improving Industrial Control Systems Cybersecurity with Defense-in-Depth Strategies.
CISA encourages organizations to implement recommended cybersecurity strategies for proactive defense of ICS assets. Organizations observing suspected malicious activity should follow established internal procedures and report findings to CISA for tracking and correlation against other incidents.
Advisory Conversion Disclaimer
This ICSA is a verbatim republication of Siemens ProductCERT SSA-970803 from a direct conversion of the vendor's Common Security Advisory Framework (CSAF) advisory. This is republished to CISA's website as a means of increasing visibility and is provided "as-is" for informational purposes only. CISA is not responsible for the editorial or technical accuracy of republished advisories and provides no warranties of any kind regarding any information contained within this advisory. Further, CISA does not endorse any commercial product or service. Please contact Siemens ProductCERT directly for any questions regarding this advisory.
Revision History
Initial Release Date: 2026-11-10
Date
Revision
Summary
2026-11-10
1
Publication Date
2026-11-17
2
Initial CISA Republication of Siemens ProductCERT SSA-970803 advisory
Legal Notice and Terms of Use

Share:

Share:

X

Facebook

WhatsApp

Reddit

Telegram

Email

Substack

Patreon

LinkedIn

Bluesky

Threads

Copy

Bookmark

Notify
On

Save for quick access. If the button does not work, press Ctrl+D

Link copied to clipboard!

Save for quick access. If the button does not work, press Ctrl+D

Source:
CISA Cybersecurity Advisories

Understanding Global Threats

Nuclear War Calculators & Tools

☢️
Blast Radius Calculator

Calculate effects at any distance

📚
All Tools & Resources

Maps, calculators, and more

🛡️
Survival Guide

How to survive nuclear attack

DEFCON System

🚨
DEFCON Hub

All DEFCON information

❓
What is DEFCON?

Learn the alert system

🔴
DEFCON Levels

All 5 levels explained

📅
Historical Events

Critical moments in history

Browse All Topics & Pages

Complete sitemap with all intelligence resources

View Sitemap →

Digital Security & Backup

Protect your data and maintain connectivity

📱
Faraday Bag

💾
External Drive

🔋
Solar Charger

📡
Satellite Phone

View All Preparedness Supplies →

Affiliate links support our mission

Global Conflict Map

Live snapshot of conflict locations and tension zones worldwide.

Map data last updated: November 24, 2026

Preview · Click to explore →

Open Conflict Map Page →

Open Conflict Map Page
→

Go deeper with the data

Guides, timelines, and calculators to help you understand today's risks.

Open Conflict Map Page

Information Library

Calculators & Tools

Raised Alerts

Related Alerts

CYBERCOM

ALERT

Nov 17, 2026 · 12:00 PM · 1 wk ago

CISA Cybersecurity Advisories: Critical Java Vulnerability Requires Immediate Patching

Purpose CISA strongly urges organizations to immediately patch the recently disclosed Oracle Java vulnerability CVE-2026-114938...

Read Full Alert →

CYBERCOM

ALERT

Nov 17, 2026 · 12:00 PM · 1 wk ago

CISA Cybersecurity Advisories: Siemens ROS# (ICSA-26-321-06)

View CSAF Summary ROS# before version 2.3.1 contains a code injection vulnerability that could allow an attacker that is able to pass a crafted...

Read Full Alert →

CYBERCOM

ALERT

Nov 17, 2026 · 12:00 PM · 1 wk ago

CISA Cybersecurity Advisories: Siemens Industrial Automation Software Products (ICSA-26-321-03)

View CSAF Summary On October 21, 2026, the Node.js project released security updates addressing a critical vulnerability in the Brotli decoder...

Read Full Alert →

CYBERCOM

ALERT

Nov 17, 2026 · 12:00 PM · 1 wk ago

CISA Cybersecurity Advisories: Siemens Industrial Software Products (ICSA-26-321-04)

View CSAF Summary On October 21, 2026, the Node.js project released security updates addressing a critical vulnerability in the Brotli decoder bundled with Node.js, commonly referred to as...

Read Full Alert →

See all Rapid Alerts

View All CYBERCOM Alerts

All Alerts

Keep Exploring

Security Alerts

All Alerts

Raised Alert Levels

All Commands

Maps & Tracking

Global Conflict Map

DEFCON Clock

Cyber Threat Maps

Current Status

Current Global Level

Level Change History

About This Site

Enable Push Notifications

×

1

Click "Allow" in the browser popup

Your browser will ask for permission to send notifications. Click "Allow" to continue.

💡
Look for a popup near your address bar

2

Setting up notifications...

Please wait while we configure your notifications.

3

Choose Your Notification Preferences

Select which types of notifications you want to receive:

💡 Before you save:

Customize your alerts : Only Critical and High alert levels are ticked to start. Tick more to hear about more, or untick any you don't want.

Limits : So readers are never flooded, this site sends no more than 10 notifications an hour and 50 a day, and a level change notification no more than once every 6 hours. At very busy times some alerts, even critical ones, are not sent as notifications, but every alert is still posted on the site. Your own choices under Quiet times and limits can lower this further.

Browser-specific : You'll need to subscribe again if you clear browser data or switch browsers.

Scroll down to view all options

What would you like to receive?

Loading options...

Filter by Priority Level
Only receive alerts of selected priority levels

Filter by Region
Only receive alerts for selected geographic commands

All Regions

Filter by Category
Only receive alerts from selected categories

Quiet times and limits
Optional. These apply only to you.

Quiet hours
No alerts during these hours, in your own time.

From
To

Most alerts per day

No limit

Still send the most urgent alerts
Critical alerts still reach you during your quiet hours or past your daily limit.

✓

Notifications enabled

You'll now receive alerts based on your preferences.

⚠️

Unable to enable notifications

An error occurred. Please try again.

Start Setup
Cancel

Get Instant Alerts

Receive notifications when important updates are published.

Click to enable notifications
Notifications are ON - click to disable

Works even when browser is closed

↑
