import mesop as me
import mesop.labs as mel

"""
This sample is made with Mesop: https://google.github.io/mesop/

for running this sample, you need to run witg the following command:
$ mesop main.py

"""


# from util.chatgpt import get_response
# from util.claude import get_response
from util.gemini import get_response


@me.page(
    security_policy=me.SecurityPolicy(
        allowed_iframe_parents=["http://localhost:32123"]
    ),
    path="/",
    title="Mesop Demo Chat",
)
def page():
    mel.chat(get_response, title="Mesop Demo Chat", bot_user="Mesop Bot")
