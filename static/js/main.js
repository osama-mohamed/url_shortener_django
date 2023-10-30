document.addEventListener("DOMContentLoaded", function() {
  document.getElementById("copyButton").addEventListener("click", async function() {
    const copyText = document.getElementById("copyLink").textContent;
    try {
      await navigator.clipboard.writeText(copyText);
      alert("Link copied to clipboard!");
    } catch (err) {
      console.error("Failed to copy text: ", err);
    }
  });
});