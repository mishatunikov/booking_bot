from pathlib import Path

from sqlalchemy.ext.asyncio import create_async_engine

BASE_DIR = Path(__file__).parent.parent
path = BASE_DIR / 'database'

if not path.exists():
    path.mkdir(parents=True)

engine = create_async_engine(f'sqlite+aiosqlite:///{path}/text.db', echo=True)
