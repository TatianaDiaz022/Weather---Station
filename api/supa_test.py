import hashlib
from supabase import create_client, Client

#Supabase data connection: URL, KEY
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNza2R4ZnF1emRlcmFhcGdhb2duIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzAxNjY1ODgsImV4cCI6MjA0NTc0MjU4OH0.T1mKwc99-A09HXZ251jSOXaZwvHvsIcTdOq3lVUZlZ4"
SUPABASE_URL = "https://cskdxfquzderaapgaogn.supabase.co"

#Connect to Supabase Client 
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

#Get and save data function
def save_data(e, p):
    #inset into users model
    enc_pass = hashlib.sha256(p.encode()).hexdigest()
    response = supabase.table('user').insert({"email": e,"password": enc_pass}).execute()
    
    if response.data:
        print(f"User has been save successfully: {response.data}")
    elif response.error:
        print(f"Error saving user: {response.error}")
      
#main
email=input("User e-mail:")
passwd=input("User password: ")
save_data(email,passwd)
   