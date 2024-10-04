 <h1>Intelligent Question Answering System Using SQuAD Dataset</h1>
 
  <p>
Fine-tuning and implementing the BERT model to answer questions using the extractive question answering method. This involves posing questions about a document and identifying the answers as spans of text in the document itself.
  </p>

<br>

# Table of Contents

- [About the Project](#about-the-project)

  * [Tech Stack](#tech-stack)
  * [Features](#features)

- [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)

- [Usage](#usage)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)
  
## About the Project
This project aims to develop an advanced Question Answering (QA) system utilizing Natural Language Processing (NLP) techniques. By leveraging the capabilities of the Hugging Face Transformers library, specifically employing pre-trained models from the AutoModel class, the system will be fine-tuned on the Stanford Question Answering Dataset (SQuAD).

### Tech Stack

<details>
 
  <ul>
    <li><a href="https://pytorch.org">PyTorch</a></li>
    <li><a href="https://huggingface.co/docs/transformers/en/index">HuggingFace Transformers</a></li>
    <li><a href="https://https://streamlit.io"> Streamlit</a></li>
  </ul>
</details>

### Features
- Contextual Question Answering:  The system can accurately extract answers from a given passage, providing precise responses based on context.

- User-Friendly Interface: An intuitive web interface allows users to easily input questions and view answers, enhancing user experience.
 
- Real-Time Response: The QA system delivers quick answers, making it suitable for interactive applications and real-time queries.

- Customizable Context Input: Users can input their own text passages alongside questions, enabling the model to answer based on varied content.

- Robust Performance Metrics: The system evaluates its performance using metrics like Exact Match (EM) and F1 score, ensuring transparency and reliability.

### Prerequisites

This project uses pip as package manager

```python
 pip install transformers
 pip install tensorflow[and-cuda]
 pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
 pip install streamlit
```

or install the packages through cmd by running pip with the requirements file in the
[repository](https://github.com/ezahpizza/BERT_Question_Answering)
## Usage



### Getting Started

1. **Installation**:
   - Clone the repository or download the project files.
   - Ensure you have Python installed (version 3.9 or higher).
   - Install the required libraries using pip:
     ```bash
     pip install -r requirements.txt
     ```

2. **Running the Application**:
   - Navigate to the project directory in your terminal.
   - Start the web application with the following command:
     ```bash
     python app.py
     ```
   - Open your web browser and go to `http://127.0.0.1:5000` (or the specified port) to access the interface.

### Interacting with the System

1. **Inputting Context**:
   - In the provided text box, paste or type the passage you want the model to reference when answering questions.

2. **Asking Questions**:
   - Enter your question related to the context in the designated question input field.

3. **Receiving Answers**:
   - Click the "Answer" button to send your question. The system will process your input and display the answer below.


#### Example Workflow

1. **Provide Context**:
   - Example passage: "The Earth revolves around the Sun in an elliptical orbit, completing one full revolution approximately every 365.25 days."

2. **Ask a Question**:
   - Example question: "How long does it take for the Earth to revolve around the Sun?"

3. **Get an Answer**:
   - The system might respond with: "Approximately 365.25 days."

#### Documentation and Support

- For detailed instructions on configuration, customization, and troubleshooting, refer to the `README.md` file in the project repository.
- For any issues or questions, you can reach out through the project’s issue tracker or contacts. 

This straightforward usage guide enables users to quickly engage with the Question Answering system, making it easy to access its functionalities and derive meaningful insights.


## License

Distributed under the Apache License. See LICENSE.txt for more information.

## Contact

Prateek Mohapatra - [LinkedIn](www.linkedin.com/in/prateekmp) - prateekmsoa@gmail.com

Project Link: [BERT_Question_Answering](https://github.com/ezahpizza/BERT_Question_Answering)

## Acknowledgements

 - [HuggingFace](https://huggingface.co/docs/transformers/index)

This project not only enhances understanding of NLP techniques but also contributes to the growing field of intelligent systems that can interact with users in a meaningful way.
