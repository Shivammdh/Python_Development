# importing the module
import pywhatkit

# using Exception Handling for
# handling unprecendented errors
try:
	
# it will perform google search
	pywhatkit.info("bhagat singh", lines = 4)
	print("\nSuccessfully Searched")

except:
	
# printing error message
	print("An Unknown Error Occured")
