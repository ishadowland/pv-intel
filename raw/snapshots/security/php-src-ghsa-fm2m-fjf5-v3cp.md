<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://github.com/php/php-src/security/advisories/GHSA-fm2m-fjf5-v3cp -->
<!-- fetched_at: 2026-11-24 07:24:33 -->
<!-- sha256: 73a418384d4f3638698fd31a40d1c7ecc98eec09ed07b7aa9822b44545397f3a -->

Partially overwritten session files can lead to remote code execution · Advisory · php/php-src · GitHub

Skip to content

You signed in with another tab or window. Reload to refresh your session.
You signed out in another tab or window. Reload to refresh your session.
You switched accounts on another tab or window. Reload to refresh your session.

Dismiss alert

{{ message }}

Partially overwritten session files can lead to remote code execution

Critical

bukka
published
GHSA-fm2m-fjf5-v3cp
Nov 19, 2026

Package

ext-session
(PHP)

Affected versions

< 8.2.36

>= 8.3.0, < 8.3.37

>= 8.4.0, < 8.4.28

>= 8.5.0, < 8.5.13

Patched versions

8.2.36

8.3.37

8.4.28

8.5.13

Description

Summary

PHP's file-based session handler can leave a session file containing parts of two different serialized sessions if a write is interrupted. An attacker who can influence the session contents and interrupt a replacement write may be able to make PHP deserialize attacker-controlled objects when the session is next opened. A suitable object gadget chain in the application can turn this into remote code execution.

This affects the files session save handler, which is PHP's default. The issue is not limited to session upload progress or PHP 8.6.

Details

When updating a session, ps_files_write() writes the new serialized data into the existing file. The vulnerable implementation does not clear the existing contents before every write. If the operation stops after replacing only part of the file, the result can contain a prefix of the new session followed by a suffix of the old one. The file lock prevents competing session operations from accessing the file during the write, but does not make an interrupted write atomic.

PHP's session decoders use its unserialization machinery to restore session values. Carefully arranged old and new data can cause the combined file to be interpreted differently from either original session. Bytes that were previously part of an ordinary string can become serialized object data. A later session_start() or another session-reading operation can then create those objects and invoke their deserialization behavior.

Session upload progress provides one way for a remote client to influence stored session data through multipart uploads. The same underlying problem can arise when an application stores large user-controlled strings in a session. In threaded PHP builds, a hard memory-limit failure in another thread can terminate the process while the session write is in progress. This provides a way to influence where the write stops.

The fix truncates the session file to zero before writing the replacement data and aborts the write if truncation fails. An interrupted write can still lose session data, but it can no longer retain the old suffix that enables this attack.

Impact

Successful exploitation can execute code with the privileges of the PHP worker. It requires attacker influence over the session data, an interruption at a useful point in the write, and an application with a suitable deserialization gadget chain. The issue can also corrupt session state. Authentication requirements depend on how the application exposes the affected session operations.

Other session storage implementations are not affected by this specific file-write defect, although their own handling of interrupted updates must be considered separately.

Affected versions

The affected code has been present since PHP 4.1.0. This is based on code inspection.

Mitigation

Upgrade to the fixed release for your PHP branch when it becomes available. As a temporary measure, disable session.upload_progress.enabled administratively if the feature is not needed, and limit the amount of untrusted data stored in sessions. Disabling upload progress removes that input path but does not fix applications that independently store attacker-controlled session data.

A session storage backend that replaces records atomically can avoid this file-write defect. The PHP update remains the recommended fix for applications using the built-in files handler.

Severity

Critical

9.2

CVSS overall score

This score calculates overall vulnerability severity from 0 to 10 and is based on the Common Vulnerability Scoring System (CVSS).

/ 10

CVSS v4 base metrics

Exploitability Metrics

Attack Vector
Network

Attack Complexity
Low

Attack Requirements
Present

Privileges Required
None

User interaction
None

Vulnerable System Impact Metrics

Confidentiality
High

Integrity
High

Availability
High

Subsequent System Impact Metrics

Confidentiality
None

Integrity
None

Availability
None

Learn more about base metrics

CVSS v4 base metrics

Exploitability Metrics

Attack Vector:
This metric reflects the context by which vulnerability exploitation is possible. This metric value (and consequently the resulting severity) will be larger the more remote (logically, and physically) an attacker can be in order to exploit the vulnerable system. The assumption is that the number of potential attackers for a vulnerability that could be exploited from across a network is larger than the number of potential attackers that could exploit a vulnerability requiring physical access to a device, and therefore warrants a greater severity.

Attack Complexity:
This metric captures measurable actions that must be taken by the attacker to actively evade or circumvent existing built-in security-enhancing conditions in order to obtain a working exploit. These are conditions whose primary purpose is to increase security and/or increase exploit engineering complexity. A vulnerability exploitable without a target-specific variable has a lower complexity than a vulnerability that would require non-trivial customization. This metric is meant to capture security mechanisms utilized by the vulnerable system.

Attack Requirements:
This metric captures the prerequisite deployment and execution conditions or variables of the vulnerable system that enable the attack. These differ from security-enhancing techniques/technologies (ref Attack Complexity) as the primary purpose of these conditions is not to explicitly mitigate attacks, but rather, emerge naturally as a consequence of the deployment and execution of the vulnerable system.

Privileges Required:
This metric describes the level of privileges an attacker must possess prior to successfully exploiting the vulnerability. The method by which the attacker obtains privileged credentials prior to the attack (e.g., free trial accounts), is outside the scope of this metric. Generally, self-service provisioned accounts do not constitute a privilege requirement if the attacker can grant themselves privileges as part of the attack.

User interaction:
This metric captures the requirement for a human user, other than the attacker, to participate in the successful compromise of the vulnerable system. This metric determines whether the vulnerability can be exploited solely at the will of the attacker, or whether a separate user (or user-initiated process) must participate in some manner.

Vulnerable System Impact Metrics

Confidentiality:
This metric measures the impact to the confidentiality of the information managed by the VULNERABLE SYSTEM due to a successfully exploited vulnerability. Confidentiality refers to limiting information access and disclosure to only authorized users, as well as preventing access by, or disclosure to, unauthorized ones.

Integrity:
This metric measures the impact to integrity of a successfully exploited vulnerability. Integrity refers to the trustworthiness and veracity of information. Integrity of the VULNERABLE SYSTEM is impacted when an attacker makes unauthorized modification of system data. Integrity is also impacted when a system user can repudiate critical actions taken in the context of the system (e.g. due to insufficient logging).

Availability:
This metric measures the impact to the availability of the VULNERABLE SYSTEM resulting from a successfully exploited vulnerability. While the Confidentiality and Integrity impact metrics apply to the loss of confidentiality or integrity of data (e.g., information, files) used by the system, this metric refers to the loss of availability of the impacted system itself, such as a networked service (e.g., web, database, email). Since availability refers to the accessibility of information resources, attacks that consume network bandwidth, processor cycles, or disk space all impact the availability of a system.

Subsequent System Impact Metrics

Confidentiality:
This metric measures the impact to the confidentiality of the information managed by the SUBSEQUENT SYSTEM due to a successfully exploited vulnerability. Confidentiality refers to limiting information access and disclosure to only authorized users, as well as preventing access by, or disclosure to, unauthorized ones.

Integrity:
This metric measures the impact to integrity of a successfully exploited vulnerability. Integrity refers to the trustworthiness and veracity of information. Integrity of the SUBSEQUENT SYSTEM is impacted when an attacker makes unauthorized modification of system data. Integrity is also impacted when a system user can repudiate critical actions taken in the context of the system (e.g. due to insufficient logging).

Availability:
This metric measures the impact to the availability of the SUBSEQUENT SYSTEM resulting from a successfully exploited vulnerability. While the Confidentiality and Integrity impact metrics apply to the loss of confidentiality or integrity of data (e.g., information, files) used by the system, this metric refers to the loss of availability of the impacted system itself, such as a networked service (e.g., web, database, email). Since availability refers to the accessibility of information resources, attacks that consume network bandwidth, processor cycles, or disk space all impact the availability of a system.

CVSS:4.0/AV:N/AC:L/AT:P/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N

CVE ID

CVE-2026-126714

Weaknesses

Weakness
CWE-367

Time-of-check Time-of-use (TOCTOU) Race Condition

The product checks the state of a resource before using that resource, but the resource's state can change between the check and the use in a way that invalidates the results of the check.
Learn more on MITRE.

Weakness
CWE-662

Improper Synchronization

The product utilizes multiple threads, processes, components, or systems to allow temporary access to a shared resource that can only be exclusive to one process at a time, but it does not properly synchronize these actions, which might cause simultaneous accesses of this resource by multiple threads or processes.
Learn more on MITRE.

Credits

zplinn

Reporter

iluuu1994

Remediation developer

arnaud-lb

Remediation reviewer

You can’t perform that action at this time.
