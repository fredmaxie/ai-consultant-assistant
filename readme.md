🧠 AI Consultant Assistant

A simple Python-based AI agent that analyzes a company or business description and recommends tailored AI use cases, ROI opportunities, and relevant tools.
Built as a proof-of-concept for AI consulting applications.

🚀 Overview

This lightweight assistant demonstrates how consultants can leverage the OpenAI API to identify and articulate AI opportunities for clients.

The assistant takes a short business description as input and returns structured insights about:

Potential AI use cases

Expected business impact or ROI

Recommended technologies or models

Implementation complexity level

This project was designed to serve as a demonstration of AI integration skills using Python, without relying on low-code tools like Make.com or Zapier.

🧩 Tech Stack

Language: Python 3.13

Library: OpenAI Python SDK

Model: GPT-4 (or GPT-5 if available in your account)

Environment: Command-line or Jupyter Notebook

⚙️ Installation

Clone or download this repository.

Open a terminal in the project folder.

Install the OpenAI SDK:

pip install openai


Set your OpenAI API key as an environment variable (Windows example):

setx OPENAI_API_KEY "your_api_key_here"


Run the script:

python main.py

💬 Example Usage

Input:

We are a mid-size logistics company. Our operations team manages deliveries manually using spreadsheets and phone calls.


Output (sample):

{
  "use_cases": [
    "Predictive delivery route optimization using real-time traffic data",
    "Automated driver dispatching based on workload and location",
    "Customer notification system for delivery status updates"
  ],
  "roi_estimate": "15–25% reduction in delivery delays and 10% cost savings within the first year",
  "recommended_tools": ["GPT-4 API", "Google Maps API", "Snowflake or AWS Redshift for data management"],
  "complexity": "Medium"
}

🎯 Purpose

This project was created to:

Demonstrate hands-on ability to build and run AI agents using Python and the OpenAI API.

Serve as a conversation piece during AI consulting interviews.

Provide a foundation for expanding into more advanced agents such as AI Readiness Evaluators, Proposal Writers, or Meeting Summarizers.

🧱 Next Steps

Planned enhancements:

Add structured JSON output for easier parsing

Wrap in a simple Streamlit web UI for live demos

Extend logic to assess AI readiness or data maturity based on business inputs

👤 Author

Fred Maxie
IT & AI Consultant