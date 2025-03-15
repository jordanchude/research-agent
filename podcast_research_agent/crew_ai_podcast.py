from crewai import Crew, Agent, Task
from tools import GoogleSearchAPI, RSSFeedParser, SocialMediaScraper, AIResearchModel, FeedlyAPI, GoogleNewsAPI

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

# Assuming you have set up your API keys
google_api = GoogleSearchAPI(api_key='your_api_key')
feedly_api = FeedlyAPI(access_token='your_access_token')

# Example usage in a task
search_results = google_api.search("latest podcast trends")
print(search_results)  # This is where you handle the output

stream_id = 'user/your_user_id/category/global.all'  # Replace with your actual stream ID
latest_articles = feedly_api.get_latest_articles(stream_id)
print(latest_articles)  # This is where you handle the output

# Initialize APIs
google_news_api = GoogleNewsAPI(api_key='your_api_key')
rss_parser = RSSFeedParser()

# Fetch news articles
news_results = google_news_api.search_news("creator economy trends", num_results=5)

# Print the results
for item in news_results.get('items', []):
    print(f"Title: {item.get('title')}")
    print(f"Link: {item.get('link')}")
    print(f"Snippet: {item.get('snippet')}\n")

# Fetch RSS feed entries
rss_entries = rss_parser.fetch_latest("https://example.com/rss")
for entry in rss_entries:
    print(entry.title, entry.link)
