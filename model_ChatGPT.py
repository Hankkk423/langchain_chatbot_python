# from langchain.llms import OpenAI  ## for the OpenAI model
from langchain.chat_models import ChatOpenAI  ## for the ChatOpenAI model
from langchain.document_loaders import DirectoryLoader  ## for loading documents
from langchain.text_splitter import CharacterTextSplitter  ## for splitting documents into "chuck_size"
from langchain.docstore.document import Document  ## for splitting documents into "chuck_size"
from langchain.prompts import PromptTemplate  ## for setting up the PromptTemplate
from langchain.chains.question_answering import load_qa_chain  ## for using "load_qa_chain"
import constants  ## for global constants
import tiktoken  ## for calculating token numbers


openai_apikey = constants.OPENAI_APIKEY
data_directory_path = constants.DATA_DIRECTORY_PATH
chat_model = 'gpt-3.5-turbo-16k'


## ----- Models ----- ##
llm = ChatOpenAI(openai_api_key=openai_apikey, temperature=0.6, model=chat_model)
# print(llm.predict("What would be a good company name for a company that makes colorful socks?"))


## ----- Load Documents ----- ##
# Load Notion page as a markdownfile file
loader = DirectoryLoader(data_directory_path)
docs = loader.load()
print('len(doc): ', len(docs))


## ----- Split Documents ----- ##
# Initialize a text splitter
splitter = CharacterTextSplitter(separator=' ', chunk_size=2048, chunk_overlap=0)
# Initialize an empty list to store split texts from all documents
all_split_texts = []

# Loop through each document and split its content
for doc in docs:
    # Use CharacterTextSplitter to split the content of the current document
    split_texts = splitter.split_text(doc.page_content)
    
    # Append the split texts to the list
    all_split_texts.extend(split_texts)

print('all_split_texts: ', all_split_texts)

def num_tokens_from_string(string: str) -> int:
    """Returns the number of tokens in a text string."""

    # Choose one of the encoding (from 'encoding function' OR 'model')
    # encoding = tiktoken.get_encoding("cl100k_base")
    encoding = tiktoken.encoding_for_model(chat_model)
    num_tokens = len(encoding.encode(string))
    return num_tokens

# Calculate total tokens for all strings in the list
total_tokens = sum(num_tokens_from_string(text) for text in all_split_texts)
print('Total tokens:', total_tokens)


## ----- Set Prompt Template ----- ##
prompt_template = """Use all of the following information to answer the question at the end. Each of sentence in the following has unique information, using "" to seperate the sentences. If you can't find the answer based on the following information, just say that you don't know and you don't have the information, don't try to make up an answer.
{context}
Question: {question}
Please give me a short response with some emojis and Answer in a warm tone:"""
PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)


## ----- function ----- ##
def chatgpt_response(msg):
    prompt = PROMPT.format(context=all_split_texts, question=msg)
    answer = llm.predict(prompt)
    tag = 'gpt'
    return answer, tag


tanswer, ttage = chatgpt_response('what is your number?')
print('test: ', tanswer, type(tanswer))
