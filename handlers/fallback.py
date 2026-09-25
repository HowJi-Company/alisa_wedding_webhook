"""
handlers/fallback.py — 罐頭訊息 handler
當使用者傳送無法辨識的訊息時，回傳使用說明
"""

import logging
from typing import Any, Mapping

from linebot.v3.messaging import AsyncMessagingApi, TextMessage

from utils.line_reply import format_log_context, safe_reply_message

logger = logging.getLogger(__name__)

FALLBACK_MESSAGE = (
    "謝謝您的訊息～ 此帳號僅提供下方圖文選單的自動查詢功能，無法個別回覆訊息。 "
    "歡迎直接點擊下方按鈕獲取婚禮資訊，若有其他問題請直接聯繫新人，謝謝您的體諒！"
)


async def handle_fallback(
    line_bot_api: AsyncMessagingApi,
    reply_token: str,
    context: Mapping[str, Any] | None = None,
) -> None:
    """
    回傳罐頭訊息，引導使用者使用 Rich Menu
    """
    reply_context = {**(context or {}), "handler": "fallback"}
    logger.info("進入 fallback handler %s", format_log_context(reply_context))
    await safe_reply_message(
        line_bot_api,
        reply_token=reply_token,
        messages=[TextMessage(text=FALLBACK_MESSAGE)],
        context=reply_context,
    )
    logger.info("fallback handler 執行完成 %s", format_log_context(reply_context))
