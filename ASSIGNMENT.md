# Onsite Assessment Exercise

**Time limit:** 2 hours for implementation + 15 minutes for walkthrough

## Context

You're building a **Study Guide** feature for an interview preparation platform. The blog is already complete (use it as a reference!), and you need to implement the study guide functionality.

## Your Task

Complete the `study_guide` app to allow users to:
1. Browse study topics (e.g., "System Design", "Python Basics")
2. View questions and answers for each topic
3. Filter questions by difficulty

## Part 1: Backend (Models) - ~45 minutes

### Task 1.1: Create the Question Snippet

In `study_guide/models.py`, create a `Question` snippet with:
- `question_text` (TextField)
- `answer_text` (RichTextField)
- `difficulty` (CharField with choices: beginner, intermediate, advanced)
- `tags` (CharField, optional - e.g., "arrays, sorting")

**Hints:**
- Use `@register_snippet` decorator
- Add `panels` for the Wagtail admin
- Implement `__str__` method

### Task 1.2: Complete the TopicPage Model

The `TopicPage` model is partially complete. Add:
- A `ParentalManyToManyField` to link `Question` snippets to this topic
- Proper `content_panels` configuration

**Hints:**
- Look at how the blog app links `Author` to `BlogPage`
- Use `FieldPanel` for the relationship field

### Task 1.3: Complete StudyGuideIndexPage.get_context()

Implement the `get_context` method to:
- Get all published `TopicPage` children
- Order them by title or publish date
- Add them to the context as `topics`

**Hints:**
- Use `TopicPage.objects.live().public().descendant_of(self)`
- Look at `BlogIndexPage.get_context()` for reference

## Part 2: Frontend (Templates) - ~45 minutes

### Task 2.1: Study Guide Index Template

Complete `study_guide/templates/study_guide/study_guide_index_page.html`:

Display a list of topics with:
- Topic title (linked to detail page)
- Description (truncated)
- Difficulty badge (color-coded: green=beginner, yellow=intermediate, red=advanced)
- Question count (e.g., "12 questions")

**Design requirements:**
- Use Tailwind CSS (already loaded in base.html)
- Card-based layout
- Responsive grid (1 column on mobile, 2-3 on desktop)

### Task 2.2: Topic Detail Template

Complete `study_guide/templates/study_guide/topic_page.html`:

Display:
- Topic title and description
- List of questions with:
  - Question text
  - Difficulty badge
  - Tags (if present)
  - Answer (hidden by default, expandable with `<details>`/`<summary>`)

**Design requirements:**
- Clean, readable layout
- Color-coded difficulty badges
- Expandable answers using HTML `<details>` element

## Part 3: Reasoning & Documentation - ~30 minutes

Create a `NOTES.md` file in the project root and answer:

1. **Wagtail Page vs Snippet:** Why is `Question` a snippet instead of a page type?

2. **Relationship Design:** Why use `ParentalManyToManyField` instead of `ForeignKey` for linking questions to topics?

3. **Query Optimization:** If a topic had 1000+ questions, how would you optimize the detail page?

4. **Content Strategy:** How would you handle questions that belong to multiple topics?

5. **UX Decision:** Why use `<details>` for answers instead of showing them immediately?

6. **Challenges:** What was the hardest part of this exercise? How did you solve it?

## Bonus Tasks (If You Finish Early)

- Add a search/filter feature to filter questions by difficulty on the topic page
- Add a "Related Topics" section to the topic detail page
- Implement a "Featured Topics" section on the study guide index
- Add question count to the topic cards on the index page

## Deliverables

1. ✅ Working code (models, templates)
2. ✅ Migrations created and applied
3. ✅ At least 2-3 sample questions created in the admin
4. ✅ `NOTES.md` with your answers
5. ✅ Be ready to walk through your code and explain your decisions

## Evaluation Criteria

We're assessing:
- **Learning ability:** Can you pick up Wagtail/Django concepts quickly?
- **Problem-solving:** How do you approach unfamiliar challenges?
- **Code quality:** Is your code clean, readable, and well-structured?
- **Communication:** Can you explain your decisions clearly?
- **Completeness:** Did you deliver working functionality?

## Tips

- **Use the blog app as a reference** - it's fully implemented!
- **Explore the Wagtail admin** - it helps you understand the data model
- **Start with models, then templates** - get the data structure right first
- **Test as you go** - don't wait until the end to check if it works
- **Ask questions** - we're here to help if you get stuck
- **Document your thinking** - write notes as you work

## Resources

- Wagtail Documentation: https://docs.wagtail.org/
- Django Documentation: https://docs.djangoproject.com/
- Tailwind CSS: https://tailwindcss.com/docs
- The `blog` app in this project (fully implemented reference)

Good luck! 🚀