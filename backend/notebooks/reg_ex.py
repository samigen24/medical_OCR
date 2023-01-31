import re


text = f""" Follow our leader Elon musk on Twitter 
            here: https://twitter.com/elonmusk, more information  
            on Tesla's products can be found at https://www.tesla.com/. 
            Also here are leading influencers for tesla-related news, 
            https://twitter.com/teslarati  
            https://twitter.com/dummy_tesla 
            https://twitter.com/dummy_2_tesla

    """


pattern = 'com\/([^e.].*)'
match = re.findall(pattern, text)
print(match[0].strip())
print(match[1].strip())
print(match[2].strip())



