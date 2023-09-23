# WhatsApp Chat Analysis Web Application

## Introduction

This web application allows you to analyze your WhatsApp chat statistics, including weekly, monthly, and daily activities. You can also extract links and media shared in the chat, among other features.

## Technologies Used

- **Python:** The core language for developing the application.
- **Streamlit Server:** Used for creating the web interface and deploying the application.
- **GitHub:** Used for version control and collaboration among team members.

## Features

1. **Chat Activity Analysis:**
   - View weekly, monthly, or daily chat activity trends.
   - Analyze the number of messages sent and received.
   - Track when the chat is most active during the day.

2. **Link and Media Extraction:**
   - Extract links shared in the chat.
   - Retrieve media files (images, videos, documents) shared in the chat.

3. **Word Cloud Generator:**
   - Generate word clouds to visualize the most commonly used words in the chat.

4. **Search Functionality:**
   - Search for specific keywords or phrases within the chat.

5. **Export Data:**
   - Export chat data and analysis results in various formats (CSV, Excel, etc.).

6. **User-Friendly Interface:**
   - Intuitive and easy-to-use web interface.

## Installation

To run this WhatsApp Chat Analysis Web Application locally, follow these steps:

1. Clone this GitHub repository to your local machine:

   ```bash
   git clone https://github.com/your-username/whatsapp-chat-analysis.git
2. Navigate to the project directory:
   ``` bash
   cd whatsapp-chat-analysis
3. Create a virtual environment (recommended):
   ```bash
      python -m venv venv
4.Activate the virtual environment:
 - On Windows : ```venv\Scripts\activate
 - On Mac/Linux : ``` source venv/bin/activate

## Usage
- Once you have installed the application, run it using the following command:

```bash
streamlit run app.py
```

 - A web browser window should open, and you can access the application locally at http://localhost:8501.

- Upload your WhatsApp chat export file (typically a .txt file) to the application.

- Explore the different analysis and extraction options available in the application's user interface.

Export your results or findings for further analysis if needed.


