// Small helpers shared by every page. Written by AI, explained in plain English.

// 1. Work out which GitHub repository this website belongs to.
//    On GitHub Pages the address looks like https://USERNAME.github.io/REPO-NAME/
//    so every friend's copy automatically links to their own files.
function repoInfo() {
  const host = location.hostname;
  if (host.endsWith(".github.io")) {
    const owner = host.split(".")[0];
    const repo = location.pathname.split("/").filter(Boolean)[0] || `${owner}.github.io`;
    return { owner, repo };
  }
  return { owner: "jawdat-rana", repo: "learn-ai-with-usecases" }; // the original course
}

// 2. Any link written as <a data-gh="path/to/file.md"> opens that file on GitHub.
//    data-gh-edit opens the file in GitHub's browser editor instead.
function wireGitHubLinks() {
  const { owner, repo } = repoInfo();
  document.querySelectorAll("[data-gh]").forEach(a => {
    a.href = `https://github.com/${owner}/${repo}/blob/main/${a.dataset.gh}`;
  });
  document.querySelectorAll("[data-gh-edit]").forEach(a => {
    a.href = `https://github.com/${owner}/${repo}/edit/main/${a.dataset.ghEdit}`;
  });
  document.querySelectorAll("[data-colab]").forEach(a => {
    a.href = `https://colab.research.google.com/github/${owner}/${repo}/blob/main/${a.dataset.colab}`;
  });
  document.querySelectorAll("[data-gh-repo]").forEach(a => {
    a.href = `https://github.com/${owner}/${repo}`;
  });
}

// 3. Read a CSV file (the kind Excel saves) into a list of rows.
//    Handles quoted values such as "Smith, John".
function parseCSV(text) {
  const rows = [];
  let row = [], field = "", inQuotes = false;
  text = text.replace(/^﻿/, "");
  for (let i = 0; i < text.length; i++) {
    const c = text[i];
    if (inQuotes) {
      if (c === '"' && text[i + 1] === '"') { field += '"'; i++; }
      else if (c === '"') inQuotes = false;
      else field += c;
    } else if (c === '"') inQuotes = true;
    else if (c === ",") { row.push(field); field = ""; }
    else if (c === "\n" || c === "\r") {
      if (c === "\r" && text[i + 1] === "\n") i++;
      row.push(field); field = "";
      if (row.some(v => v !== "")) rows.push(row);
      row = [];
    } else field += c;
  }
  row.push(field);
  if (row.some(v => v !== "")) rows.push(row);
  const header = rows.shift().map(h => h.trim());
  return rows.map(r => Object.fromEntries(header.map((h, i) => [h, (r[i] ?? "").trim()])));
}

async function fetchCSV(path) {
  const res = await fetch(path);
  if (!res.ok) throw new Error(`Could not load ${path} (${res.status})`);
  return parseCSV(await res.text());
}

const fmtUSD = n => "$" + Math.round(n).toLocaleString("en-US");
const fmtM = n => "$" + (n / 1e6).toFixed(1) + "M";
const esc = s => String(s).replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

document.addEventListener("DOMContentLoaded", wireGitHubLinks);
