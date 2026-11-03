# System Design Papers — Reading Tracker

A lineage-ordered reading canon for systems research, from 1960s foundations to modern failure science, with a note for every paper read.

## Layout

| Folder | Contents |
|---|---|
| [`papers/`](papers/) | PDFs grouped by era (open/author-hosted copies) |
| [`notes/`](notes/) | One note per paper, in the same era folder as its PDF and named like it (`<year>-<author>-<topic>.md`). Start from [`notes/_TEMPLATE.md`](notes/_TEMPLATE.md) |
| [`books/`](books/) | Books list and any copies you own ([`books/README.md`](books/README.md)) |
| [`scripts/`](scripts/) | `download_papers.py` re-fetches any missing PDFs into the right era folder |

`papers/` and `notes/` share the same era folders:

```
papers/                                notes/
├── era-1-foundations-1960s-70s/       ├── era-1-foundations-1960s-70s/
├── era-2-distributed-theory-1980s-90s/├── era-2-distributed-theory-1980s-90s/
├── era-3-internet-scale-2000s-10s/    ├── era-3-internet-scale-2000s-10s/
├── era-4-failure-science-2014-now/    ├── era-4-failure-science-2014-now/
└── method/                            └── method/
```

## How to mark progress

- **PDF:** 📄 links to the file in `papers/<era>/`. ❌ means no free copy was found; drop your own copy into that era's folder with the filename the script lists.
- **Status:** ⬜ not started · 🟨 reading · ✅ read
- **Notes:** after reading, copy `notes/_TEMPLATE.md` to `notes/<era>/<pdf-name>.md` and replace `—` with `[notes](notes/<era>/<pdf-name>.md)`.

Method: Keshav's three passes ([📄](papers/method/2007-keshav-how-to-read-a-paper.pdf)). Target: about 2 papers a week, roughly 100 a year.

---

## Era 1 (1960s–70s): Foundations of decomposition and concurrency

| # | Year | Paper | PDF | Status | Notes |
|---|---|---|---|---|---|
| 1 | 1961 | Little — *A Proof for the Queuing Formula L = λW* | ❌ ([INFORMS](https://doi.org/10.1287/opre.9.3.383)) | ⬜ | — |
| 2 | 1967 | Amdahl — *Validity of the Single Processor Approach to Achieving Large Scale Computing Capabilities* | ❌ ([ACM](https://doi.org/10.1145/1465482.1465560)) | ⬜ | — |
| 3 | 1965 | Dijkstra — *Solution of a Problem in Concurrent Programming Control* | ❌ ([ACM](https://doi.org/10.1145/365559.365617)) | ⬜ | — |
| 4 | 1968 | Dijkstra — *The Structure of the "THE"-Multiprogramming System* | [📄](papers/era-1-foundations-1960s-70s/1968-dijkstra-THE-multiprogramming-system.pdf) | ⬜ | — |
| 5 | 1968 | Conway — *How Do Committees Invent?* | [📄](papers/era-1-foundations-1960s-70s/1968-conway-how-do-committees-invent.pdf) | ⬜ | — |
| 6 | 1968 | Denning — *The Working Set Model for Program Behavior* | [📄](papers/era-1-foundations-1960s-70s/1968-denning-working-set-model.pdf) | ⬜ | — |
| 7 | 1970 | Codd — *A Relational Model of Data for Large Shared Data Banks* | [📄](papers/era-1-foundations-1960s-70s/1970-codd-relational-model.pdf) | ⬜ | — |
| 8 | 1972 | Parnas — *On the Criteria To Be Used in Decomposing Systems into Modules* ⭐ | [📄](papers/era-1-foundations-1960s-70s/1972-parnas-decomposing-systems-into-modules.pdf) | ⬜ | — |
| 9 | 1974 | Cerf & Kahn — *A Protocol for Packet Network Intercommunication* | [📄](papers/era-1-foundations-1960s-70s/1974-cerf-kahn-packet-network-intercommunication.pdf) | ⬜ | — |
| 10 | 1974 | Ritchie & Thompson — *The UNIX Time-Sharing System* | [📄](papers/era-1-foundations-1960s-70s/1974-ritchie-thompson-unix-time-sharing.pdf) | ⬜ | — |
| 11 | 1978 | Lamport — *Time, Clocks, and the Ordering of Events in a Distributed System* | [📄](papers/era-1-foundations-1960s-70s/1978-lamport-time-clocks-ordering.pdf) | ⬜ | — |
| 12 | 1978 | Gray — *Notes on Data Base Operating Systems* | [📄](papers/era-1-foundations-1960s-70s/1978-gray-notes-on-database-operating-systems.pdf) | ⬜ | — |

## Era 2 (1980s–90s): Distributed systems theory and design principles

| # | Year | Paper | PDF | Status | Notes |
|---|---|---|---|---|---|
| 13 | 1981 | Gray — *The Transaction Concept: Virtues and Limitations* | [📄](papers/era-2-distributed-theory-1980s-90s/1981-gray-transaction-concept.pdf) | ⬜ | — |
| 14 | 1982 | Lamport, Shostak & Pease — *The Byzantine Generals Problem* | [📄](papers/era-2-distributed-theory-1980s-90s/1982-lamport-shostak-pease-byzantine-generals.pdf) | ⬜ | — |
| 15 | 1983 | Lampson — *Hints for Computer System Design* ⭐ (re-read yearly) | [📄](papers/era-2-distributed-theory-1980s-90s/1983-lampson-hints-for-computer-system-design.pdf) | ⬜ | — |
| 16 | 1984 | Saltzer, Reed & Clark — *End-to-End Arguments in System Design* | [📄](papers/era-2-distributed-theory-1980s-90s/1984-saltzer-reed-clark-end-to-end-arguments.pdf) | ⬜ | — |
| 17 | 1984 | Birrell & Nelson — *Implementing Remote Procedure Calls* | [📄](papers/era-2-distributed-theory-1980s-90s/1984-birrell-nelson-implementing-rpc.pdf) | ⬜ | — |
| 18 | 1985 | Fischer, Lynch & Paterson — *Impossibility of Distributed Consensus with One Faulty Process* (FLP) | [📄](papers/era-2-distributed-theory-1980s-90s/1985-fischer-lynch-paterson-FLP-impossibility.pdf) | ⬜ | — |
| 19 | 1985 | Chandy & Lamport — *Distributed Snapshots* | [📄](papers/era-2-distributed-theory-1980s-90s/1985-chandy-lamport-distributed-snapshots.pdf) | ⬜ | — |
| 20 | 1988 | Jacobson — *Congestion Avoidance and Control* | [📄](papers/era-2-distributed-theory-1980s-90s/1988-jacobson-congestion-avoidance-and-control.pdf) | ⬜ | — |
| 21 | 1990 | Herlihy & Wing — *Linearizability* | [📄](papers/era-2-distributed-theory-1980s-90s/1990-herlihy-wing-linearizability.pdf) | ⬜ | — |
| 22 | 1990 | Schneider — *Implementing Fault-Tolerant Services Using the State Machine Approach* | [📄](papers/era-2-distributed-theory-1980s-90s/1990-schneider-state-machine-approach.pdf) | ⬜ | — |
| 23 | 1994 | Waldo et al. — *A Note on Distributed Computing* | [📄](papers/era-2-distributed-theory-1980s-90s/1994-waldo-note-on-distributed-computing.pdf) | ⬜ | — |
| 24 | 1996 | Gray et al. — *The Dangers of Replication and a Solution* | [📄](papers/era-2-distributed-theory-1980s-90s/1996-gray-dangers-of-replication.pdf) | ⬜ | — |
| 25 | 1997 | Karger et al. — *Consistent Hashing and Random Trees* | [📄](papers/era-2-distributed-theory-1980s-90s/1997-karger-consistent-hashing.pdf) | ⬜ | — |
| 26 | 1997 | Fox et al. — *Cluster-Based Scalable Network Services* | [📄](papers/era-2-distributed-theory-1980s-90s/1997-fox-cluster-based-scalable-network-services.pdf) | ⬜ | — |
| 27 | 1999 | Fox & Brewer — *Harvest, Yield, and Scalable Tolerant Systems* | [📄](papers/era-2-distributed-theory-1980s-90s/1999-fox-brewer-harvest-yield.pdf) | ⬜ | — |
| 28 | 1998 | Lamport — *The Part-Time Parliament* | [📄](papers/era-2-distributed-theory-1980s-90s/1998-lamport-part-time-parliament.pdf) | ⬜ | — |
| 29 | 2001 | Lamport — *Paxos Made Simple* | [📄](papers/era-2-distributed-theory-1980s-90s/2001-lamport-paxos-made-simple.pdf) | ⬜ | — |

## Era 3 (2000s–2010s): Internet-scale systems

| # | Year | Paper | PDF | Status | Notes |
|---|---|---|---|---|---|
| 30 | 2000 | Brewer — *Towards Robust Distributed Systems* (CAP keynote, PODC) | [📄](papers/era-3-internet-scale-2000s-10s/2000-brewer-CAP-podc-keynote.pdf) | ⬜ | — |
| 31 | 2002 | Gilbert & Lynch — *Brewer's Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services* | [📄](papers/era-3-internet-scale-2000s-10s/2002-gilbert-lynch-CAP-proof.pdf) | ⬜ | — |
| 32 | 2001 | Brewer — *Lessons from Giant-Scale Services* | [📄](papers/era-3-internet-scale-2000s-10s/2001-brewer-lessons-from-giant-scale-services.pdf) | ⬜ | — |
| 33 | 2003 | Ghemawat et al. — *The Google File System* | [📄](papers/era-3-internet-scale-2000s-10s/2003-ghemawat-GFS.pdf) | ⬜ | — |
| 34 | 2004 | Dean & Ghemawat — *MapReduce* | [📄](papers/era-3-internet-scale-2000s-10s/2004-dean-ghemawat-MapReduce.pdf) | ⬜ | — |
| 35 | 2006 | Chang et al. — *Bigtable* | [📄](papers/era-3-internet-scale-2000s-10s/2006-chang-Bigtable.pdf) | ⬜ | — |
| 36 | 2006 | Burrows — *The Chubby Lock Service* | [📄](papers/era-3-internet-scale-2000s-10s/2006-burrows-Chubby.pdf) | ⬜ | — |
| 37 | 2012 | Corbett et al. — *Spanner* | [📄](papers/era-3-internet-scale-2000s-10s/2012-corbett-Spanner.pdf) | ⬜ | — |
| 38 | 2015 | Verma et al. — *Large-scale Cluster Management at Google with Borg* | [📄](papers/era-3-internet-scale-2000s-10s/2015-verma-Borg.pdf) | ⬜ | — |
| 39 | 2007 | DeCandia et al. — *Dynamo: Amazon's Highly Available Key-value Store* | [📄](papers/era-3-internet-scale-2000s-10s/2007-decandia-Dynamo.pdf) | ⬜ | — |
| 40 | 2007 | Hamilton — *On Designing and Deploying Internet-Scale Services* | [📄](papers/era-3-internet-scale-2000s-10s/2007-hamilton-designing-deploying-internet-scale-services.pdf) | ⬜ | — |
| 41 | 2007 | Helland — *Life Beyond Distributed Transactions* | [📄](papers/era-3-internet-scale-2000s-10s/2007-helland-life-beyond-distributed-transactions.pdf) | ⬜ | — |
| 42 | 2009 | Helland & Campbell — *Building on Quicksand* | [📄](papers/era-3-internet-scale-2000s-10s/2009-helland-campbell-building-on-quicksand.pdf) | ⬜ | — |
| 43 | 2011 | Shapiro et al. — *Conflict-Free Replicated Data Types* | ❌ ([HAL](https://inria.hal.science/inria-00609399)) | ⬜ | — |
| 44 | 2013 | Dean & Barroso — *The Tail at Scale* ⭐ | [📄](papers/era-3-internet-scale-2000s-10s/2013-dean-barroso-tail-at-scale.pdf) | ⬜ | — |
| 45 | 2014 | Bailis et al. — *Coordination Avoidance in Database Systems* | [📄](papers/era-3-internet-scale-2000s-10s/2014-bailis-coordination-avoidance.pdf) | ⬜ | — |
| 46 | 2014 | Ongaro & Ousterhout — *In Search of an Understandable Consensus Algorithm* (Raft) | [📄](papers/era-3-internet-scale-2000s-10s/2014-ongaro-ousterhout-Raft.pdf) | ⬜ | — |
| 47 | 2015 | McSherry et al. — *Scalability! But at what COST?* | [📄](papers/era-3-internet-scale-2000s-10s/2015-mcsherry-scalability-but-at-what-COST.pdf) | ⬜ | — |

## Era 4 (2014–now): Failure science

| # | Year | Paper | PDF | Status | Notes |
|---|---|---|---|---|---|
| 48 | 2014 | Yuan et al. — *Simple Testing Can Prevent Most Critical Failures* | [📄](papers/era-4-failure-science-2014-now/2014-yuan-simple-testing-prevents-critical-failures.pdf) | ⬜ | — |
| 49 | 2017 | Huang et al. — *Gray Failure: The Achilles' Heel of Cloud-Scale Systems* | [📄](papers/era-4-failure-science-2014-now/2017-huang-gray-failure.pdf) | ⬜ | — |
| 50 | 2020 | Hellerstein & Alvaro — *Keeping CALM: When Distributed Consistency Is Easy* | [📄](papers/era-4-failure-science-2014-now/2020-hellerstein-alvaro-keeping-CALM.pdf) | ⬜ | — |
| 51 | 2021 | Bronson et al. — *Metastable Failures in Distributed Systems* ⭐ | [📄](papers/era-4-failure-science-2014-now/2021-bronson-metastable-failures.pdf) | ⬜ | — |
| 52 | 2022 | Huang et al. — *Metastable Failures in the Wild* (follow-up) | [📄](papers/era-4-failure-science-2014-now/2022-huang-metastable-failures-in-the-wild.pdf) | ⬜ | — |

## Method

| # | Year | Paper | PDF | Status | Notes |
|---|---|---|---|---|---|
| 53 | 2007 | Keshav — *How to Read a Paper* | [📄](papers/method/2007-keshav-how-to-read-a-paper.pdf) | ⬜ | — |

---

## Books

See [`books/README.md`](books/README.md) for the list and progress.

## Progress

- Papers read: **0 / 53**
- Books read: **0 / 7**

## 12-month plan

- [ ] **Months 1–3:** Eras 1 and 2, plus Harchol-Balter's book. Start the incident journal.
- [ ] **Months 4–6:** Eras 3 and 4. Learn TLA+. Pick one research direction and write a two-page problem statement.
- [ ] **Months 7–9:** Build a simulator or model. Reproduce a known result first (for example, tail-latency amplification from *The Tail at Scale*), then push into the new question.
- [ ] **Months 10–12:** Workshop paper or SoCC/Middleware submission, plus an ACM Queue-style essay on the same topic.
