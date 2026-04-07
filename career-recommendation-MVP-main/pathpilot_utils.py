import json
from functools import lru_cache
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

from typing import Dict, List, Set, Any
import re

CAREERS: Dict[str, Dict[str, object]] = {
    "ai engineer": {
        "title": "AI Engineer",
        "overview": "Build and deploy machine learning solutions for real-world products.",
        "why": "Your interest in AI maps directly to this role, and your technical curiosity is a strong fit for model building.",
        "salary_range": "INR 12L - 30L / year",
        "development_plan": [
            "Learn Python, statistics, and core ML concepts.",
            "Build small models with public datasets.",
            "Practice deploying AI features into apps.",
        ],
        "emoji": "🤖",
        "skills": ["Python", "ML", "Data"],
    },
    "entrepreneur": {
        "title": "Entrepreneur",
        "overview": "Build and grow new ventures around customer needs and market opportunities.",
        "why": "Your business mindset and leadership potential fit the venture-building path.",
        "salary_range": "Variable: INR 0 - 1Cr+ / year",
        "development_plan": [
            "Study problem discovery and customer validation.",
            "Learn basics of pricing, sales, and operations.",
            "Launch a small project or side venture.",
        ],
        "emoji": "💼",
        "skills": ["Strategy", "Leadership", "Execution"],
    },
    "ui/ux designer": {
        "title": "UI/UX Designer",
        "overview": "Design user-centered digital experiences and product interfaces.",
        "why": "Your design interest suggests strong potential for crafting intuitive experiences.",
        "salary_range": "INR 7L - 22L / year",
        "development_plan": [
            "Learn UX principles and visual hierarchy.",
            "Create wireframes and interactive prototypes.",
            "Build a portfolio with redesigned product screens.",
        ],
        "emoji": "🎨",
        "skills": ["Design", "Research", "Prototyping"],
    },
    "software developer": {
        "title": "Software Developer",
        "overview": "Build reliable software applications using modern engineering practices.",
        "why": "Your coding interest and problem-solving mindset align with software development.",
        "salary_range": "INR 8L - 28L / year",
        "development_plan": [
            "Master Python basics and programming logic.",
            "Create small apps and APIs.",
            "Practice debugging and version control workflows.",
        ],
        "emoji": "💻",
        "skills": ["Coding", "APIs", "Debugging"],
    },
    "career consultant": {
        "title": "Career Consultant",
        "overview": "Guide people in career planning, skill development, and role transitions.",
        "why": "Your profile is broad and adaptable, making a consulting path a solid fallback.",
        "salary_range": "INR 6L - 18L / year",
        "development_plan": [
            "Practice coaching and communication skills.",
            "Learn career frameworks and goal-setting methods.",
            "Support others with structured career advice.",
        ],
        "emoji": "🧭",
        "skills": ["Communication", "Coaching", "Planning"],
    },
    "doctor": {
        "title": "Doctor",
        "overview": "Diagnose and treat patients while delivering evidence-based clinical care.",
        "why": "Your medical and healthcare-oriented interests align strongly with patient care roles.",
        "salary_range": "INR 10L - 35L / year",
        "development_plan": [
            "Strengthen biology and clinical fundamentals.",
            "Complete relevant medical education and licensing.",
            "Build practical experience through rotations and supervised practice.",
        ],
        "emoji": "🩺",
        "skills": ["Clinical Knowledge", "Patient Care", "Decision Making"],
    },
    "nurse": {
        "title": "Nurse",
        "overview": "Provide frontline patient care, monitoring, and care coordination in healthcare settings.",
        "why": "Your healthcare focus and people-first mindset fit nursing pathways.",
        "salary_range": "INR 4L - 12L / year",
        "development_plan": [
            "Pursue nursing education and practical labs.",
            "Develop patient assessment and emergency response skills.",
            "Gain supervised clinical experience and certifications.",
        ],
        "emoji": "👩‍⚕️",
        "skills": ["Patient Care", "Empathy", "Clinical Procedures"],
    },
    "financial analyst": {
        "title": "Financial Analyst",
        "overview": "Analyze financial data to guide investment and business decisions.",
        "why": "Your finance interest and analytical orientation map well to this role.",
        "salary_range": "INR 7L - 24L / year",
        "development_plan": [
            "Build accounting and corporate finance foundations.",
            "Practice spreadsheet modeling and financial analysis.",
            "Work on valuation and reporting case studies.",
        ],
        "emoji": "📈",
        "skills": ["Financial Modeling", "Excel", "Analysis"],
    },
    "accountant": {
        "title": "Accountant",
        "overview": "Manage financial records, reporting, and compliance for organizations.",
        "why": "Your profile indicates strong alignment with structured finance and reporting work.",
        "salary_range": "INR 5L - 14L / year",
        "development_plan": [
            "Learn accounting standards and reporting workflows.",
            "Practice journal entries, reconciliations, and tax basics.",
            "Pursue professional accounting certification tracks.",
        ],
        "emoji": "🧾",
        "skills": ["Accounting", "Compliance", "Attention to Detail"],
    },
}


CAREER_KEYWORDS: Dict[str, Set[str]] = {
    "ai engineer": {"ai", "machine learning", "ml", "data", "python", "model", "artificial intelligence", "tech"},
    "entrepreneur": {"business", "startup", "founder", "strategy", "market", "sales"},
    "ui/ux designer": {"design", "ui", "ux", "figma", "prototype", "creative", "user"},
    "software developer": {"coding", "software", "programming", "developer", "api", "backend", "frontend", "python", "java", "javascript"},
    "career consultant": {"career", "guidance", "coaching", "communication", "planning"},
    "doctor": {"medical", "medicine", "doctor", "healthcare", "clinical", "patient", "hospital", "mbbs"},
    "nurse": {"nursing", "nurse", "healthcare", "patient", "hospital", "clinical"},
    "financial analyst": {"finance", "financial", "investment", "analyst", "banking", "equity", "valuation", "accounting"},
    "accountant": {"accounting", "accountant", "audit", "tax", "finance", "bookkeeping", "compliance"},
}


GITHUB_SIGNAL_MAP: Dict[str, str] = {
    "python": "Python",
    "javascript": "JavaScript",
    "typescript": "TypeScript",
    "java": "Java",
    "c": "C",
    "c++": "C++",
    "cpp": "C++",
    "csharp": "C#",
    "go": "Go",
    "golang": "Go",
    "rust": "Rust",
    "kotlin": "Kotlin",
    "swift": "Swift",
    "php": "PHP",
    "ruby": "Ruby",
    "react": "React",
    "nextjs": "Next.js",
    "next": "Next.js",
    "node": "Node.js",
    "nodejs": "Node.js",
    "django": "Django",
    "flask": "Flask",
    "fastapi": "FastAPI",
    "streamlit": "Streamlit",
    "tensorflow": "TensorFlow",
    "pytorch": "PyTorch",
    "scikit": "Scikit-learn",
    "ml": "Machine Learning",
    "ai": "AI",
    "data": "Data Analysis",
    "sql": "SQL",
    "mongodb": "MongoDB",
    "postgresql": "PostgreSQL",
    "docker": "Docker",
    "kubernetes": "Kubernetes",
    "aws": "AWS",
    "azure": "Azure",
    "gcp": "GCP",
}


def parse_skills(text: str) -> List[str]:
    values = [item.strip().title() for item in text.split(",") if item.strip()]
    deduped: List[str] = []
    for value in values:
        if value not in deduped:
            deduped.append(value)
    return deduped[:6]


def normalize_words(text: str) -> Set[str]:
    lowered = text.lower().replace("/", " ").replace("-", " ").replace(",", " ")
    return {part.strip() for part in lowered.split() if part.strip()}


def expand_keyword_tokens(keywords: Set[str]) -> Set[str]:
    tokens: Set[str] = set()
    for keyword in keywords:
        kw = keyword.strip().lower()
        if not kw:
            continue
        tokens.add(kw)
        tokens |= normalize_words(kw)
    return tokens


def _dedupe_keep_order(items: List[str], limit: int = 10) -> List[str]:
    output: List[str] = []
    for item in items:
        if item and item not in output:
            output.append(item)
    return output[:limit]


def _extract_github_username(github_url: str) -> str:
    if not github_url:
        return ""

    text = github_url.strip().rstrip("/")
    if text.startswith("@"):
        return text[1:]

    parsed = urlparse(text if "//" in text else f"https://{text}")
    if "github.com" not in parsed.netloc.lower():
        return ""

    parts = [part for part in parsed.path.split("/") if part]
    if not parts:
        return ""

    username = parts[0].strip()
    if username.lower() in {"features", "topics", "orgs", "about", "marketplace", "settings", "login"}:
        return ""
    return username


def _map_github_tokens_to_skills(tokens: Set[str]) -> List[str]:
    inferred: List[str] = []
    for token in tokens:
        mapped = GITHUB_SIGNAL_MAP.get(token)
        if mapped:
            inferred.append(mapped)
    return _dedupe_keep_order(inferred, limit=8)


def _read_json(url: str) -> object:
    request = Request(url, headers={"User-Agent": "PathPilot-App", "Accept": "application/vnd.github+json"})
    with urlopen(request, timeout=8) as response:
        return json.loads(response.read().decode("utf-8"))


@lru_cache(maxsize=32)
def fetch_github_skill_signals(github_url: str) -> List[str]:
    username = _extract_github_username(github_url)
    if not username:
        return []

    try:
        profile_data = _read_json(f"https://api.github.com/users/{username}")
        repos_data = _read_json(f"https://api.github.com/users/{username}/repos?per_page=20&sort=updated")

        tokens: Set[str] = set()
        if isinstance(profile_data, dict):
            profile_text = " ".join(
                [
                    str(profile_data.get("bio", "") or ""),
                    str(profile_data.get("company", "") or ""),
                ]
            )
            tokens |= normalize_words(profile_text)

        if isinstance(repos_data, list):
            for repo in repos_data:
                if not isinstance(repo, dict):
                    continue

                language = str(repo.get("language") or "").strip().lower()
                if language:
                    tokens.add(language)

                repo_text = " ".join(
                    [
                        str(repo.get("name", "") or ""),
                        str(repo.get("description", "") or ""),
                    ]
                )
                tokens |= normalize_words(repo_text)

                topics = repo.get("topics") or []
                if isinstance(topics, list):
                    for topic in topics:
                        tokens |= normalize_words(str(topic))

        return _map_github_tokens_to_skills(tokens)
    except (HTTPError, URLError, TimeoutError, ValueError):
        return []


def map_interest_to_primary_role(interest: str) -> str:
    lowered = interest.lower()
    if any(term in lowered for term in ["medical", "medicine", "doctor", "health", "healthcare", "nursing"]):
        return "doctor"
    if any(term in lowered for term in ["finance", "financial", "bank", "investment", "account"]):
        return "financial analyst"
    if "ai" in lowered:
        return "ai engineer"
    if "business" in lowered:
        return "entrepreneur"
    if "design" in lowered:
        return "ui/ux designer"
    if "coding" in lowered:
        return "software developer"
    return "career consultant"


def detect_domain(interest_words: Set[str], industry_words: Set[str], education_words: Set[str], skill_words: Set[str]) -> str:
    all_words = interest_words | industry_words | education_words | skill_words

    medical_terms = {
        "medical", "medicine", "doctor", "health", "healthcare", "nursing", "nurse", "clinical", "hospital", "patient", "mbbs"
    }
    finance_terms = {
        "finance", "financial", "bank", "banking", "investment", "investments", "equity", "account", "accounting", "audit", "tax"
    }

    if all_words & medical_terms:
        return "medical"
    if all_words & finance_terms:
        return "finance"
    return "general"


def build_recommendations(profile: Dict[str, str]) -> List[Dict[str, object]]:
    primary = map_interest_to_primary_role(profile["interest"])
    skills = parse_skills(profile["skills_text"])
    github_signals = fetch_github_skill_signals(profile.get("github_url", ""))
    combined_profile_skills = _dedupe_keep_order(skills + github_signals, limit=10)

    interest_words = normalize_words(profile.get("interest", ""))
    industry_words = normalize_words(profile.get("industry", ""))
    education_words = normalize_words(profile.get("education", ""))
    skill_words = {s.lower() for s in combined_profile_skills}

    domain = detect_domain(interest_words, industry_words, education_words, skill_words)

    if domain == "medical":
        candidate_keys = {"doctor", "nurse", "career consultant", "entrepreneur"}
    elif domain == "finance":
        candidate_keys = {"financial analyst", "accountant", "entrepreneur", "career consultant"}
    else:
        candidate_keys = set(CAREER_KEYWORDS.keys())

    career_scores: List[Dict[str, object]] = []
    for key, keywords in CAREER_KEYWORDS.items():
        if key not in candidate_keys:
            continue
        keyword_tokens = expand_keyword_tokens(keywords)
        score = 0

        score += len(interest_words & keyword_tokens) * 5
        score += len(industry_words & keyword_tokens) * 4
        score += len(skill_words & keyword_tokens) * 3
        score += len(education_words & keyword_tokens) * 2

        if key == primary:
            score += 8

        # Light domain boosts for richer finance/medical behavior.
        if "finance" in industry_words and key in {"financial analyst", "accountant"}:
            score += 6
        if "healthcare" in industry_words and key in {"doctor", "nurse"}:
            score += 6

        career_scores.append({"key": key, "score": score})

    career_scores.sort(key=lambda item: item["score"], reverse=True)

    ordered_keys = [entry["key"] for entry in career_scores]
    primary_score = 0
    for entry in career_scores:
        if entry["key"] == primary:
            primary_score = int(entry["score"])
            break

    top_score = int(career_scores[0]["score"]) if career_scores else 0

    # Avoid showing Career Consultant first for most profiles unless it is truly the best match.
    should_promote_primary = (
        primary in ordered_keys
        and primary != "career consultant"
        and (primary_score > 0 or top_score == 0)
    )

    if should_promote_primary:
        ordered_keys.remove(primary)
        ordered_keys.insert(0, primary)

    if top_score == 0:
        fallback_order: List[str] = [primary, "software developer", "ai engineer", "financial analyst", "doctor", "career consultant"]
        seen: Set[str] = set()
        ordered_keys = [key for key in fallback_order + ordered_keys if key in candidate_keys and not (key in seen or seen.add(key))]

    recommendations: List[Dict[str, object]] = []
    for key in ordered_keys[:5]:
        item = CAREERS[key]
        combined_skills = combined_profile_skills[:4] + [s for s in item["skills"] if s not in combined_profile_skills]
        matched = list((interest_words | industry_words | skill_words) & expand_keyword_tokens(CAREER_KEYWORDS.get(key, set())))
        matched = [token.replace("_", " ").title() for token in matched if token]
        dynamic_why = item["why"]
        if matched:
            dynamic_why = f"Matched signals: {', '.join(matched[:3])}. {item['why']}"
        if github_signals:
            dynamic_why += f" GitHub signals detected: {', '.join(github_signals[:3])}."
        recommendations.append(
            {
                "title": item["title"],
                "career_overview": item["overview"],
                "personalized_explanation": dynamic_why,
                "why_this_career": dynamic_why,
                "development_plan": item["development_plan"],
                "emoji": item["emoji"],
                "skills": combined_skills[:5],
                "salary_range": item.get("salary_range", "INR 6L - 18L / year"),
                "match_score": max(65, 95 - (len(recommendations) * 5)),
            }
        )
    return recommendations


MENTOR_QUESTIONS: List[Dict[str, Any]] = [
    {
        "id": "thinking_style",
        "prompt": "When solving a tough challenge, what feels most natural to you?",
        "options": [
            {"label": "Break it into clear logic and systems", "value": "logic"},
            {"label": "Imagine bold ideas and test creatively", "value": "creative"},
            {"label": "Blend structure with creative experimentation", "value": "balanced"},
            {"label": "Look at people impact before technical detail", "value": "human"},
        ],
    },
    {
        "id": "motivation",
        "prompt": "What keeps you most driven in your career decisions right now?",
        "options": [
            {"label": "High income and rapid growth", "value": "money"},
            {"label": "Purpose and passion for the work", "value": "passion"},
            {"label": "Stability and long-term security", "value": "stability"},
            {"label": "Freedom and flexibility", "value": "freedom"},
        ],
    },
    {
        "id": "skill_confidence",
        "prompt": "How confident are you in your current skill base for competitive roles?",
        "options": [
            {"label": "High confidence, I can execute now", "value": "high"},
            {"label": "Moderate, I can grow fast with guidance", "value": "medium"},
            {"label": "Early stage, I need a clear build-up plan", "value": "early"},
            {"label": "Strong in one area, weak in others", "value": "spiky"},
        ],
    },
    {
        "id": "work_preference",
        "prompt": "Which work setup helps you perform at your best?",
        "options": [
            {"label": "Deep solo focus and ownership", "value": "solo"},
            {"label": "Fast collaboration with diverse teams", "value": "team"},
            {"label": "Hybrid: autonomy with strategic collaboration", "value": "hybrid"},
            {"label": "High interaction with users or clients", "value": "client"},
        ],
    },
    {
        "id": "effort_tolerance",
        "prompt": "How much stretch are you willing to handle in the next 12 months?",
        "options": [
            {"label": "Intense sprint mode for major growth", "value": "high"},
            {"label": "Consistent effort with healthy balance", "value": "medium"},
            {"label": "Steady but lower-pressure pace", "value": "low"},
            {"label": "Focused bursts around key milestones", "value": "burst"},
        ],
    },
    {
        "id": "problem_solving",
        "prompt": "What kind of problems make you feel energized?",
        "options": [
            {"label": "Technical systems and optimization", "value": "systems"},
            {"label": "People behavior and user journeys", "value": "people"},
            {"label": "Business strategy and growth levers", "value": "business"},
            {"label": "Innovation in products and experiences", "value": "innovation"},
        ],
    },
]


MENTOR_CAREERS: List[Dict[str, Any]] = [
    {
        "title": "AI Product Manager",
        "salary_range": "INR 18L - 45L / year",
        "skills_required": ["Product Thinking", "AI Fundamentals", "User Research", "Experimentation", "Stakeholder Leadership"],
        "industry_insights": "AI-native products are hiring leaders who can connect models, users, and business outcomes.",
        "risks": "Role pressure is high; weak technical fluency can slow execution credibility.",
        "roadmap": {
            "0-3": ["Master product metrics and AI basics", "Audit 5 AI products and reverse-engineer decisions"],
            "3-6": ["Ship one end-to-end AI feature concept", "Build portfolio case study with tradeoffs"],
            "6-12": ["Lead cross-functional execution in internship/startup", "Refine PM storytelling for interviews"],
        },
        "fit_weights": {"logic": 2, "creative": 2, "balanced": 3, "human": 2, "money": 2, "passion": 2, "freedom": 1, "team": 2, "hybrid": 2, "innovation": 3, "business": 3},
    },
    {
        "title": "Software Engineer",
        "salary_range": "INR 10L - 35L / year",
        "skills_required": ["Programming", "System Design", "Debugging", "APIs", "Version Control"],
        "industry_insights": "Engineering talent with product sense is in strong demand across startups and global teams.",
        "risks": "Without portfolio depth, competition can feel crowded in entry-level hiring.",
        "roadmap": {
            "0-3": ["Sharpen language fundamentals and DSA", "Build two practical mini-projects"],
            "3-6": ["Develop production-style full-stack project", "Practice code reviews and testing"],
            "6-12": ["Contribute to open source or freelance projects", "Target high-quality internship/job pipelines"],
        },
        "fit_weights": {"logic": 3, "balanced": 2, "money": 2, "stability": 2, "solo": 2, "hybrid": 2, "systems": 3, "high": 2},
    },
    {
        "title": "UX Designer",
        "salary_range": "INR 8L - 24L / year",
        "skills_required": ["UX Research", "Visual Design", "Interaction Design", "Prototyping", "Storytelling"],
        "industry_insights": "Teams want designers who can prove user impact, not just beautiful screens.",
        "risks": "Portfolio quality matters heavily; generic designs get filtered quickly.",
        "roadmap": {
            "0-3": ["Learn design foundations and heuristics", "Redesign 3 real product flows"],
            "3-6": ["Create detailed UX case studies", "Run user tests and iterate"],
            "6-12": ["Specialize in product or AI experience design", "Pitch portfolio to product-led companies"],
        },
        "fit_weights": {"creative": 3, "human": 3, "passion": 2, "freedom": 2, "team": 2, "client": 2, "people": 3, "innovation": 2},
    },
    {
        "title": "Data Analyst",
        "salary_range": "INR 7L - 20L / year",
        "skills_required": ["SQL", "Data Visualization", "Statistics", "Business Analysis", "Dashboarding"],
        "industry_insights": "Data-driven decision teams are expanding in fintech, healthcare, and commerce.",
        "risks": "If you only report numbers and skip business interpretation, growth may plateau.",
        "roadmap": {
            "0-3": ["Build SQL and Excel power skills", "Learn one BI tool deeply"],
            "3-6": ["Publish 3 analysis projects with insights", "Practice business storytelling"],
            "6-12": ["Solve domain-specific analytics cases", "Move toward product analytics ownership"],
        },
        "fit_weights": {"logic": 3, "stability": 2, "systems": 2, "business": 2, "medium": 1, "spiky": 1},
    },
    {
        "title": "Growth Strategist",
        "salary_range": "INR 9L - 28L / year",
        "skills_required": ["Growth Experiments", "Marketing Analytics", "Funnel Design", "Copy Strategy", "Conversion Optimization"],
        "industry_insights": "Startups reward operators who can tie campaigns directly to revenue and retention.",
        "risks": "Fast cycles can lead to burnout without strong prioritization systems.",
        "roadmap": {
            "0-3": ["Study core growth loops and channels", "Run small A/B experiments"],
            "3-6": ["Build acquisition-to-retention dashboard", "Own one measurable growth objective"],
            "6-12": ["Lead multi-channel growth strategy", "Scale repeatable playbooks"],
        },
        "fit_weights": {"creative": 2, "balanced": 2, "money": 2, "freedom": 2, "business": 3, "innovation": 2, "burst": 2, "high": 1},
    },
    {
        "title": "Management Consultant",
        "salary_range": "INR 14L - 40L / year",
        "skills_required": ["Structured Problem Solving", "Business Communication", "Research", "Slide Writing", "Client Management"],
        "industry_insights": "Consulting remains a strong launchpad for high-ownership business leadership tracks.",
        "risks": "Demanding hours and travel can challenge work-life boundaries.",
        "roadmap": {
            "0-3": ["Master case frameworks and communication", "Practice problem decomposition daily"],
            "3-6": ["Build a strategy project portfolio", "Improve executive presentation quality"],
            "6-12": ["Crack interview case rounds", "Pick specialization in sector or function"],
        },
        "fit_weights": {"logic": 2, "balanced": 2, "money": 2, "stability": 1, "team": 2, "client": 3, "business": 3, "high": 2},
    },
]


MENTOR_MODES: Dict[str, Dict[str, str]] = {
    "Founder Coach": {
        "question_prefix": "From a high-ownership builder lens:",
        "advice_style": "Bias toward action, momentum, and intelligent risk.",
        "roadmap_focus": "Focus: execution speed, validation, and growth signals.",
    },
    "Corporate Strategist": {
        "question_prefix": "From a strategic long-term career lens:",
        "advice_style": "Bias toward consistency, compounding expertise, and durable progression.",
        "roadmap_focus": "Focus: structured milestones, capability depth, and role progression.",
    },
    "Creative Career Architect": {
        "question_prefix": "From a creative opportunity-design lens:",
        "advice_style": "Bias toward originality, portfolio quality, and differentiated positioning.",
        "roadmap_focus": "Focus: experimentation, craft signature, and unconventional leverage.",
    },
}


def get_mentor_questions() -> List[Dict[str, Any]]:
    return MENTOR_QUESTIONS


def _make_persona(answers: Dict[str, str]) -> Dict[str, Any]:
    style = answers.get("thinking_style", "balanced")
    motivation = answers.get("motivation", "passion")
    confidence = answers.get("skill_confidence", "medium")
    work = answers.get("work_preference", "hybrid")
    effort = answers.get("effort_tolerance", "medium")
    mindset = answers.get("problem_solving", "innovation")

    style_text = {
        "logic": "structured and analytical",
        "creative": "imaginative and idea-driven",
        "balanced": "strategic with both logic and creativity",
        "human": "people-first and empathetic",
    }.get(style, "strategic")

    motivation_text = {
        "money": "high-growth outcomes and financial upside",
        "passion": "meaningful work and long-term fulfillment",
        "stability": "security and predictable progression",
        "freedom": "autonomy and flexible career design",
    }.get(motivation, "impact")

    confidence_text = {
        "high": "ready to execute at a competitive level",
        "medium": "positioned to scale quickly with focused practice",
        "early": "in foundation-building mode with strong upside",
        "spiky": "strong in select areas with room to balance your stack",
    }.get(confidence, "growing steadily")

    strengths: List[str] = []
    if style in {"logic", "balanced"}:
        strengths.append("Clear decision-making under ambiguity")
    if style in {"creative", "balanced"}:
        strengths.append("Generates fresh, practical ideas")
    if work in {"team", "hybrid", "client"}:
        strengths.append("Collaborates effectively across people")
    if mindset in {"systems", "business"}:
        strengths.append("Thinks in systems and leverage")
    if mindset in {"people", "innovation"}:
        strengths.append("Strong user and problem empathy")
    if effort in {"high", "burst"}:
        strengths.append("Can sustain focused growth sprints")

    strengths = strengths[:4] or ["Consistent learner mindset", "Adaptable in changing environments"]

    persona = (
        f"You are a {style_text} builder motivated by {motivation_text}. "
        f"Right now you are {confidence_text}, with a preference for {work}-oriented work dynamics."
    )

    return {
        "summary": persona,
        "strengths": strengths,
    }


def _score_career(answers: Dict[str, str], career: Dict[str, Any]) -> int:
    score = 55
    weights = career.get("fit_weights", {})
    for key in [
        answers.get("thinking_style", ""),
        answers.get("motivation", ""),
        answers.get("skill_confidence", ""),
        answers.get("work_preference", ""),
        answers.get("effort_tolerance", ""),
        answers.get("problem_solving", ""),
    ]:
        score += int(weights.get(key, 0)) * 4
    return min(96, max(60, score))


def _fit_explanation(answers: Dict[str, str], career_title: str) -> str:
    style = answers.get("thinking_style", "balanced")
    motivation = answers.get("motivation", "passion")
    work = answers.get("work_preference", "hybrid")

    style_part = {
        "logic": "Your structured thinking is ideal for high-clarity execution.",
        "creative": "Your creative processing gives you an edge in non-obvious opportunities.",
        "balanced": "Your balance of logic and creativity maps well to modern cross-functional roles.",
        "human": "Your people-first mindset aligns with user-centric and influence-heavy roles.",
    }.get(style, "Your mindset aligns well with evolving role demands.")

    motivation_part = {
        "money": "This path has strong upside when you build depth and consistency.",
        "passion": "This path can deliver both craft mastery and personal meaning.",
        "stability": "This role offers a dependable growth curve with clear milestones.",
        "freedom": "This path supports autonomy once core capability is established.",
    }.get(motivation, "This role aligns with long-term growth.")

    work_part = {
        "solo": "It rewards ownership and deep focus.",
        "team": "It benefits from collaborative momentum and communication.",
        "hybrid": "It gives room for independent ownership and strategic collaboration.",
        "client": "It creates high-value opportunities through direct stakeholder interaction.",
    }.get(work, "It fits your natural workflow.")

    return f"{career_title} fits because {style_part} {motivation_part} {work_part}"


def build_mentor_report(answers: Dict[str, str]) -> Dict[str, Any]:
    persona = _make_persona(answers)

    scored: List[Dict[str, Any]] = []
    for career in MENTOR_CAREERS:
        scored.append(
            {
                "title": career["title"],
                "match_score": _score_career(answers, career),
                "salary_range": career["salary_range"],
                "skills_required": career["skills_required"],
                "industry_insights": career["industry_insights"],
                "risks": career["risks"],
                "roadmap": career["roadmap"],
                "personalized_explanation": _fit_explanation(answers, career["title"]),
            }
        )

    scored.sort(key=lambda item: int(item["match_score"]), reverse=True)
    top_three = scored[:3]

    labeled = [
        {"label": "Primary Career", **top_three[0]},
        {"label": "Secondary Career", **top_three[1]},
        {"label": "Exploratory Option", **top_three[2]},
    ]

    final_advice = (
        "Commit to one primary track for the next 90 days, but keep a weekly 20% exploration block for the secondary path. "
        "Consistency beats intensity spikes. Build visible proof of work every month."
    )

    return {
        "persona": persona,
        "careers": labeled,
        "final_advice": final_advice,
    }


def _salary_to_lpa(expected_salary: str) -> int:
    text = (expected_salary or "").lower().replace(",", "")
    match = re.search(r"(\d+)", text)
    if not match:
        return 12
    value = int(match.group(1))
    if "k" in text:
        return max(4, value // 100)
    return max(4, min(80, value))


def _ordered_skills_to_focus(profile: Dict[str, str], career_skills: List[str], limit: int = 6) -> List[str]:
    profile_skills = [part.strip().title() for part in str(profile.get("skills_text", "")).split(",") if part.strip()]

    ordered: List[str] = []

    # 1) Keep strongest user signals first if they are relevant.
    for skill in profile_skills:
        if skill in career_skills and skill not in ordered:
            ordered.append(skill)

    # 2) Then fill with role-critical skills.
    for skill in career_skills:
        if skill not in ordered:
            ordered.append(skill)

    # 3) Ensure stable output length.
    fallback = ["Communication", "Problem Solving", "Execution Discipline", "Learning Agility"]
    for skill in fallback:
        if skill not in ordered:
            ordered.append(skill)

    return ordered[:limit]


def _build_development_plan(roadmap: Dict[str, List[str]]) -> List[str]:
    plan: List[str] = []
    for phase in ["0-3", "3-6", "6-12"]:
        steps = roadmap.get(phase, [])
        if steps:
            plan.append(f"{phase} months: {steps[0]}")
    return plan[:3]


def _salary_upper_lpa(salary_range: str) -> int:
    nums = re.findall(r"\d+", salary_range or "")
    if not nums:
        return 15
    if len(nums) == 1:
        return int(nums[0])
    return int(nums[1])


def build_dynamic_questions(profile: Dict[str, str]) -> List[Dict[str, Any]]:
    domain = profile.get("domain_interest", "Technology")
    experience = profile.get("experience_level", "Beginner")
    confidence = profile.get("confidence_level", "Medium")
    mode = profile.get("mentor_mode", "Corporate Strategist")
    mode_style = MENTOR_MODES.get(mode, MENTOR_MODES["Corporate Strategist"])

    domain_scenario = {
        "Technology": "Your product crashes during launch week. What do you do first?",
        "Design": "Your design gets rejected for low business impact. What is your first response?",
        "Business": "Revenue drops 20% in one quarter. Which move do you prioritize?",
        "Finance": "You find inconsistent financial assumptions in a board deck. What next?",
        "Healthcare": "A patient-care workflow slows the entire team. Where do you intervene first?",
        "Marketing": "Campaign engagement drops despite high spend. What do you test first?",
    }

    confidence_prompt = (
        "You need to choose one stretch project this month. How do you decide?"
        if confidence in {"High", "Medium"}
        else "You feel underprepared for a bigger role. What is your most effective next move?"
    )

    questions = [
        {
            "id": "thinking_style",
            "prompt": "In complex situations, how does your mind naturally organize decisions?",
            "options": [
                {"label": "I map logic, constraints, and execution paths", "value": "logic"},
                {"label": "I explore bold possibilities before narrowing", "value": "creative"},
                {"label": "I combine analysis with experimentation", "value": "balanced"},
                {"label": "I prioritize people impact and context first", "value": "human"},
            ],
        },
        {
            "id": "motivation",
            "prompt": "What outcome matters most for your next career chapter?",
            "options": [
                {"label": "Maximize compensation and growth speed", "value": "money"},
                {"label": "Build meaningful work I care about", "value": "passion"},
                {"label": "Secure predictable long-term progression", "value": "stability"},
                {"label": "Create autonomy and lifestyle flexibility", "value": "freedom"},
            ],
        },
        {
            "id": "domain_scenario",
            "prompt": domain_scenario.get(domain, domain_scenario["Technology"]),
            "options": [
                {"label": "Stabilize priorities using first-principles analysis", "value": "systems"},
                {"label": "Interview users/stakeholders and adapt direction", "value": "people"},
                {"label": "Run focused experiments and iterate quickly", "value": "innovation"},
                {"label": "Align business goals, then execute in sprints", "value": "business"},
            ],
        },
        {
            "id": "confidence_move",
            "prompt": confidence_prompt,
            "options": [
                {"label": "Pick the highest-impact project with mentorship", "value": "high"},
                {"label": "Choose a mid-risk project and ship consistently", "value": "medium"},
                {"label": "Start smaller, strengthen core stack first", "value": "early"},
                {"label": "Take a niche challenge matching my strongest skill", "value": "spiky"},
            ],
        },
        {
            "id": "work_preference",
            "prompt": f"At your current {experience} stage, which work style unlocks your best output?",
            "options": [
                {"label": "Deep solo execution with clear ownership", "value": "solo"},
                {"label": "Cross-functional collaboration with fast loops", "value": "team"},
                {"label": "Hybrid mode: independent build + strategic sync", "value": "hybrid"},
                {"label": "Client or user-facing problem solving", "value": "client"},
            ],
        },
        {
            "id": "effort_tolerance",
            "prompt": "How hard are you willing to push in the next 12 months for career acceleration?",
            "options": [
                {"label": "Intense build mode with high discipline", "value": "high"},
                {"label": "Strong consistency without burnout", "value": "medium"},
                {"label": "Steady pace with low volatility", "value": "low"},
                {"label": "Milestone-based sprints with recovery", "value": "burst"},
            ],
        },
    ]

    for question in questions:
        question["prompt"] = f"{mode_style['question_prefix']} {question['prompt']}"

    return questions


def build_hybrid_coach_report(profile: Dict[str, str], answers: Dict[str, str]) -> Dict[str, Any]:
    persona = _make_persona(answers)
    expected_lpa = _salary_to_lpa(profile.get("expected_salary", ""))
    mode = profile.get("mentor_mode", "Corporate Strategist")
    mode_style = MENTOR_MODES.get(mode, MENTOR_MODES["Corporate Strategist"])

    mode_roadmap_step: Dict[str, str] = {
        "Founder Coach": "Publish one measurable growth experiment and review weekly outcomes.",
        "Corporate Strategist": "Document monthly capability milestones and mentor feedback loops.",
        "Creative Career Architect": "Ship one signature portfolio artifact that demonstrates differentiated thinking.",
    }

    scored: List[Dict[str, Any]] = []
    for career in MENTOR_CAREERS:
        score = _score_career(answers, career)
        explanation = _fit_explanation(answers, career["title"])
        if profile.get("career_priority", "") == "income":
            score = min(98, score + 2)
        if profile.get("career_priority", "") == "stability" and "consultant" in career["title"].lower():
            score = max(60, score - 2)

        roadmap = {
            "0-3": list(career["roadmap"].get("0-3", [])) + [mode_roadmap_step.get(mode, "")],
            "3-6": list(career["roadmap"].get("3-6", [])),
            "6-12": list(career["roadmap"].get("6-12", [])),
        }
        skills_to_focus = _ordered_skills_to_focus(profile, list(career["skills_required"]), limit=6)

        scored.append(
            {
                "title": career["title"],
                "match_score": score,
                "salary_range": career["salary_range"],
                "skills_required": career["skills_required"],
                "skills_to_focus": skills_to_focus,
                "industry_insights": career["industry_insights"],
                "risks": career["risks"],
                "roadmap": roadmap,
                "development_plan": _build_development_plan(roadmap),
                "personalized_explanation": f"{explanation} {mode_style['advice_style']}",
                "salary_trajectory": {
                    "0-3": f"INR {max(4, expected_lpa - 3)}L - {max(6, expected_lpa)}L",
                    "3-6": f"INR {max(5, expected_lpa - 1)}L - {expected_lpa + 2}L",
                    "6-12": f"INR {expected_lpa}L - {expected_lpa + 5}L",
                },
            }
        )

    scored.sort(key=lambda item: int(item["match_score"]), reverse=True)
    top_three = scored[:3]
    careers = [
        {"label": "Primary Career", **top_three[0]},
        {"label": "Secondary Career", **top_three[1]},
        {"label": "Exploratory Option", **top_three[2]},
    ]

    top_score = int(top_three[0]["match_score"])
    avg_score = int(sum(int(c["match_score"]) for c in top_three) / len(top_three))
    career_confidence_score = min(98, max(65, int((top_score * 0.7) + (avg_score * 0.3))))

    confidence_base = {"Low": 52, "Medium": 66, "High": 78}.get(str(profile.get("confidence_level", "Medium")), 66)
    experience_boost = {"Beginner": 0, "Intermediate": 8, "Advanced": 14}.get(str(profile.get("experience_level", "Beginner")), 0)
    user_readiness_score = min(95, confidence_base + experience_boost)
    market_benchmark_score = min(95, max(60, int(avg_score) + 4))

    upper_salary_target = _salary_upper_lpa(top_three[0].get("salary_range", ""))
    expected_lpa = _salary_to_lpa(profile.get("expected_salary", ""))
    salary_gap = max(0, expected_lpa - upper_salary_target)

    if salary_gap >= 5:
        comparison_summary = "Ambition is high; market fit needs faster capability proof."
    elif user_readiness_score >= market_benchmark_score:
        comparison_summary = "You are tracking above current market readiness for your targets."
    else:
        comparison_summary = "You are close to market readiness; focus on targeted skill depth."

    effort = str(answers.get("effort_tolerance", "medium"))
    if effort in {"low", "medium"}:
        risk_of_inaction = "If you delay focused execution, opportunities may shift to faster movers in your target track."
    else:
        risk_of_inaction = "Your pace potential is high; inaction would mainly cost compounding momentum and earnings upside."

    fast_path = max(top_three, key=lambda c: _salary_upper_lpa(str(c.get("salary_range", ""))))["title"]
    safe_candidates = [c for c in top_three if c["title"] in {"Software Engineer", "Data Analyst", "Management Consultant"}]
    safe_path = safe_candidates[0]["title"] if safe_candidates else top_three[1]["title"]

    name = str(profile.get("name", "You")).strip() or "You"
    base_summary = str(persona.get("summary", "")).strip()
    if base_summary.lower().startswith("you are "):
        base_summary = base_summary[8:]

    persona_summary = (
        f"{name} is {base_summary.lower()} "
        f"With {profile.get('experience_level', 'current')} experience and a {profile.get('career_priority', 'balanced')} priority, "
        "the best strategy is focused execution with selective exploration."
    )

    final_advice = (
        "Choose one primary lane for 12 weeks, publish one proof-of-work artifact every month, and review your strategy on the last Sunday of each month. "
        "That rhythm compounds faster than random effort."
    )

    mode_advice: Dict[str, str] = {
        "Founder Coach": "Keep decisions fast but evidence-backed. Momentum with signal beats perfection.",
        "Corporate Strategist": "Build repeatable excellence. Reliability and depth create long-term leverage.",
        "Creative Career Architect": "Protect creative range while shipping tangible outcomes. Distinct work earns premium opportunities.",
    }

    motivational_insight = (
        f"{profile.get('name', 'You')}, clarity plus weekly execution beats overthinking. "
        "Ship proof, review progress, and your direction will compound faster than you expect."
    )

    return {
        "profile_snapshot": {
            "name": profile.get("name", ""),
            "education": profile.get("education", ""),
            "domain_interest": profile.get("domain_interest", ""),
            "career_priority": profile.get("career_priority", ""),
            "expected_salary": profile.get("expected_salary", ""),
            "mentor_mode": mode,
        },
        "persona": {
            "summary": persona_summary,
            "strengths": persona.get("strengths", []),
        },
        "strategic_snapshot": {
            "career_confidence_score": career_confidence_score,
            "user_readiness_score": user_readiness_score,
            "market_benchmark_score": market_benchmark_score,
            "comparison_summary": comparison_summary,
            "risk_of_inaction": risk_of_inaction,
            "fast_path": fast_path,
            "safe_path": safe_path,
            "motivational_insight": motivational_insight,
        },
        "careers": careers,
        "final_advice": f"{final_advice} {mode_advice.get(mode, '')}",
    }
