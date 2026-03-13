# EpiAgent: Autonomous AI for Disease Outbreak Detection

## Overview

EpiAgent is an Agentic AI system designed to detect potential disease outbreaks at an early stage by continuously analyzing multiple health-related data sources.

The system gathers information from public health databases, clinical reports, environmental data, and digital signals such as news and social media. Using Natural Language Processing (NLP) and Machine Learning (ML) techniques, the system identifies abnormal disease patterns and evaluates potential outbreak risks.

When a possible outbreak is detected, EpiAgent analyzes the severity of the situation and predicts how the disease may spread across regions. Based on this analysis, the system recommends response strategies such as vaccine planning, healthcare resource allocation, and containment measures.

The goal of EpiAgent is to provide early warning alerts and intelligent decision support for public health authorities, enabling faster and more effective responses to emerging health threats.

## System Architecture

![System Architecture](system_architecture.png)

## Workflow Diagram

![Workflow](workflow_final_diagram.png)

## How to Run the Prototype

1. Install Python 3

2. Install the required libraries

pip install pandas numpy

3. Run the manager agent

python main_agent.py

The Manager Agent coordinates multiple autonomous agents including the Data Agent, NLP Agent, Detection Agent, Prediction Agent, and Response Agent.

Each agent performs its task independently and reports its results back to the Manager Agent. The manager can also query any agent dynamically and combines all agent reports to determine potential outbreaks and recommend response actions.
