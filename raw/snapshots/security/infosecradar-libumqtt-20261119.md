<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://infosecradar.com/stories/2026/11/19/libumqtt -->
<!-- fetched_at: 2026-11-20 07:12:14 -->
<!-- sha256: d493290637a64bed6cfb6bab5c81682bd7810b6ebd320b1b73b17a28bb5efa54 -->

libumqtt — InfoSecRadar

Summary

A critical vulnerability (CVE-2026-125132) has been identified in libumqtt versions up to and including 1.1.1. Successful exploitation could lead to denial of service, memory corruption, or information disclosure for remote attackers. No patches are currently available, and users are advised to contact libumqtt for support.

IFF Assessment

FOE
This vulnerability allows remote attackers to cause denial of service, memory corruption, and information disclosure, posing a significant risk to affected systems.

Severity

8.6

High

The CVSS score of 8.6 (HIGH) is assigned due to the vulnerability's attack vector (Network), low complexity, no privileges or user interaction required, and its impact on confidentiality, integrity, and availability.

Defender Context

This vulnerability in libumqtt, an MQTT client library, affects multiple critical infrastructure sectors, making it a significant concern for defenders. The lack of available patches and the open nature of the vulnerability (remote, unauthenticated exploitation) necessitate proactive monitoring and potential segmentation or isolation of affected systems.

Read Full Story →
