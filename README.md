# LangChain ChatBot: OpenAI Model Using Custom Data

Welcome to the LangChain ChatBot project, where we leverage the power of the LangChain library to create a customized chatbot that can answer questions using your own provided data.

## Introduction

In today's fast-paced digital world, interactive AI-powered chatbots have become an integral part of various industries, from customer support to information retrieval. The LangChain ChatBot project empowers you to harness the capabilities of OpenAI's advanced language models and LangChain library to develop your own intelligent chatbot tailored to your specific domain and knowledge base.

Whether you're building a chatbot to assist users with frequently asked questions, provide insights on a particular topic, or engage in meaningful conversations, this project provides you with a solid foundation to get started.

## Key Features

- **Customizable Responses:** The chatbot generates responses based on your provided dataset, allowing you to create personalized interactions with users.
- **Integration with LangChain:** LangChain's seamless integration with OpenAI's language models enables smooth development and deployment of the chatbot.
- **Easy Configuration:** Set up your API key and data directory path in the `constants.py` file to start using the chatbot with minimal setup.
- **Scalable Design:** The project architecture is designed to handle various types of documents and adapt to evolving requirements.

## Installation

To get started, follow these steps to set up the project:

1. Clone this repository to your local machine.
2. Install the required dependencies by running: pip install -r requirements.txt
3. Collect your custom data documents and place them in the `data/` directory as `.txt` files.

## Usage

1. Set up your OpenAI API key by editing the `constants.py` file and replacing `'YOUR_OPENAI_API_KEY'` with your actual API key.
2. Configure the data directory path in the `constants.py` file to point to your `data/` directory.
3. Select a model type based on your requirements. You can experiment with different model parameters for generating responses.
4. Run the code and watch your chatbot come to life! It will answer questions based on the documents you've provided.

## Getting Started

If you're new to this project, follow these steps to quickly get started:

1. Clone the repository
2. Install the dependencies as mentioned in the Installation section.
3. Follow the Usage instructions to set up your API key and data directory path.
4. Run the provided code to see the chatbot in action

## Customization

You can customize the chatbot's behavior by adjusting various parameters in the code. Feel free to explore different options, such as changing the model type, adjusting temperature, or modifying the prompt template.

## License

This project is licensed under the MIT License. You can find more details in the LICENSE file.


