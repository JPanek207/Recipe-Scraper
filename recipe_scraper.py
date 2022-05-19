import requests
from bs4 import BeautifulSoup
import random

# Paste the direct link to your recipe website - here I've linked to a recipe website after applying the filters 'Main Course' and 'Healthy-Ish'
URL = "https://www.halfbakedharvest.com/recipes/?_recipe_meal=main-course&_recipe_diet_specific=healthy-ish"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

recipe_name=[]

# Here is where we focus our search - here I'm targeting the 'h3 class = "post-summary__title"' - this is found in the developer console for the website.
# Each website will have a different target based on how the website is set up/what information we're looking to gather
recipe_name_list = soup.find_all("h3",class_="post-summary__title")

# Here I've grouped our titles and URLs into a list
for recipe in recipe_name_list:
  title = recipe.text
  url = recipe.find("a")["href"]
  recipe_name.append((title, url))

random_recipe_name = random.sample(recipe_name, 10)

# Here I've cleaned up the output to provide each recipe title and associated URL on their own individual lines
print(*random_recipe_name, sep = '\n')




