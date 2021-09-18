import pywhatkit
  
# using Exception Handling
# to avoid exceptions
try:
    pywhatkit.text_to_handwriting("""Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.

It is used for:

web development (server-side),
software development,
mathematics,
system scripting.
What can Python do?
Python can be used on a server to create web applications.
Python can be used alongside software to create workflows.
Python can connect to database systems. It can also read and modify files.
Python can be used to handle big data and perform complex mathematics.
Python can be used for rapid prototyping, or for production-ready software development.
Why Python?
Python""",rgb=(0,0,255))
    print("writing...")
  
except:
    print("Network Error Occured")
