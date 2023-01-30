story = {
    "start": "My super Hero is my Mum as she is the one who raised by a looked after me.",
    "middle": "She is the one the one who always wants what is best for me and for me and to succeed",
    "end": "and she is completly irreplaceable",
}

print(story)
print(type(story))
print(story.keys())

print(story.values())

print(story["start"])
print(story["middle"])
print(story["end"])

story["super_hero"] = "My-Dad"
print(story)