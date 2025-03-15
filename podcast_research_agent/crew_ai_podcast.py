from crewai import Crew, Agent, Task
from tools import GoogleSearchAPI, RSSFeedParser, SocialMediaScraper, AIResearchModel

# Define the Research & Content Development Agent
research_agent = Agent(
    name="Research & Content Development Agent",
    role="Identifies trending podcast topics, analyzes industry trends, and creates structured episode outlines.",
    tools=[GoogleSearchAPI(), RSSFeedParser(), SocialMediaScraper(), AIResearchModel()]
)

# Define Tasks
task_trend_analysis = Task(
    name="Analyze Industry Trends",
    agent=research_agent,
    description="Fetch trending topics from Google, RSS feeds, and social media. Identify high-engagement keywords and competitor strategies."
)

task_content_outline = Task(
    name="Generate Episode Outline",
    agent=research_agent,
    description="Create a structured episode outline using research insights, including key discussion points and audience engagement patterns."
)

# Define Crew
crew = Crew(
    agents=[research_agent],
    tasks=[task_trend_analysis, task_content_outline]
)

# Run the Workflow
crew.kickoff()
