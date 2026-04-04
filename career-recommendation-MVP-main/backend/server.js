const express = require("express");
const cors = require("cors");
const careers = require("./careers");

const app = express();

// Allow frontend to send data
app.use(cors());
app.use(express.json());

// MAIN API
app.post("/recommend", (req, res) => {

  // Step 1: Receive data from frontend
  const { interest, industry, education, skills } = req.body;

  // Step 2: Add score to every career
  const scoredCareers = careers.map(career => {

    let score = 0;
    let reasons = [];

    // Interest match
    if (career.interest === interest) {
      score += 4;
      reasons.push("matches your interest");
    }

    // Industry match
    if (career.industry === industry) {
      score += 3;
      reasons.push("fits your preferred industry");
    }

    // Skill match
    career.skills.forEach(skill => {
      if (skills.includes(skill)) {
        score += 2;
        reasons.push(`uses your ${skill} skill`);
      }
    });

    // Education match
    if (career.minEdu === education) {
      score += 1;
      reasons.push("aligns with your education level");
    }

    return { ...career, score, reasons };
  });

  // Step 3: Sort by best score
  scoredCareers.sort((a, b) => b.score - a.score);

  // Step 4: Send top 5 to frontend
  res.json(scoredCareers.slice(0, 5));
});

// Start server
app.listen(3000, () => {
  console.log("Backend running on http://localhost:3000");
});