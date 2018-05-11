import psycopg2

def conexao():

    from env.env import lerEnv

    Config = lerEnv()

    HOST = Config.get("credenciaisBanco", "HOST")
    #PORTA = Config.get("credenciaisBanco", "PORTA")
    POSTGRES_USER = Config.get("credenciaisBanco", "POSTGRES_USER")
    POSTGRES_PASSWORD = Config.get("credenciaisBanco", "POSTGRES_PASSWORD")
    POSTGRES_DB = Config.get("credenciaisBanco", "POSTGRES_DB")

    con = psycopg2.connect("host=" + HOST + 
                           " dbname=" + POSTGRES_DB +  
                           " user=" + POSTGRES_USER +  
                           " password=" + POSTGRES_PASSWORD)

    return con
