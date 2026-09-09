---
title: CRISPR 넉다운을 qPCR로 확인할 때 프라이머 위치가 중요한 이유
date: 2026-09-01
permalink: /posts/2026-09-01/
lang: ko
translation: /en/posts/2026-09-01/
tags:
  - biology
  - molecular-biology
  - lab-tips
---

CRISPR-Cas9으로 넉다운이 잘 되었는지 RT-qPCR로 확인하는 경우가 많다. 마우스나 계대배양한 세포야 희석되겠지만, 스크리닝 등의 이유로 gRNA로 자르자마자 확인하는 경우 뽑은 RNA에 gRNA까지 같이 딸려와서 해당부분의 qPCR을 방해할 수 있다.

그러므로 논문에서 말하듯 이중 나선이 생긴걸 잘 풀어내고 역전사를 하는 효소를 쓰거나, 보통의(그런 좋은 효소 따로 살 일 없는) 실험자들의 경우에는 gRNA 타겟팅 지역으로부터 조금 먼 부분을 qPCR에서 타겟팅하는 부분으로 쓰는게 좋다.

PCR primer 디자인을 현명하게 하시길.

## 참고문헌

- https://www.nature.com/articles/s41587-026-03291-1
