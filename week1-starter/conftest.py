import sys
from pathlib import Path

# 让 tests/ 里能直接 `from io_utils import ...`
sys.path.insert(0, str(Path(__file__).parent))
