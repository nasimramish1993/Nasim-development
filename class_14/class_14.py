import pandas as pd
import os 
from jinja2 import Template
# from pyhtml2pdf import converter

# Dictionary will capture the variables and data we want to have on the pretty pdf
pdf_variables_dict = {}

# Lets get the name and fav colors for our PDF! 
first_name = input("What is your first name?: ").title()
fav_color = input("What is your favorite color?: ").title()

pdf_variables_dict.update({"firstname": first_name, "fav color": fav_color})
print(pdf_variables_dict)
template = Template('<p style="text-align: center;"><strong> Hi, {{firstname}}, your favorite color is {{fav_color}}</strong></p>')
# pdf_template = '''
# <p style="text-align: center;"><strong> Hi, {{firstname}}, your favorite color is {{fav_color}}</strong></p>
# '''

func= open("name_and_color.html", 'w')
func.write(template.render(pdf_variables_dict))