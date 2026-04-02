# Site Structure: nonairesumes.com
**Generated:** 2026-04-02

---

## URL Hierarchy

```
nonairesumes.com/
│
├── [Homepage]
│   Target: "human resume writing service", "non AI resumes"
│   Schema: ProfessionalService, WebSite
│
├── /services/                              [Services hub]
│   ├── /services/resume-writing/           [Primary — "professional resume writing service"]
│   ├── /services/executive-resume/         ["executive resume writing service"]
│   ├── /services/resume-review/            [Already exists — "resume review service"]
│   ├── /services/linkedin-optimization/    ["LinkedIn profile optimization service"]
│   ├── /services/cover-letter/             ["cover letter writing service"]
│   └── /services/career-change-resume/     ["career change resume service"]
│
├── /why-human/                             [PILLAR — "human written resume", "non AI resume"]
│   Schema: Article, FAQPage
│
├── /ats-guide/                             [PILLAR — "ATS resume guide", "ATS friendly resume"]
│   Schema: Article
│
├── /industries/                            [Industry vertical hub]
│   ├── /industries/tech-resume/            ["tech resume writing service"]
│   ├── /industries/healthcare-resume/      ["healthcare resume writer"]
│   ├── /industries/finance-resume/         ["finance resume writer"]
│   ├── /industries/government-resume/      ["government resume writer"]
│   └── /industries/executive-resume/       ["executive resume writer"]
│
├── /compare/                               [Comparison hub]
│   ├── /compare/human-vs-ai-resume/        ["human vs AI resume writer"]
│   ├── /compare/topresume-alternative/     ["topresume alternative"]
│   ├── /compare/zipjob-alternative/        ["zipjob alternative"]
│   └── /compare/resume-writing-services/   ["best resume writing service review"]
│
├── /writers/                               [Team/E-E-A-T page]
│   Schema: Person (per writer)
│
├── /guarantee/                             [60-day guarantee details]
│
├── /research/                              [Data/research hub]
│   └── /research/ai-resume-survey-2026/    [Original research — link bait]
│
├── /faq/                                   [FAQ — featured snippets]
│   Schema: FAQPage
│
├── /blog/                                  [Content hub — already exists]
│   ├── /blog/can-ats-detect-ai-resumes/
│   ├── /blog/ai-resume-red-flags/
│   ├── /blog/chatgpt-resume/
│   ├── /blog/why-resume-gets-rejected/
│   ├── /blog/ats-resume-mistakes/
│   └── [12+ more posts per roadmap]
│
├── /shop/                                  [Already exists — products/checkout]
│
├── /about/
├── /contact/
└── /press/                                 [Media mentions — future]
```

---

## Internal Linking Map

### Conversion Funnel Paths

**Path 1: Awareness → Conversion (Blog)**
```
Blog Post → /why-human/ → /services/resume-writing/ → /shop/
```

**Path 2: Direct Service Intent**
```
Homepage → /services/resume-writing/ → /writers/ → /shop/
```

**Path 3: ATS-Aware User**
```
/ats-guide/ → /services/resume-writing/ → /guarantee/ → /shop/
```

**Path 4: Comparison Shopper**
```
/compare/human-vs-ai-resume/ → /why-human/ → /services/resume-writing/ → /shop/
```

**Path 5: Industry-Specific**
```
/industries/tech-resume/ → Blog (tech resume tips) → /services/resume-writing/ → /shop/
```

---

## Internal Link Rules

| Page Type | Must Link To | Should Link To |
|-----------|-------------|----------------|
| Blog posts | 1 service page, /ats-guide/ or /why-human/ | Related blog posts, /faq/ |
| Service pages | /shop/, /writers/, /guarantee/ | Related service pages, relevant blog posts |
| Industry pages | Main /services/resume-writing/, /shop/ | Relevant blog posts |
| Pillar pages (/why-human/, /ats-guide/) | /services/resume-writing/, /shop/ | Blog posts, /compare/ pages |
| Comparison pages | /services/resume-writing/, /why-human/ | /writers/, /guarantee/ |
| Homepage | /services/resume-writing/, /why-human/, /blog/ | /writers/, /guarantee/ |

---

## Page Priority Tiers

### Tier 1 (Revenue-critical — highest optimization priority)
- Homepage
- /services/resume-writing/
- /shop/
- /why-human/

### Tier 2 (Traffic-driving — SEO priority)
- /ats-guide/
- /blog/* (all posts)
- /compare/human-vs-ai-resume/
- /services/resume-review/
- /services/linkedin-optimization/

### Tier 3 (Supporting — E-E-A-T + long-tail)
- /writers/
- /industries/*
- /faq/
- /guarantee/
- /compare/* (competitor alternatives)

### Tier 4 (Operational)
- /about/
- /contact/
- /privacy-policy/
- /terms/

---

## Meta Tag Templates

### Homepage
```
<title>Human Resume Writing Service | Non AI Resumes</title>
<meta name="description" content="Certified human resume writers who craft ATS-optimized resumes — zero AI. 60-day interview guarantee. Get 3x more interviews or we rewrite for free.">
```

### /services/resume-writing/
```
<title>Professional Resume Writing Service | Human Writers | Non AI Resumes</title>
<meta name="description" content="100% human-written, ATS-optimized resumes by certified professional writers. Matched 1-on-1 with a specialist. 60-day interview guarantee.">
```

### /why-human/
```
<title>Why Human-Written Resumes Beat AI Every Time | Non AI Resumes</title>
<meta name="description" content="Discover why AI resumes get rejected by ATS and hiring managers — and how human resume writers consistently outperform AI tools.">
```

### /ats-guide/
```
<title>Complete ATS Resume Guide 2026: Beat the Bots | Non AI Resumes</title>
<meta name="description" content="Everything you need to know about ATS resume optimization. Formatting rules, keyword strategy, common mistakes, and expert tips from certified resume writers.">
```

### Blog post template
```
<title>[Post Title] | Non AI Resumes Blog</title>
<meta name="description" content="[2–3 sentence compelling description including primary keyword]">
```

---

## XML Sitemap Structure

Priority assignments for sitemap.xml:

| Page | Priority | Change Frequency |
|------|----------|-----------------|
| Homepage | 1.0 | weekly |
| /services/* | 0.9 | monthly |
| /why-human/ | 0.9 | monthly |
| /ats-guide/ | 0.9 | monthly |
| /shop/ | 0.9 | weekly |
| /blog/* | 0.8 | weekly |
| /industries/* | 0.8 | monthly |
| /compare/* | 0.8 | monthly |
| /writers/ | 0.7 | monthly |
| /faq/ | 0.7 | monthly |
| /guarantee/ | 0.7 | monthly |
| /about/, /contact/ | 0.5 | yearly |
