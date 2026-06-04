import pg8000.dbapi
import ssl

def main():
    # Supabase DB credentials via Pooler Host from config
    username = "postgres.vlhzvprprqiljuaresnb"
    password = "PocSecurePassWord2026!"
    host = "aws-1-eu-west-2.pooler.supabase.com"
    port = 6543
    database = "postgres"

    print("Connecting to Supabase PostgreSQL database via Pooler to set up Storage Bucket...")
    
    # Configure SSL
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    try:
        conn = pg8000.dbapi.connect(
            user=username,
            password=password,
            host=host,
            port=port,
            database=database,
            ssl_context=ssl_context
        )
        cursor = conn.cursor()
        
        # Create storage bucket
        print("Creating storage bucket 'poc-files' if not exists...")
        cursor.execute("""
            INSERT INTO storage.buckets (id, name, public)
            VALUES ('poc-files', 'poc-files', true)
            ON CONFLICT (id) DO NOTHING;
        """)
        
        # Enable RLS on storage.objects if not already enabled (it is by default in Supabase)
        print("Creating storage security policies...")
        
        cursor.execute("DROP POLICY IF EXISTS \"Public Select Access\" ON storage.objects;")
        cursor.execute("CREATE POLICY \"Public Select Access\" ON storage.objects FOR SELECT USING (bucket_id = 'poc-files');")
        
        cursor.execute("DROP POLICY IF EXISTS \"Public Insert Access\" ON storage.objects;")
        cursor.execute("CREATE POLICY \"Public Insert Access\" ON storage.objects FOR INSERT WITH CHECK (bucket_id = 'poc-files');")
        
        cursor.execute("DROP POLICY IF EXISTS \"Public Delete Access\" ON storage.objects;")
        cursor.execute("CREATE POLICY \"Public Delete Access\" ON storage.objects FOR DELETE USING (bucket_id = 'poc-files');")
        
        conn.commit()
        print("Storage bucket successfully created and public policies applied!")
        
        cursor.close()
        conn.close()
    except Exception as e:
        print("Error configuring storage bucket:", e)

if __name__ == "__main__":
    main()
