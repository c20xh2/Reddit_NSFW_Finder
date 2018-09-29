def get_config():
	# Parse config file and return values 

	with open('config', 'r') as config_file:

		for line in config_file:
			line = line.strip()
	
			config_name = line.split('=')[0]

			# Remove the '' around the values

			config_value = line.split('=',1)[1][1:][:-1]

			if config_name == 'user_agent':
				user_agent = config_value
			if config_name == 'client_id':
				client_id = config_value
			if config_name == 'client_secret':
				client_secret = config_value
			if config_name == 'username':
				username = config_value
			if config_name == 'password':
				password = config_value

	return user_agent, client_id, client_secret, username, password



def get_old_data(seen_log_file, nothanks_log_file):

	# Make sure the files exist

	with open(seen_log_file, 'a') as f:
		pass
	with open(nothanks_log_file, 'a') as f:
		pass

	# Read them and store each line in a list
	seen_list = []
	with open(seen_log_file, 'r') as f:
		for line in f:
			seen_list.append(line.strip())
	with open(nothanks_log_file, 'r') as f:
		for line in f:
			seen_list.append(line.strip())


	return seen_list

def get_filters(accepted_filter_file, forbidden_filter_file):
	
	# Parse filters files and append data to lists

	with open(accepted_filter_file, 'r') as file:
		accepted_keywords = []
		for line in file:
			if line[1] == '#':
				pass
			else:
				accepted_keywords.append(line.strip())

	with open(forbidden_filter_file, 'r') as file:
		forbidden_keywords = []
		for line in file:
			if line[1] == '#':
				pass
			else:
				forbidden_keywords.append(line.strip())

	return accepted_keywords, forbidden_keywords