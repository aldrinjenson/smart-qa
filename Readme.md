# Smart QA

Streamlit-based web application designed for efficient data analysis and visualization. With support for various data formats such as CSV, Excel, and JSON, this tool empowers users to extract valuable insights seamlessly.

## Features

- **Intelligent Questioning**: Interact with your data by asking direct questions and receive insightful answers.
- **Visual Summaries**: Instantly generate visualizations and summaries based on the document, providing a quick overview of key patterns and trends.
- **Question-specific Visualizations**: Obtain visualizations and infographics tailored to the questions you pose, enhancing your understanding of the data.
- **Compatibility**: Smart QA is designed to seamlessly work with both OpenAI and any self-hosted Language Model.

## Demo

https://github.com/aldrinjenson/smart-qa/assets/53407417/12142e98-76c6-4ca5-ba70-59db5dd57e5f

https://github.com/aldrinjenson/smart-qa/assets/53407417/f74ffdaa-2c2b-4554-9c4f-88a89c7dd400

## Installation

To install Smart QA, follow these steps:

1. Clone the repository: `git clone https://github.com/yourusername/smart-qa.git`
2. Navigate to the project folder: `cd smart-qa`
3. Install dependencies: `pip install -r requirements.txt`
4. Create a `.env` file similar to `.env.example`

## Usage

1. Run the application: `streamlit run app.py`
2. Access the application at [http://localhost:8501](http://localhost:8501) in your browser.

## Built With

Smart QA is built using [Streamlit](https://streamlit.io/) and integrates with [Microsoft LIDA](https://github.com/microsoft/lida) for enhanced functionalities.

## Todo

- **Trend Analysis Modules**: Enhance the application by incorporating improved trend analysis modules.
- **Anomaly Detection**: Implement features to detect and highlight anomalies within the data.
- **Integration with GPT-4-V**: Connect with GPT-4-V to leverage advanced inference capabilities, especially when dealing with graphical data.
- Dockerise the application
- Add function calling to decide between sql based and LIDA based approaches

## Contributions

Contributions welcome : )
