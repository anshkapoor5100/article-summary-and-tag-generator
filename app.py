import streamlit as st
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from langchain.messages import HumanMessage, SystemMessage

from schema import AnalysisResult
from constants import modelName, systemPrompt

load_dotenv()

try:
    agent = create_agent(
        model=modelName,
        response_format=ToolStrategy(AnalysisResult)
    )
except Exception as e:
    st.error(f"Failed to initialize agent: {e}")
    st.stop()

st.title("Text Analysis")

query = st.text_area("Provide content to get summary and key entities")

if st.button("Analyze") and query:
    try:
        with st.spinner("Analyzing..."):
            conversation = {
                "messages": [
                    SystemMessage(content=systemPrompt),
                    HumanMessage(content=query)
                ]
            }

            result = agent.invoke(conversation)
            response = result["structured_response"]

        st.subheader("Summary")
        st.write(response.summary)

        st.subheader("Key Entities")
        for entity in response.key_entities:
            st.write(f"• {entity}")

        st.subheader("Confidence Score")
        st.write(f"{response.confidence_score}/10")

    except Exception as e:
        st.error(f"Analysis failed: {e}")