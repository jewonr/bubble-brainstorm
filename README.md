# 말풍선 브레인스토밍

브레인스토밍 중에 나온 말을 입력하면 아이폰 메시지 모양 말풍선으로 떠다니고, 다 모이면 비슷한 것끼리 분류한 뒤, 고른 아이디어만 AI에게 붙여넣을 프롬프트 텍스트로 정리해 줍니다.

디자인은 [thebestwaytosendadm-client](https://github.com/jewonr/thebestwaytosendadm-client)를 따릅니다: SUIT-600 폰트, 자간 -0.5px 말풍선 글자, `#1973DD` / `#DDDDDD` 말풍선, 70px 알약 입력창과 둥근 ↑ 버튼.

## 흐름

1. **모으기** — 입력한 아이디어가 말풍선으로 떠다닙니다. 오래된 것일수록 색이 연해집니다. 누르면 수정·삭제, 끌면 이동. 여러 줄을 붙여넣으면 줄마다 하나씩 들어갑니다.
2. **고르기** — '정리하기'를 누르면 그룹으로 분류됩니다. 말풍선을 눌러 선택/제외하고, 끌어서(휴대폰은 길게 눌러서) 다른 그룹으로 옮깁니다.
3. **프롬프트** — 고른 아이디어를 그룹별 마크다운으로 정리합니다. 끝에 붙일 요청을 고르고 복사합니다.

작업 내용은 브라우저(localStorage)에 저장됩니다.

## 분류 방식

- **claude.ai 아티팩트로 열면** 보는 사람의 Claude 계정으로 Claude가 분류합니다.
- **GitHub Pages에서는** 주제 줄 오른쪽 ‘Gemini 연결’에 각자의 Google Gemini API 키를 넣으면 Gemini가 분류합니다.
  - 키는 [Google AI Studio](https://aistudio.google.com/apikey)에서 무료로 만들 수 있습니다. 무료 등급에서는 입력한 내용이 Google 서비스 개선에 쓰일 수 있습니다.
  - 키는 그 브라우저의 localStorage에만 저장되고 `generativelanguage.googleapis.com`으로만 보내집니다. 공용 컴퓨터에서는 쓰지 마세요.
  - 모델 이름은 자주 바뀌므로 키로 쓸 수 있는 모델 목록을 먼저 받아, 가장 최신의 안정판 Flash를 씁니다. 무료 한도에 걸리면 Flash-Lite 등 다음 모델로 한 번씩 더 시도합니다(최대 3개).
  - JSON 스키마 구조화 출력(`responseSchema`)으로 그룹을 받습니다.
- 키가 없거나 호출이 실패하면 겹치는 단어를 기준으로 묶는 간이 분류로 대신합니다. 결과는 끌어서 바로잡을 수 있습니다.

## 파일

| 경로 | 설명 |
| --- | --- |
| `src/index.html` | 원본 (HTML·CSS·JS 한 파일). 고칠 때는 이 파일을 수정합니다. |
| `build.py` | 폰트를 넣어 `index.html`을 만듭니다. |
| `index.html` | 빌드 결과. GitHub Pages가 이 파일을 보여 줍니다. |
| `fonts/` | SUIT SemiBold 웹폰트와 라이선스(SIL OFL 1.1). |

## 수정 후 배포

```bash
python3 build.py
git add -A && git commit -m "..." && git push
```

GitHub 저장소 Settings → Pages에서 **Deploy from a branch**, 브랜치 `main`, 폴더 `/ (root)`를 고르면 `https://<사용자명>.github.io/<저장소명>/`에 올라갑니다.

## 라이선스

SUIT 폰트 © SUNN, [SIL Open Font License 1.1](fonts/OFL.txt).
