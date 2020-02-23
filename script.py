from textgenrnn import textgenrnn
from discord_webhook import DiscordWebhook
import pytumblr
import oauth
import oauth2 #one of them works, idk which one
import time
while True:
    textgen = textgenrnn(weights_path='weights.hdf5',
                     vocab_path='vocab.json',
                     config_path='config.json')

    textgen.generate_samples(n=1, max_gen_length=300)
    textgen.generate_to_file('temp.txt', n=1, max_gen_length=300)
    f = open ("temp.txt","r")  # i know this isn't the best method, it is to create a temp file to then read to a variable
    string = f.read()
    string
    webhook = DiscordWebhook(url='DISCORD_WEBHOOK_LINK', content = string) # discord webhook 
    client = pytumblr.TumblrRestClient(
  'CONSUMER_KEY',
  'CONSUMER_SECRET',
  'OAUTH_TOKEN',
  'OAUTH_SECRET')
    client.create_text("BLOG_NAME", state="published", slug="", title="", body=string) #tumblr posting
    webhook.execute()
    time.sleep(360)