# 말풍선 브레인스토밍

아이들과 시뮬레이션 프로그램을 기획할 때 쓰는 브레인스토밍 보드입니다. 나온 말을 입력하면 아이폰 메시지 모양 말풍선으로 떠다니고, '분류하기'를 누르면 다음 화면에서 아이들이 직접 끌어서 **기능**과 **디자인**으로 나눕니다.

디자인은 [thebestwaytosendadm-client](https://github.com/jewonr/thebestwaytosendadm-client)를 따릅니다: SUIT-600 폰트, 자간 -0.5px 말풍선 글자, `#1973DD` / `#DDDDDD` 말풍선, 70px 알약 입력창과 둥근 ↑ 버튼.

## 흐름

1. **모으기** — 입력한 아이디어가 말풍선으로 떠다닙니다. 오래된 것일수록 색이 연해집니다. 누르면 빼기·수정·삭제, 끌면 이동. 여러 줄을 붙여넣으면 줄마다 하나씩 들어갑니다.
2. **분류하기** — 다음 화면이 오른쪽에서 밀려 들어옵니다. 위에 아직 나누지 않은 말풍선이 있고, 아래 기능·디자인 칸으로 끌어다 놓습니다. 말풍선을 누르면 '기능으로'·'디자인으로'로도 옮길 수 있습니다.
3. 분류 화면에서 새로 입력한 말풍선은 위쪽에 들어옵니다. '‹ 모으기'를 누르면 떠다니는 화면으로 돌아갑니다.

AI 분류는 없습니다. 작업 내용은 브라우저(localStorage)에 저장됩니다.

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

GitHub 저장소 Settings → Pages에서 **Deploy from a branch**, 브랜치 `main`, 폴더 `/ (root)`가 선택되어 있으면 1분쯤 뒤 `https://jewonr.github.io/bubble-brainstorm/`에 반영됩니다.

## 라이선스

SUIT 폰트 © SUNN, [SIL Open Font License 1.1](fonts/OFL.txt).
