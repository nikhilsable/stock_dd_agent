import streamlit as st
from main import analyze_stock

def convert_txt_to_md(text, stock_ticker):
    """plain text saved to a .md file.

    Args:
        text (str): The plain text content
        stock_ticker (str): The stock ticker of the output Markdown file (without the .md extension).
    """
    with open(f"{stock_ticker}_stock_dd.md", "w") as f:
        f.write(text)

    print(f'Markdown file "{stock_ticker}_stock_dd.md" created successfully!')

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
    
    st.title("📚 Fundamental Analyst for Stocks")
    st.subheader("🤖 Investment Recommendations Powered by AI ")
    
    # Input field for stock ticker
    stock_ticker = st.text_input("Enter stock ticker (e.g., AAPL):")
    
    if st.button("Get Analysis"):
        if stock_ticker:
            with st.status("🤖 **Agents working.. While you wait, check out what they are reviewing.... **", state="running", expanded=True) as status:
                with st.container(height=500, border=False):
                    output = analyze_stock(stock_ticker)

                status.update(label="✅ Report Ready!",
                    state="complete", expanded=False)
            
            st.subheader("📈 Here is your Report 📈")
            st.markdown(output)
            convert_txt_to_md(output, stock_ticker) 


if __name__ == "__main__":
    st.set_page_config(page_icon="💰", layout="wide")
    main()





