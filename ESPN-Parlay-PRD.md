# Product Requirements Document (PRD)

## Title
AI-Powered Jupyter Notebook for Betting Parlay Analysis

## Objective
Develop a feature-rich Jupyter Notebook that ingests player-level betting statistics and parlay summary data from CSV files and uses them to evaluate bet viability, calculate expected value, and generate alternative betting strategies. The goal is to support smarter decision-making in sports betting with data-driven analysis.

## Key Features
- Load and process structured player prop data from `player_stats.csv`
- Load and interpret parlay risk data from `parlay_summary.csv`
- Calculate implied vs. true probabilities
- Visualize probability vs. payout relationships
- Highlight weakest legs in parlays
- Suggest optimized alternative parlay structures based on adjusted thresholds
- Export results into CSV or display-ready tables

## Inputs
- `player_stats.csv`: Contains player names and individual probabilities for prop outcomes
- `parlay_summary.csv`: Contains the total expected value, odds, and combined probability for the full parlay

## Outputs
- Pandas DataFrames
- Probability and value assessment plots
- Tables comparing original vs alternative parlays
- Exportable CSV summaries

## Users
- Sports bettors
- Analysts building betting models
- Educators teaching probabilistic modeling

## Constraints
- Must run in Jupyter Notebook (Python-based)
- Must only use open-source libraries: `pandas`, `matplotlib`, `numpy`
- Must be compatible with Cursor environment
