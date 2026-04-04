const careerDescriptions = {
  "Software Developer":
    "Designs, develops, and maintains software applications and systems using programming languages and frameworks.",

  "Data Analyst":
    "Analyzes data to identify trends, patterns, and insights that help organizations make informed decisions.",

  "Healthcare Administrator":
    "Manages healthcare facilities and operations, ensuring efficient services and coordination.",

  "Digital Marketer":
    "Promotes products or brands using digital channels like social media, search engines, and content platforms.",

  "Product Manager":
    "Leads product development by defining requirements, coordinating teams, and aligning products with business goals."
};
async function getRecommendations() {

  const education = document.getElementById("education").value;
  const interest = document.getElementById("interest").value;
  const industry = document.getElementById("industry").value;

  const skills = Array.from(
    document.querySelectorAll("input[type=checkbox]:checked")
  ).map(skill => skill.value);

  const payload = {
    education,
    interest,
    industry,
    skills
  };

  const response = await fetch("http://localhost:3000/recommend", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(payload)
  });

  const data = await response.json();

  const resultsDiv = document.getElementById("results");
  resultsDiv.innerHTML = "";

  if (data.length === 0) {
    resultsDiv.innerHTML = "<p>No recommendations found. Try selecting more skills.</p>";
    return;
  }

  data.forEach(career => {
  const card = document.createElement("div");
  card.className = "card";

  const description =
    careerDescriptions[career.title] || 
    "This career aligns well with your profile and interests.";

  const rationale = 
    "This career is recommended because it " +
    career.reasons.join(", ") +
    ", making it a strong match for your background.";

  const devPlan = career.developmentPlan 
    ? career.developmentPlan.split('\n').map(step => `<li>${step}</li>`).join('')
    : "<li>No specific development plan available.</li>";

  card.innerHTML = `
    <h3>${career.title}</h3>

    <p><b>Career Overview:</b><br>
    ${description}</p>

    <p><b>Why this career?</b><br>
    ${rationale}</p>
    
    <p><b>Development Plan:</b><br>
    <ul style="margin-top: 5px; margin-bottom: 10px; padding-left: 20px;">
      ${devPlan}
    </ul>
    </p>

    <p><b>Match Score:</b> ${career.score}</p>
  `;

  resultsDiv.appendChild(card);
});
}