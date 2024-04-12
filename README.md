# RegAffairsBot

RegAffairsBot is an advanced interactive chatbot powered by OpenAI's GPT-4 model, specifically designed to assist with regulatory affairs, compliance, and related queries. It leverages the latest advancements in AI to provide accurate and context-aware assistance through an intuitive web interface.

## Features

- **Interactive Chat**: Engage in detailed conversations with the bot to get answers to complex regulatory queries.
- **Text and Document Generation**: Automatically generate comprehensive documents and responses pertaining to regulatory requirements.
- **Persistent Conversation Threads**: Utilize OpenAI's Assistants API to manage conversation threads, maintaining context and history over extended interactions.
- **File Handling and Annotation**: Use the Assistants API to handle file interactions, allowing the bot to analyze and reference documents dynamically during conversations.
- **Security and Privacy**: Secure API key management and robust conversation data handling to ensure user data privacy and security.

## Getting Started

### Prerequisites

Ensure you have Python 3.8 or newer installed. You will also need Streamlit, the OpenAI library, and dotenv for environment management.

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/priyamthakar/RegAffairsBot.git
   cd RegAffairsBot
   ```

2. **Install Dependencies:**
   ```bash
   pip install streamlit openai python-dotenv
   ```

3. **Environment Setup:**
   - Obtain an API key from [OpenAI](https://platform.openai.com/account/api-keys).
   - Create a `.env` file at the root of the project and add your API key:
     ```
     OPENAI_API_KEY='your_openai_api_key_here'
     ```

### Running the Bot

Execute the bot locally by running:

```bash
streamlit run main.py
```

Navigate to `http://localhost:8501` in your browser to start interacting with RegAffairsBot.

## Configuration

Modify `main.py` to customize the bot's settings and behavior. Important configurations include:

- **Model Configuration**: Default to using the `gpt-4` model. This can be adjusted based on your specific needs or the availability of newer models.
- **API Key Management**: Streamlit's sidebar is configured to securely input your API key during runtime.

## Advanced Features

### Using Assistants API

RegAffairsBot leverages the Assistants API for several advanced features:

- **Thread Management**: Manage long conversations effectively with thread truncation to fit the model’s context window.
- **File Management**: Handle and reference multiple file formats within conversations for data-driven insights.
- **Custom Tool Integration**: Incorporate custom or OpenAI-hosted tools like code interpreters or knowledge retrieval systems to enhance the bot's functionality.

### Custom Assistant Creation

To create an assistant tailored to specific tasks such as data visualization:

1. **File Upload**:
   ```python
   file = client.files.create(
     file=open("data.csv", "rb"),
     purpose='assistants'
   )
   ```

2. **Assistant Creation**:
   ```python
   assistant = client.beta.assistants.create(
     name="Data Visualizer",
     description="Analyzes and visualizes data from CSV files.",
     model="gpt-4-turbo",
     tools=[{"type": "code_interpreter"}],
     file_ids=[file.id]
   )
   ```

## Security

Implement best practices to ensure the security of the mainlication and user data:

- **API Key Security**: Use environment variables and secure input fields to manage API keys safely.
- **Data Access Controls**: Implement authorization checks before performing actions with the Assistants API to ensure that users can only access data they are permitted to.

## Support and Feedback

For support, feature requests, or feedback, please open an issue in the GitHub repository.

## Contributing

Contributions are welcome! Refer to CONTRIBUTING.md in the repository for guidelines on how to contribute effectively.

## License

This project is licensed under the MIT License.
