# Start here: set up in about 15 minutes

No installing, no command line. Everything happens in your web browser.

By the end you'll have:

- your own copy of this course on GitHub
- your own website at `https://YOUR-USERNAME.github.io/learn-ai-with-usecases/`
  with the interactive dashboards
- a journal page you can edit in the browser

---

## 1. Create a free GitHub account (3 min)

GitHub is a website where people store and share files, mostly code. It's
free, and you'll only use the website.

1. Go to **github.com/signup**.
2. Enter your email, a password and a **username**. Choose a professional
   one: it becomes part of your website address
   (`username.github.io`).
3. Verify your email. Choose the **Free** plan if asked.

## 2. Copy the course into your account (2 min)

1. Open the course: **github.com/jawdat-rana/learn-ai-with-usecases**
2. Click the green **Use this template** button (top right), then **Create a
   new repository**.
3. Repository name: `learn-ai-with-usecases` (keep the same name so the links
   in the course work).
4. Choose **Public**. (Free GitHub Pages websites need a public repository.
   Only synthetic data lives here, so that's fine. **Never put company data
   in it.**)
5. Click **Create repository**. You now have your own copy, and nothing you
   do affects anyone else's.

> **Don't see "Use this template"?** Click **Fork** instead (top right) and
> then **Create fork**. It works the same for this course.

## 3. Switch on your website (3 min)

1. In **your** copy, click **Settings** (the tab with a gear, top of the page).
2. In the left menu click **Pages**.
3. Under **Build and deployment → Source**, choose **Deploy from a branch**.
4. Under **Branch**, choose **main** and **/ (root)**, then click **Save**.
5. Wait 1 to 2 minutes and refresh. A box appears at the top: "Your site is
   live at https://YOUR-USERNAME.github.io/learn-ai-with-usecases/". Open it
   and bookmark it.

## 4. Edit your first page in the browser (3 min)

1. In your repository, click **my-ai-journal.md**.
2. Click the **pencil icon** (Edit this file), top right of the file.
3. Under "About me", write your role and one thing you'd like AI to help with.
4. Click **Commit changes…**, then **Commit changes** again. Done: you've
   just made your first commit, which is GitHub's word for "saved a version".

Every file in this course can be edited the same way. GitHub keeps every
version, so you can't break anything permanently.

## 5. Get your free AI tools ready (4 min)

You need **at least one** of these (all have free plans):

- **Claude** at claude.ai
- **ChatGPT** at chatgpt.com
- **Gemini** at gemini.google.com

And a **Google account** for **Google Colab** (colab.research.google.com),
which runs Python code in your browser for free. You won't write code; you'll
run code the AI wrote.

Free plans have daily limits. If you hit one, switch tools or come back
later. Trying the same prompt in two tools is a good habit anyway.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| The website shows "404" | Wait 2 more minutes. Check Settings → Pages shows the **main** branch and **/ (root)**. Make sure the repository is **Public**. |
| Dashboards say "Could not load the data" | You opened the file on github.com instead of your website. Use the `github.io` address. |
| A link in the course opens Jawdat's copy, not mine | Links in the Markdown files point to the original course. On your website, links point to your own copy automatically. To fix a Markdown link, edit the file and replace `jawdat-rana` with your username. |
| Colab says "Warning: this notebook was not authored by Google" | That's normal for notebooks from GitHub. Click **Run anyway**: the code only reads this course's sample data. |
| I committed something by mistake | Open the file, click **History**, open the earlier version, copy it back. Or just ask in the group. |

**Next:** open your website, then start with
[Foundations 1: How AI chat tools work](00-foundations/01-how-ai-works.md).
