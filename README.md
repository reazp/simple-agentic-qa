# Simple Agentic QA

A simple agentic question-answering system using Python and AI agents.

## Files

simple-agentic-qa/
│
├── tests/
│ └── test_simple_get_request.py
│
├── agent/
│ ├── **init**.py
│ ├── runner.py
│ ├── failure_parser.py
│ ├── fixer.py
│ └── github_client.py
│
├── requirements.txt
├── agent_main.py
└── .github/workflows/ci.yml

## Setup

1. Create a virtual environment
2. Install dependencies
3. Run the agent

## Agentic Logic Flow

Run pytest
↓
Pytest Fails
↓
Agent Runs
↓
Parse Failure
↓
Call API To Validate
↓
Generate Fix Suggestion
↓
Create New Branch
↓
Modify Test File
↓
Commit
↓
Open Pull Request

## Usage

```bash
python agent.py
```
