import praw
import logging
from time import sleep
from datetime import datetime
from lib import utilities

seen_log_file = './logs/seen.csv'
nothanks_log_file = './logs/nothanks.csv'
error_log_file = './logs/errors.csv'

accepted_filter_file = './accepted_keywords.txt'
forbidden_filter_file = './forbidden_keywords.txt'

# Get configs 
user_agent, client_id, client_secret, username, password = utilities.get_config()

# Get past data
seen_list = utilities.get_old_data(seen_log_file, nothanks_log_file)

# Get filters
accepted_keywords, forbidden_keywords = utilities.get_filters(accepted_filter_file, forbidden_filter_file)


# Get praw object
reddit = praw.Reddit(user_agent=user_agent,
                     client_id=client_id, client_secret=client_secret,
                     username=username, password=password)

script_running = True

total_seen = len(seen_list)

with open(seen_log_file, 'a') as seen_writer:

	with open(nothanks_log_file, 'a') as nothanks_writer:

		while script_running:
			try:
			
				sleep(2)
				declined = False

				# Use the random subreddit finder
				new_subreddit = reddit.random_subreddit(nsfw=True)
				# Get the name of the subreddit
				new_subreddit = new_subreddit.display_name
				# Format url for logs 
				url = 'https://old.reddit.com/r/{}'.format(new_subreddit)
				# Get current date
				date = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')

				if url not in seen_list:

					# Check if we have a forbidden word in the subreddit name
					for bad_keyword in forbidden_keywords:
						if bad_keyword.lower() in new_subreddit.lower():
							# We found a bad word, double check with the accepted_keywords list
							for ok_keyword in accepted_keywords:
								if ok_keyword.lower() in new_subreddit.lower():
									# This might be a false positive (ex: 'men' in 'women' string)
									declined = False
									break
								else:
									# No thank you
									declined = True


					total_seen += 1

					if declined:
						# Add to current seen list
						seen_list.append(url)
						print('{:<25} [-]   {:<50} {} '.format(date, url, total_seen))
						# Add to nothanks file
						nothanks_writer.write('{},{}\n'.format(date, url))

					else:
						# Add to current seen list
						seen_list.append(url)	
						print('{:<25} [+]   {:<50} {}'.format(date, url, total_seen))	
						# Add to seen file
						seen_writer.write('{},{}\n'.format(date, url))

			except KeyboardInterrupt:
				script_running = False
			except Exception as e:
				print(e)
				with open(error_log_file, 'a') as errorlog:
					errorlog.write('{}\n'.format(e))
					script_running = False