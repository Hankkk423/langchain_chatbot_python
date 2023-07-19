from langchain.llms import OpenAI  ## for the OpenAI model
# from langchain.chat_models import ChatOpenAI  ## for the ChatOpenAI model
from langchain.document_loaders import DirectoryLoader  ## for loading documents
from langchain.text_splitter import CharacterTextSplitter  ## for splitting documents into "chuck_size"
from langchain.docstore.document import Document  ## for splitting documents into "chuck_size"
from langchain.prompts import PromptTemplate  ## for setting up the PromptTemplate
from langchain.chains.question_answering import load_qa_chain  ## for using "load_qa_chain"
import constants  ## for global constants


openai_apikey = constants.OPENAI_APIKEY
data_directory_path = constants.DATA_DIRECTORY_PATH


## ----- Models ----- ##
llm = OpenAI(openai_api_key=openai_apikey, temperature=0.6)
#print(llm.predict("What would be a good company name for a company that makes colorful socks?"))
# llm = ChatOpenAI(temperature=0.9, model="gpt-3.5-turbo-0613", openai_api_key=openai_apikey)


## ----- Load Documents ----- ##
# Load Notion page as a markdownfile file
loader = DirectoryLoader(data_directory_path)
docs = loader.load()
print(len(docs))


## ----- Split Documents ----- ##
# Initialize a text splitter
splitter = CharacterTextSplitter(separator=' ', chunk_size=2048, chunk_overlap=0)
# Split your documents
split_docs = splitter.split_documents(docs)


## ----- Set Prompt Template/ Load Chain ----- ##
prompt_template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.
{context}
Question: {question}
Please give me a short response with some emojis and Answer in a warm tone:"""
PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)

chain = load_qa_chain(llm, chain_type="stuff", prompt=PROMPT)
# query = 'How are you?'
# print(chain.run(input_documents=docs, question=query), return_only_outputs=True)
# print(chain({"input_documents": docs, "question": query}, return_only_outputs=True))


## ----- function ----- ##
def gpt_response(msg):
    answer = chain.run(input_documents=split_docs, question=msg, return_only_outputs=True)
    tag = 'gpt'
    return answer, tag

tanswer, ttage = gpt_response('Can I go on the weekend?')
print('test: ', tanswer, type(tanswer))

