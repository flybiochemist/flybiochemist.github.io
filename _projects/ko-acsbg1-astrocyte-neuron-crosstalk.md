---
title: "ACSBG1을 매개로 한 별아교세포-신경세포 상호작용"
collection: projects
permalink: /ko/projects/acsbg1-astrocyte-neuron-crosstalk
lang: ko
translation: /projects/acsbg1-astrocyte-neuron-crosstalk
order: 2
status: "BioRxiv 프리프린트 (2026)"
summary: "별아교세포에만 발현하는 지질 대사 효소가 어떻게 신경세포 안의 α-Synuclein을 바꾸는지, 그리고 그 효소를 없앴을 때 왜 파킨슨병 모델 마우스가 회복되는지에 관한 연구입니다."
---

## 질문

α-Synuclein(α-Syn) 병리는 신경세포에서 일어나는 문제이지만, 신경세포는 혼자 있지 않습니다. 별아교세포가 신경세포의 대사를 지원하고 뇌의 지질 처리를 상당 부분 담당하는데, 질병 상황에서는 보호하는 상태에서 반응성 상태로 성질이 바뀝니다.

이전에 수행한 유전체 전체 스크리닝에서 **ACSBG1**(Acyl-CoA Synthetase Bubblegum Family Member 1)이 생체 내에서 α-Syn 양을 조절하는 인자로 확인되었습니다. ACSBG1은 긴 사슬 및 매우 긴 사슬 지방산을 fatty acyl-CoA로 전환하는 효소이며, 뇌에서는 거의 별아교세포에서만 발현됩니다.

여기서 분명한 의문이 남았습니다. **신경세포가 아닌 세포 안에 있는 지질 대사 효소가, 어떻게 신경세포 안의 α-Syn을 바꾸는가?**

## 접근 방법

핵심 실험은 조건 배지(conditioned medium) 전달입니다. 야생형 또는 *Acsbg1* 넉아웃 마우스에서 얻은 일차 배양 별아교세포를 TNF-α와 IL-1α로 자극해 반응성 상태로 만든 뒤, 그 배지를 일차 배양 신경세포에 옮겼습니다. 그 주위로 별아교세포가 무엇을 하고 무엇을 내보내는지를 함께 분석했습니다.

- 별아교세포 자체의 RNA-seq
- 분비된 배지에 대한 사이토카인 항체 어레이와 비표적 지질체 분석
- 후보 사이토카인과 사슬 길이별 합성 스핑고신의 개별 첨가(add-back) 실험
- 효소 활성만을 분리해 보기 위한 촉매 활성 결손 ACSBG1(K701A) 변이체
- 생체 내 검증을 위한 *Acsbg1* 넉아웃과 Thy1-α-Syn(Line 61) 형질전환 마우스의 교배

## 발견한 것

<figure class="project__figure">
<svg viewBox="0 0 720 286" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="acsbg1-ko-title acsbg1-ko-desc">
  <title id="acsbg1-ko-title">별아교세포의 ACSBG1이 신경세포 알파시뉴클레인 인산화를 일으키는 경로</title>
  <desc id="acsbg1-ko-desc">두 개의 경로를 비교합니다. 야생형 별아교세포에서는 TNF-알파와 IL-1알파 자극으로 ACSBG1이 활성화된 반응성 상태가 되고, IL-6, RANTES, MIP-3알파와 함께 긴 사슬 스핑고신 C20:1 및 C22:1을 분비하며, 신경세포에서 세린 129 인산화 알파시뉴클레인이 증가합니다. Acsbg1 넉아웃 별아교세포에서는 같은 자극에도 사이토카인 분비가 줄고 스핑고신이 기준 수준으로 돌아가며, 신경세포의 인산화 알파시뉴클레인은 증가하지 않습니다.</desc>

  <defs>
    <marker id="ac-ko-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="var(--global-text-color)"/>
    </marker>
  </defs>

  <text x="6" y="20" font-size="12" font-weight="bold" fill="var(--global-base-color)">야생형 별아교세포 &#8212; 병리가 전달됨</text>
  <g stroke="var(--global-text-color)" stroke-width="1" fill="none">
    <rect x="6" y="34" width="76" height="64" rx="4"/>
    <rect x="110" y="34" width="140" height="64" rx="4"/>
    <rect x="278" y="34" width="210" height="64" rx="4" stroke="var(--global-base-color)" fill="var(--global-base-color)" fill-opacity="0.08"/>
    <rect x="516" y="34" width="88" height="64" rx="4"/>
  </g>
  <g font-size="12" fill="var(--global-text-color)" text-anchor="middle">
    <text x="44" y="62">TNF-&#945;</text>
    <text x="44" y="78">IL-1&#945;</text>
    <text x="180" y="62">반응성 별아교세포</text>
    <text x="180" y="80" font-weight="bold">ACSBG1 활성</text>
    <text x="383" y="56">IL-6 &#183; RANTES &#183; MIP-3&#945;</text>
    <text x="383" y="74">스핑고신</text>
    <text x="383" y="90" font-weight="bold">C20:1 / C22:1</text>
    <text x="560" y="72">신경세포</text>
    <text x="662" y="64" font-weight="bold" fill="var(--global-base-color)">pS129-&#945;-Syn</text>
    <text x="662" y="80" font-weight="bold" fill="var(--global-base-color)">증가 &#8593;</text>
  </g>
  <g stroke="var(--global-text-color)" stroke-width="1.5" marker-end="url(#ac-ko-arrow)">
    <line x1="84" y1="66" x2="106" y2="66"/>
    <line x1="252" y1="66" x2="274" y2="66"/>
    <line x1="490" y1="66" x2="512" y2="66"/>
    <line x1="606" y1="66" x2="624" y2="66"/>
  </g>

  <text x="6" y="162" font-size="12" font-weight="bold" fill="var(--global-text-color)">Acsbg1 넉아웃 &#8212; 연결이 끊김</text>
  <g stroke="var(--global-text-color)" stroke-width="1" fill="none" stroke-opacity="0.55">
    <rect x="6" y="176" width="76" height="64" rx="4"/>
    <rect x="110" y="176" width="140" height="64" rx="4"/>
    <rect x="278" y="176" width="210" height="64" rx="4" stroke-dasharray="4 3"/>
    <rect x="516" y="176" width="88" height="64" rx="4"/>
  </g>
  <g font-size="12" fill="var(--global-text-color)" text-anchor="middle">
    <text x="44" y="204">TNF-&#945;</text>
    <text x="44" y="220">IL-1&#945;</text>
    <text x="180" y="204">반응성 별아교세포</text>
    <text x="180" y="222" font-weight="bold">Acsbg1 넉아웃</text>
    <text x="383" y="198">사이토카인 분비 감소</text>
    <text x="383" y="216">스핑고신은 기준</text>
    <text x="383" y="232">수준으로 회복</text>
    <text x="560" y="214">신경세포</text>
    <text x="662" y="214" font-weight="bold">변화 없음</text>
  </g>
  <g stroke="var(--global-text-color)" stroke-width="1.5" stroke-opacity="0.55" marker-end="url(#ac-ko-arrow)">
    <line x1="84" y1="208" x2="106" y2="208"/>
    <line x1="252" y1="208" x2="274" y2="208"/>
    <line x1="490" y1="208" x2="512" y2="208"/>
  </g>

  <text x="6" y="276" font-size="11" fill="var(--global-text-color)" fill-opacity="0.75">사이토카인 하나만으로도, C20:1 또는 C22:1 스핑고신 하나만으로도 신경세포의 pS129-&#945;-Syn을 올리기에 충분합니다.</text>
</svg>
<figcaption>ACSBG1은 별아교세포의 지질 처리와 염증성 분비물을 연결합니다. 이 효소를 없애면 별아교세포는 여전히 반응성이지만, 신경세포에 도달하는 매개 물질이 사라집니다.</figcaption>
</figure>

**병리는 배지를 통해 전달됩니다.** 반응성 야생형 별아교세포의 조건 배지는 신경세포의 총 α-Syn과 pS129-α-Syn을 모두 증가시켰습니다. 반응성 *Acsbg1* 넉아웃 별아교세포의 배지는 그렇지 않았습니다.

**매개 물질은 하나가 아니라 둘입니다.** *Acsbg1*이 없으면 별아교세포의 TNF 신호전달 전사 반응이 둔해지고 염증 매개 물질의 분비가 줄었습니다. 그중 **IL-6, RANTES, MIP-3α** 세 가지가 두드러졌는데, 이들 각각을 정상 배지에 하나씩만 넣어 주어도 신경세포의 α-Syn과, 특히 pS129-α-Syn을 올리기에 충분했습니다.

지질 쪽도 나란히 움직였습니다. 사이토카인 자극은 야생형 배지에서 스핑고신, LBPA, 헥소실세라마이드를 증가시켰고, *Acsbg1*을 없애면 이들이 기준 수준으로 돌아왔습니다. 넉아웃 배지에 합성 스핑고신을 넣어 본 결과 사슬 길이에 따른 선택성이 뚜렷했습니다. **C20:1과 C22:1은 신경세포의 pS129-α-Syn을 다시 올렸지만, C16:1과 C18:1은 아무 영향이 없었습니다.**

**단백질의 존재가 아니라 효소 활성이 중요합니다.** 범-ACS 억제제인 Triacsin C는 넉아웃과 같은 효과를 냈습니다. 넉아웃 별아교세포에 야생형 ACSBG1을 다시 발현시키면 신경세포 병리를 일으키는 능력이 회복되었지만, 촉매 활성이 없는 K701A 변이체는 그렇지 않았습니다.

**생체 내에서도 성립합니다.** Thy1-α-Syn 마우스에서 *Acsbg1*을 없애자 상동 행동과 세우기 행동이 정상화되었고, 평행봉과 폴 테스트 수행이 개선되었으며, 대뇌피질과 중뇌의 총 α-Syn 및 pS129-α-Syn이 감소하고, GFAP 별아교세포 활성화가 해소되었으며, PSD95가 보존되었습니다. 표지자만 움직인 것이 아니라 시냅스가 실제로 보호되었다는 뜻입니다.

## ACSBG1이 좋은 표적인 이유

발현 범위가 특이하게 좁습니다. 뇌에서는 별아교세포에, 말초에서는 정소와 난소 정도에 국한됩니다. 게다가 *Acsbg1* 넉아웃 마우스는 뚜렷한 기본 표현형을 보이지 않습니다. 건강한 상태에서는 뇌가 이 효소의 소실을 견딘다는 뜻입니다. 종합하면 치료 범위(therapeutic index)가 넓은 표적일 가능성이 큽니다. 질병과 연관된 별아교세포 반응성만 선택적으로 낮추면서 부수적인 손실은 크지 않을 수 있습니다.

## 다음 단계

Thy1-α-Syn은 과발현 모델이고, 생후 5주부터 이미 결손이 심해서 로타로드나 악력 검사는 바닥에 닿아 있어 개선을 구분해 내기 어렵습니다. 자연스러운 다음 단계는 [*Snca*<sup>G51D/G51D</sup> 넉인 모델](/ko/projects/g51d-knock-in-mice)에서 *Acsbg1* 결손을 시험하는 것입니다. 이 모델은 내인성 발현 수준에서 병리가 진행되고, 운동 증상이 나타나기 전 전구기 구간이 존재합니다. 이 조합이라면 이미 포화된 표현형을 둔화시키는 것이 아니라, 진행 중인 시누클레인병증을 실제로 늦출 수 있는지를 확인할 수 있을 것입니다.

## 참고 문헌

Kim Y\*, Vaidya B\*, Kim J, Bitar S, Shajan FJ, Verma AK, Yalamanchili HK, Singh S, Zoghbi HY. Astrocytic ACSBG1 depletion improves lipid-cytokine signaling and attenuates α-Synuclein pathology in a Parkinson's disease mouse model. *BioRxiv* May 2026. [doi:10.64898/2026.05.20.726454](https://doi.org/10.64898/2026.05.20.726454)

\* 공동 제1저자
