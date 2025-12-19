Nice work — what you added goes beyond the official Day 21 scope, so your README should clearly separate course requirements vs custom enhancements.
Here’s a clean, professional README.md you can paste directly.

🐍 Snake Game — Day 21 (Enhanced Version)

This project is an extended version of the Snake Game from Day 21 of the 100 Days of Code (Python) course.
In addition to the core requirements, several custom features were implemented to improve gameplay and difficulty scaling.

✅ Core Features (Course Requirements)

Snake movement using keyboard controls

Random food generation

Snake growth after eating food

Wall collision detection → Game Over

Tail collision detection → Game Over

Score tracking

Smooth animation using screen.tracer(0)

🚀 Custom Enhancements (Not Included in Course)
1️⃣ Dynamic Speed Increase

The snake speed increases as the player scores more points.

Score	Speed
0–4	Normal
5	Faster
10	Fastest

Implementation:

Controlled using time.sleep(delay)

Delay is reduced when score milestones are reached

2️⃣ Special Bonus Food 🍎🔥

Every 5th food becomes a special bonus food.

Special food properties:

Red color

Larger size

Different shape

Appears for 4 seconds only

Normal food disappears while special food is active

Technical details:

Implemented using a separate Turtle object

Controlled via special_active flag

Automatically removed using ontimer()

3️⃣ Bonus Scoring System

Normal food → +1 point

Special food → +10 points

This introduces a risk–reward mechanic, encouraging players to chase bonus food before it disappears.

4️⃣ Clean Game State Management

Normal food and special food never appear at the same time

Collision logic adapts based on food state

Prevents double scoring or visual glitches

🧠 Design Decisions

Distance-based collision detection for food and tail

Coordinate-based collision detection for walls

Object-Oriented Design:

Snake → movement & body logic

Food → normal + special food management

Scoreboard → score display & game over message

🎮 Controls

⬆️ Up Arrow → Move Up

⬇️ Down Arrow → Move Down

⬅️ Left Arrow → Move Left

➡️ Right Arrow → Move Right

🛠 Technologies Used

Python 3

Turtle Graphics

Object-Oriented Programming (OOP)

📌 Notes

This version was built to:

Practice game state control

Improve OOP design skills

Go beyond tutorial-based implementation

⭐ Future Improvements (Ideas)

High score persistence (file I/O)

Pause / Resume feature

Levels with increasing difficulty

Sound effects for food & collisions

💡 This project represents a transition from beginner concepts to structured game logic and state management.
