import streamlit as st
import os
from main import analyze_stock
import  base64  # For download button functionality


#  Function to convert plain text to markdown and save it to a file
def convert_txt_to_md(text: str, stock_ticker: str):
    """Converts plain text to Markdown format and saves it to a  file.

    Args:
        text (str): The plain text content to be converted.
        stock_ticker (str): The stock ticker to  be used as the filename (without the .md extension).
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

def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href

def main():
    # apply_black_yellow_theme()
    apply_custom_css()

    st.title("📚 Fundamental Analyst for Stocks")
    st.subheader("🤖 Investment Recommendations Powered by AI Agents")
    st.markdown("---")

    # Get stock ticker
    stock_ticker = st.text_input(" Enter stock ticker (e.g., AAPL. ETF's not supported yet..):", placeholder="AAPL", value="")  # Placeholder and initial value

    if st.button("Get Recommendation"):
        if stock_ticker:
            with st.status("🤖 **Agents working.. While you wait, check out what they are reviewing.... **", state="running", expanded=True) as status:
                with st.container(height=500, border=False):
                    with st.spinner("Analyzing... 🤖"):
                        output = analyze_stock(stock_ticker)
                status.update(label="✅ Report Ready!",
                    state="complete", expanded=False)

            # Display Recommendation
            st.subheader("📈 Stock Recommendation 📈")
            st.markdown(output)

            # Create and display download button
            md_filename = f"{stock_ticker}_stock_dd.md"
            convert_txt_to_md(output, stock_ticker)
            st.markdown(get_binary_file_downloader_html(md_filename, 'Markdown Report'), unsafe_allow_html=True)
            # Additional UI elements (examples)
            st.success("Analysis completed successfully! 🎉")  # Success  message


if __name__ == "__main__":
    st.set_page_config(page_icon="💰", layout="wide", page_title="Stock Recommender 3000")  # Enhanced page config
    main()




