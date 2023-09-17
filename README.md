# Mimic 1
_Author mimicking using OpenAI with available local information._

## Intro
Evaluate existing AI large language models (llm's) to determine optimal parameters and use within the following contexts:
- **Recreate:** Generate document sections based on previous examples within the document knowledge base. 
- **Novel Generation:** Generate novel text based on the user query.
- **Improvements:** Based on a given selection of text, improve the text grammatically, structurally, and contextually.
- **Mimic:** Mimic tbe writing style of an author in order to reproduce text inline with an author's standards and idiosyncrasies.


## Application
An application has been developed in order to effectively query a user's document knowledge based. 
This application is open to further development based on the results of the **experimentation** to produce optimal results. 
The application can be used as follows: 



## Privacy
OpenAI will come into contact with local information sources. 
OpenAI collects account information, user content, communication information, and social media interactions ([https://openai.com/policies/privacy-policy](https://openai.com/policies/privacy-policy))

However, it is **important** to note that OpenAI's models are not trained on the output or inputs to the models. 
The link stating this is as follows: [https://openai.com/api-data-privacy](https://openai.com/api-data-privacy).

## Tools
LangChain presents an optimal framework in which to work with OpenAI and its LLM models. 
[https://python.langchain.com/docs/get_started/introduction.html](https://python.langchain.com/docs/get_started/introduction.html)

## Resources 
- [Use Your Locally Stored Files To Get Response From GPT - OpenAI | Langchain | Python](https://youtu.be/NC1Ni9KS-rk?si=kFklvimKPrXVfcYy)
- [Query Your Data with GPT-4 | Embeddings, Vector Databases | Langchain JS Knowledgebase](https://youtu.be/jRnUPUTkZmU?si=Jn3xJ_QxXcsum87r)
- [Using ChatGPT with YOUR OWN Data. This is magical. (LangChain OpenAI API)](https://youtu.be/9AXP7tCI9PI?si=JHWz1gXPsrirzkx2)
- [Create Your Own ChatGPT with PDF Data in 5 Minutes (LangChain Tutorial)](https://youtu.be/au2WVVGUvc8?si=zIr2_AOj_-BUwIrL)


## Outline

### Project Structure
```
kb (Knowledge Base) /
    Local information making up the knowledge base of the project
notebooks/
    Jupyter notebooks dealing with exploration and experimentation outside of the application developement
frontend/
    The directory containing the source code for the application frontend. Comprised of html, css, and javascript
backend/
    The directory containing the source code fro the application backend. Powered by FastAPI
```

### Local Information Formats Supported
- Docx
- PDF
- txt
- md