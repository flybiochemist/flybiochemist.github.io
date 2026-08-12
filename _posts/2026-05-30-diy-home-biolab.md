---
title: 700만원으로 홈랩 꾸리기
date: 2026-05-30
permalink: /posts/2026-05-30-2/
tags:
  - biology
  - lab-tips
---

최소한의 비용으로 홈랩을 꾸리기 위해 무엇이 필요한지 가끔 AI들과 이야기하며 업데이트하고 있다.

## 기본장비 갖추기

1. 냉장고 - 가정용(4°C/-20°C), 좀더 강한 냉동을 원한다면 참치냉동고(-50~-60°C)를 사용한다. 가격은 50~100만원 정도(개당)
2. 인큐베이터: 계란부화기 사용. 5-10만원. shaker/rocker는 Alibaba를 통해 부품 주문후 조립(개당 3-5만원)
3. 원심분리기, PCR기기: 중고 구매(30-100만원). 또는 Raspberry Pi 기반 DIY PCR 오픈소스 기기(OpenPCR, Ninja PCR)
4. DNA 전기영동/UV light - 아크릴 + 부품도면짜서 조립
5. 파이펫 - 중고 20-30만원, 팁은 씻어서 재사용
6. 현미경 - 기존현미경 + LED & 필터 + 웹캠

이정도면 작은 실험 준비에 필요한 장비들을 500만원 정도 안에서 갖추었다.

## 기본재료 갖추기

- 박테리아: DH5alpha 사용(보통 실험실과 같음)
- 동물세포: CO2와 고온조건이 필요없는(22-25°C) 초파리 세포 사용, 하지만 FBS는 사서 써야함
- Taq polymerase: 해당 박테리아 분양(ATCC 25104) 후 직접 추출/정제
- Transfection reagent: Polyethylenimine(PEI) 사용
- DNA/RNA 추출: kit을 안쓰던 옛날 방식으로 추출
- DNA 래더: 람다 DNA를 HindIII, EcoRI으로 잘라서 만듦
- DNA restriction enzyme: 이건 상업적으로 구매
- 필요한 화합물과 플라스틱웨어: 역시 구매
- 항체: 유전자를 GFP로 태깅, Addgene의 anti-GFP nanobody expressing bacteria(Plasmid #49172)를 정제하여 GFP 디텍션

이정도면 간단한 실험을 적당한 비용으로 진행할 수 있다. 재료비도 한 200만원정도. 도합 700이면 홈랩 가능.

## 참고문헌

- https://www.hackteria.org/about/
- https://sphere.diybio.org/
