def decrypt_story():
    storyText = get_story_string()
    obj1 = CiphertextMessage(storyText)
    return obj1.decrypt_message()