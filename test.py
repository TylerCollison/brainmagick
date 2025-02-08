from brainmagick import studies

counter = 0
for recording in studies.api.from_selection({"study": "broderick2019"}): 
    print ("loading recording #" + str(counter))
    recording.raw()
    recording.events()
    counter += 1