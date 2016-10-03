import aiml 
k=aiml.Kernel()
k.learn("std.xml")
k.respond("load")
while True:print k.respond(raw_input("message:"))
