from crewai import Task
from textwrap import dedent

class StockAnalysisTasks():
  def research(self, agent, company):
    return Task(description=dedent(f"""
        Collect and summarize recent news articles, press
        releases, and market analyses related to the stock and
        its industry.
        Pay special attention to any significant events, market
        sentiments, and analysts' opinions. Also include upcoming 
        events like earnings and others.
  
        Your final answer MUST be a report that includes a
        comprehensive summary of the latest news, any notable
        shifts in market sentiment, and potential impacts on 
        the stock.
        Also make sure to return the stock ticker.
        
        {self.__tip_section()}
  
        Make sure to use the most recent data as possible.
  
        Selected company by the customer: {company}
      """),
      agent=agent,
      expected_output="""final answer MUST be a text report that includes a
        comprehensive summary of the latest news, any notable
        shifts in market sentiment, and potential impacts on 
        the stock.Also make sure to return the stock ticker.
        Make sure to use the most recent data as possible.""",
    )
    
  def financial_analysis(self, agent): 
    return Task(description=dedent(f"""
        Conduct a thorough analysis of the stock's financial
        health and market performance. 
        This includes examining key financial metrics such as
        P/E ratio, EPS growth, revenue trends, and 
        debt-to-equity ratio. 
        Also, analyze the stock's performance in comparison 
        to its industry peers and overall market trends.

        Your final report MUST expand on the summary provided
        but now including a clear assessment of the stock's
        financial standing, its strengths and weaknesses, 
        and how it fares against its competitors in the current
        market scenario.{self.__tip_section()}

        Make sure to use the most recent data as much as possible.
      """),
      agent=agent,
      expected_output="""final text report MUST expand on the summary provided by your colleague, 
        the researcher, but now including a clear assessment of the stock's
        financial standing, its strengths and weaknesses, 
        and how it fares against its competitors in the current
        market scenario. Make sure to use the most recent data as much as possible""",

    )

  def filings_analysis(self, agent):
    return Task(description=dedent(f"""
        Analyze the latest 10-Q and 10-K filings from EDGAR for
        the stock in question. 
        Focus on key sections like Management's Discussion and
        Analysis, financial statements, insider trading activity, 
        and any disclosed risks.
        Extract relevant data and insights that could influence
        the stock's future performance.

        Your final answer must be an expanded report that now
        also highlights significant findings from these filings,
        including any red flags or positive indicators for
        your customer. Always cite the quarterly report you are referencing. 
        {self.__tip_section()}        
      """),
      agent=agent,
      expected_output="""An expanded text report that 
        highlights key financial statistics/ratios from these filings,
        including any red flags or positive indicators for
        your customer.""",

    )

  def recommend(self, agent):
    return Task(description=dedent(f"""
        Review and synthesize the analyses provided by the
        Financial Analyst and the Research Analyst.
        Combine these insights to form a comprehensive
        investment recommendation. 
        
        You MUST Consider all aspects, including financial
        health, market sentiment, and qualitative data from
        EDGAR filings.

        Make sure to include a section that shows insider 
        trading activity, and upcoming events like earnings.

        Your final answer MUST be a recommendation for your
        customer. It should be a full super detailed report, providing a 
        clear investment stance and strategy with supporting evidence.
        Make it pretty and well formatted for your customer.
        {self.__tip_section()}
      """),
      agent=agent,
      expected_output="""A comprehensive
        investment recommendation in text format.
        
        You MUST Consider all aspects, including financial
        health, market sentiment, and qualitative data from
        EDGAR filings.

        Make sure to include a section that shows insider 
        trading activity, and upcoming events like earnings.

        Your final answer MUST be a recommendation for your
        customer. It should be a  super detailed report(including key finance ratios from most recent 10-K and 10-Q filings), providing a 
        clear investment stance and strategy with supporting evidence.
        Make the report well formatted for your customer.""",
    )

  def __tip_section(self):
    return "If you do your BEST WORK, I'll give you a $10,000 commission!"
