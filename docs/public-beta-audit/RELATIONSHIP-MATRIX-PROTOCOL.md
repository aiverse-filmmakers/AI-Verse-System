# Whole-System Relationship Matrix Protocol

**Date:** 2026-09-15  
**Purpose:** ensure "everything in relation with everything else" is audited without wasting context on meaningless pairwise rereads.

## 1. Direction matters

A relationship is directional.

~~~text
A -> B
~~~

is audited separately from:

~~~text
B -> A
~~~

because read/write/control authority may differ.

## 2. Pair states

Each directional repo pair receives one state:

- UNKNOWN
- REQUIRED
- ALLOWED
- FORBIDDEN
- NONE

### REQUIRED
Current supported architecture requires the relation.

### ALLOWED
Relation may exist but is not required for baseline operation.

### FORBIDDEN
The architecture relies on this direct relation not existing.

Example:
Dashboard -> Token projection may be required.
Dashboard -> Token canonical database write may be forbidden.

### NONE
No current direct relationship is intended or found.

NONE is not assumed automatically. Sensitive pairs need negative-space evidence.

## 3. Relation dimensions

One pair may have several dimensions with different states:

- lifecycle/discovery;
- read;
- write;
- command/control;
- event;
- identity/scope;
- permission/approval;
- telemetry/cost;
- credential/effect;
- release/version;
- migration;
- health/readiness.

Example:

~~~text
Multiple Bots -> Token
telemetry evidence: REQUIRED
canonical pricing write: FORBIDDEN
historical/global cost read: ALLOWED/REQUIRED through supported Token projection
~~~

## 4. Matrix construction

### A0
Create the matrix with UNKNOWN states.

### A1
Every standalone repo records:
- outbound claims;
- inbound claims;
- forbidden dependency claims.

These claims do not yet resolve the matrix.

### A2.1
Resolve claims by checking both sides and implementation evidence.

If repo A claims B supports endpoint X but B does not, record:
- matrix relation PARTIAL/CONTRADICTED;
- finding;
- affected journeys.

## 5. Complete-system guarantee

With 14 scoped repositories there are 182 directional inter-repo pairs.

We do **not** reread both repos from scratch 182 times.

Instead:

1. A1 reconstructs each repo once.
2. A2.1 classifies all 182 directional pairs from the independent packets.
3. REQUIRED/FORBIDDEN/sensitive NONE pairs get focused evidence checks.
4. Later A2 tasks audit relation dimensions across the entire graph.
5. A3 verifies the graph in real end-to-end journeys.

This gives all-pair coverage without context explosion.

## 6. Sensitive forbidden seams

Always inspect, where relevant:

- Dashboard direct canonical owner writes;
- Apps direct canonical owner writes;
- Gateway durable semantic Memory ownership;
- Brain security/permission enforcement;
- Multiple Bots canonical Token pricing/cost ownership;
- Automations bypassing consent/permission;
- Connections leaking raw credentials;
- Distribution mutating runtime state outside lifecycle contracts;
- direct cross-system/workspace reads;
- any component writing another owner's private state files/DB directly.

## 7. Matrix cell evidence

A resolved cell should record:

~~~text
From:
To:
Dimension:
State:
Evidence:
Contract:
Observed implementation:
Tests:
Contradictions:
Finding IDs:
Last reviewed ref(s):
~~~

## 8. Completion rule

A2.1 is not complete until:

- all pairs are classified;
- every REQUIRED pair has at least one evidence path;
- every FORBIDDEN pair has explicit negative-space/enforcement evidence;
- sensitive NONE pairs have evidence;
- unresolved material UNKNOWN cells become findings;
- matrix refs match the audit snapshot.
