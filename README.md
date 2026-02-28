# AWS Data Engineering Capstone Project

## Overview
This project demonstrates an end-to-end data engineering pipeline built on AWS to ingest, transform, catalog, and analyze large-scale fisheries data from the Sea Around Us dataset.

The goal was to enable data analysts to query historical fishing activity in global high seas and Exclusive Economic Zones (EEZs using serverless AWS services.

---

## Architecture
- Amazon S3 for raw and transformed data storage
- AWS Glue Crawler for schema discovery and metadata management
- Amazon Athena for SQL-based analytics
- AWS Cloud9 for development and transformation workflows

---

## Dataset
Source: Sea Around Us  
Data includes:
- Fishing year
- Country (fishing_entity)
- Fish species
- Tonnes caught
- Landed value (USD, 2010)
- Ocean region (high seas vs EEZ)

---

## Data Pipeline Steps

### 1. Data Ingestion
- Downloaded CSV files for:
  - Global high seas
  - Pacific Western Central high seas
  - Fiji EEZ
- Stored transformed data in Amazon S3

### 2. Data Transformation
- Converted large CSV files to Apache Parquet using Pandas
- Standardized column names across datasets
- Optimized data for analytics and cost-efficient querying

### 3. Metadata & Cataloging
- Used AWS Glue Crawler to automatically infer schemas
- Created a centralized Glue database (`fishdb`)

### 4. Analytics with Athena
- Queried multiple Parquet files simultaneously
- Used SQL to analyze fishing trends
- Created reusable Athena views for reporting

---

## Key Analysis Performed
- Annual value of fish caught by Fiji in:
  - High seas
  - Fiji EEZ
  - Combined regions
- Species-based analysis (Mackerels)
- Country-wise ranking of fishing activity

---

## Technologies Used
- AWS S3
- AWS Glue
- Amazon Athena
- AWS Cloud9
- Python (Pandas)
- SQL

---

## Key Learnings
- Schema unification across heterogeneous datasets
- Serverless analytics using Athena
- Cost-efficient storage with Parquet
- Building production-style data lakes on AWS