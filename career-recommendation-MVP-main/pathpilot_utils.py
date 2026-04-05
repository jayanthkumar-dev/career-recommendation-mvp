import json
from functools import lru_cache
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

from typing import Dict, List, Set

CAREERS: Dict[str, Dict[str, object]] = {
    "ai engineer": {
        "title": "AI Engineer",
        "overview": "Build and deploy machine learning solutions for real-world products.",
        "why": "Your interest in AI maps directly to this role, and your technical curiosity is a strong fit for model building.",
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
        dynamic_why = item["why"]
        if matched:
            dynamic_why = f"Matched signals: {', '.join(matched[:3])}. {item['why']}"
        if github_signals:
            dynamic_why += f" GitHub signals detected: {', '.join(github_signals[:3])}."
        recommendations.append(
            {
                "title": item["title"],
                "career_overview": item["overview"],
                "why_this_career": dynamic_why,
                "development_plan": item["development_plan"],
                "emoji": item["emoji"],
                "skills": combined_skills[:5],
                "match_score": max(65, 95 - (len(recommendations) * 5)),
            }
        )
    return recommendations
