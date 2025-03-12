# LLM Gateway

## Overview
The LLM Gateway is a serverless implementation designed to route requests to various Large Language Model (LLM) providers through a single endpoint. This simplifies the process of interacting with multiple LLM services by providing a unified interface.

## Features
- **Single Endpoint Access**: Interact with multiple LLM providers using one endpoint.
- **Scalable and Serverless**: Built using AWS SAM (Serverless Application Model) for scalability and ease of deployment.

## Usage
1. **Deployment**: Deploy the application using AWS SAM CLI. Ensure you have the necessary AWS credentials and permissions.
2. **Configuration**: Configure the LLM providers you wish to use by updating the `template.yml` file with the necessary endpoints.
3. **Invocation**: Send requests to the deployed endpoint. The gateway will route the requests to the appropriate LLM provider based on your configuration.
4. **Using with LangChain**: You can use this endpoint with LangChain by setting `base_url` in the LangChain model API configuration. This allows LangChain to send requests to the LLM Gateway instead of directly calling individual LLM providers.

### Example Configuration in LangChain:
```python
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(
    base_url="https://your-deployed-llm-gateway-url.com",
    default_headers={"x-api-key": "your-apigateway-key"}  # Set API Gateway key using env variable
)
```
This setup allows LangChain to interact with your LLM Gateway seamlessly while also supporting API Gateway authentication.

## Configuration
- **template.yml**: This file contains the configuration for the AWS resources and the routing logic for the LLM providers. Update this file with your specific provider details and any other necessary configurations.

## Prerequisites
- AWS Account
- AWS SAM CLI
- API keys for the LLM providers you intend to use

## Getting Started
1. Clone the repository.
2. Navigate to the project directory.
3. Deploy the application using the following command:
   
   ```sh
   sam deploy --guided
   ```
   
4. Follow the prompts to complete the deployment.

## Support
For any issues or questions, please contact the project maintainers or open an issue in the repository.

