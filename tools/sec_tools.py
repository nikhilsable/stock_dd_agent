from langchain.tools import tool
import os
from langchain.text_splitter import CharacterTextSplitter
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from sec_downloader import Downloader
from unstructured.partition.html import partition_html


# Initialize the downloader with your company name and email
dl = Downloader("NS", "sample@sample.com")

class SECTools():
  @tool("Search 10-Q form")
  def search_10q(data: str) -> str:
    """
    Useful to search information from the latest 10-Q form for a
    given stock.
    The input to this tool should be a pipe (|) separated text of
    length two, representing a valid stock ticker you are interested and what
    question you have from it.
		For example, `AAPL|what was last quarter's revenue`.
    """
    stock, ask = data.split("|")
    html = dl.get_filing_html(ticker=stock, form="10-Q")
    elements = partition_html(text=html)
    answer = SECTools.__embedding_search(elements, ask)
    return answer

  @tool("Search 10-K form")
  def search_10k(data: str) -> str:

    """
    Useful to search information from the latest 10-K form for a
    given stock.
    The input to this tool should be a pipe (|) separated text of
    length two, representing a valid stock ticker you are interested, what
    question you have from it.
    For example, `AAPL|what was last year's revenue`.
    """
    stock, ask = data.split("|")
    html = dl.get_filing_html(ticker=stock, form="10-K")
    elements = partition_html(text=html)
    answer = SECTools.__embedding_search(elements, ask)
    return answer

  def __embedding_search(elements, ask):
    content = "\n".join([str(el) for el in elements])
    text_splitter = CharacterTextSplitter(
        separator = "\n",
        chunk_size = 1000,
        chunk_overlap  = 150,
        length_function = len,
        is_separator_regex = False,
    )
    docs = text_splitter.create_documents([content])

    # Initialize the Electra embedder with your API key and project ID
    api_gemini = os.environ.get("GEMINI_API_KEY")
    embedder = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=api_gemini)

    # Create a FAISS retriever using the Electra embeddings
    retriever = FAISS.from_documents(
        docs, embedder
    ).as_retriever()

    answers = retriever.get_relevant_documents(ask, top_k=4)
    answers = "\n\n".join([a.page_content for a in answers])
    return answers