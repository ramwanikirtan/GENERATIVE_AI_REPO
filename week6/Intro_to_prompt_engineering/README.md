# **Prompt Engineering for Generative AI - Week 6**

## **Introduction to Week 6: Prompt Engineering**
Prompt engineering is the key to unlocking the true potential of Generative AI. In Week 6, we cover two crucial parts:

- **Week 6.1: Basic Prompt Engineering**
- **Week 6.2: Types of Prompts (Text, Image, Video)**

This repository will help you understand how to structure effective prompts to work with generative AI tools and make them deliver meaningful, actionable results. From crafting the right language to applying advanced techniques for refining AI-generated outputs, we’ll cover the foundations and then build on them with practical applications and advanced strategies.

---

## How to run the labs (quick)

1. Pick a platform (ChatGPT / OpenAI Playground for text, DALL·E/MidJourney for images, Runway for video).
2. Use the prompt gallery below — paste prompts into the UI, adjust sliders/options, and run.
3. Save outputs in a shared Google Drive folder and paste results into the class evaluation Sheet.
---


## **Week 6.1: Basic Prompt Engineering**

### **What is Prompt Engineering?**

At its core, prompt engineering is the process of crafting clear, concise, and highly specific instructions for AI models. These instructions guide AI systems (such as GPT-3, DALL-E, and others) to produce the desired output. The goal is to improve the efficiency and accuracy of the AI response by providing it with structured inputs that reduce ambiguity.

### **Analogy:**
Think of prompt engineering like giving directions to a GPS. If you say, “Take me somewhere,” the GPS will not know your destination. However, if you say, “Take me to [address],” the GPS knows exactly where to guide you. Similarly, well-engineered prompts tell the AI exactly what kind of result you want.

---

### **The Core Components of a Good Prompt**
To design effective prompts, it's essential to understand the basic components:

1. **Instruction**: What do you want the AI to do? (e.g., "Generate a summary," "Write a paragraph," "Create a report")

2. **Context**: Provide background information or constraints to guide the AI. (e.g., “Write for a professional audience,” “Based on the latest research,” “Consider current trends”)

3. **Input Data**: What information or data is needed to complete the task? (e.g., “Use the provided statistics,” “Reference this article,” “Include this data set”)

4. **Output Format**: Specify how the output should be structured. (e.g., “Write a 500-word article,” “List 5 points,” “Create 3 slides”)

#### **Example:**
A vague prompt:  
> “Write about global warming.”

A specific prompt:  
> “Write a 300-word blog post explaining the impact of global warming on coastal cities, highlighting the economic and social consequences, and using data from 2020 reports.”

By refining prompts to include specific instructions, context, and desired output format, you get more accurate and tailored results.

---

### **Why Prompt Engineering Matters**

Prompt engineering plays a significant role in enhancing the quality of the AI output, reducing iteration time, and improving user control over the generated content.

- **Efficiency**: A well-designed prompt ensures the AI can deliver precise results in a shorter time.
- **Accuracy**: Clear instructions help prevent irrelevant or erroneous outputs, ensuring the content aligns with your requirements.
- **Creativity**: With clear instructions, the AI can generate creative ideas, especially in marketing, design, and storytelling.

---

### **Best Practices for Prompt Engineering**

#### **1. Be Specific**
Ambiguity leads to irrelevant outputs. Always be clear about what you want.  
**Example:**  
Instead of saying, “Tell me about the environment,” say, “Explain the environmental effects of plastic pollution on marine life.”

#### **2. Provide Context**
The more background information you give the AI, the more accurate and contextually relevant the output will be.  
**Example:**  
For an article about climate change, you can add context: “Write a 500-word article for a non-technical audience, focusing on the causes and effects of climate change, and provide examples from the latest 2024 research.”

#### **3. Test and Refine**
Effective prompting requires continuous testing and refinement. Start with a basic prompt, evaluate the output, and refine the prompt until you achieve the desired result.  
**Example:**  
Start with: “Write about renewable energy.”  
Refine: “Write a 400-word essay discussing the economic benefits of solar power in reducing energy costs for businesses in North America.”

---

## **Week 6.2: Types of Prompts (Text, Image, Video)**

### **Types of Prompts Overview**
While text prompts are the most common, generative AI tools today allow us to create not only written content but also images and videos. The structure of the prompt will differ depending on the type of content you wish to generate.

---

### **1. Text Prompts**

Text prompts are used for creating written content, including articles, reports, blog posts, emails, and even code.

#### **Best Practices for Text Prompts:**
- **Be specific with your request**: Tell the AI exactly what you need (e.g., word count, tone, target audience).
- **Define the style**: Whether it’s formal, casual, persuasive, or technical, specifying the tone is crucial for generating relevant text.

#### **Example Prompt:**
> “Write a 300-word blog post on the benefits of daily exercise for mental health, with a casual tone aimed at young professionals, using one personal anecdote.”

---

### **2. Image Prompts**

Image prompts instruct generative models (e.g., DALL-E, MidJourney) to create images based on text descriptions.

#### **Best Practices for Image Prompts:**
- **Describe the scene vividly**: Include details such as setting, characters, objects, lighting, and mood.
- **Specify the style**: Define whether you want the image to be photorealistic, minimalist, abstract, etc.

#### **Example Prompt:**
> “Create a high-resolution image of a futuristic city with flying cars, neon signs, and skyscrapers, set during a vibrant sunset, in a cyberpunk style.”

#### **Use Case:**
Marketing teams can leverage AI image generators to create custom visuals for ad campaigns, saving time and costs compared to traditional graphic design processes.

---

### **3. Video Prompts**

Video prompts are used to generate video content or manipulate existing footage. Tools like **RunwayML** allow users to create custom videos, animations, and transitions based on text inputs.

#### **Best Practices for Video Prompts:**
- **Be clear about the video type**: Specify if it’s an animation, live-action, or explainer video.
- **Describe the pace and tone**: Should it be fast-paced or slow? Should the video have a serious or playful tone?

#### **Example Prompt:**
> “Create a 60-second animated explainer video on how blockchain works, featuring colorful visuals, simple text overlays, and a friendly voiceover.”

#### **Use Case:**
Video generation AI tools are commonly used in eLearning to create explainer videos, simplifying complex concepts for students.

---

## **Practical Use Cases for Prompt Engineering**

### **Case Study 1: Marketing Campaign**

A marketing team wants to generate multiple social media posts for a product launch:

- **Prompt for Text Generation**: “Write five different promotional tweets for our new eco-friendly product launch, highlighting its unique features, and maintaining a positive, upbeat tone.”
- **Prompt for Image Generation**: “Create five images of the eco-friendly product in use, in various natural settings, with bright and clean visuals.”
- **Prompt for Video Generation**: “Generate a 30-second promotional video for the eco-friendly product, featuring upbeat music, a model using the product in an outdoor setting, and animated text highlighting its benefits.”

By generating multiple types of content (text, image, video) using specific prompts, the marketing team can launch a well-rounded campaign in less time.

---
## Prompt gallery (copy/paste)

- Short summary (ChatGPT):
	"Summarize the following article in 4 sentences and list 2 key takeaways. Article: <paste text>"

- Quiz generator (ChatGPT):
	"Generate 5 multiple-choice questions (A–D) from the following text, with answers and brief explanations. Text: <paste text>"

- Brand image (MidJourney / DALL·E):
	"A vivid, editorial-style photo of young professionals walking in an urban plaza, pastel color grading, shallow depth of field, high contrast." 

- Explainer video (Runway):
	"Create a 20-second explainer about composting with three scenes: kitchen scraps, compost assembly, and top tips. Friendly narrator tone."
---

## Exercises (no-code)

1. Prompt Variants: Create 4 variants of the same task and compare outputs in the Sheet.
2. Visual Iteration: Generate 6 image variations and pick the best—explain why.
3. Mini-project: Build a "Lecture-to-Quiz" Zapier flow: Form -> OpenAI -> Sheet.
---
## **Tools and Resources for Prompt Engineering**

1. **OpenAI GPT-3**: Use this for creating text-based prompts and generating articles, emails, stories, and more.  
   [Visit OpenAI](https://openai.com)

2. **DALL-E**: A powerful tool for generating unique images based on text descriptions. Perfect for visual design.  
   [Visit DALL-E](https://openai.com/dall-e)

3. **RunwayML**: Provides tools for generating and editing videos, images, and even audio, enabling creatives to produce dynamic content.  
   [Visit RunwayML](https://runwayml.com)

4. **MidJourney**: Another image generation tool known for its detailed and creative visuals based on text input.  
   [Visit MidJourney](https://midjourney.com)

---

## **Conclusion**

By mastering prompt engineering, you are laying the foundation for successful interactions with generative AI models. This week’s focus on basic prompt design and the different types of prompts will provide you with the tools to generate accurate, creative, and high-quality results in your AI projects.

Next week (Week 7), we’ll cover **refining prompts**—a skill that will help you further optimize your AI outputs and learn from real-time feedback.



