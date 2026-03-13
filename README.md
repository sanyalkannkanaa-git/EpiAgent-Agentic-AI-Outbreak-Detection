# EpiAgent: Autonomous AI for Disease Outbreak Detection

## Overview

EpiAgent is an Agentic AI system designed to detect potential disease outbreaks at an early stage by continuously analyzing multiple health-related data sources.

The system gathers information from public health databases, clinical reports, environmental data, and digital signals such as news and social media. Using Natural Language Processing (NLP) and Machine Learning (ML) techniques, the system identifies abnormal disease patterns and evaluates potential outbreak risks.

When a possible outbreak is detected, EpiAgent analyzes the severity of the situation and predicts how the disease may spread across regions. Based on this analysis, the system recommends response strategies such as vaccine planning, healthcare resource allocation, and containment measures.

The goal of EpiAgent is to provide early warning alerts and intelligent decision support for public health authorities, enabling faster and more effective responses to emerging health threats.
Note: This project presents a prototype simulation of an Agentic AI outbreak detection system intended to demonstrate system architecture and decision workflow.

## System Architecture

![System Architecture](system_architecture.png)

## Multi-Agent Design

EpiAgent follows a manager-driven multi-agent architecture.

A central **Manager Agent** coordinates several specialized autonomous agents:

- **Data Agent** – collects and preprocesses health data
- **NLP Agent** – extracts signals from reports and news
- **Detection Agent** – detects anomalies in case trends
- **Prediction Agent** – estimates outbreak severity and spread risk
- **Response Agent** – generates recommended public health actions

Each agent performs its task independently and reports results back to the Manager Agent.  
The Manager Agent can query any agent dynamically and combines all results to make the final outbreak assessment.

## Workflow Diagram

![Workflow](workflow_final_diagram.png)

## Project Structure

main_agent.py – Manager agent that coordinates all other agents  

data_agent.py – Collects and preprocesses health data  

nlp_agent.py – Extracts health-related signals from reports and news  

detection_agent.py – Detects abnormal disease patterns using anomaly detection  

prediction_agent.py – Estimates outbreak severity and potential spread  

response_agent.py – Generates response recommendations based on predicted severity  

health_data.csv – Example dataset used for the prototype  

system_architecture.png – System architecture diagram  

workflow_final_diagram.png – Multi-agent workflow diagram

## How to Run the Prototype

1. Install Python 3

2. Install the required libraries

pip install pandas numpy

3. Run the manager agent

python main_agent.py

The Manager Agent coordinates multiple autonomous agents including the Data Agent, NLP Agent, Detection Agent, Prediction Agent, and Response Agent.

Each agent performs its task independently and reports its results back to the Manager Agent. The manager can also query any agent dynamically and combines all agent reports to determine potential outbreaks and recommend response actions.

## Technologies Used
Python  
Pandas  
NumPy  
Agent-based modular architecture  
Simple anomaly detection (Z-score)  
Prototype epidemic prediction logic

## Future Improvements

Integrate real-time health surveillance data sources  
Use Large Language Models for medical report analysis  
Apply epidemiological models such as SIR or SEIR  
Add geospatial outbreak risk mapping  
Deploy as a real-time health monitoring platform


