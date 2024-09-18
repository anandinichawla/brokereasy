

import os 
import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    
    #path to the excel file 
    file_path = 'files/simpledata.xlsx'

    #read the excel file using pandas 
    df = pd.read_excel(file_path)

#    # Add a new column for the phone icon
#     df['Phone Icon'] = '<i class="fas fa-phone"></i>'  # Static phone icon for every row

    # Add a new column for the phone icon, wrapped in a 'tel:' link
    
    
    print(df.columns)


    df['Phone Icon'] = df['Phone Number '].apply(lambda x: f'<a href="tel:{x}"><i class="fas fa-phone"></i></a>')

    # Convert DataFrame to HTML (escape=False to allow rendering of HTML tags)
    table_html = df.to_html(classes='table table-striped', escape=False)  

    # Render the template with the table
    return render_template('index.html', table_html=table_html)

if __name__ == '__main__':
    app.run(debug=True)


