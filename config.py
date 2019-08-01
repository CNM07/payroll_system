class Config:
    # identifier of db://(missing part is driver/connecter/adapter-by default it is psychopg2)(sth sth):password@host:port/dbname
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:system*@127.0.0.1:5432/july_payroll'
    Environment = 'Development'
    Debug = True

class Development(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:system*@127.0.0.1:5432/july_payroll'
    Environment = 'Development'
    Debug = True

class Testing(Config):
    Debug = False

class Production(Config):
    SQLALCHEMY_DATABASE_URI = ''
    Environment = 'Production'
    Debug = False
