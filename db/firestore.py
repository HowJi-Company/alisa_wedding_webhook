"""
db/firestore.py — Firestore AsyncClient 管理
提供全域 client 實例，以及 init/close 生命週期函式
"""

import json
import os
import logging
from google.cloud.firestore_v1.async_client import AsyncClient
from google.oauth2 import service_account

logger = logging.getLogger(__name__)

# 全域 AsyncClient，由 lifespan 初始化後供各 handler 使用
_db: AsyncClient | None = None


def _build_firestore_client() -> AsyncClient:
    """
    建立 Firestore AsyncClient。

    優先順序：
    1. GOOGLE_CREDENTIALS_JSON：整份 service account JSON（Railway 用）
    2. GOOGLE_APPLICATION_CREDENTIALS：本機金鑰檔路徑
    3. 預設 ADC
    """
    raw_json = os.environ.get("GOOGLE_CREDENTIALS_JSON", "").strip()
    if raw_json:
        info = json.loads(raw_json)
        credentials = service_account.Credentials.from_service_account_info(info)
        project_id = info.get("project_id")
        logger.info("Firestore 使用 GOOGLE_CREDENTIALS_JSON")
        return AsyncClient(project=project_id, credentials=credentials)

    credentials_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if credentials_path:
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path
        logger.info("Firestore 使用 GOOGLE_APPLICATION_CREDENTIALS")

    return AsyncClient()


async def init_firestore() -> None:
    """初始化 Firestore AsyncClient。"""
    global _db
    _db = _build_firestore_client()
    logger.info("Firestore AsyncClient 建立完成")


async def close_firestore() -> None:
    """關閉 Firestore 連線，釋放資源"""
    global _db
    if _db is not None:
        _db.close()
        _db = None
        logger.info("Firestore AsyncClient 已關閉")


def get_db() -> AsyncClient:
    """取得全域 Firestore AsyncClient，若未初始化則拋出例外"""
    if _db is None:
        raise RuntimeError("Firestore AsyncClient 尚未初始化，請先呼叫 init_firestore()")
    return _db


# ── 常用集合名稱常數 ──────────────────────────────────────────
COLLECTION_SETTINGS = "settings"
DOC_MAIN = "main"
COLLECTION_SEATS = "guests"
COLLECTION_USER_STATES = "user_states"
