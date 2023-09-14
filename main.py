import openai
from dotenv import dotenv_values

config = dotenv_values(".env")

openai.api_key = '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'
def gen_blog(topic):
    response = openai.Completion.create(
        model = 'text-davinci-002',
        prompt = 'Write a paragraph about the follow topic.' + topic,
        max_tokens = 400,
        temperature = 0.3
    )

    retrieve_blog = response.choices[0].text
    return retrieve_blog

write_more = True

while write_more:
    answer = input('Write a paragraph? Y or N')
    if answer == 'Y':
        topic = input('What should this talk about?')
        print(gen_blog(topic))
    else:
        write_more = False
