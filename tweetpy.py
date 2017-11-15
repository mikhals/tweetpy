import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "VALUE",
    "consumer_secret"     : "VALUE",
    "access_token"        : "VALUE",
    "access_token_secret" : "VALUE" 
    }

  api = get_api(cfg)

  def tweet_image():
    image_path=raw_input("Type path for image :")
    tweet=raw_input("Type your tweet:")
    status = api.update_with_media(image_path, tweet)
    

  tweet = raw_input("Type quit to quit\nType image to tweet with image\nEnter your tweet :")
  
  while tweet !='quit':
    if tweet !='image':
      status = api.update_status(status=tweet)
      tweet = raw_input("Type quit to quit\nEnter your tweet :")
    elif tweet == 'image':
      tweet_image()
      tweet = raw_input("Type quit to quit\nEnter your tweet :")
      
    
  print("Bye!!")
  
  
  
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()

