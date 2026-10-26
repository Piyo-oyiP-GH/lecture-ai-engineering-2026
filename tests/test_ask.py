"""素のLLM質問スクリプトのテスト（APIキーもAPI呼び出しも不要）。"""

from types import SimpleNamespace
from unittest.mock import call, patch

from app.ask import MODEL, interactive_chat


def test_interactive_chat_reuses_chat_session_for_follow_up_questions(capsys):
    with (
        patch("app.ask.genai.Client") as client_class,
        patch("app.ask.get_api_key", return_value="test-key"),
        patch("builtins.input", side_effect=["最初の質問", "続きの質問", "exit"]),
    ):
        chat = client_class.return_value.chats.create.return_value
        chat.send_message.side_effect = [
            SimpleNamespace(text="最初の回答", usage_metadata=None),
            SimpleNamespace(text="続きの回答", usage_metadata=None),
        ]
        interactive_chat()

    client_class.return_value.chats.create.assert_called_once_with(model=MODEL)
    assert chat.send_message.call_args_list == [
        call("最初の質問"),
        call("続きの質問"),
    ]
    assert "最初の回答" in capsys.readouterr().out
