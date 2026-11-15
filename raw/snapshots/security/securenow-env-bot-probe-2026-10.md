<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://www.securenow.ai/blog/why-is-my-app-getting-env-wp-login-requests -->
<!-- fetched_at: 2026-11-16 07:11:20 -->
<!-- sha256: bf8f0d9a4e0a23c36ab21c962d41b67b9cccfc2b69aaa2397d82ca2b869d983d -->

Why Is My App Getting /.env and wp-login.php Requests?
Why Is My App Getting /.env and wp-login.php Requests?

Those requests come from automated vulnerability scanners. Bots sweep every reachable host asking for files that leak secrets ( /.env , /.git/config , /.aws/credentials ) and for software with known exploits ( /wp-login.php , /phpinfo.php , /actuator ), whether or not your app runs any of it. On a Node.js or Next.js app they are mostly noise, but any one of them returning a real 200 is an incident.

This guide covers what each probe is looking for, a five-minute check that you aren't exposing anything, what to do if you are, and how to keep the noise out of your way.

Why a Node.js app gets WordPress and PHP probes

Scanners don't fingerprint you first. A request for /wp-login.php costs them almost nothing, so they send the whole list to every host they find. They find hosts by sweeping IP ranges, by reading certificate transparency logs (every TLS certificate you issue is published, which is why a brand-new subdomain often gets probed soon after it gets a certificate) and from DNS datasets. Showing up in their traffic means you're on the internet, not that someone picked you.

The traffic typically comes from cloud and VPS address ranges, rotates IPs, and uses either a library user agent ( python-requests , Go-http-client , curl ) or a fake browser string. Blocking a single address achieves very little.

What each probe is looking for

Requested path What the scanner hopes to find Risk for a Node.js / Next.js app
/.env , /.env.local , /.env.production , /api/.env An environment file with database URLs, API keys, signing secrets High if served: every secret in it is compromised
/.git/config , /.git/HEAD An exposed Git directory; tools can rebuild source and history from it High if served: your code plus any secret ever committed
/.aws/credentials , /.ssh/id_rsa A home directory served as a web root High if served
/.DS_Store , /.vscode/sftp.json , /config.json , /docker-compose.yml File listings, deploy credentials, infrastructure config Medium to high if served
/backup.zip , /db.sql , /site.tar.gz Forgotten backups and database dumps High if served
/wp-login.php , /wp-admin/ , /xmlrpc.php WordPress to brute-force or exploit through plugins None unless WordPress runs on this host
/phpinfo.php , /info.php A PHP configuration dump with paths and environment None without PHP
/shell.php , /wso.php , /alfa.php A web shell left behind by someone else's earlier compromise None without PHP
/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php PHPUnit remote code execution (CVE-2017-9841) None without PHP
/actuator , /actuator/env , /actuator/heapdump Spring Boot management endpoints that leak config and memory None unless a Java service shares the host
/server-status Apache's status page, listing live requests and client IPs Low; check any Apache in front of you

The top half of the table is what matters for a JavaScript stack: dotfiles, config files and backups. The PHP, WordPress and Java rows are noise unless something else lives on the same host, such as a forgotten marketing site or a reverse proxy's default page.

Check that you aren't exposing anything

Run this against production, not localhost. Production is where a static directory, CDN or container image differs from what you think you shipped.

Copy BASE="https://yourapp.com"
tmp=$(mktemp)
for p in /.env /.env.local /.env.production /.git/config /.git/HEAD \
/.aws/credentials /.DS_Store /.vscode/sftp.json /config.json \
/docker-compose.yml /backup.zip /db.sql /server-status /actuator/env; do
code=$(curl -s --max-time 10 -o "$tmp" -w '%{http_code}' "$BASE$p")
printf '%s %-22s %s\n' "$code" "$p" "$(head -c 60 "$tmp" | tr -d '\r\n')"
done
rm -f "$tmp"

Every line should start with 404 (or 403). For any 200, read the preview column:

<!DOCTYPE html> or your app's HTML : a catch-all or single-page-app fallback is answering every path. It isn't a leak, but every scanner now thinks it found something, and real problems hide in that noise. Return a genuine 404 for unknown paths.

DATABASE_URL= , [core] , ref: refs/heads/ , [default] , or PK (the start of a zip file): real exposure. Skip to the next section.

Then check the places these files usually leak from in JavaScript projects.

Express static pointed at the project root. express.static(__dirname) serves everything next to your code. On Express 4, the default dotfile handling only hides a path whose last segment starts with a dot, so /.env gets a 404 while /.git/config is served. Serve a dedicated folder and set the option explicitly:

Copy app.use(express.static(path.join(__dirname, 'public'), { dotfiles: 'deny' }));

Next.js public/ . Everything in public/ is served from the site root. Look for anything that isn't a public asset:

Copy find public -name '.*' -o -name '*.sql' -o -name '*.zip' -o -name '*.bak'

Client bundles. Variables prefixed NEXT_PUBLIC_ or VITE_ are compiled into JavaScript anyone can download. After a build, search it for secret-key formats:

Copy grep -rEo "sk_live_[0-9A-Za-z]{6}|sk-proj-[0-9A-Za-z_-]{6}|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY" .next/static | head

Container images. COPY . . without a .dockerignore puts .env and .git inside the image. List what actually shipped, without needing a shell in the image:

Copy cid=$(docker create yourimage:latest)
docker export "$cid" | tar -t | grep -E '(^|/)\.(env|git)(/|$|\.)' | head
docker rm "$cid" > /dev/null

nginx and static hosting. A root that points at the repository instead of a build folder serves dotfiles. Deny them while keeping /.well-known/ , which certificate renewal and security.txt use:

Copy location ~ /\.(?!well-known/) {
deny all;
}

The same applies to S3 or CDN uploads: sync the build output directory, never the project root.

If one of them returned a 200

Treat it as a confirmed leak, not a maybe. Scanners that find a live .env are built to use what's in it. Work in this order:

Stop serving it and redeploy , then rerun the curl check. Purge the path from any CDN cache.

Rotate every secret in the file , starting with what grants the most: cloud keys, database passwords, payment and email provider keys, OAuth client secrets, then session and JWT signing secrets (rotating those logs every user out, which is the point). For an exposed .git , assume the full source and history are public: scan history with a tool such as gitleaks or trufflehog and rotate anything found there as well.

Find who fetched it. With nginx's default combined log format, field 9 is the status and field 7 the path:

Copy zcat -f /var/log/nginx/access.log* | awk '$9 == 200 && $7 ~ /^\/\.(env|git)/ {print $1, $4, $7}'

Follow those IPs. Pull everything else each one requested, then look for use of the leaked credentials on the provider side: AWS CloudTrail for the access key, your database's connection logs, the payment or email provider's API logs.

Copy zcat -f /var/log/nginx/access.log* | awk '$1 == "203.0.113.7"'

Check for persistence created since the first 200: new admin users, new API keys, changed webhook URLs, unfamiliar OAuth apps.

If every request in your logs shows the same few addresses, you're logging your load balancer rather than the client. Fix that before you need it; the proxy section of Express rate limiting in production explains how.

How to reduce the noise

You can't stop the internet scanning you. You can make each probe cheap, keep it out of your alerts, and stop chasing addresses one by one.

Answer probes with a fast 404 before routing or rendering. On Next.js, an unknown path otherwise goes through your not-found page render. Short-circuit the obvious ones in middleware (Next.js 16 renames the file to proxy.ts and the export to proxy ; the logic is the same):

Copy // middleware.ts
import { NextResponse, type NextRequest } from 'next/server';

const PROBE = /^\/(?:\.(?!well-known\/)|wp-|xmlrpc\.php|phpmyadmin|cgi-bin\/|actuator|server-status)|\.(?:php|aspx?|jsp|cgi)$/i;

export function middleware(req: NextRequest) {
if (PROBE.test(req.nextUrl.pathname)) {
return new NextResponse(null, { status: 404 });
}
return NextResponse.next();
}

In Express, reuse the same PROBE regex in middleware registered before static files and routes:

Copy app.use((req, res, next) => {
if (PROBE.test(req.path)) return res.status(404).end();
next();
});

Rate-limit IPs that collect 404s. Real visitors rarely hit more than a handful of missing pages; a scanner hits dozens in seconds. express-rate-limit can count only 404 responses. Register it before the probe filter so those 404s count, and set trust proxy correctly first or you'll be limiting your load balancer:

Copy import rateLimit from 'express-rate-limit';

app.use(rateLimit({
windowMs: 10 * 60 * 1000,
limit: 30, // 30 404s per IP per 10 minutes
skipSuccessfulRequests: true,
requestWasSuccessful: (req, res) => res.statusCode !== 404,
}));

Once an IP crosses the limit it gets a 429 on every route for the rest of the window. Keep the threshold generous if search crawlers regularly hit broken links on your site.

Block known scanner infrastructure, not individual IPs. IP-reputation feeds and managed WAF rule sets already track many of the hosts doing this, which beats a hand-kept list that goes stale as scanners rotate. The Next.js and Express bot-blocking guides cover both edge and in-process options.

Log probes quietly. Keep the records, since they're evidence if something ever returns 200, but don't alert on a 404 for /wp-login.php . Alert on the patterns below.

When it's not noise

Generic probes are background radiation. These are different and deserve a look:

A probe gets a 2xx with real content. See above.

The same IP moves from probes to your real routes : /api/auth/login , /api/users/1 , /api/users/2 , your actual admin path. It has stopped guessing and started working on your app.

Probes that match your stack. Requests carrying an x-middleware-subrequest header target the Next.js middleware bypass (CVE-2025-29927, fixed in 15.2.3 with backports to older release lines). GraphQL introspection queries are mapping your schema.

Payloads on routes that exist : ' OR 1=1-- , ../../etc/passwd , ${jndi: , <script> in parameters or bodies.

Volume on authentication : bursts of failed logins, password resets or OTP requests. That's credential stuffing or abuse, covered in how to tell if your web app is under attack .

Sequential IDs : one client walking /api/invoices/1001 , 1002 , 1003 . Enumeration only pays off if an authorization check is missing somewhere.

The useful question isn't "who is scanning me" but "did anything get a response it shouldn't have, and is anyone working on my actual routes?"

Let your coding agent sort signal from noise

Raw access logs answer "what was requested". The questions that matter are relational: which IPs probed you this week, did any probe get a 2xx, what else did those IPs touch, and are they known for abuse elsewhere.

That's the production view SecureNow adds. The securenow npm package records each request as a trace with the client IP, route and status. Its IP intelligence adds geo, abuse history and a verdict for each address, and its firewall can reject requests from known-bad IPs, using a feed refreshed hourly, before they reach your routes. With the MCP server connected, your coding agent can ask those questions directly (you can too, with securenow ip <address> and securenow ip traces <address> ) and propose a block that you approve and can reverse. Scanners won't go away; you'll know which ones deserve attention.

Next step

Run the curl check above against production today. Then paste the free secrets and API-key hygiene prompt into your coding agent to find where secrets could leak from your repository, build and deploy config. If you also want the production side, SecureNow has a 14-day trial with no credit card .

Related

How to block bot traffic in Next.js

Adding an IP firewall to Express without Cloudflare

The SecureNow Firewall

Frequently Asked Questions
Why is my server getting requests for /.env?
Automated scanners request /.env on every host they find, hoping a misconfigured server returns an environment file full of database URLs and API keys. It doesn't mean you were singled out, only that your host is reachable. It matters only if the request gets a 200 with real content.

Should I worry about wp-login.php requests on a Node.js app?
Not by themselves. Bots send WordPress paths to every site without checking what it runs, so a Node.js or Next.js app just answers 404. Make sure nothing else on the same host, such as an old marketing site, actually runs WordPress.

Should I worry about /.git/config requests?
Check that the path returns 404 in production. If your .git directory is served, attackers can rebuild your source code and its history, including any secret ever committed. Express 4's static middleware serves files inside dot-directories unless you configure it not to.

Should I block every IP that requests /.env?
Blocking them one at a time is wasted effort because scanners rotate addresses constantly. Return fast 404s, rate-limit IPs that collect many 404s, and rely on an IP-reputation feed or managed WAF rules for known scanner infrastructure.

What should I do if /.env returned a 200?
Treat it as a confirmed leak: stop serving the file, rotate every secret in it, and find every IP that received a 200 on that path. Then check your cloud, database and payment provider logs for use of those credentials.

Recommended reading
How to Investigate an Account Takeover by Asking Questions A step-by-step account takeover investigation in plain English: the ten questions to ask, where each answer lives in your logs, traces and security events, and what to check before you call it closed.
Oct 28

Why Per-IP Rate Limits Fail Against Rotating IPs (and What to Count Instead) One login, 100 rotating IPs: a 10-per-minute-per-IP limit let 275 of 275 requests through. How to spot rotation in your traffic and what to key your limits on.
Oct 27

Rate Limit per API Key, per Session or per IP in Node.js, Without Code Changes Add rate limits by route and method, counted per IP, per API key, per session cookie or globally, written in plain English and shared across servers with Redis.
Oct 27

Privacy settings
