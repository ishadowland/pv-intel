<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://www.defconlevel.com/alert/2026-11-19-cisa-cybersecurity-advisories-autonomy-logic-openplc-runtime-icsa-26-323-01 -->
<!-- fetched_at: 2026-11-24 07:12:51 -->
<!-- sha256: e67757ae2f7e448884fe6b81b72774d1e32cf0a56b8a00fd83853e061f5a3ea9 -->

Autonomy Logic OpenPLC Runtime (ICSA-26-323-01) | Defcon Level

Skip to main content

Cyber Threat Official statement
At a glance
What Cyber Threat Who CISA Cybersecurity Advisories When Nov 19, 2026 at 12:00 PM UTC Statement from CISA Cybersecurity Advisories, November 19.
Summary
Successful exploitation of this vulnerability could allow several unauthenticated admin accounts to be created.
The following versions of Autonomy Logic OpenPLC Runtime are affected:
OpenPLC Runtime &lt;=4.2.4 (CVE-2026-126088)
CVSS
Vendor
Equipment v3 8.1
Autonomy Logic
OpenPLC Runtime
1 Vulnerability
Concurrent Execution using Shared Resource with Improper Synchronization ('Race Condition')
Background
Critical Infrastructure Sectors: Critical Manufacturing, Energy, Transportation Systems, Water and Wastewater Systems
Countries/Areas Deployed: Worldwide
Company Headquarters Location: United States
Vulnerabilities
CVE-2026-126088
In Autonomy Logic OpenPLC Runtime versions 4.2.4 and prior, a race condition allows multiple concurrent requests to pass the existence check before any user is committed, resulting in several unauthenticated admin accounts being created.
Read More
1 Affected Product
Autonomy Logic OpenPLC Runtime &lt;=4.2.4
Product Status: known_affected
Remediations
Vendor fix
Update to OpenPLC Runtime version 4.3.0 or later.
Additional Metrics
Relevant CWE: CWE-362 Concurrent Execution using Shared Resource with Improper Synchronization ('Race Condition')
CVSS Version
Base Score
Base Severity
Vector String
3.1
8.1
High
CVSS:3.1/av:N/ac:H/PR:N/ui:N/S:U/C:H/I:H/a:H
4.0
9.2
Critical
CVSS:4.0/av:N/ac:H/at:P/PR:N/ui:N/VC:H/vi:H/va:H/SC:N/si:N/sa:N
View CVE Details
Acknowledgments
Noureddin Lutfi reported this vulnerability to CISA.
Recommended Practices
CISA recommends users take defensive measures to minimize the risk of exploitation of these vulnerabilities. Minimize network exposure for all control system devices and/or systems, ensuring they are not accessible from the internet. Locate control system networks and remote devices behind firewalls and isolating them from business networks.
When remote access is required, use more secure methods, such as Virtual Private Networks (VPNs), recognizing VPNs may have vulnerabilities and should be updated to the most current version available. Also recognize VPN is only as secure as the connected devices.
CISA reminds organizations to perform proper impact analysis and risk assessment prior to deploying defensive measures. Several CISA products detailing cyber defense best practices are available for reading and download, including Improving Industrial Control Systems Cybersecurity with Defense-in-Depth Strategies.
CISA encourages organizations to implement recommended cybersecurity strategies for proactive defense of ICS assets. Organizations observing suspected malicious activity should follow established internal procedures and report findings to CISA for tracking and correlation against other incidents.
CISA also recommends users take the following measures to protect themselves from social engineering attacks:
Do not click web links or open attachments in unsolicited email messages. Refer to Recognizing and Avoiding Email Scams for more information on avoiding email scams.
Refer to Avoiding Social Engineering and Phishing Attacks for more information on social engineering attacks. No known public exploitation specifically targeting these vulnerabilities has been reported to CISA at this time.
Revision History
Initial Release Date: 2026-11-19
Date
Revision
Summary
2026-11-19
1
Initial Publication
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

Related Preparedness Gear

Be prepared for evolving situations

📦
Emergency Kit

📻
Emergency Radio

🩹
First Aid

🔦
Flashlight

View All Preparedness Supplies →

Affiliate links support our mission

Global Conflict Map

Live snapshot of conflict locations and tension zones worldwide.

Map data last updated: November 23, 2026

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

ALERT

Nov 19, 2026 · 12:00 PM · 4 d ago

CISA Cybersecurity Advisories: libumqtt (ICSA-26-323-03)

View CSAF Summary Successful exploitation of this vulnerability could allow a remote attacker to cause a denial of service, memory corruption, or...

Read Full Alert →

ALERT

Nov 19, 2026 · 12:00 PM · 4 d ago

CISA Cybersecurity Advisories: Elecbrakes EB2, VM1, ELBC2000 (ICSA-26-323-02)

View CSAF Summary Successful exploitation of these vulnerabilities could allow an attacker to gain control of the brakes of a trailer, modify the...

Read Full Alert →

ALERT

Nov 20, 2026 · 12:00 AM · 3 d ago

SAP NetWeaver Improper Neutralization of Special Elements in Data Query Logic Vulnerability (CVE-2025-42884)

SAP NetWeaver Enterprise Portal contains an improper neutralization of special elements in data query logic vulnerability that allows an...

Read Full Alert →

CYBERCOM

ALERT

Nov 17, 2026 · 12:00 PM · 6 d ago

CISA Cybersecurity Advisories: Critical Java Vulnerability Requires Immediate Patching

Purpose CISA strongly urges organizations to immediately patch the recently disclosed Oracle Java vulnerability CVE-2026-114938...

Read Full Alert →

See all Rapid Alerts
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
