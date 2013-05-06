import json

# Preferences
#
# 	This class represents all game preferences stored in a dictionary
# 	Each preference is a key/value structure where key = preference name
#	and value = preference value
#

class Preferences :

	# Preferences dictionary
	# Don't forget to add preference with default value
	preferences = {}
	preferences["width"] = 640
	preferences["height"] = 480
	
	# Get value for given key
	def value(self, key) :
		return self.preferences[key]
		
	# Set value for given key
	def setValue(self,key,value) :
		self.preferences[key] = value
		
	# Serialize preferences dict in "path" file
	def serialize(self, path) :
		f = open(path, 'w')
		json.dump(self.preferences,f)
		f.close()
	
	# Deserialize preferences dict from "path" file
	def deserialize(self, path) :
		f = open(path, 'r')
		self.preferences = json.load(f)
