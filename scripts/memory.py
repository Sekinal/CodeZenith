from llama_index import LLMPredictor, PromptHelper, ServiceContext, Document, GPTSimpleVectorIndex
from langchain.chat_models import ChatOpenAI
import os

# Define LLM
llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo"))

# Define prompt helper
# set maximum input size
max_input_size = 4096
# set number of output tokens
num_output = 256
# set maximum chunk overlap
max_chunk_overlap = 20
prompt_helper = PromptHelper(max_input_size, num_output, max_chunk_overlap)

# Define service context
service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)

def store_to_memory(message):
    message_to_store = Document(message)
    
    # Check if "memory" directory exists, and create it if it doesn't
    if not os.path.exists("memory"):
        os.makedirs("memory")
        # Create a new "index" file inside the "memory" directory

        index = GPTSimpleVectorIndex.from_documents([], service_context=service_context)
        index.insert(message_to_store)
        index.save_to_disk('memory/index.json')
        
    elif not os.path.exists("memory/index.json"):
        index = GPTSimpleVectorIndex.from_documents([], service_context=service_context)
        index.insert(message_to_store)
        index.save_to_disk('memory/index.json')
    else:
        index = GPTSimpleVectorIndex.load_from_disk('memory/index.json', service_context=service_context)
        index.insert(message_to_store)
        index.save_to_disk('memory/index.json')
        

def extract_from_memory(message):
    if not os.path.exists("memory"):
        return ''
         
    index = GPTSimpleVectorIndex.load_from_disk('memory/index.json', service_context=service_context)
    response = index.query(message, mode="default")
    
    return response