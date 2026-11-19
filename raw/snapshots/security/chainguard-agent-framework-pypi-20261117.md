<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://www.chainguard.dev/fr-FR/unchained/microsoft-agent-framework-compromised-on-pypi-november-2026 -->
<!-- fetched_at: 2026-11-20 07:13:33 -->
<!-- sha256: 773f947ddd081205b725e9fc3b97fded1f0b03a16db739ad4f82470c47d5aca5 -->

Microsoft agent-framework compromised on PyPI: 1.26.1 and 1.26.2 ship a credential stealer that runs on every Python start (November 2026)

Platform Products
Code safely with agents

Chainguard Agent Skills

Chainguard Workspaces

Chainguard Harness

Build with trusted artifacts

Chainguard Containers

Chainguard Libraries

Chainguard VMs

Chainguard OS Packages

Ship through trusted CI

Chainguard Actions

Chainguard Checks

Platform
Chainguard Factory

Chainguard Guardener

Integrations

Image Directory
Updated daily

POURQUOI CHAINGUARD Parcourir le répertoire d'images Parcourir toutes les images

Solutions Compliance
FedRAMP

PCI DSS

CMMC 2.0

SOC 2

Use Cases
AI Security

Golden Images

CVE Remediation

Industry
Technology

Public Sector

Financial Services

Telecommunications

Clients Customers
Customer Stories

Chainguard Reviews

À LA UNE Anduril fait confiance à Chainguard pour innover à la vitesse et à l'échelle requises par ses missions. Lisez l'histoire

Ressources Learn
Events & Webinars

Supply Chain Security 101

Chainguard Courses

Slack Community

Developers
Documentation

Trust Center

Major Malware Attacks

FEATURED EVENT 2026 Gartner® Magic Quadrant™ for Software Supply Chain Security Download the report

Entreprise Company
About Us

Blog

Open Source Leadership

Partners

Newsroom

Careers

Contact us

NOUS RECRUTONS Carrières chez Chainguard Voir les postes à pourvoir

Tarifs Contactez-nous Se connecter

Subscribe to our newsletter
Tous les articles 17 novembre 2026

Microsoft agent-framework compromised on PyPI: 1.26.1 and 1.26.2 ship a credential stealer that runs on every Python start (November 2026)

Quincy Castro
CISO
Chainguard

View all articles

Quincy Castro CISO

TL;DR
What happened: On November 17, 2026, two releases of Microsoft's agent-framework package on PyPI, 1.26.1 and 1.26.2, were published through the Microsoft-associated PyPI publisher with a credential stealer inside. Researchers describe it as an account compromise, not a typosquat. 1.26.2 was published after PyPI had quarantined 1.26.1.

How it runs: Each version drops a .pth file into site-packages (agent_framework_meta.pth in 1.26.1, af_runtime_diag.pth in 1.26.2). Python processes .pth files at interpreter start, so the stealer runs every time Python starts in that environment, whether or not anything imports agent_framework.

What it steals: Environment variables matching TOKEN, SECRET, PASSWORD, KEY, AZURE, AWS, GITHUB, OPENAI, PIP, NPM and NUGET; credential files including Azure CLI JSON, pip.conf, .npmrc, .netrc, Git credential stores, Docker config.json, Hugging Face tokens, Azure Pipelines .credentials, .env files and GitHub Actions runner temp files; /proc/<pid>/environ of other processes; and freshly minted GitHub Actions OIDC tokens, Azure DevOps OIDC tokens, Azure managed identity tokens for nine Azure resource types, and Azure Instance Metadata Service data.

Where it goes: zlib-compressed, base64-encoded JSON posted over HTTPS to a webhook.site endpoint hidden behind a base64 string, with User-Agent runtime-diagnostics/1.

Chainguard customers: Not affected. Chainguard Libraries for Python flagged and blocked agent-framework 1.26.1 at 20:36:08 UTC, 48 seconds after it reached PyPI, and 1.26.2 at 21:09:21 UTC, 42 seconds after publication. Neither version was ever served to customers from Chainguard Repository.

What to do: Search lockfiles, caches and build logs for agent-framework 1.26.1 or 1.26.2. On any host that installed either, do not start Python; remove the .pth and payload files with shell tools, isolate the host, rotate every credential it could reach, and revoke GitHub Actions and Azure DevOps runtime credentials.

agent-framework is Microsoft's SDK for building AI agents, and it sits in exactly the environments this stealer targets: CI runners with OIDC federation to Azure, developer machines with Azure CLI logins, and production workloads with managed identities. The payload is built for that audience. It does not spray for every credential type; it goes for Azure managed identity tokens, GitHub Actions and Azure DevOps OIDC tokens, and the local files where AI developers keep provider keys.
This post covers what the two releases do, how to check whether you installed them, and why Chainguard Libraries customers never received them.
Affected packages
Two PyPI releases of agent-framework. The GitHub source is not reported as modified.
agent-framework 1.26.1 , published November 17, 2026 at 20:35:20 UTC. Payload files: agent_framework_meta.pth and _telemetry.py.

agent-framework 1.26.2 , published November 17, 2026 at 21:08:39 UTC, after PyPI had quarantined 1.26.1. Payload files: af_runtime_diag.pth and af_runtime_diag.py.

The Microsoft-associated PyPI publisher has been quarantined. Researchers believe the attacker may still hold publishing access, so treat any further agent-framework release on November 17 or 18 with suspicion until Microsoft confirms it.
What the malware does
The two versions use the same technique with renamed files. Details below are from the 1.26.2 artifact.
Startup trigger. af_runtime_diag.pth is 23 bytes: a single import of af_runtime_diag. Python runs .pth files when the interpreter starts, so the stealer runs on pip, pytest, IDE language servers and every script in the environment, not only code that uses agent_framework. It sets _AF_TEL=1 as a guard against running twice and forks a child process, falling back to a daemon thread.

Collect. Hostname, username, working directory, the first 20 command-line arguments, and every environment variable whose name matches TOKEN, SECRET, PASSWORD, KEY, AZURE, AWS, GITHUB, OPENAI, PIP, NPM or NUGET. Up to 80 credential files under 256 KiB each: Azure CLI JSON, pip.conf, .npmrc, .netrc, Git credential stores, Docker config.json, Hugging Face tokens, Foundry config, Azure Pipelines .credentials, .env and JSON app files, and GitHub Actions runner temp files. Up to 300 /proc/<pid>/environ entries filtered for secret-like names, so it reads other processes' secrets too.

Mint new tokens. It requests GitHub Actions OIDC tokens for the api://AzureADTokenExchange and https://management.azure.com/ audiences, Azure DevOps OIDC tokens (API 7.1), and Azure managed identity tokens for Management, AI, ML, Cognitive Services, Storage, Key Vault, Search, Graph and Container Registry. It also reads the Azure Instance Metadata Service at 169.254.169.254.

Exfiltrate. Everything is serialized to JSON, zlib-compressed at level 9, base64-encoded and sent by HTTPS POST to a webhook.site URL stored as a base64 string. Headers are Content-Type: application/octet-stream and User-Agent: runtime-diagnostics/1. Errors are swallowed by broad exception handlers.

What it does not do. No second-stage download, no command parsing, no OS-level persistence. Once the files are removed from site-packages the stealer is gone. The damage is the credentials already sent.

Indicators of compromise
Packages
pypi/agent-framework@1.26.1

pypi/agent-framework@1.26.2

Files in site-packages
1.26.1: agent_framework_meta.pth, _telemetry.py

1.26.2: af_runtime_diag.pth (SHA256 325e7e9f0ec94e41ad1a1b7a3f18a6b8b5bffece2e2b97b8d3369eb967452f93), af_runtime_diag.py (SHA256 54d885b7d7161c9ed96489c66364c4bfbf635929166843bba10d97d46b5a2e1f), agent_framework_meta/__init__.py (SHA256 5f04333fc30dc7a1af5407996249761531ee75df423f3ea58460dc64ae8e49f1), agent_framework-1.26.2.dist-info/METADATA (SHA256 056b52a6cec4e911cb6e7debae8fd49dad3255ef109357d0f7a386b0a2bc7461)

Network
https://webhook.site/d381fd80-ec62-42ad-8f5c-d1b15103c9bb and the same path with ?t=telemetry. Block the full path, not the webhook.site domain, which is a legitimate shared service.

HTTP headers User-Agent: runtime-diagnostics/1 and Content-Type: application/octet-stream on outbound POSTs

Host
Environment variable _AF_TEL=1 in a Python process

Outbound requests to 169.254.169.254 from a process that should not need instance metadata

How to check if you're affected
Warning: do not run Python or pip in an environment you suspect. Each interpreter start runs the payload again. Use shell tools.
Search lockfiles and manifests: grep -rn "agent-framework" requirements*.txt poetry.lock uv.lock Pipfile.lock pyproject.toml, and look for 1.26.1 or 1.26.2.

Search for the payload files: find / -path "*site-packages/af_runtime_diag.pth" -o -path "*site-packages/af_runtime_diag.py" -o -path "*site-packages/agent_framework_meta.pth" -o -path "*site-packages/_telemetry.py" 2>/dev/null

List executable .pth lines in every site-packages directory and inspect any you do not recognize.

Search CI build logs and pip caches for either version. A cached wheel means a build installed it.

Search proxy and DNS logs for the webhook UUID path and for the runtime-diagnostics/1 user agent.

In Azure, review managed identity and OIDC token issuance for the affected workloads in the window after install.

Immediate steps if you're affected
Isolate the host or runner and stop any CI job that installed either version.

Remove the payload before starting Python again. Delete the .pth and .py files above and their __pycache__ entries with shell tools. pip uninstall starts Python and runs the stealer once more.

Rotate everything the process could read: every environment variable secret, pip, npm and NuGet tokens, Git and Docker credentials, Hugging Face and OpenAI keys, Azure CLI sessions, and any secret in a .env file on the host.

Revoke runtime identities. Invalidate GitHub Actions and Azure DevOps OIDC-derived sessions, rotate federated credentials, and review Azure activity logs for managed identity use you did not initiate.

Treat other processes' secrets as exposed. The stealer reads /proc environ, so anything running on the same host at the time is in scope.

Rebuild environments and images from a known-good dependency set. Pin agent-framework to a confirmed-clean version once Microsoft publishes one.

Why Chainguard customers were protected
Chainguard Libraries for Python customers never received either version. Every new package version is scanned for malicious behavior before it can be served from Chainguard Repository. Our malware and greyware scanner blocked both releases before any customer could pull them.
agent-framework 1.26.1 reached PyPI at 20:35:20 UTC on November 17. blocked it at 20:36:08 UTC, 48 seconds later.

agent-framework 1.26.2 reached PyPI at 21:08:39 UTC. blocked it at 21:09:21 UTC, 42 seconds later.

Both blocks were made without any outside signal. No OSV or vendor advisory existed when our scanner acted, and the first public write-up appeared more than an hour later. The decision came from what the scan found in the wheel itself: a .pth file with executable code, a payload that reads .npmrc, .git-credentials, .netrc, Docker config and Hugging Face tokens, references to the cloud instance metadata endpoint, and a new network import that the previous release did not have. The scan classified the behavior as overt hostile behavior with concealment.
Chainguard Containers are not affected. Chainguard does not ship agent-framework in any image, and our Python images pull dependencies through Chainguard Libraries rather than directly from PyPI.
Customers with a cooldown policy had a second layer: a new release is held until it has aged, which keeps a same-day compromise like this one out of reach regardless of scan outcome.
The bigger picture
A trusted publisher is not a trusted release. Both versions came from the Microsoft-associated PyPI publisher. Provenance tells you which account pushed the button, not whether the account was theirs that day. The wheel's behavior is the only thing you can verify.

The .pth trick keeps working. LiteLLM 1.107.0 in October used the same startup hook. It runs before any application code and on tools that never import the package, so an unused dependency in a lockfile is still a live stealer.

The target is the AI build chain. The credential list is Azure identities, OIDC tokens, Hugging Face and OpenAI keys. Attackers are going where the model access and the cloud spend are.

Seconds matter when the second release follows the quarantine. 1.26.2 shipped 33 minutes after 1.26.1, after PyPI had already quarantined the first. A per-version block that fires in under a minute, with no human in the loop, is what covers that gap.

Want to learn more about Chainguard?
Chainguard Libraries lets your team turn off direct access to PyPI, npm, Maven Central, Go Proxy and NuGet and use secure-by-default endpoints instead. Every package version is scanned for malware and greyware, built from verified source where possible, and held by cooldown policies you set, so a release like agent-framework 1.26.1 never reaches a developer or a runner. Learn more about Chainguard Libraries for Python , or get in touch with our team.

Share this article

Articles connexes

sécurité 19 nov. 2026
What CISOs and CTOs need to do to minimize agentic risk in 2027

Behn Williams + 1 other

sécurité 19 nov. 2026
PHP's November security release: What it is and what to update

Quincy Castro

sécurité 18 nov. 2026
Innovating safely with AI: Security and engineering leaders on life after the patch era

Quincy Castro + 3 others

sécurité 18 nov. 2026
React2STEAL: What it is and what to check

Quincy Castro

sécurité 17 nov. 2026
Java4Shell: How a malformed Base64 string breaks the JVM on AVX-512

Quincy Castro

sécurité 16 nov. 2026
Prevention Under Pressure: Why most AI governance is "detection wearing prevention clothes"

John Sapp + 1 other

Commencez à développer avec Chainguard
