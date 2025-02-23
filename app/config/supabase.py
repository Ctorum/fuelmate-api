from supabase import create_client
from decouple import config

supabase_url = config('SUPABASE_URL')
supabase_key = config('SUPABASE_KEY')

supabase_client = create_client(supabase_url, supabase_key)
