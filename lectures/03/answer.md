# 第3回 解答

## 演習

- 第1回（素のLLM）とエージェントの回答の違い：第一回は講座固有の情報を知らないため、一般的な推測で回答した。　第三回は事前に用語集（search_glossary）を検索してから回答を生成した。
- `--trace` で見えたツール呼び出し（ツール名と引数）：ツール名: search_glossary / 引数: {'query': 'LoRA'}　ツール名: search_glossary / 引数: {'query': 'QLoRA'}
- 1つの質問での LLM 呼び出し回数（`requests`）：2回
- 追加したツールと、docstring に書いた説明：追加したツール：make_quiz　　書いた説明："""指定した回の用語から 1 つを選び、 確認問題と答えを返す。
「第 2 回の確認問題を出して」のように、 復習用の問題を求められたときに使う。
"""

## 宿題

- 取り組んだレベル：基礎
- やったこと：INSTRUCTIONS から「必ず search_glossary で用語集を確認する」を「search_glossary を使用してはならない。」に変更して「$ uv run python -m app.agent --trace "LoRA とQLoRAの違いは？ "」の結果を比較
- 結果：普通にそのままsearch_glossaryが使われた。
- 気づき・疑問：「回の内容を聞かれたら get_lecture_summary を使う。」が間接的に影響していた。この文章をINSTRUCTIONから削除すると、search_glossaryが呼ばれなくなった。モデルには相反する手掛かりを与えているからか。
