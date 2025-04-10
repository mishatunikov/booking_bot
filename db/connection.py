import dotenv
import os

from sqlalchemy.ext.asyncio import create_async_engine

dotenv.load_dotenv()

engine = create_async_engine(os.getenv('DATABASE_URL'), echo=True)
