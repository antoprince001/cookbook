from crew import LatestAiDevelopmentCrew
import chainlit as cl
from dotenv import load_dotenv
load_dotenv()


@cl.on_chat_start
async def on_chat_start():
    latest_ai_development_crew = LatestAiDevelopmentCrew()
    cl.user_session.set("crewobject", latest_ai_development_crew)
    await cl.Message(
        content="Please type the topic you would like to get a report about."
    ).send()


@cl.on_message
async def main(message: cl.Message):
    latest_ai_development_crew = cl.user_session.get("crewobject") 
    inputs = {
        'topic': message.content
    }
    output = latest_ai_development_crew.crew().kickoff(inputs=inputs)
    await cl.Message(
        content=f"{output}",
    ).send()
