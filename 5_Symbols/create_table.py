import pg8000.dbapi
import ssl

def main():
    # Supabase DB credentials via Pooler Host from config
    username = "postgres.vlhzvprprqiljuaresnb"
    password = "PocSecurePassWord2026!"
    host = "aws-1-eu-west-2.pooler.supabase.com"
    port = 6543
    database = "postgres"

    print("Connecting to Supabase PostgreSQL database via Pooler...")
    
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
        
        # Create table
        print("Creating table 'tasks' if not exists...")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id SERIAL PRIMARY KEY,
                title TEXT NOT NULL,
                completed BOOLEAN DEFAULT FALSE,
                created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
            );
        """)
        
        # Enable Row Level Security (RLS) but add policy for anonymous access for simple POC
        print("Enabling RLS and setting policies...")
        cursor.execute("ALTER TABLE tasks ENABLE ROW LEVEL SECURITY;")
        cursor.execute("DROP POLICY IF EXISTS \"Allow public access\" ON tasks;")
        cursor.execute("CREATE POLICY \"Allow public access\" ON tasks FOR ALL USING (true) WITH CHECK (true);")
        
        # Insert sample data
        print("Inserting sample tasks...")
        cursor.execute("INSERT INTO tasks (title, completed) VALUES ('Configure Azure KeyVault', true);")
        cursor.execute("INSERT INTO tasks (title, completed) VALUES ('Initialize Supabase POC project', true);")
        cursor.execute("INSERT INTO tasks (title, completed) VALUES ('Create dynamic frontend menu', false);")
        
        conn.commit()
        print("Database successfully configured and populated with sample data!")
        
        # Verify inserted data
        cursor.execute("SELECT id, title, completed FROM tasks;")
        rows = cursor.fetchall()
        print("Current tasks in database:")
        for row in rows:
            print(f" - [{ 'x' if row[2] else ' ' }] ID {row[0]}: {row[1]}")
            
        cursor.close()
        conn.close()
    except Exception as e:
        print("Error connecting or executing queries:", e)

if __name__ == "__main__":
    main()
