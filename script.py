import time

import pytumblr
from dhooks import Webhook
from textgenrnn import textgenrnn

hook = Webhook('Webhook')

client = pytumblr.TumblrRestClient(
    'CONSUMER_KEY',
    'CONSUMER_SECRET',
    'OAUTH_TOKEN',
    'OAUTH_SECRET'
)

while True:
    textgen = textgenrnn(weights_path='weights.hdf5')
    string = textgen.generate(
        return_as_list=True, max_gen_length=1000)[0]
    if len(string) < 10:
        continue
    try:
        client.create_text("BLOG_NAME", state="published", slug="",
                           title="", body=string)  # tumblr posting
        hook.send(str(string))
    except:
        continue
    time.sleep(360)
