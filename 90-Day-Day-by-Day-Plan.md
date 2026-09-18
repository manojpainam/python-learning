# 90-Day Python + Full-Stack Engineer Roadmap (Final Merged Plan)

**Target:** 3+ YOE
**Primary focus:** Python + Backend + Full-Stack Development
**Duration:** 90 days
**Weekdays:** 1.5–2 hours/day
**Weekends:** 5+ hours/day
**Buffer:** 7 dedicated revision/buffer days, woven into the plan (Days 7, 14, 35, 49, 63, 75, 82)

---

## How to Use This File

- Change `[ ]` to `[x]` when a task is completed.
- Use the **Status** column/marker:
  - `⬜ Not Started`
  - `🟡 In Progress`
  - `🟢 Done`
  - `🔴 Needs Revision`
- Do not mark a topic `Done` just because you watched/read it.
- A topic is **Done** only when you can:
  1. Explain it without notes.
  2. Write a small example/code for it.
  3. Answer at least 1–2 interview questions about it.
  4. Explain where it is used in a real application.

---

## Master Day-by-Day Status Table (Quick View)

Use this table for a one-glance overview of the whole 90 days. Full topic checklists, interview questions, and practice tasks for each day are in the **Phase-by-Phase Detail** section below — open that section when you actually sit down to study a given day.

| Day | Phase | Topic | Status |
|---:|---|---|---|
| 1 | 0 | Baseline: Python basics + DSA baseline | 🟢 |
| 2 | 0 | Python fundamentals — data structures deep dive | 🟢 |
| 3 | 0 | Functions + scope (LEGB, closures, recursion) | 🟢 |
| 4 | 0 | OOP basics | ⬜ |
| 5 | 0 | Git + Linux basics | ⬜ |
| 6 | 0 | DSA basics (Big O, arrays, hashmap, stack, queue) | ⬜ |
| 7 | 0 | **Weekly Revision / Buffer** | ⬜ |
| 8 | 1 | Python execution model (CPython, bytecode) | ⬜ |
| 9 | 1 | Python data structure internals (hashing, list/dict internals) | ⬜ |
| 10 | 1 | Comprehensions (list/dict/set/generator expr) | ⬜ |
| 11 | 1 | Iterators + generators | ⬜ |
| 12 | 1 | Decorators | ⬜ |
| 13 | 1 | Context managers | ⬜ |
| 14 | 1 | **Weekly Revision / Buffer** | ⬜ |
| 15 | 1 | Exception handling | ⬜ |
| 16 | 1 | Modules + packages | ⬜ |
| 17 | 1 | Virtual environments + packaging | ⬜ |
| 18 | 1 | Testing (pytest, fixtures, mocking) | ⬜ |
| 19 | 1 | Logging | ⬜ |
| 20 | 1 | Python concurrency (threads, processes, GIL, async) | ⬜ |
| 21 | 1 | Big Python Revision + 30-min mock interview | ⬜ |
| 22 | 2 | HTTP fundamentals | ⬜ |
| 23 | 2 | HTTP status codes | ⬜ |
| 24 | 2 | REST API design | ⬜ |
| 25 | 2 | Authentication + authorization (JWT) | ⬜ |
| 26 | 2 | FastAPI basics (CRUD) | ⬜ |
| 27 | 2 | FastAPI intermediate (Pydantic, DI, middleware) | ⬜ |
| 28 | 2 | Weekly Revision | ⬜ |
| 29 | 2 | Django fundamentals | ⬜ |
| 30 | 2 | Django ORM | ⬜ |
| 31 | 2 | Database relationships (1:1, 1:M, M:M) | ⬜ |
| 32 | 2 | Django REST Framework | ⬜ |
| 33 | 2 | DRF auth + permissions | ⬜ |
| 34 | 2 | API optimization (N+1, select/prefetch_related, caching) | ⬜ |
| 35 | 2 | **Backend Revision / Buffer** — build a mini backend | ⬜ |
| 36 | 3 | SQL fundamentals | ⬜ |
| 37 | 3 | SQL joins | ⬜ |
| 38 | 3 | Aggregations | ⬜ |
| 39 | 3 | Subqueries | ⬜ |
| 40 | 3 | CTEs | ⬜ |
| 41 | 3 | Window functions | ⬜ |
| 42 | 3 | SQL Revision | ⬜ |
| 43 | 3 | Database fundamentals (keys, constraints) | ⬜ |
| 44 | 3 | Normalization (1NF-3NF, denormalization) | ⬜ |
| 45 | 3 | Indexes | ⬜ |
| 46 | 3 | Transactions + ACID | ⬜ |
| 47 | 3 | Isolation levels | ⬜ |
| 48 | 3 | Database optimization (explain plans, slow queries) | ⬜ |
| 49 | 3 | **SQL + Database Revision / Buffer** | ⬜ |
| 50 | 4 | JavaScript fundamentals | ⬜ |
| 51 | 4 | Scope + closures (JS) | ⬜ |
| 52 | 4 | Arrays + objects (map/filter/reduce, destructuring) | ⬜ |
| 53 | 4 | Async JavaScript (promises, async/await) | ⬜ |
| 54 | 4 | Event loop | ⬜ |
| 55 | 4 | API calls (fetch, GET/POST, error/loading states) | ⬜ |
| 56 | 4 | JavaScript Revision | ⬜ |
| 57 | 4 | React fundamentals | ⬜ |
| 58 | 4 | React hooks (useState, useEffect) | ⬜ |
| 59 | 4 | More React hooks (useMemo, useCallback, useRef) | ⬜ |
| 60 | 4 | React forms (controlled components, validation) | ⬜ |
| 61 | 4 | React API integration | ⬜ |
| 62 | 4 | Routing + authentication (protected routes) | ⬜ |
| 63 | 4 | **React Revision / Buffer** — build a small app | ⬜ |
| 64 | 5 | Full-stack project: architecture + requirements | ⬜ |
| 65 | 5 | Full-stack project: database design (ER diagram) | ⬜ |
| 66 | 5 | Full-stack project: backend build (1/3) | ⬜ |
| 67 | 5 | Full-stack project: backend build (2/3) | ⬜ |
| 68 | 5 | Full-stack project: backend build (3/3) | ⬜ |
| 69 | 5 | Full-stack project: frontend build (1/3) | ⬜ |
| 70 | 5 | Full-stack project: frontend build (2/3) | ⬜ |
| 71 | 5 | Full-stack project: frontend build (3/3) | ⬜ |
| 72 | 5 | Full-stack project: integration (1/2) | ⬜ |
| 73 | 5 | Full-stack project: integration (2/2) | ⬜ |
| 74 | 5 | Full-stack project: testing (backend + frontend) | ⬜ |
| 75 | 5 | **Project Cleanup / Buffer** — README, docs, refactor | ⬜ |
| 76 | 6 | Docker | ⬜ |
| 77 | 6 | CI/CD (GitHub Actions) | ⬜ |
| 78 | 6 | Cloud fundamentals | ⬜ |
| 79 | 6 | System design basics (scalability, availability) | ⬜ |
| 80 | 6 | System design components (LB, cache, queue, CDN) | ⬜ |
| 81 | 6 | System design practice (URL shortener, rate limiter) | ⬜ |
| 82 | 6 | **System Design Revision / Buffer** | ⬜ |
| 83 | 7 | Python interview revision | ⬜ |
| 84 | 7 | Backend interview revision | ⬜ |
| 85 | 7 | SQL interview revision | ⬜ |
| 86 | 7 | DSA interview revision | ⬜ |
| 87 | 7 | System design interview practice | ⬜ |
| 88 | 7 | Project interview prep (architecture Q&A) | ⬜ |
| 89 | 7 | Full mock interview (5 rounds × 30 min) | ⬜ |
| 90 | 7 | Final revision — no new topics | ⬜ |

---

# Overall Roadmap

| Phase | Days | Focus | Status |
|---|---:|---|---|
| Phase 0 | 1–7 | Fundamentals + Baseline | ⬜ |
| Phase 1 | 8–21 | Strong Python | ⬜ |
| Phase 2 | 22–35 | Backend Development | ⬜ |
| Phase 3 | 36–49 | SQL + Databases | ⬜ |
| Phase 4 | 50–63 | JavaScript + React | ⬜ |
| Phase 5 | 64–75 | Full-Stack Project | ⬜ |
| Phase 6 | 76–82 | DevOps + System Design | ⬜ |
| Phase 7 | 83–90 | Interview Preparation | ⬜ |

---

# Daily Study Pattern

## Weekdays — 1.5–2 Hours
- [ ] 45–60 min — New concept
- [ ] 30–40 min — Coding / problem solving
- [ ] 15–20 min — Revision

## Weekends — 5+ Hours
- [ ] 2 hours — Main topic / project
- [ ] 1.5 hours — DSA + SQL
- [ ] 1.5–2 hours — Project + revision
- [ ] Breaks included between sessions

---

# Revision System

For every important topic:
- [ ] D+1 — Quick recall
- [ ] D+3 — Short practice
- [ ] D+7 — Weekly revision
- [ ] D+14 — Recall + coding
- [ ] D+30 — Long-term revision
- [ ] D+60 — Interview-style recall
- [ ] D+90 — Final revision

### Revision Rule
Do not reread everything. Instead:
> Close your notes and try to explain/code the concept from memory.

---

# PHASE-BY-PHASE DETAIL

# PHASE 0 — DAYS 1–7
# Programming + Software Engineering Basics

## Day 1 — Baseline
### Python Basics
- [X] Variables
- [X] Data types
- [X] `if / elif / else`
- [X] Loops
- [X] Functions
- [X] Lists
- [X] Tuples
- [X] Dictionaries
- [X] Sets
- [X] Strings
### DSA Baseline
- [X] Two Sum
- [X] Contains Duplicate
### Status
- [X] Day 1 completed — Status: 🟢

---

## Day 2 — Python Fundamentals
- [X] List
- [X] Tuple
- [X] Set
- [X] Dictionary
- [X] String
- [X] Mutable vs immutable
- [X] Indexing
- [X] Slicing
- [X] Iteration
- [X] Membership
- [X] Copying
- [X] `a = b` vs `a.copy()`
### Practice
- [X] Write examples for each data structure
- [X] Solve 2 small problems
### Status
- [X] Day 2 completed — Status: 🟢

---

## Day 3 — Functions + Scope
- [X] Local scope
- [X] Global scope
- [X] LEGB rule
- [X] Parameters
- [X] Default arguments
- [X] `*args`
- [X] `**kwargs`
- [X] Lambda
- [X] Closures
- [X] Recursion
### Practice
- [X] Write examples for local/global scope
- [X] Write a closure
- [X] Write a recursive function
### Interview Questions
- [X] Explain LEGB
- [X] Difference between `*args` and `**kwargs`
- [X] What is a closure?
### Status
- [X] Day 3 completed — Status: ⬜

---

## Day 4 — OOP
- [X] Class
- [X] Object
- [X] Constructor
- [X] Instance variable
- [X] Class variable
- [X] Instance method
- [X] `classmethod`
- [X] `staticmethod`
- [X] Inheritance
- [X] Composition
- [ ] Polymorphism
- [ ] Encapsulation
### Interview Questions
- [ ] Composition vs inheritance
- [ ] `classmethod` vs `staticmethod`
- [ ] Class variable vs instance variable
### Practice
- [ ] Build a small OOP example
### Status
- [ ] Day 4 completed — Status: ⬜

---

## Day 5 — Git + Linux Basics
### Git
- [ ] `git clone`
- [ ] `git status`
- [ ] `git add`
- [ ] `git commit`
- [ ] `git push`
- [ ] `git pull`
- [ ] `git branch`
- [ ] `git switch`
- [ ] `git merge`
- [ ] `git rebase`
- [ ] `git stash`
- [ ] `git log`
- [ ] `git reset`
### Linux
- [ ] `ls`
- [ ] `cd`
- [ ] `pwd`
- [ ] `mkdir`
- [ ] `rm`
- [ ] `cp`
- [ ] `mv`
- [ ] `grep`
- [ ] `cat`
- [ ] `head`
- [ ] `tail`
- [ ] `ps`
- [ ] `kill`
- [ ] `chmod`
### Practice
- [ ] Create a Git repository
- [ ] Create a branch
- [ ] Make commits
- [ ] Merge branches
- [ ] Practice rebase
- [ ] Practice stash
### Status
- [ ] Day 5 completed — Status: ⬜

---

## Day 6 — DSA Basics
- [ ] Big O
- [ ] Time complexity
- [ ] Space complexity
- [ ] Arrays
- [ ] Strings
- [ ] HashMap
- [ ] Set
- [ ] Stack
- [ ] Queue
### Practice
- [ ] Solve 3–4 easy problems
- [ ] Write time and space complexity for each
### Status
- [ ] Day 6 completed — Status: ⬜

---

## Day 7 — WEEKLY REVISION / BUFFER
### Python
- [ ] Mutable vs immutable
- [ ] List vs tuple
- [ ] Set vs dictionary
- [ ] Scope
- [ ] `*args / **kwargs`
- [ ] OOP
### Git
- [ ] Branch
- [ ] Commit
- [ ] Merge
- [ ] Rebase
- [ ] Stash
### DSA
- [ ] Solve 3 problems without looking at solutions
### Buffer
- [ ] Catch up on missed topics
- [ ] Review weak areas
### Status
- [ ] Day 7 completed — Status: ⬜

---

# PHASE 1 — DAYS 8–21
# Strong Python

## Day 8 — Python Execution Model
- [ ] Python interpreter
- [ ] CPython
- [ ] Bytecode
- [ ] `.pyc`
- [ ] `is` vs `==`
### Practice
- [ ] Explain how Python code executes at a high level
### Status
- [ ] Day 8 completed — Status: ⬜

---

## Day 9 — Python Data Structures Internals
- [ ] List internals
- [ ] Dictionary internals
- [ ] Set internals
- [ ] Tuple internals
- [ ] Hashing
- [ ] Average O(1) dictionary lookup
### Interview Questions
- [ ] Why is dictionary lookup usually O(1)?
- [ ] Why is inserting into the middle of a list expensive?
### Status
- [ ] Day 9 completed — Status: ⬜

---

## Day 10 — Comprehensions
- [ ] List comprehensions
- [ ] Dictionary comprehensions
- [ ] Set comprehensions
- [ ] Generator expressions
### Practice
- [ ] Convert 5 normal loops into comprehensions
- [ ] Identify cases where a comprehension hurts readability
### Status
- [ ] Day 10 completed — Status: ⬜

---

## Day 11 — Iterators + Generators
- [ ] `iter()`
- [ ] `next()`
- [ ] `yield`
- [ ] Iterator protocol
- [ ] Generator vs list
- [ ] Lazy evaluation
### Practice
- [ ] Build a custom iterator
- [ ] Build a generator
- [ ] Explain why generators save memory
### Status
- [ ] Day 11 completed — Status: ⬜

---

## Day 12 — Decorators
- [ ] Functions as first-class objects
- [ ] Higher-order functions
- [ ] Decorators
- [ ] `@decorator`
- [ ] `*args / **kwargs` in decorators
- [ ] `functools.wraps`
### Practice
- [ ] Build `@log_execution`
- [ ] Build `@timer`
### Status
- [ ] Day 12 completed — Status: ⬜

---

## Day 13 — Context Managers
- [ ] `with`
- [ ] Context manager protocol
- [ ] `__enter__`
- [ ] `__exit__`
- [ ] `contextlib`
### Practice
- [ ] Build a custom context manager
### Status
- [ ] Day 13 completed — Status: ⬜

---

## Day 14 — WEEKLY REVISION / BUFFER
- [ ] Generators
- [ ] Decorators
- [ ] Context managers
- [ ] Comprehensions
- [ ] Python execution model
- [ ] Python data structures
- [ ] Solve 5 DSA problems
### Recall Test
- [ ] Explain each topic without notes
- [ ] Write one example for each
### Status
- [ ] Day 14 completed — Status: ⬜

---

## Day 15 — Exception Handling
- [ ] `try`
- [ ] `except`
- [ ] `else`
- [ ] `finally`
- [ ] Custom exceptions
- [ ] Exception hierarchy
- [ ] Good exception handling practices
### Practice
- [ ] Build custom exception classes
### Status
- [ ] Day 15 completed — Status: ⬜

---

## Day 16 — Modules + Packages
- [ ] Module
- [ ] Package
- [ ] `__init__.py`
- [ ] `__name__`
- [ ] `__main__`
- [ ] Imports
- [ ] Absolute vs relative imports
### Status
- [ ] Day 16 completed — Status: ⬜

---

## Day 17 — Virtual Environments + Packaging
- [ ] `venv`
- [ ] `pip`
- [ ] `requirements.txt`
- [ ] `pyproject.toml`
- [ ] Dependency management
### Practice
- [ ] Create a virtual environment
- [ ] Install dependencies
- [ ] Freeze dependencies
- [ ] Run a Python project from a clean environment
### Status
- [ ] Day 17 completed — Status: ⬜

---

## Day 18 — Testing
- [ ] Unit testing
- [ ] Integration testing
- [ ] `pytest`
- [ ] Fixtures
- [ ] Mocking
- [ ] Assertions
### Practice
- [ ] Write 5 pytest tests
- [ ] Create a fixture
- [ ] Mock an external dependency
### Status
- [ ] Day 18 completed — Status: ⬜

---

## Day 19 — Logging
- [ ] Python `logging`
- [ ] DEBUG
- [ ] INFO
- [ ] WARNING
- [ ] ERROR
- [ ] CRITICAL
- [ ] Logging best practices
### Practice
- [ ] Add logging to a small application
### Status
- [ ] Day 19 completed — Status: ⬜

---

## Day 20 — Python Concurrency
- [ ] Process
- [ ] Thread
- [ ] Coroutine
- [ ] Async programming
- [ ] GIL
- [ ] CPU-bound vs I/O-bound
### Interview Questions
- [ ] What is the GIL?
- [ ] Thread vs process?
- [ ] When would you use async?
### Status
- [ ] Day 20 completed — Status: ⬜

---

## Day 21 — BIG PYTHON REVISION
### Python
- [ ] OOP
- [ ] Decorators
- [ ] Generators
- [ ] Iterators
- [ ] Context managers
- [ ] Exceptions
- [ ] Packages
- [ ] Testing
- [ ] Logging
- [ ] GIL
- [ ] Async
### DSA
- [ ] Arrays
- [ ] HashMap
- [ ] Strings
- [ ] Solve 5 problems
### Mock Interview
- [ ] 30-minute Python mock interview
### Buffer
- [ ] Catch up on anything missed
### Status
- [ ] Day 21 completed — Status: ⬜

---

# PHASE 2 — DAYS 22–35
# Backend Development
Primary stack: **Python + FastAPI/Django + REST APIs**

## Day 22 — HTTP Fundamentals
- [ ] Client
- [ ] Server
- [ ] Request
- [ ] Response
- [ ] HTTP
- [ ] Headers
- [ ] Body
- [ ] Cookies
### Status
- [ ] Day 22 completed — Status: ⬜

---

## Day 23 — HTTP Status Codes
- [ ] 200, 201, 204
- [ ] 400, 401, 403, 404, 409, 422
- [ ] 500
### Practice
- [ ] Explain when each status code should be used
### Status
- [ ] Day 23 completed — Status: ⬜

---

## Day 24 — REST API Design
- [ ] REST principles
- [ ] Resources
- [ ] URLs
- [ ] HTTP methods
- [ ] Status codes
- [ ] Pagination
- [ ] Filtering
- [ ] Sorting
- [ ] API versioning
### Practice
- [ ] Design a User API
- [ ] Design a Product API
- [ ] Design an Order API
### Status
- [ ] Day 24 completed — Status: ⬜

---

## Day 25 — Authentication + Authorization
- [ ] Authentication
- [ ] Authorization
- [ ] Sessions
- [ ] JWT
- [ ] Access token
- [ ] Refresh token
- [ ] Roles
- [ ] Permissions
### Interview Questions
- [ ] Authentication vs authorization
- [ ] How does JWT work?
- [ ] Access token vs refresh token
### Status
- [ ] Day 25 completed — Status: ⬜

---

## Day 26 — FastAPI Basics
- [ ] FastAPI setup
- [ ] Routes
- [ ] Path parameters
- [ ] Query parameters
- [ ] Request body
- [ ] Response models
- [ ] CRUD APIs
### Practice
- [ ] Build `/users`
- [ ] Build `/products`
- [ ] Build `/orders`
### Status
- [ ] Day 26 completed — Status: ⬜

---

## Day 27 — FastAPI Intermediate
- [ ] Pydantic
- [ ] Validation
- [ ] Dependency Injection
- [ ] Middleware
- [ ] Exception handling
- [ ] Background tasks
### Practice
- [ ] Add validation
- [ ] Add centralized error handling
- [ ] Add dependency injection
### Status
- [ ] Day 27 completed — Status: ⬜

---

## Day 28 — WEEKLY REVISION
- [ ] HTTP
- [ ] Status codes
- [ ] REST
- [ ] Authentication
- [ ] FastAPI
- [ ] Pydantic
- [ ] Dependency injection
### Practice
- [ ] Build a small API from scratch without tutorial
### Status
- [ ] Day 28 completed — Status: ⬜

---

## Day 29 — Django Fundamentals
- [ ] Django project
- [ ] Django app
- [ ] URLs
- [ ] Views
- [ ] Models
- [ ] Templates
- [ ] Settings
- [ ] Migrations
### Status
- [ ] Day 29 completed — Status: ⬜

---

## Day 30 — Django ORM
- [ ] `.objects.get()`
- [ ] `.filter()`
- [ ] `.create()`
- [ ] QuerySets
- [ ] CRUD
- [ ] ORM basics
### Practice
- [ ] Write 10 ORM queries
### Status
- [ ] Day 30 completed — Status: ⬜

---

## Day 31 — Database Relationships
- [ ] One-to-One
- [ ] One-to-Many
- [ ] Many-to-Many
- [ ] ForeignKey
- [ ] Relationship queries
### Practice
- [ ] Model User → Orders
- [ ] Model Product → Orders
- [ ] Model User → Profile
### Status
- [ ] Day 31 completed — Status: ⬜

---

## Day 32 — Django REST Framework
- [ ] Serializer
- [ ] APIView
- [ ] ViewSet
- [ ] Router
- [ ] Request/response
- [ ] CRUD API
### Status
- [ ] Day 32 completed — Status: ⬜

---

## Day 33 — DRF Authentication + Permissions
- [ ] Authentication
- [ ] Permissions
- [ ] JWT integration
- [ ] Role-based access
- [ ] Protected endpoints
### Practice
- [ ] Create user/admin roles
- [ ] Protect endpoints
### Status
- [ ] Day 33 completed — Status: ⬜

---

## Day 34 — API Optimization
- [ ] `select_related`
- [ ] `prefetch_related`
- [ ] N+1 query problem
- [ ] Pagination
- [ ] Caching
- [ ] Query optimization
### Interview Questions
- [ ] What is N+1?
- [ ] `select_related` vs `prefetch_related`
- [ ] When should you cache?
### Status
- [ ] Day 34 completed — Status: ⬜

---

## Day 35 — BACKEND REVISION / BUFFER
### Mini Backend — Build:
- [ ] User
- [ ] Product
- [ ] Order
- [ ] Authentication
- [ ] CRUD
- [ ] Database
- [ ] Validation
- [ ] Pagination
- [ ] Error handling
### Interview Practice
- [ ] Explain your API architecture
- [ ] Explain authentication flow
- [ ] Explain database interaction
### Status
- [ ] Day 35 completed — Status: ⬜

---

# PHASE 3 — DAYS 36–49
# SQL + Databases

## Day 36 — SQL Fundamentals
- [ ] SELECT, FROM, WHERE, ORDER BY, GROUP BY, HAVING
### Practice
- [ ] Solve 5 SQL problems
### Status
- [ ] Day 36 completed — Status: ⬜

---

## Day 37 — SQL Joins
- [ ] INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL JOIN, Self join
### Practice
- [ ] Solve 5 join problems
### Status
- [ ] Day 37 completed — Status: ⬜

---

## Day 38 — Aggregations
- [ ] COUNT, SUM, AVG, MIN, MAX, GROUP BY, HAVING
### Practice
- [ ] Solve 5 aggregation problems
### Status
- [ ] Day 38 completed — Status: ⬜

---

## Day 39 — Subqueries
- [ ] Scalar subquery, correlated subquery, `IN`, `EXISTS`
### Practice
- [ ] Solve 5 subquery problems
### Status
- [ ] Day 39 completed — Status: ⬜

---

## Day 40 — CTEs
- [ ] `WITH`, CTE use cases, multiple CTEs, recursive CTE basics
### Practice
- [ ] Solve 3 CTE problems
### Status
- [ ] Day 40 completed — Status: ⬜

---

## Day 41 — Window Functions
- [ ] `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `LEAD`, `LAG`, `PARTITION BY`
### Practice
- [ ] Solve 5 window-function problems
### Status
- [ ] Day 41 completed — Status: ⬜

---

## Day 42 — SQL REVISION
- [ ] Joins, aggregations, subqueries, CTEs, window functions
### Practice
- [ ] Solve 10–15 SQL problems
### Status
- [ ] Day 42 completed — Status: ⬜

---

## Day 43 — Database Fundamentals
- [ ] Primary key, foreign key, candidate key, composite key, constraints
### Status
- [ ] Day 43 completed — Status: ⬜

---

## Day 44 — Normalization
- [ ] 1NF, 2NF, 3NF, denormalization, when to normalize/denormalize
### Status
- [ ] Day 44 completed — Status: ⬜

---

## Day 45 — Indexes
- [ ] Why indexes, B-Tree concept, index scan vs full table scan
- [ ] Composite index, trade-offs, selectivity
### Interview Questions
- [ ] When does an index help?
- [ ] When can an index hurt?
- [ ] How do you choose a composite index?
### Status
- [ ] Day 45 completed — Status: ⬜

---

## Day 46 — Transactions
- [ ] Transactions, ACID, commit, rollback
- [ ] Atomicity, consistency, isolation, durability
### Status
- [ ] Day 46 completed — Status: ⬜

---

## Day 47 — Isolation Levels
- [ ] Dirty read, non-repeatable read, phantom read
- [ ] Read Uncommitted, Read Committed, Repeatable Read, Serializable
### Status
- [ ] Day 47 completed — Status: ⬜

---

## Day 48 — Database Optimization
- [ ] Explain plans, slow queries, index optimization, query optimization
- [ ] N+1 queries, connection pooling
### Practice
- [ ] Take one slow query and optimize it
### Status
- [ ] Day 48 completed — Status: ⬜

---

## Day 49 — SQL + DATABASE REVISION / BUFFER
### Practice
- [ ] 10 SQL interview questions
- [ ] 5 database interview questions
- [ ] Explain indexes, transactions, isolation levels, normalization
### Status
- [ ] Day 49 completed — Status: ⬜

---

# PHASE 4 — DAYS 50–63
# JavaScript + React

## Day 50 — JavaScript Fundamentals
- [ ] `var`, `let`, `const`, data types, operators, conditionals, loops, functions
### Status
- [ ] Day 50 completed — Status: ⬜

---

## Day 51 — Scope + Closures
- [ ] Scope, lexical scope, closure, hoisting, temporal dead zone
### Practice
- [ ] Write a closure example
- [ ] Explain closure without notes
### Status
- [ ] Day 51 completed — Status: ⬜

---

## Day 52 — Arrays + Objects
- [ ] `map`, `filter`, `reduce`, `find`, `some`, `every`
- [ ] Object/array destructuring, spread/rest operator
### Practice
- [ ] Solve 5 JavaScript problems
### Status
- [ ] Day 52 completed — Status: ⬜

---

## Day 53 — Async JavaScript
- [ ] Promise, `async`, `await`, promise chaining, error handling, `Promise.all`
### Status
- [ ] Day 53 completed — Status: ⬜

---

## Day 54 — Event Loop
- [ ] Call stack, Web APIs, task queue, microtask queue, event loop
### Interview Questions
- [ ] Explain JavaScript event loop
- [ ] Promise vs callback
- [ ] Microtask vs task queue
### Status
- [ ] Day 54 completed — Status: ⬜

---

## Day 55 — API Calls
- [ ] `fetch`, GET/POST requests, headers, JSON, error handling, loading state
### Practice
- [ ] Consume your backend API from JavaScript
### Status
- [ ] Day 55 completed — Status: ⬜

---

## Day 56 — JAVASCRIPT REVISION
- [ ] Scope, closures, arrays, objects, promises, async/await, event loop, API calls
### Practice
- [ ] Solve 5 JS questions
- [ ] Explain event loop
### Status
- [ ] Day 56 completed — Status: ⬜

---

## Day 57 — React Fundamentals
- [ ] Components, JSX, props, state, composition, conditional rendering
### Practice
- [ ] Build 3 components
### Status
- [ ] Day 57 completed — Status: ⬜

---

## Day 58 — React Hooks
- [ ] `useState`, `useEffect`, dependency array, lifecycle concept
### Practice
- [ ] Build a CRUD component
### Status
- [ ] Day 58 completed — Status: ⬜

---

## Day 59 — More React Hooks
- [ ] `useMemo`, `useCallback`, `useRef`, when NOT to memoize
### Status
- [ ] Day 59 completed — Status: ⬜

---

## Day 60 — React Forms
- [ ] Controlled components, form state, validation, error messages, submit handling
### Practice
- [ ] Build login form
- [ ] Build create-item form
### Status
- [ ] Day 60 completed — Status: ⬜

---

## Day 61 — React API Integration
- [ ] API service layer, GET/POST/PUT/PATCH/DELETE, loading/error states
### Practice
- [ ] Connect React to backend
### Status
- [ ] Day 61 completed — Status: ⬜

---

## Day 62 — Routing + Authentication
- [ ] React routing, protected routes, login flow, token handling, logout, auth state
### Status
- [ ] Day 62 completed — Status: ⬜

---

## Day 63 — REACT REVISION / BUFFER
### Build
- [ ] Small React app: login, dashboard, list, create, edit, delete, API integration
### Revision
- [ ] Hooks, props, state, event loop, promises
### Status
- [ ] Day 63 completed — Status: ⬜

---

# PHASE 5 — DAYS 64–75
# Full-Stack Project

## Recommended Project
Build a production-style **Task / Job / Expense Management System**

```text
React
   ↓
REST API
   ↓
FastAPI / Django
   ↓
PostgreSQL
```

Features: Authentication, Users, Roles, CRUD, Search, Filtering, Pagination, Dashboard, Error handling, Testing, Docker

## Day 64 — Architecture
- [ ] Define requirements, user roles, features
- [ ] Draw architecture, create folder structure, define API endpoints
### Status
- [ ] Day 64 completed — Status: ⬜

---

## Day 65 — Database Design
- [ ] Design ER diagram — users, roles, main entity, supporting tables
- [ ] Relationships, indexes, constraints
### Status
- [ ] Day 65 completed — Status: ⬜

---

## Days 66–68 — Backend
- [ ] Project setup, database setup, models
- [ ] Authentication, users, CRUD
- [ ] Validation, error handling, pagination, filtering, search
### Status
- [ ] Day 66 / 67 / 68 completed — Status: ⬜

---

## Days 69–71 — Frontend
- [ ] React setup, login, dashboard
- [ ] List/create/edit page, delete action
- [ ] Search, pagination, loading/error states
### Status
- [ ] Day 69 / 70 / 71 completed — Status: ⬜

---

## Days 72–73 — Integration
- [ ] Connect frontend to backend, auth flow, protected routes
- [ ] Token handling, API error handling, form validation, loading states
### Status
- [ ] Day 72 / 73 completed — Status: ⬜

---

## Day 74 — Testing
### Backend
- [ ] Unit tests, API tests, authentication tests, validation tests, error-case tests
### Frontend
- [ ] Basic component tests, API error handling tests
### Status
- [ ] Day 74 completed — Status: ⬜

---

## Day 75 — Project Cleanup / BUFFER
- [ ] Refactor code, improve naming, remove duplication
- [ ] Review architecture, DB queries
- [ ] Add environment variables + `.env.example`
- [ ] Write README, add API docs, screenshots, setup instructions
- [ ] Review Git history
### Interview Practice
- [ ] Explain architecture, database design, authentication, API design, key technical decisions
### Status
- [ ] Day 75 completed — Status: ⬜

---

# PHASE 6 — DAYS 76–82
# DevOps + System Design

## Day 76 — Docker
- [ ] Docker image, container, Dockerfile, Docker Compose, volume, network, env vars
### Practice
- [ ] Dockerize backend
- [ ] Dockerize frontend
- [ ] Run database with Docker
### Status
- [ ] Day 76 completed — Status: ⬜

---

## Day 77 — CI/CD
- [ ] CI/CD concept, GitHub Actions, run tests automatically, build application
### Practice
- [ ] Create CI workflow
- [ ] Run tests on push
### Status
- [ ] Day 77 completed — Status: ⬜

---

## Day 78 — Cloud Fundamentals
- [ ] Server, VM, load balancer, storage, database, DNS, networking basics, env config
### Status
- [ ] Day 78 completed — Status: ⬜

---

## Day 79 — System Design Basics
- [ ] Scalability, availability, reliability, latency, throughput
- [ ] Horizontal vs vertical scaling
### Interview Practice
- [ ] Explain each term with an example
### Status
- [ ] Day 79 completed — Status: ⬜

---

## Day 80 — System Design Components
- [ ] Load balancer, cache, database, message queue, CDN, API gateway, read replica, connection pool
### Status
- [ ] Day 80 completed — Status: ⬜

---

## Day 81 — System Design Practice
### Design
- [ ] URL Shortener
- [ ] Rate Limiter
### For Each: requirements, APIs, database, components, scaling, bottlenecks, failure scenarios
### Status
- [ ] Day 81 completed — Status: ⬜

---

## Day 82 — SYSTEM DESIGN REVISION / BUFFER
### Practice
- [ ] Explain your full-stack project's architecture
- [ ] Explain what happens at 10x traffic
- [ ] Explain caching strategy, DB scaling, load balancing, queues
### Status
- [ ] Day 82 completed — Status: ⬜

---

# PHASE 7 — DAYS 83–90
# Interview Mode

From here, focus less on new material and more on **retrieval + problem solving + communication**.

## Day 83 — Python Interview
Revise: OOP, decorators, generators, iterators, context managers, memory, GIL, async, threads, processes
### Practice
- [ ] 20 Python interview questions
- [ ] 2 Python coding problems
### Status
- [ ] Day 83 completed — Status: ⬜

---

## Day 84 — Backend Interview
Revise: REST, JWT, authentication, authorization, middleware, ORM, N+1, caching, API design, validation, error handling
### Practice
- [ ] 20 backend interview questions
### Status
- [ ] Day 84 completed — Status: ⬜

---

## Day 85 — SQL Interview
Revise: joins, aggregations, subqueries, CTEs, window functions, indexes, transactions, isolation levels
### Practice
- [ ] Solve 10 SQL questions
### Status
- [ ] Day 85 completed — Status: ⬜

---

## Day 86 — DSA Interview
Priority: arrays, hashmap, strings, two pointers, sliding window, stack, binary search, linked list, trees, heap, graph, recursion/backtracking, basic DP
### Practice
- [ ] Solve 4–5 interview problems
- [ ] Explain brute force → optimized → complexity for each
### Status
- [ ] Day 86 completed — Status: ⬜

---

## Day 87 — System Design Interview
Practice: URL Shortener, Chat application, E-commerce system, Notification system
### For every design: requirements, APIs, data model, architecture, scaling, caching, failure handling
### Status
- [ ] Day 87 completed — Status: ⬜

---

## Day 88 — Project Interview
Be ready to answer: why this architecture, why Python/FastAPI/Django/React/PostgreSQL, how auth/authz works, how APIs are structured, how errors are handled, how you test, what happens at 10x traffic, what you'd improve, hardest technical problem, trade-offs made
### Status
- [ ] Day 88 completed — Status: ⬜

---

## Day 89 — FULL MOCK INTERVIEW
- [ ] Round 1 — DSA (30 min)
- [ ] Round 2 — Python (30 min)
- [ ] Round 3 — Backend (30 min)
- [ ] Round 4 — System Design (30 min)
- [ ] Round 5 — Project (30 min)
### Review
- [ ] Identify weak areas, write down questions you couldn't answer, revise them
### Status
- [ ] Day 89 completed — Status: ⬜

---

# DAY 90 — FINAL REVISION
## No New Topics
- [ ] Python: OOP, scope, decorators, generators, iterators, context managers, exceptions, GIL, async, threads, processes
- [ ] SQL: joins, window functions, CTEs, indexes, transactions, isolation levels
- [ ] Backend: REST, JWT, authentication, authorization, ORM, N+1, caching, API design
- [ ] React/JS: scope, closures, promises, async/await, event loop, components, props, state, hooks, API integration, routing
- [ ] System Design: load balancer, cache, database, queue, CDN, API gateway, scaling, availability, reliability
- [ ] DevOps: Docker, Docker Compose, CI/CD, cloud fundamentals
- [ ] Project: architecture, database, APIs, authentication, testing, deployment, trade-offs

### Final Checklist
- [ ] Resume updated (bullets quantified)
- [ ] GitHub project polished, README complete
- [ ] LinkedIn updated
- [ ] 100+ quality DSA problems targeted
- [ ] SQL practice completed
- [ ] 2+ system design mocks completed
- [ ] 2+ full mock interviews completed
- [ ] Personal interview cheat sheet completed
### Status
- [ ] Day 90 completed — Status: ⬜

---

# DSA TRACKER
Target: **100–130 quality problems**

| Topic | Target | Done | Status |
|---|---:|---:|---|
| Arrays | 10 | ⬜ | ⬜ |
| HashMap / Set | 10 | ⬜ | ⬜ |
| Strings | 8 | ⬜ | ⬜ |
| Two Pointers | 8 | ⬜ | ⬜ |
| Sliding Window | 8 | ⬜ | ⬜ |
| Stack | 6 | ⬜ | ⬜ |
| Binary Search | 8 | ⬜ | ⬜ |
| Linked List | 8 | ⬜ | ⬜ |
| Trees | 10 | ⬜ | ⬜ |
| Heap | 6 | ⬜ | ⬜ |
| Graph | 8 | ⬜ | ⬜ |
| Recursion | 5 | ⬜ | ⬜ |
| Backtracking | 5 | ⬜ | ⬜ |
| Dynamic Programming | 10 | ⬜ | ⬜ |

---

# SQL TRACKER
Target: **50+ SQL problems**

| Topic | Target | Done | Status |
|---|---:|---:|---|
| SELECT / WHERE | 5 | ⬜ | ⬜ |
| GROUP BY / HAVING | 5 | ⬜ | ⬜ |
| Joins | 10 | ⬜ | ⬜ |
| Subqueries | 5 | ⬜ | ⬜ |
| CTEs | 5 | ⬜ | ⬜ |
| Window Functions | 10 | ⬜ | ⬜ |
| Mixed Interview SQL | 10 | ⬜ | ⬜ |

---

# PYTHON INTERVIEW TRACKER

| Topic | Learned | Revised | Can Explain | Can Code | Status |
|---|---|---|---|---|---|
| Scope / LEGB | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| Mutable vs Immutable | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| OOP | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| Decorators | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| Generators | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| Iterators | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| Context Managers | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| Exceptions | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| Testing | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| Logging | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| GIL | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| Threading | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| Multiprocessing | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| Async Python | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |

---

# BACKEND TRACKER

| Topic | Learned | Practiced | Interview Ready | Status |
|---|---|---|---|---|
| HTTP | ⬜ | ⬜ | ⬜ | ⬜ |
| REST | ⬜ | ⬜ | ⬜ | ⬜ |
| Status Codes | ⬜ | ⬜ | ⬜ | ⬜ |
| JWT | ⬜ | ⬜ | ⬜ | ⬜ |
| Authentication | ⬜ | ⬜ | ⬜ | ⬜ |
| Authorization | ⬜ | ⬜ | ⬜ | ⬜ |
| FastAPI | ⬜ | ⬜ | ⬜ | ⬜ |
| Django | ⬜ | ⬜ | ⬜ | ⬜ |
| Django REST Framework | ⬜ | ⬜ | ⬜ | ⬜ |
| ORM | ⬜ | ⬜ | ⬜ | ⬜ |
| N+1 | ⬜ | ⬜ | ⬜ | ⬜ |
| Caching | ⬜ | ⬜ | ⬜ | ⬜ |
| Pagination | ⬜ | ⬜ | ⬜ | ⬜ |
| API Testing | ⬜ | ⬜ | ⬜ | ⬜ |

---

# DATABASE TRACKER

| Topic | Learned | Practiced | Interview Ready | Status |
|---|---|---|---|---|
| SQL Basics | ⬜ | ⬜ | ⬜ | ⬜ |
| Joins | ⬜ | ⬜ | ⬜ | ⬜ |
| CTEs | ⬜ | ⬜ | ⬜ | ⬜ |
| Window Functions | ⬜ | ⬜ | ⬜ | ⬜ |
| Primary / Foreign Keys | ⬜ | ⬜ | ⬜ | ⬜ |
| Normalization | ⬜ | ⬜ | ⬜ | ⬜ |
| Indexes | ⬜ | ⬜ | ⬜ | ⬜ |
| ACID | ⬜ | ⬜ | ⬜ | ⬜ |
| Transactions | ⬜ | ⬜ | ⬜ | ⬜ |
| Isolation Levels | ⬜ | ⬜ | ⬜ | ⬜ |
| Query Optimization | ⬜ | ⬜ | ⬜ | ⬜ |

---

# JAVASCRIPT + REACT TRACKER

| Topic | Learned | Practiced | Interview Ready | Status |
|---|---|---|---|---|
| JS Variables | ⬜ | ⬜ | ⬜ | ⬜ |
| Scope | ⬜ | ⬜ | ⬜ | ⬜ |
| Closures | ⬜ | ⬜ | ⬜ | ⬜ |
| Array Methods | ⬜ | ⬜ | ⬜ | ⬜ |
| Promises | ⬜ | ⬜ | ⬜ | ⬜ |
| Async/Await | ⬜ | ⬜ | ⬜ | ⬜ |
| Event Loop | ⬜ | ⬜ | ⬜ | ⬜ |
| React Components | ⬜ | ⬜ | ⬜ | ⬜ |
| Props | ⬜ | ⬜ | ⬜ | ⬜ |
| State | ⬜ | ⬜ | ⬜ | ⬜ |
| useState | ⬜ | ⬜ | ⬜ | ⬜ |
| useEffect | ⬜ | ⬜ | ⬜ | ⬜ |
| useMemo | ⬜ | ⬜ | ⬜ | ⬜ |
| useCallback | ⬜ | ⬜ | ⬜ | ⬜ |
| useRef | ⬜ | ⬜ | ⬜ | ⬜ |
| Routing | ⬜ | ⬜ | ⬜ | ⬜ |
| API Integration | ⬜ | ⬜ | ⬜ | ⬜ |
| Authentication | ⬜ | ⬜ | ⬜ | ⬜ |

---

# SYSTEM DESIGN TRACKER

| Topic | Learned | Practiced | Can Explain | Status |
|---|---|---|---|---|
| Scalability | ⬜ | ⬜ | ⬜ | ⬜ |
| Availability | ⬜ | ⬜ | ⬜ | ⬜ |
| Reliability | ⬜ | ⬜ | ⬜ | ⬜ |
| Latency | ⬜ | ⬜ | ⬜ | ⬜ |
| Throughput | ⬜ | ⬜ | ⬜ | ⬜ |
| Load Balancer | ⬜ | ⬜ | ⬜ | ⬜ |
| Cache | ⬜ | ⬜ | ⬜ | ⬜ |
| Message Queue | ⬜ | ⬜ | ⬜ | ⬜ |
| CDN | ⬜ | ⬜ | ⬜ | ⬜ |
| API Gateway | ⬜ | ⬜ | ⬜ | ⬜ |
| Database Scaling | ⬜ | ⬜ | ⬜ | ⬜ |

---

# DEVOPS TRACKER

| Topic | Learned | Practiced | Status |
|---|---|---|---|
| Docker | ⬜ | ⬜ | ⬜ |
| Dockerfile | ⬜ | ⬜ | ⬜ |
| Docker Compose | ⬜ | ⬜ | ⬜ |
| Volumes | ⬜ | ⬜ | ⬜ |
| Networks | ⬜ | ⬜ | ⬜ |
| CI/CD | ⬜ | ⬜ | ⬜ |
| GitHub Actions | ⬜ | ⬜ | ⬜ |
| Cloud Fundamentals | ⬜ | ⬜ | ⬜ |
| DNS | ⬜ | ⬜ | ⬜ |
| Load Balancing | ⬜ | ⬜ | ⬜ |

---

# WEEKLY REVIEW TEMPLATE
Copy this section every Sunday.

## Week: ______
### Topics Completed
- [ ] Topic 1
- [ ] Topic 2
- [ ] Topic 3
### DSA
Problems solved: `____`
### SQL
Problems solved: `____`
### Revision
- [ ] D+1 revision completed
- [ ] D+7 revision completed
- [ ] Old weak topics revised
### What I Still Don't Understand
1.
2.
3.
### Topics Needing Revision
1.
2.
3.
### Biggest Learning This Week
>
### Next Week's Priority
1.
2.
3.
### Overall Week Status
- [ ] 🟢 Good
- [ ] 🟡 Need improvement
- [ ] 🔴 Behind schedule

---

# FINAL 90-DAY SCORECARD

| Area | Target | Status |
|---|---|---|
| Python | Strong interview level | ⬜ |
| Backend | Strong practical level | ⬜ |
| SQL | Strong interview level | ⬜ |
| Database | Strong fundamentals | ⬜ |
| DSA | 100–130 quality problems | ⬜ |
| JavaScript | Intermediate | ⬜ |
| React | Intermediate | ⬜ |
| System Design | Interview-ready fundamentals | ⬜ |
| Docker | Practical knowledge | ⬜ |
| CI/CD | Basic practical knowledge | ⬜ |
| Cloud | Fundamentals | ⬜ |
| Full-Stack Project | Production-style project | ⬜ |
| Resume | Interview-ready | ⬜ |
| GitHub | Polished | ⬜ |
| Mock Interviews | 2+ completed | ⬜ |

---

# Target Skill Distribution

```text
Python / Backend       30%
DSA                    20%
SQL / Database         15%
Full Stack             15%
System Design          10%
DevOps / Cloud          5%
Behavioral / Resume     5%
```

---

# Important Rules

## Rule 1 — Don't Chase Quantity
100–130 **quality** DSA problems are better than 300 problems you cannot reproduce.

## Rule 2 — Understand Before Memorizing
For every coding problem:
```text
Problem → Brute Force → Why it works → Optimization → Code → Complexity → Explain without looking
```

## Rule 3 — Build While Learning
Do not wait until Day 64 to start thinking about applications. Whenever you learn a concept, ask:
> Where would I use this in a real backend/full-stack application?

## Rule 4 — Revision Is Mandatory
A topic isn't finished when you understand it once. The goal is:
> Learn → Recall → Apply → Explain → Repeat

## Rule 5 — Don't Let One Missed Day Break the Plan
Use the buffer days. If you miss a weekday:
- [ ] Move the topic to the next available buffer/revision slot.
- [ ] Do not double your study time the next day.
- [ ] Protect the long-term consistency.

---

# End Goal

By Day 90, you should be able to position yourself as:
> **Python Backend / Full-Stack Engineer with 3+ YOE**

and confidently discuss:
```text
Python → FastAPI / Django → REST APIs → PostgreSQL / SQL → React / JavaScript → Testing → Docker → CI/CD → System Design
```

The objective is not to know every technology. The objective is to become **strong, explainable, interview-ready, and capable of building real software.**