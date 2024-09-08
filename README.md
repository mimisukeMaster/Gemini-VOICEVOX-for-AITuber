# Gemini-VOICEVOX-for-AITuber
 書籍「AITuberを作ってみたら生成AIプログラミングがよくわかった件」の中で紹介されている、LLMのAPIを使った実装部分を元に、OpenAI APIの代わりにGeminiAPIを使用するよう変更したものです。

 OpenAPI が無料で使えるプランがないため、十分な無料枠を提供しているGemini APIに変更しました。

## Requirements
以下のパッケージを`pip`でインストールしてください。
 ```cmd
google-generativeai
python-dotenv
sounddevice
soundfile
numpy
requests
```
## Directory
```
Gemini-VOICEVOX-for-AITuber
| .env (作成してください)
| gemini_api.py
| gemini_voicevox.py
| make_list_sound_device.py
| voicevox_adapter.py
∟ play_sound.py
```
### gemini_api.py
Gemini APIを呼んで回答を出力するのみのスクリプトです。（API Keyの確認用）

### gemini_voicevox.py
メインのスクリプトです。Gemini API による回答を、VOICEVOXで読み上げます。

### make_list_sound_device.py
使用できるスピーカーを表示するスクリプトです。(後述)

### voicevox_adapter.py
VOICEVOXのAPIを呼ぶスクリプトです。

### play_sound.py
音を鳴らす処理を行うスクリプトです。

## Initial Setup
1. Gemini API Key を取得し、そのAPIKeyを`.env`ファイルに格納してください。
```env
API_KEY="**************"
```

2. 使用できるPC付属のスピーカーを設定する必要があります。[make_list_sound_device.py](/make_list_sound_device.py)を実行して、PCに搭載されているスピーカー名を取得してください。<br>
その後、[gemini_voicevox](/gemini_voicevox.py)の以下の`Speaker`を変更してください。
```py
play_sound = PlaySound("Speaker")
```
例えば、以下のような場合
```log
0 Microsoft サウンド マッパー - Input, MME (2 in, 0 out)
>  1 Microphone Array (AMD Audio Dev, MME (2 in, 0 out)
   2 Microsoft サウンド マッパー - Output, MME (0 in, 2 out)
   3 スピーカー (Realtek(R) Audio), MME (0 in, 2 out)
   :
```
`3`を使うならば、`スピーカー (Realtek(R) Audio)`に変更します。

## Execution
**必ずVOICEVOXソフトを起動してから**、[gemini_voicevox](/gemini_voicevox.py)を実行してください。

## Customize
[voicevox_adapter.py](/voicevox_adapter.py)にて、`speaker_id`を変更することで喋らせる声を変更できます。

## Reference
VOICEVOX ソフトのインストール
- https://voicevox.hiroshiba.jp/

ソフト起動中に閲覧できるドキュメントページ
- http://localhost:50021/docs

## LICENCE
Gemini-VOICEVOX-for-AITuber is under [MIT license](/LICENSE).