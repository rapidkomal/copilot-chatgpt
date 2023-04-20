import openai
openai.api_key = "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"
from dotenv import load_dotenv

load_dotenv()


def list_openai_models():
    openai.organization = os.getenv(OPENAI_ORGANIZATION_KEY)
    openai.api_key = os.getenv(OPENAI_API_KEY)
    model_list = openai.Model.list()
    for i in model_list['data']:
        print(i['id'])
list_openai_models()
image_url = "/Users/komal/Desktop/logo.jpg"
prompt = f"Describe this image: {image_url}"

# response = openai.Completion.create(
#     engine="image-alpha-001",
#     prompt=prompt,
#     max_tokens=128,
#     n = 1,
#     stop=None,
#     temperature=0.7
#
# )
#
# description = response.choices[0].text.strip()
# print(description)