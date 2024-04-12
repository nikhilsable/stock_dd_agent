# import streamlit as st
# from crewai import Agent, Task
# from main import analyze_stock


# def icon(emoji: str):
#     """Shows an emoji as a Notion-style page icon."""
#     st.write(
#         f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
#         unsafe_allow_html=True,
#     )

# def main():
#     st.set_page_config(page_icon="💰", layout="wide")
#     icon("📚 Fundamental Analyst for Stocks 📚")

#     st.subheader(" 🤖 Investment Recommendations Powered by AI.. 🤖 ",
#                  divider="rainbow", anchor=False)

#     # Input field for stock ticker
#     stock_ticker = st.text_input("Enter stock ticker (e.g., AAPL):")
    
#     if st.button("Get Analysis"):
#         if stock_ticker:
#             with st.status("🤖 **Agents working.. While you wait, check out what they are reviewing.... **", state="running", expanded=True) as status:
#                 with st.container(height=500, border=False):
#                     output = analyze_stock(stock_ticker)
#                 status.update(label="✅ Report Ready!",
#                             state="complete", expanded=False)

#             st.subheader("📈Here is your Report 📈 ", anchor=False, divider="rainbow")
#             st.markdown(output)

# if __name__ == "__main__":
#     main()

import streamlit as st
from main import analyze_stock

# Custom CSS styling for muted tones
def apply_custom_css():
    st.markdown(
        """
        <style>
            .fullScreenFrame {
                background-color: #f1f1f1;
            }
            .stApp {
                color: #555;
                background-color: #f9f9f9;
            }
            .stTextInput>div>div {
                background-color: #f2f2f2;
            }
            .stTextInput input {
                color: #333;
            }
            .stButton>button {
                background-color: #ccc;
                color: #333;
            }
            .stAlert {
                background-color: #e8e8e8;
            }
            .stMarkdown {
                color: #555;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

def main():
    apply_custom_css()
    
    st.title("📚 Fundamental Analyst for Stocks 📚")
    st.subheader("🤖 Investment Recommendations Powered by AI.. 🤖")
    
    # Input field for stock ticker
    stock_ticker = st.text_input("Enter stock ticker (e.g., AAPL):")
    
    if st.button("Get Analysis"):
        if stock_ticker:
            with st.spinner("🤖 **Agents are working. Please wait while the analysis is in progress...**"):
                output = analyze_stock(stock_ticker)
            
            st.success("✅ Report Ready!")
            st.subheader("📈 Here is your Report 📈")
            st.markdown(output)

if __name__ == "__main__":
    st.set_page_config(page_icon="💰", layout="wide")
    main()
