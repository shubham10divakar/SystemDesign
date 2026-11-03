"""Download openly hosted copies of the reading-canon papers into ../papers.

Usage:  python scripts/download_papers.py
Skips files that already exist. Each entry may list several mirror URLs;
the first one that returns a real PDF wins.
"""
import pathlib
import subprocess
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAPERS = ROOT / "papers"

# (era-folder/filename, [urls...])
CANON = [
    # Era 1
    ("era-1-foundations-1960s-70s/1961-little-queuing-formula-L-lambda-W.pdf", []),  # paywalled (INFORMS); add manually
    ("era-1-foundations-1960s-70s/1967-amdahl-single-processor-approach.pdf", [
        "https://www-inst.eecs.berkeley.edu/~n252/paper/Amdahl.pdf"]),
    ("era-1-foundations-1960s-70s/1965-dijkstra-concurrent-programming-control.pdf", [
        "https://rust-class.org/static/classes/class19/dijkstra.pdf"]),
    ("era-1-foundations-1960s-70s/1968-dijkstra-THE-multiprogramming-system.pdf", [
        "https://www.cs.utexas.edu/users/EWD/ewd01xx/EWD196.PDF"]),
    ("era-1-foundations-1960s-70s/1968-conway-how-do-committees-invent.pdf", [
        "https://www.melconway.com/Home/pdf/committees.pdf"]),
    ("era-1-foundations-1960s-70s/1968-denning-working-set-model.pdf", [
        "https://denninginstitute.com/pjd/PUBS/WSModel_1968.pdf"]),
    ("era-1-foundations-1960s-70s/1970-codd-relational-model.pdf", [
        "https://www.seas.upenn.edu/~zives/03f/cis550/codd.pdf"]),
    ("era-1-foundations-1960s-70s/1972-parnas-decomposing-systems-into-modules.pdf", [
        "https://www.win.tue.nl/~wstomv/edu/2ip30/references/criteria_for_modularization.pdf"]),
    ("era-1-foundations-1960s-70s/1974-cerf-kahn-packet-network-intercommunication.pdf", [
        "https://www.cs.princeton.edu/courses/archive/fall06/cos561/papers/cerf74.pdf"]),
    ("era-1-foundations-1960s-70s/1974-ritchie-thompson-unix-time-sharing.pdf", [
        "https://dsf.berkeley.edu/cs262/unix.pdf"]),
    ("era-1-foundations-1960s-70s/1978-lamport-time-clocks-ordering.pdf", [
        "https://lamport.azurewebsites.net/pubs/time-clocks.pdf"]),
    ("era-1-foundations-1960s-70s/1978-gray-notes-on-database-operating-systems.pdf", [
        "https://jimgray.azurewebsites.net/papers/dbos.pdf",
        "http://jimgray.azurewebsites.net/papers/DBOS.pdf"]),
    # Era 2
    ("era-2-distributed-theory-1980s-90s/1981-gray-transaction-concept.pdf", [
        "https://jimgray.azurewebsites.net/papers/thetransactionconcept.pdf"]),
    ("era-2-distributed-theory-1980s-90s/1982-lamport-shostak-pease-byzantine-generals.pdf", [
        "https://lamport.azurewebsites.net/pubs/byz.pdf"]),
    ("era-2-distributed-theory-1980s-90s/1983-lampson-hints-for-computer-system-design.pdf", [
        "https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/acrobat-17.pdf"]),
    ("era-2-distributed-theory-1980s-90s/1984-saltzer-reed-clark-end-to-end-arguments.pdf", [
        "https://web.mit.edu/Saltzer/www/publications/endtoend/endtoend.pdf"]),
    ("era-2-distributed-theory-1980s-90s/1984-birrell-nelson-implementing-rpc.pdf", [
        "https://web.eecs.umich.edu/~mosharaf/Readings/RPC.pdf"]),
    ("era-2-distributed-theory-1980s-90s/1985-fischer-lynch-paterson-FLP-impossibility.pdf", [
        "https://groups.csail.mit.edu/tds/papers/Lynch/jacm85.pdf"]),
    ("era-2-distributed-theory-1980s-90s/1985-chandy-lamport-distributed-snapshots.pdf", [
        "https://lamport.azurewebsites.net/pubs/chandy.pdf"]),
    ("era-2-distributed-theory-1980s-90s/1988-jacobson-congestion-avoidance-and-control.pdf", [
        "https://ee.lbl.gov/papers/congavoid.pdf"]),
    ("era-2-distributed-theory-1980s-90s/1990-herlihy-wing-linearizability.pdf", [
        "https://cs.brown.edu/~mph/HerlihyW90/p463-herlihy.pdf"]),
    ("era-2-distributed-theory-1980s-90s/1990-schneider-state-machine-approach.pdf", [
        "https://www.cs.cornell.edu/fbs/publications/SMSurvey.pdf"]),
    ("era-2-distributed-theory-1980s-90s/1994-waldo-note-on-distributed-computing.pdf", [
        "https://doc.akka.io/docs/misc/smli_tr-94-29.pdf",
        "https://scholar.harvard.edu/files/waldo/files/waldo-94.pdf"]),
    ("era-2-distributed-theory-1980s-90s/1996-gray-dangers-of-replication.pdf", [
        "https://dsf.berkeley.edu/cs286/papers/dangers-sigmod1996.pdf",
        "https://jimgray.azurewebsites.net/papers/replicationdangers.pdf"]),
    ("era-2-distributed-theory-1980s-90s/1997-karger-consistent-hashing.pdf", [
        "https://www.cs.princeton.edu/courses/archive/fall09/cos518/papers/chash.pdf",
        "https://www.akamai.com/site/en/documents/research-paper/consistent-hashing-and-random-trees-distributed-caching-protocols-for-relieving-hot-spots-on-the-world-wide-web-technical-publication.pdf"]),
    ("era-2-distributed-theory-1980s-90s/1997-fox-cluster-based-scalable-network-services.pdf", [
        "https://people.eecs.berkeley.edu/~brewer/papers/TACC-sosp.pdf"]),
    ("era-2-distributed-theory-1980s-90s/1999-fox-brewer-harvest-yield.pdf", [
        "https://s3.amazonaws.com/systemsandpapers/papers/FOX_Brewer_99-Harvest_Yield_and_Scalable_Tolerant_Systems.pdf"]),
    ("era-2-distributed-theory-1980s-90s/1998-lamport-part-time-parliament.pdf", [
        "https://lamport.azurewebsites.net/pubs/lamport-paxos.pdf"]),
    ("era-2-distributed-theory-1980s-90s/2001-lamport-paxos-made-simple.pdf", [
        "https://lamport.azurewebsites.net/pubs/paxos-simple.pdf"]),
    # Era 3
    ("era-3-internet-scale-2000s-10s/2000-brewer-CAP-podc-keynote.pdf", [
        "https://people.eecs.berkeley.edu/~brewer/cs262b-2004/PODC-keynote.pdf"]),
    ("era-3-internet-scale-2000s-10s/2002-gilbert-lynch-CAP-proof.pdf", [
        "https://groups.csail.mit.edu/tds/papers/Gilbert/Brewer2.pdf"]),
    ("era-3-internet-scale-2000s-10s/2001-brewer-lessons-from-giant-scale-services.pdf", [
        "https://people.eecs.berkeley.edu/~brewer/Giant.pdf"]),
    ("era-3-internet-scale-2000s-10s/2003-ghemawat-GFS.pdf", [
        "https://static.googleusercontent.com/media/research.google.com/en//archive/gfs-sosp2003.pdf"]),
    ("era-3-internet-scale-2000s-10s/2004-dean-ghemawat-MapReduce.pdf", [
        "https://static.googleusercontent.com/media/research.google.com/en//archive/mapreduce-osdi04.pdf"]),
    ("era-3-internet-scale-2000s-10s/2006-chang-Bigtable.pdf", [
        "https://static.googleusercontent.com/media/research.google.com/en//archive/bigtable-osdi06.pdf"]),
    ("era-3-internet-scale-2000s-10s/2006-burrows-Chubby.pdf", [
        "https://static.googleusercontent.com/media/research.google.com/en//archive/chubby-osdi06.pdf"]),
    ("era-3-internet-scale-2000s-10s/2012-corbett-Spanner.pdf", [
        "https://static.googleusercontent.com/media/research.google.com/en//archive/spanner-osdi2012.pdf"]),
    ("era-3-internet-scale-2000s-10s/2015-verma-Borg.pdf", [
        "https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/43438.pdf"]),
    ("era-3-internet-scale-2000s-10s/2007-decandia-Dynamo.pdf", [
        "https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf"]),
    ("era-3-internet-scale-2000s-10s/2007-hamilton-designing-deploying-internet-scale-services.pdf", [
        "https://www.usenix.org/legacy/event/lisa07/tech/full_papers/hamilton/hamilton.pdf"]),
    ("era-3-internet-scale-2000s-10s/2007-helland-life-beyond-distributed-transactions.pdf", [
        "https://www.cidrdb.org/cidr2007/papers/cidr07p15.pdf"]),
    ("era-3-internet-scale-2000s-10s/2009-helland-campbell-building-on-quicksand.pdf", [
        "https://www.cidrdb.org/cidr2009/Paper_133.pdf"]),
    ("era-3-internet-scale-2000s-10s/2011-shapiro-CRDTs.pdf", [
        "https://inria.hal.science/inria-00609399/document",
        "https://hal.inria.fr/inria-00609399v1/document"]),
    ("era-3-internet-scale-2000s-10s/2013-dean-barroso-tail-at-scale.pdf", [
        "https://www.barroso.org/publications/TheTailAtScale.pdf"]),
    ("era-3-internet-scale-2000s-10s/2014-bailis-coordination-avoidance.pdf", [
        "https://www.vldb.org/pvldb/vol8/p185-bailis.pdf"]),
    ("era-3-internet-scale-2000s-10s/2014-ongaro-ousterhout-Raft.pdf", [
        "https://raft.github.io/raft.pdf"]),
    ("era-3-internet-scale-2000s-10s/2015-mcsherry-scalability-but-at-what-COST.pdf", [
        "https://www.usenix.org/system/files/conference/hotos15/hotos15-paper-mcsherry.pdf"]),
    # Era 4
    ("era-4-failure-science-2014-now/2014-yuan-simple-testing-prevents-critical-failures.pdf", [
        "https://www.usenix.org/system/files/conference/osdi14/osdi14-paper-yuan.pdf"]),
    ("era-4-failure-science-2014-now/2017-huang-gray-failure.pdf", [
        "https://www.microsoft.com/en-us/research/wp-content/uploads/2017/06/paper-1.pdf"]),
    ("era-4-failure-science-2014-now/2020-hellerstein-alvaro-keeping-CALM.pdf", [
        "https://arxiv.org/pdf/1901.01930"]),
    ("era-4-failure-science-2014-now/2021-bronson-metastable-failures.pdf", [
        "https://sigops.org/s/conferences/hotos/2021/papers/hotos21-s11-bronson.pdf"]),
    ("era-4-failure-science-2014-now/2022-huang-metastable-failures-in-the-wild.pdf", [
        "https://www.usenix.org/system/files/osdi22-huang-lexiang.pdf"]),
    # Method
    ("method/2007-keshav-how-to-read-a-paper.pdf", [
        "https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf"]),
]


def fetch(url: str) -> bytes | None:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (paper-downloader)"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            data = r.read()
    except Exception as e:  # noqa: BLE001
        # Python's CA bundle fails on some university hosts; fall back to curl
        try:
            data = subprocess.run(["curl", "-sL", "-A", "Mozilla/5.0", "--max-time", "90", url],
                                  capture_output=True, check=True).stdout
        except Exception:  # noqa: BLE001
            print(f"    ! {url}: {e}")
            return None
    if not data.startswith(b"%PDF"):
        print(f"    ! {url}: not a PDF")
        return None
    return data


def main() -> int:
    PAPERS.mkdir(exist_ok=True)
    missing = []
    for name, urls in CANON:
        dest = PAPERS / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.exists():
            print(f"= {name}")
            continue
        for url in urls:
            data = fetch(url)
            if data:
                dest.write_bytes(data)
                print(f"+ {name}")
                break
        else:
            missing.append(name)
            print(f"- MISSING {name}")
    print(f"\n{len(CANON) - len(missing)}/{len(CANON)} present. Missing:")
    for m in missing:
        print("  ", m)
    return 0


if __name__ == "__main__":
    sys.exit(main())
