import streamlit as st

from utils import extract_pdf, create_vector_text

from langchain_ollama import OllamaLLM

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


# Page configuration
st.set_page_config(
    page_title="Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Resume Analyzer")

# Upload resume
resume_file = st.file_uploader(
    "Upload your resume (PDF format)",
    type=["pdf"]
)

# Job description
jd_text = st.text_area(
    "Paste the job description here",
    height=200
)


if st.button("Analyze Resume"):

    if resume_file and jd_text:

        # Extract resume text
        resume_text = extract_pdf(resume_file)

        # Combine resume and job description
        combine_text = resume_text + "\n\n" + jd_text

        # Create vector store
        vectorstore = create_vector_text(combine_text)

        # Create retriever
        retriever = vectorstore.as_retriever()

        # Load Ollama model
        llm = OllamaLLM(model="gemma2:2b")

        # Prompt
        prompt = ChatPromptTemplate.from_template("""
You are a professional resume analyzer.

You will be given a resume and a job description.

Analyze the resume in the context of the job description and provide
a detailed analysis of how well the candidate's skills, experience,
and qualifications match the requirements of the job.

Provide specific examples from the resume that demonstrate relevant
skills and experience.

Highlight areas where the candidate may be lacking or could improve.

Your analysis should be clear, concise, well-structured, and actionable.

Context:
{context}

Question:
{question}

Provide the following:

1. Skills Gap Analysis
2. Missing Technologies
3. ATS Score (0-100)
4. 10 technical questions that can be asked in the interview
5. Resume improvement suggestions
6. Summary of the candidate's strengths and weaknesses
7. Overall recommendation for the candidate's suitability for the job
8. Provide a score for each of the above points (0-10)
9. Provide a final score for the candidate's overall suitability for the job (0-100)
10. Provide a final recommendation for the candidate's overall suitability for the job (Yes/No)
""")

        # Create LangChain chain
        chain = (
            {
                "context": retriever,
                "question": RunnablePassthrough()
            }
            | prompt
            | llm
            | StrOutputParser()
        )

        # Run analysis
        response = chain.invoke(
            "Analyze the resume in the context of the job description."
        )

        # Display result
        st.subheader("📊 Analysis Result")
        st.write(response)

    else:
        st.warning(
            "Please upload a resume and provide a job description before analyzing."
        )