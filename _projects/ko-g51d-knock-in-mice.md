---
title: "G51D 넉인 마우스"
collection: projects
permalink: /ko/projects/g51d-knock-in-mice
lang: ko
translation: /projects/g51d-knock-in-mice
order: 1
status: "PNAS 게재 (2024)"
summary: "파킨슨병을 일으키는 SNCA 돌연변이를 원래 유전자 자리에 넣은 마우스로, 사람에게서 증상이 나타나는 순서 — 후각과 장이 먼저, 운동은 한참 뒤 — 를 그대로 재현합니다."
---

## 기존 모델의 한계

파킨슨병은 대개 산발성으로, 나이가 들어 발병합니다. 그래서 마우스로 모델링하기가 어렵습니다. 대부분의 α-Synuclein(α-Syn) 모델은 *Thy1*이나 *prion* 같은 외래 프로모터를 써서 단백질을 과발현시키거나, 미리 만든 섬유(preformed fibril)나 바이러스를 흑질에 직접 주입합니다.

이런 모델들은 α-Syn이 과도하면 독성을 띤다는 사실은 잘 보여주었습니다. 하지만 제가 관심을 두는 질문 — **병이 어디에서 시작해서 어떻게 퍼지는가** — 에는 오히려 방해가 됩니다. 과발현 모델은 사람의 파킨슨병에서는 침범되지 않는 뇌 영역까지 α-Syn을 밀어 넣고, 주입 모델은 말초 조직을 아예 건너뜁니다. 사람에게서 가장 이른 병리가 나타난다고 알려진 바로 그 부위인데도 말입니다.

## 접근 방법

CRISPR-Cas9으로 마우스의 내인성 *Snca* 유전자 자리를 직접 편집해, 사람의 파킨슨병 유발 점 돌연변이를 넣었습니다. 돌연변이 α-Syn이 원래의 프로모터 아래에서, 원래의 발현량으로, 원래의 시공간적 분포를 유지한 채 발현되도록 한 것입니다.

시도한 네 가지 돌연변이(A30P, E46K, H50Q, G51D) 중 세 개의 계통을 확립했고, H50Q는 얻지 못했습니다. 세 계통 모두에서 *Snca* mRNA와 α-Syn 단백질 양이 야생형과 비슷했는데, 이는 이 마우스들이 발현량이 아니라 돌연변이 자체의 효과를 보여준다는 뜻입니다. 마우스의 짧은 수명 안에서는 이형접합 표현형이 드러나지 않는 경우가 많아 동형접합체를 분석했습니다.

세 계통 중 동형접합 *Snca*<sup>G51D/G51D</sup>가 가장 많은 정보를 주었습니다. G51D는 알려진 *SNCA* 돌연변이 중 사람에게서 발병이 가장 이른 편으로, 10대에 시작되는 경우도 있습니다.

## 마우스가 보여준 것

표현형이 나타나는 순서가 정해져 있다는 점, 그 순서 자체가 핵심입니다.

<figure class="project__figure">
<svg viewBox="0 0 720 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="g51d-ko-title g51d-ko-desc">
  <title id="g51d-ko-title">Snca G51D/G51D 마우스의 병리와 증상 진행 순서</title>
  <desc id="g51d-ko-desc">생후 3개월부터 18개월까지의 시간 축입니다. 증상이 나타나기 전인 3개월에 후각망울, 장 신경, 미주신경핵에서 인산화 알파시뉴클레인이 관찰됩니다. 6개월에 후각 저하와 장 통과 지연이 나타나고, 9개월에 운동 협응 장애가 시작됩니다. 12개월에는 보행 이상과 아교세포 활성화가 나타나고 병리가 흑질에 도달하며, 18개월에 도파민 신경세포가 소실되고 도파민이 감소합니다. 3개월에서 9개월 사이가 전구기이며 Braak 1기와 2기에 해당합니다.</desc>

  <rect x="34" y="36" width="310" height="228" rx="4" fill="var(--global-base-color)" fill-opacity="0.08"/>
  <text x="189" y="26" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--global-base-color)">전구기 &#8212; Braak I&#8211;II</text>
  <text x="522" y="26" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--global-text-color)">운동 증상기 &#8212; Braak III&#8211;IV</text>

  <g font-size="12" fill="var(--global-text-color)" text-anchor="middle">
    <text x="104" y="66">후각망울, 장 신경,</text>
    <text x="104" y="82">미주신경핵에서</text>
    <text x="104" y="98">pS129-&#945;-Syn</text>
    <text x="454" y="66">pS129-&#945;-Syn이</text>
    <text x="454" y="82">흑질에 도달;</text>
    <text x="454" y="98">아교세포 활성화</text>
  </g>
  <g stroke="var(--global-text-color)" stroke-opacity="0.35" stroke-width="1">
    <line x1="104" y1="108" x2="104" y2="152"/>
    <line x1="454" y1="108" x2="454" y2="152"/>
    <line x1="224" y1="188" x2="224" y2="206"/>
    <line x1="344" y1="188" x2="344" y2="206"/>
    <line x1="624" y1="188" x2="624" y2="206"/>
  </g>

  <line x1="44" y1="160" x2="684" y2="160" stroke="var(--global-text-color)" stroke-width="1.5"/>
  <g fill="var(--global-bg-color)" stroke="var(--global-text-color)" stroke-width="1.5">
    <circle cx="104" cy="160" r="5"/>
    <circle cx="224" cy="160" r="5"/>
    <circle cx="454" cy="160" r="5"/>
    <circle cx="624" cy="160" r="5"/>
  </g>
  <circle cx="344" cy="160" r="6" fill="var(--global-base-color)" stroke="var(--global-base-color)"/>

  <g font-size="11" font-weight="bold" fill="var(--global-text-color)" text-anchor="middle">
    <text x="104" y="180">3개월</text>
    <text x="224" y="180">6개월</text>
    <text x="344" y="180">9개월</text>
    <text x="454" y="180">12개월</text>
    <text x="624" y="180">18개월</text>
  </g>

  <g font-size="12" fill="var(--global-text-color)" text-anchor="middle">
    <text x="224" y="220">후각 저하,</text>
    <text x="224" y="236">장 통과 지연</text>
    <text x="344" y="220" font-weight="bold">운동 협응 장애</text>
    <text x="344" y="236">(로타로드, 발빠짐)</text>
    <text x="454" y="220">보행 이상</text>
    <text x="624" y="220">도파민 신경세포 소실,</text>
    <text x="624" y="236">도파민 감소</text>
  </g>

  <text x="44" y="288" font-size="11" fill="var(--global-text-color)" fill-opacity="0.75">축 위쪽은 분자 수준의 병리, 아래쪽은 행동 수준의 증상입니다.</text>
</svg>
<figcaption>첫 운동 증상보다 6개월 앞서 병리를 확인할 수 있습니다. 음영 구간이 비가역적 손상 이전에 치료법을 시험할 수 있는 창입니다.</figcaption>
</figure>

비운동 증상이 운동 증상보다 3개월 앞서 나타나는데, 이는 환자에게서 20년에 걸쳐 나타나는 전구 증상과 같은 순서입니다.

**세 가지 병적 α-Syn 형태**가 이 마우스에서 만들어집니다. S129가 인산화된 α-Syn, blue native PAGE에서 60 kDa부터 250 kDa 이상까지 관찰되는 가용성 올리고머, 그리고 Triton X-100에 녹지 않는 응집체입니다.

**대뇌피질 병리는 특정 층에 국한됩니다.** 3개월에는 II층과 IV층에서 신호가 나타나고, 12개월이 되면 V층까지 확장됩니다. *SNCA* 돌연변이를 가진 환자의 사후 조직에서 루이소체가 관찰되는 층과 같습니다. 반면 *Thy1*-α-Syn 과발현 마우스는 모든 피질 층에서 신호를 보입니다.

**병리는 신경세포에서 일어납니다.** pS129-α-Syn은 NeuN과 함께 관찰되고, 별아교세포에서는 나타나지 않으며, 희소돌기아교세포에서는 5% 미만에서만 보입니다. G51D 환자가 희소돌기아교세포에서 병리가 시작되는 다계통위축증(MSA)과 비슷한 양상을 보이는 경우가 있기 때문에 이 점이 중요합니다. 이 마우스는 MSA가 아니라 파킨슨병을 닮았습니다.

**운동 장애가 도파민 감소보다 먼저 옵니다.** 9개월과 18개월의 차이입니다. 신경세포의 사멸 자체보다는 도파민 신경세포의 기능 이상이 초기 운동 표현형을 이끄는 것으로 보이며, 신경염증이 세포 사멸보다 기능 이상과 더 잘 맞아떨어집니다.

## 왜 중요한가

이 진행 과정은 Braak 병기와 잘 맞습니다. 1–2기(3–6개월)에 후각과 미주신경이 침범되고, 3–4기(9–12개월)에 흑질에 도달합니다. 3개월에 이미 병리를 확인할 수 있지만 운동 증상은 9개월에야 나타나기 때문에, 이 모델은 **전구기라는 시험 구간**을 제공합니다. 비가역적인 신경세포 소실이 일어나기 훨씬 전에 후보 치료법을 시험해 볼 수 있는 시기입니다.

지금은 이 모델을 이용해, 병의 결과를 치료하는 것이 아니라 진행 경과 자체를 바꿀 수 있는지를 묻고 있습니다. [ACSBG1을 매개로 한 별아교세포-신경세포 상호작용](/ko/projects/acsbg1-astrocyte-neuron-crosstalk) 연구도 그중 하나입니다.

## 참고 문헌

Kim Y, McInnes J, Kim J, Liang YW, Veeraragavan S, Garza AR, Belfort DW, Arenkiel B, Samaco R, Zoghbi HY. Olfactory deficit and gastrointestinal dysfunction precede motor abnormalities in alpha-synuclein G51D knock-in mice. *Proc. Natl. Acad. Sci. U.S.A.* 2024, 121(39) e2406479121. [doi:10.1073/pnas.2406479121](https://doi.org/10.1073/pnas.2406479121)
