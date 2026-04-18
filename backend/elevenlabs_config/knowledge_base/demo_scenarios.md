# Demo Talking-Point Scenarios

> 3 pre-written scenarios to use during the demo video recording. Each has intentional mistakes to showcase FluentAI's detection.

---

## Scenario 1: Job Interview Practice

**Setup:** User is practicing for a software engineering interview with Sarah Chen (HR persona).

**What the user says (with intentional mistakes):**

> "So, um, I have been working as a developer since, like, 3 years now. I work in a company that, um, make mobile applications. My main responsibility is, you know, building the frontend. I think I'm, like, pretty good at it, basically.
>
> When I face a challenge, I usually, um, try to figure out by myself first. Like, there was this one time when the app was crashing and nobody could find the problem. So I, um, stayed late and I was able to, you know, found the bug. It was a memory leak. My manager was very happy and he said me that I did a good job.
>
> I want to join your company because, um, I think it's a good company. It has many interesting project and I could learn more stuffs there."

**What FluentAI should catch:**
- Grammar: "since 3 years" → "for 3 years", "make" → "makes", "found" → "find", "said me" → "told me", "many interesting project" → "projects", "stuffs" → "things/skills"
- Fillers: um (×5), like (×3), you know (×2), basically (×1)
- Vocabulary: "good" (overused), "pretty good" (vague), "stuffs" (incorrect)
- Missed idioms: Could use "hit the ground running", "go the extra mile", "steep learning curve"
- Confidence: Excessive hedging with "I think" and "like"

---

## Scenario 2: Casual Conversation

**Setup:** User is chatting with Coach Alex about weekend plans and hobbies.

**What the user says (with intentional mistakes):**

> "On the weekend I usually, um, stay at home and watching Netflix. Sometimes I go to gym but not very often. I should to exercise more, I know.
>
> My favorite hobby is cooking. I like to cook many different type of food. Last week I tried to make, um, pasta from scratch and it was, like, really difficult. The dough was too much sticky and I don't knew what to do. But at the end it turn out okay, you know.
>
> I also like reading but I didn't read a book since a long time. I think the last book I readed was, um, maybe two months ago. It was about, like, psychology and how people make decisions. It was very interesting book."

**What FluentAI should catch:**
- Grammar: "watching" → "watch", "should to exercise" → "should exercise", "type" → "types", "too much sticky" → "too sticky", "don't knew" → "didn't know", "it turn out" → "it turned out", "didn't read since" → "haven't read for", "readed" → "read", "very interesting book" → "a very interesting book"
- Fillers: um (×3), like (×2), you know (×1)
- Vocabulary: "okay" (weak), could use more descriptive words
- Missed idioms: "once in a blue moon" (for gym), "a piece of cake" (contrast with difficulty), "from scratch" (already used — good!)
- Complexity: All simple sentences, no compound/complex structures

---

## Scenario 3: Presentation / Public Speaking

**Setup:** User is practicing a presentation about their project with David Park (VP persona in pressure mode).

**What the user says (with intentional mistakes):**

> "So, um, thank you for giving me the opportunity to present my project. Basically, what we builded is a, um, platform that help small businesses to manage their inventory.
>
> The problem is that many small business don't have, like, a good system for tracking their products. They use, you know, spreadsheets or even paper. This is very inefficient and it cause many problem.
>
> Our solution is, um, basically a web application that can track inventory in real time. We already have, like, 50 users who is using the platform and the feedback has been very positive. Most of them said that it save them many hours per week.
>
> In terms of the future, we are planning to, um, add more features and expand to other markets. I believe our platform can, you know, be very successful because the market is, like, very big and there is a lot of demand for this kind of solution."

**What FluentAI should catch:**
- Grammar: "builded" → "built", "help" → "helps", "business" → "businesses", "cause" → "causes", "problem" → "problems", "who is using" → "who are using", "it save" → "it saves"
- Fillers: um (×4), like (×3), you know (×2), basically (×2), so (×1)
- Vocabulary: "good" (vague), "very" (overused ×4), "big" (weak)
- Missed idioms: "move the needle", "from the ground up", "ahead of the curve", "raise the bar"
- Coherence: Decent structure but transitions are weak (no "furthermore", "as a result", "consequently")
- Confidence: Hedging with "I believe" and "I think", filler-heavy opening undermines authority
- Complexity: Almost all simple/compound sentences, no complex structures

---

## How to Use These in the Demo

1. **Start recording** with the FluentAI landing page visible
2. **Select a goal** (e.g., Job Interviews) → complete the diagnostic (use Scenario 1 content)
3. **Show the report card** — zoom in on the grammar errors caught, filler word count, and Ghost Correction
4. **Play the "Future You" audio** — the corrected version in the user's cloned voice
5. **Show the Speech DNA radar** — explain the 8 dimensions
6. **Start a lesson from the roadmap** (use Scenario 3 for variety)
7. **Show the live sidebar** updating during the conversation
8. **End and show the updated DNA** — compare before/after
