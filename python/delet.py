import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

connectDatabase = os.getenv("conn")


    # Connect to the PostgreSQL database
conn = psycopg2.connect(connectDatabase)
cursor = conn.cursor()

    # Retrieve the user's question and corresponding answer from the database
query ="DELETE id,user_id,question,answer,search_date FROM search_history WHERE user_id = '13'"
cursor.execute(query)
results = cursor.fetchall()

    # Display the user's question and the corresponding answer(s)

    #     receive_message( "No history found.", align="right")

    # Close the database connection
conn.close()

    # Clear the entry field
