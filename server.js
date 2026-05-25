import express from "express";
import bodyParser from "body-parser";
import OpenAI from "openai";
import dotenv from "dotenv";

dotenv.config();

const app = express();
app.use(bodyParser.json());

const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY
});

app.post("/chat", async (req, res) => {
  const userMessage = req.body.message;

  const response = await client.chat.completions.create({
    model: "gpt-4o-mini",
    messages: [
  {
    role: "system",
    content: `
You are MoneshSys AI chatbot for the website moneshsys.com.

Your job:
- Explain about MoneshSys Technologies website
- Answer questions about services, founder, products
- Help users navigate the website
- Be friendly and simple

Website info:
- Name: MoneshSys Technologies
- Services: Web development, apps, Scan2PDF, MiniForm
- Founder: Monesh K.K
- Purpose: Student tech learning platform
`
  },
  {
    role: "user",
    content: userMessage
  }
]
  });

  res.json({
    reply: response.choices[0].message.content
  });
});

app.listen(3000, () => {
  console.log("Server running on http://localhost:3000");
});
