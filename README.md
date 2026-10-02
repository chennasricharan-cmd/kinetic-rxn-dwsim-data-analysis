# Kinetic Reaction DWSIM Data Analysis

A data-driven acetaldehyde PFR reactor analysis project integrating process simulation, automated data generation, machine learning, SQL analytics, Power BI visualization, and Streamlit deployment.

## 📌 Project Overview

This project develops an end-to-end workflow for analyzing an acetaldehyde Plug Flow Reactor (PFR) using simulation-generated process data.

The reactor is modeled and simulated in DWSIM, and multiple operating conditions are varied to generate a large dataset. The resulting data is then processed using Python for validation, exploratory analysis, visualization, and machine learning.

The project further integrates MySQL/SQL for structured data analysis, Power BI for interactive dashboards, and Streamlit for an interactive machine-learning application.

The overall workflow is:

**DWSIM Simulation → Data Generation → Python Analysis → Machine Learning → SQL Analytics → Power BI → Streamlit**

---

## 🎯 Objectives

- Model an acetaldehyde PFR reactor using DWSIM.
- Automate simulation runs for different operating conditions.
- Generate a large simulation dataset.
- Validate and analyze the generated data using Python.
- Study relationships between reactor operating conditions and conversion.
- Develop machine-learning models for conversion prediction.
- Compare different ML models using standard performance metrics.
- Store and analyze the dataset using MySQL and SQL.
- Develop interactive Power BI dashboards.
- Deploy an interactive prediction application using Streamlit.
- Search for operating conditions corresponding to a specified target conversion.

---

## ⚙️ Process Simulation

The process simulation is performed using **DWSIM** with a Plug Flow Reactor (PFR).

Different operating conditions are varied during automated simulation runs, including parameters such as:

- Temperature
- Pressure
- Reactor volume
- Residence time
- Heat load
- Feed/product flow variables
- Conversion

The simulation results are collected into a structured dataset for further analysis.

Approximately **3000 simulation cases** are used for the data-driven analysis.

---

## 💼 Business Problem

Chemical process industries need to operate reactors under conditions that provide the required product conversion while avoiding unnecessary operating costs and excessive trial-and-error during process development.

For a PFR reactor, changes in operating conditions such as temperature, pressure, reactor volume, residence time, and heat load can affect conversion. Evaluating many combinations directly through process simulation can be time-consuming, making it difficult to quickly explore the operating space.

This project addresses this problem by creating a **data-driven reactor analysis and decision-support workflow**.

DWSIM is used to generate simulation data for different operating conditions. Machine-learning models are then trained to learn the relationship between process variables and reactor conversion. SQL provides structured data analysis, Power BI provides interactive process monitoring and visualization, and Streamlit provides an accessible interface for prediction and operating-condition exploration.

### Business Value

The system can help to:

- Reduce repetitive simulation-based analysis during early-stage process studies.
- Quickly estimate reactor conversion for different operating conditions.
- Explore the relationship between operating variables and reactor performance.
- Identify candidate operating conditions corresponding to a desired conversion.
- Centralize and query large amounts of simulation data using SQL.
- Provide interactive dashboards for engineering and process-data analysis.
- Provide a user-friendly interface for ML-based conversion prediction.


## 🔄 Project Workflow

```text
                    DWSIM
                      │
                      ▼
             PFR Reactor Simulation
                      │
                      ▼
          Automated Data Generation
                      │
                      ▼
             Simulation Dataset
                      │
                      ▼
              Python / Jupyter
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
    Data Validation             EDA
          │                       │
          └───────────┬───────────┘
                      ▼
             Machine Learning
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
       Linear       XGBoost      KNN
     Regression
          │           │           │
          └───────────┼───────────┘
                      ▼
               Model Comparison
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
       MySQL                    Power BI
          │                       │
       SQL Analysis          Interactive
                              Dashboard
          │
          └───────────┬───────────┘
                      ▼
                  Streamlit
                      │
                      ▼
             Interactive Prediction
                      │
                      ▼
          Target Conversion Search

- Support faster comparison of operating scenarios before detailed process validation.

The system is intended as a **decision-support and analysis tool**, with final operating conditions requiring validation through the underlying process simulation and appropriate engineering constraints.
