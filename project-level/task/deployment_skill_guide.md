# A guide to writing a product's deployment skill

The deployment skill of a product is the skill an agent reads when it prepares or checks a
deployment of that product: what runs where, how a change reaches it, what the agent may touch and
what only the human may. The-way holds no such skill, because what to run and where differs for
every product. It holds a list of what such a skill covers (WAY-139) and this guide, which shows on
one real skill what an answer to each item of the list can look like.

## What the guide is, and what it is not

- **Who reads it, and when.** The agent that writes or completes a deployment skill, for the item of
  *To do* that the check in `<the-way>/project-level/task/skill/resolve_gaps.md` adds for that work,
  or for the task split off for it. That item and that task point here. The refinement of any other
  task does not read this file.
- **It binds nothing.** What binds is the list in WAY-139 and the check of it in
  `resolve_gaps.md`. Whether a skill covers an item is decided there, not here. The product writes
  and keeps its own skill. This guide is no ready-made skill, and no skill for any kind of server:
  the skill shown below describes one small rented server behind a tunnel, and a product on a hosted
  platform, a container service or another machine answers the same questions with other words.
- **Where the example comes from.** The skill `loop2-deploy` of the public product loop2, read at
  one commit: [`SKILL.md`](https://github.com/mariusznazar/loop2/blob/e54f23c0ea3bd1db13d2635333417eb50412d6a0/.claude/skills/loop2-deploy/SKILL.md)
  and, beside it, the three files of its
  [`references/`](https://github.com/mariusznazar/loop2/tree/e54f23c0ea3bd1db13d2635333417eb50412d6a0/.claude/skills/loop2-deploy/references).
  Every fragment below is taken from that commit. Loop2 may have changed its skill since; the
  fragments show how a product answered at that commit.

## How to read a part

Each part below stands for one item of the list and has two halves.

- **The questions the product answers.** What the item asks, in the words of a product that is not
  loop2. The questions help to write an answer; they set no condition, and the list in WAY-139 and
  the check in `resolve_gaps.md` alone decide whether a skill covers an item.
- **How loop2 answered.** A short fragment of the skill, shortened where it says `…`. What belongs
  to loop2 alone, its server, its tunnel and Cloudflare settings, its commands, paths, names and
  deployment parameters, stands inside `[loop2: …]`. What stands outside the brackets is the shape
  of the answer, which another product may keep and fill with its own. The public address of the game
  and the sender address of its mail are replaced by `game.example.com` and `game@example.com`, and
  where the original names the place where its owner keeps a copy of a secret, the fragment says
  that the copy stays outside the server, with the human.

## 1. What the skill is for and when an agent reaches for it

A session finds a skill by its description, so the description is the first answer.

Questions:

- What may a person or an agent ask of this skill, in the words they would use: deploy, see what
  runs, roll back, read a log, rotate a secret, learn why a deployment failed?
- Does the description name each of those topics, and say when to use the skill, so that a session
  that meets such a question finds it without being told its name?
- What does the first page tell a reader who knows nothing of the product: what runs, where, and
  how a change reaches it?
- What does the skill leave to other documents or to the human alone, and does it say so?

How loop2 answered:

> description: How [loop2: loop2's test-server] deployment works - seeing which commit runs, reading
> the deploy log and [loop2: its exit codes 2-8], [loop2: database backups and restores], rolling
> back, [loop2: blocking or unblocking a player account], what an agent may read on the server
> versus what only the human changes, secrets, setup, failed deployments, the log record and alerts.
> Use for any question about deploying or the [loop2: test server].
>
> [loop2: Loop2 runs in a Docker Compose project with an application and a Cloudflare Tunnel
> connector.] … A push to [loop2: `main` starts `.github/workflows/deploy.yml`, whose SSH call
> passes the commit to the installed `/usr/local/bin/loop2-deploy`]. The server fetches the code,
> prepares both images before replacing either container, recreates both services, waits for their
> health checks, then probes the application inside its container. Nothing is shipped from GitHub to
> the server.
>
> The public address is `https://game.example.com/`. [loop2: Cloudflare's remotely managed tunnel
> forwards it to `http://app:3000` over the private Compose network. The application publishes no
> host port.]

## 2. A preview of deployments

The list says "a preview of deployments" and does not define it. This guide reads it as both of
two things, and the skill of loop2 answers each in its own place: how to see what a deployment did
and what runs now, and how the human puts a change on the server to look at before it is merged.

Questions:

- Who starts a deployment, and what starts it: a merge, a command, a button?
- Can a change be deployed to look at before it reaches the product's main line, and who does that?
- How does anyone tell which version runs now, by a source that cannot be wrong about it (the
  running thing itself, not the checkout beside it)?
- Where does a deployment write its stages and its end, and what does a good end and a bad end look
  like in that record?
- How is the health of what runs checked after a deployment, and what does a passing check prove
  and not prove?

How loop2 answered:

> The [loop2: server log] starts a run with `start: commit <sha>, path: ..., running commit: <sha>`
> and ends with `deployed <sha>, previously <sha>` or `stage <name>: ... (exit N)`. …
>
> The running application commit comes from its label, not the checkout or connector image. Run
> this in bash on the server (…): [loop2: `docker inspect --type container --format '{{ index
> .Config.Labels "org.opencontainers.image.revision" }}' loop2`]
>
> Internal application probe … Expected lines: [loop2: root `200` and API `404 application/json`
> (charset may follow)]. This proves internal HTTP only; the human checks the public page/API and
> [loop2: outside-host IPv6 port] separately.

And for a change before the merge, the skill describes the human's trial deployment of the branch:

> The request stays a blocked draft until [loop2: the password measurement and the public journey]
> have been done on its head commit. The human does everything here (…). … **Deployment.** Run
> [loop2: `loop2-deploy <request head sha>` with `SSH_ORIGINAL_COMMAND` unset]. The server log must
> end with `deployed <sha>, previously <sha>`. Check both services' health, the internal probe and
> [loop2: both limits] with the narrow commands in [loop2: `SKILL.md`].

## 3. Where the secrets lie and how they are rotated

Questions:

- Which secrets does the running product need, and where does each lie: a file, a store of the
  platform, a variable of the host? Which of them reach the running product, and which only the
  automation that deploys?
- Who can read each at run time, and what happens when it is missing or malformed: does the product
  refuse to start, and does the deployment fail visibly?
- Where is a copy kept outside the server, so that losing the server does not lose the secret, and
  who holds it? (The skill names the kind of place, never the secret.)
- How is each secret rotated: the steps in order, who runs each, what the product does meanwhile
  (do users stay signed in, is there an outage), and how long an old value stays valid before it is
  retired?
- What may an agent read about a secret (its owner and mode, never its content), and what must it
  never print or copy into the repository or a request?

How loop2 answered:

> **Session keys:** the file [loop2: `/etc/loop2/session-secrets`] holds [loop2: a JSON array of
> keys, newest first, owner root, group 1000, mode 0440], outside the checkout. [loop2: Compose
> mounts it read-only only into `app`.] The human creates it before the first deployment of [loop2:
> an accounts commit] and rotates it; a copy stays outside the server, with the human. … A missing
> or invalid file stops the application before it listens: the deployment ends with [loop2: exit 8].

In its setup reference, the rotation is written as the human's steps, each with its check:

> **Rotating: a new key first, the old one kept.** 1. Set the file from the current one with a new
> key prepended. The block stops, with the file unchanged, if the file is not in
> the [loop2: one-line form this procedure writes] (…). 2. Replace the copy kept outside the server with
> the file's new content. 3. Read the running application commit from its label (not the checkout's
> HEAD) and deploy exactly that commit with the installed script, … Deployment force-recreates the
> application, which reads the file again; [loop2: players stay signed in]. 4. Check … that a player
> who was signed in before is still signed in.
>
> **Retiring an old key.** Remove a key no earlier than [loop2: 30 days after the last deployment
> that could sign with it]: …, since [loop2: a session lasts 30 days from its last request and every
> response is signed again with the first key]. …

The same reference keeps a list of rotations, one line for each secret, so that a reader finds the
right sequence by the secret's name:

> - **[loop2: Tunnel token]:** read the currently running application revision label …, [loop2:
> refresh the token in Cloudflare, replace the server file] … Deploy that running application SHA
> using the [loop2: installed script]. …
> - **[loop2: SMTP password]:** replace the file and the private copy, then deploy the running
> application commit to recreate the container; …

## 4. Rollback, with its number of steps and what happens to the data

Questions:

- What is a rollback of this product, in the commands or requests a person runs, and how many steps
  does it take? Is there more than one route (a fast one that lasts until the next deployment, a
  durable one through a revert)?
- Who runs each step?
- What happens to the data: is anything restored, or does the data stay as it is while the code goes
  back? What does the product keep outside the code that a rollback does not touch?
- What can make a rollback impossible or harmful, such as data in a form older code refuses?
- Which changes outside the code does a rollback not undo (settings of a host, DNS, installed
  scripts), and how are they undone?
- What is checked after a rollback?

How loop2 answered:

> An ordinary rollback within the same route is one deployment: merge a revert request, or the human
> runs [loop2: `loop2-deploy <earlier sha>`]. A fast rollback lasts until the next push to `main`;
> a revert keeps the branch and server aligned. No earlier product image is retained for recovery.
>
> **A rollback changes code, never data.** The accounts, sessions and session-key file stay as they
> are, … and nothing is restored from an earlier time. … An application refuses a database whose
> schema version is newer than it knows, so an old commit may fail health with [loop2: exit 8] on a
> newer database. …

Where a rollback crosses a change of route, its troubleshooting reference lists four Cloudflare
changes and then counts the steps:

> … [loop2: 3. Restore the Origin Rule matching only `game.example.com`, destination port 18080.] …
> This is **[loop2: script installation, one deployment and four Cloudflare changes]**; public
> traffic can be unavailable between those actions. …

## 5. What the agent does and what the human does

This part may not contradict WAY-140: an effect outside the product's repository (on a server, in
DNS, on keys or on an external account) is made only by a human, through a human action the task
document names; reading outside the repository stays with the agent.

Questions:

- Which reads may the agent make, by which commands, and how are they bounded (a tail of a fixed
  size, a search for a fixed string)?
- Which reads must it never make, because they expose a secret or personal data?
- Which changes are the human's? Who prepares the commands for the human?
- Does the tool the agent uses to reach the host enforce these limits, or are they an agreement the
  skill states, and does the skill say which?
- What may the agent put into a report of what it read, and what does it leave out?

How loop2 answered:

> The agent reads only, through the [loop2: `mikrus` MCP: `servers` gives the server ID and `exec`
> runs commands]. Never copy the ID, server name, SSH port, user, address or any secret into
> repository files or requests. The MCP has full rights, so the following limits are an agreement:
>
> - Allowed: [loop2: bounded `tail` of the deploy log; `docker ps`; `docker compose -p loop2 ps` …;
> the metadata of the session-key file only, `stat -c '%U %g %a' /etc/loop2/session-secrets`
> (expects `root 1000 440`)] …
> - No [loop2: token-file, session-key-file or SMTP-password-file] reads, … no reading or copying of
> the [loop2: account database or its volume] (it holds e-mail addresses and password hashes), …
> arbitrary container execution, restarts, deployments, key changes or secret rotation. …
>
> Every server or Cloudflare change is the human's, [loop2: except deployment started by the existing
> automation]. The agent prepares the commands. …

The sentence names a third actor beside the agent's reads and the human's changes: the automation
the product already has, here the deployment of a merged commit. A skill names that automation too,
and the human's merge is what starts the automated deployment; what a task changes outside the
repository stays the human's (WAY-140). On what the agent
may say of what it read, the skill's section on seeing deployments adds:

> … Treat service logs as potentially sensitive; report selected, redacted diagnosis, not raw logs.

The skill also marks what only the human does for the one command whose output would expose data:

> **Only the human** installs the script and schedule, runs the backup, changes a key, … restores. An
> agent never runs the backup command: its fixed word sends every address and password hash to
> standard output.

## 6. How to read the logs

Questions:

- Which logs exist for the running product and for its deployments, and where does each lie?
- By which exact commands does an agent read each, bounded so that it never pulls a whole log?
- How does the record show a stage and a failure (a stage name, an exit code), and what does each
  value mean for the running product?
- What may the agent quote of it?
- Does the answer repeat what the product's decision on the logs says about how an agent reads
  them (WAY-165)? A skill and a decision that give an agent two instructions drift apart, so the
  skill repeats the decision's answer, and a change of the decision is followed by a rewrite of the
  skill (WAY-139). A decision silent on how an agent reads the logs answers nothing for this item;
  the skill then answers it as it answers the others.

How loop2 answered:

> **How an agent reads it.** Bounded, and by a fixed string: for a failure from before the last
> deployment, [loop2: `grep -F -m 50 -- '"failure":"' /var/log/loop2-app.log
> /var/log/loop2-app.log.1`] (`-m` limits each file), then [loop2: `zgrep -F -m 50`] on the older
> ones. …

Its section on log stages and exit codes holds the table of the deploy log's ends:

> | Exit | Stage | Meaning | Running services |
> |---|---|---|---|
> | 0 | — | [loop2: both healthy; internal HTTP passed] | [loop2: new commit] |
> | 5 | resources | [loop2: less than 1024 MiB available memory, 4 GiB free Docker disk, or unreadable] | untouched |
> | 8 | switch, probe | [loop2: either service fails health within 120 seconds or internal HTTP fails] | may be partly running or broken |

The table is loop2's own, a list of the exit codes it gives; the rows for the codes 2 to 4, 6 and 7
are left out here. What carries to another product is that the log names each stage and each end, and that
the skill says what each means for the running product.

## 7. How long the record lives, between deployments too

Questions:

- Where does the record of what the running product does go, and what part of it dies when a
  deployment replaces the thing that wrote it?
- For each place it lies in: how long does a line live, and what bounds it (age, size, rotation)?
- Does the record survive a deployment, a restart of the host and a rollback? What does it miss?
- Does it hold personal data, and how are its lines reported?

Two examples of an answer:

- a lifetime stated for each place, with what bounds it and what it misses; or
- the human's refusal to settle the item, recorded in the skill. WAY-139 says that a skill that
  records the refusal covers the item, and that the question does not return at a later deployment.

How loop2 answered (the first kind):

> **How long each lives.** A running container's log: until the next deployment, and [loop2: not
> above about 100 MB]. The dump: [loop2: `logrotate` rotates it weekly, or sooner when it passes 100 MiB, and
> keeps four rotated files …, so a line lives about four weeks, shorter when the size forces a
> rotation]. It survives deployments, a host restart and a rollback to an older commit, as long as
> [loop2: the installed deploy script is the one that has the dump]. It misses a container removed
> any other way than by that script, and the few seconds between the copy and the stop of the old
> container.

In its paragraph on how an agent reads the record, the skill adds what the file holds:

> … The file holds the game's lines for those weeks, with [loop2: `accountId` values, and the human's
> `account-block` lines]: it is the retention of that data [loop2: (D-252)], and its lines are
> reported selected and redacted like other service logs.

The refusal is not loop2's, which settled the item. An answer of that kind, in words written for this
guide:

> **How long the record lives.** The human has chosen to leave this unsettled. This skill gives no
> answer to it, and an agent does not ask again.

## 8. How a human learns of a failure

Questions:

- Does something tell the human that the running product failed, without the human looking: a tool
  that collects failures, an alert, a scheduled check? Which, and what does each see?
- What does each fail to see: a host that is off, the service the notice itself depends on?
- What does a message hold, and what is kept out of it because of the way it travels?
- How often does it send, and what is held back?
- What does an agent read once a message has arrived?
- What is the answer when nothing tells the human, and the human chose it knowingly?

A complete answer is one of three: a tool that collects failures, an alert, or a deliberate absence
(WAY-270). The absence is a full answer when the skill says that nothing tells the human and that the
human chose it.

How loop2 answered (an alert, with its limits):

> **The three ways the owner learns the game failed.** 1. **The watcher** ([loop2: `loop2-watch`,
> root, cron every five minutes]). It reads state and health of [loop2: both containers] and the fresh failure
> lines of the game container's log … and calls [loop2: `pusher`] with a fixed subject and one fixed
> [loop2: Polish] sentence per kind, which name the kind and send the reader here. It never puts a
> number, a commit, an account or any output into a message, because [loop2: `pusher` may travel
> unencrypted]. … [loop2: At most one message per kind in six hours and six in all in 24 hours]; …
> 2. **The scheduled check of the public address** ([loop2: `.github/workflows/check-address.yml`]).
> [loop2: Every five minutes, at minutes that are not the top of the hour,] GitHub Actions opens the
> public address, [loop2: up to six attempts 20 seconds apart], and the run fails unless one
> answers 200. GitHub then
> notifies the owner of the failed run. It sees what the watcher cannot: a server that is off, a
> fallen tunnel, a Cloudflare fault. 3. **[loop2: The browser's report.]** …
>
> **The four limits of the scheduled check.** Alone it fails in four ways. (1) When the server and
> GitHub are both down, nothing is sent. (2) GitHub disables a scheduled workflow after 60 days with
> no activity in the repository, … (3) GitHub sends the failure notice … to the user who last changed
> the cron line, so notifications set off, or set on another account, give a silence taken for "it
> works". …

The deliberate absence is not loop2's either. An answer of that kind, in words written for this guide:

> **How a human learns of a failure.** Nothing tells the human. No tool collects failures and no alert
> is set; the human chose this and learns of a failure from the people who use the product.
