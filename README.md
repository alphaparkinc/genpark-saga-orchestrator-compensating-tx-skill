# genpark-saga-orchestrator-compensating-tx-skill

[![CI](https://github.com/alphaparkinc/genpark-saga-orchestrator-compensating-tx-skill/actions/workflows/ci.yml/badge.svg)](https://github.com/alphaparkinc/genpark-saga-orchestrator-compensating-tx-skill/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

> Saga pattern orchestrator coordinating multi-service workflows with forward action sequencing and backward compensating transaction rollbacks.

## Architecture

```mermaid
flowchart TD
    Client[AI Agent / Transaction Client] -->|Begin Tx / Commit| Engine[genpark-saga-orchestrator-compensating-tx-skill]
    Engine --> TxCoordinator[Distributed Transaction & Saga Coordinator]
    TxCoordinator --> Storage[(Distributed Partition Stores)]
```

## Features
- Pure standard library Python implementation with strictly zero pip dependencies.
- Production-grade transactional patterns (2PC, Saga compensations, TCC reservations, Percolator).
- Native Model Context Protocol (MCP) server support for AI agent distributed transactions.

## Installation

```bash
git clone https://github.com/alphaparkinc/genpark-saga-orchestrator-compensating-tx-skill.git
cd genpark-saga-orchestrator-compensating-tx-skill
```

## Quickstart

```bash
python example_usage.py
```
