// Mobile hamburger navigation toggle
document.addEventListener("DOMContentLoaded", () => {
  const hamburger = document.getElementById("hamburger");
  const navLinks = document.getElementById("navLinks");

  if (hamburger && navLinks) {
    hamburger.addEventListener("click", () => {
      hamburger.classList.toggle("open");
      navLinks.classList.toggle("open");
    });

    // Close the menu when a link is clicked (better mobile UX)
    navLinks.querySelectorAll("a").forEach((link) => {
      link.addEventListener("click", () => {
        hamburger.classList.remove("open");
        navLinks.classList.remove("open");
      });
    });
  }

  // Auto-dismiss flash messages after a few seconds
  const flashMessages = document.querySelectorAll(".flash");
  flashMessages.forEach((el) => {
    setTimeout(() => {
      el.style.transition = "opacity 0.4s ease";
      el.style.opacity = "0";
      setTimeout(() => el.remove(), 400);
    }, 5000);
  });

  // Read more / Read less toggle for truncated project descriptions
  // (badge-list and project-card-links live outside this <p>, as siblings in
  // the markup, so they are never affected by the expand/collapse toggle.)
  document.querySelectorAll(".read-more-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      const description = btn.closest(".project-description");
      if (!description) return;
      const expanded = description.classList.toggle("expanded");
      btn.textContent = expanded ? "Read less" : "Read more";
    });
  });

  // Achievement lightbox (View Achievement buttons on the Achievements page)
  const lightbox = document.getElementById("achievementLightbox");
  if (lightbox) {
    const lightboxImage = document.getElementById("lightboxImage");
    const lightboxTitle = document.getElementById("lightboxTitle");
    const lightboxDate = document.getElementById("lightboxDate");
    const lightboxCategory = document.getElementById("lightboxCategory");
    const lightboxDescription = document.getElementById("lightboxDescription");
    const closeBtn = document.getElementById("lightboxClose");
    const backdrop = document.getElementById("lightboxBackdrop");

    const openAchievementLightbox = (btn) => {
      lightboxImage.src = btn.dataset.image;
      lightboxImage.onerror = () => { lightboxImage.src = btn.dataset.fallback; };
      lightboxImage.alt = btn.dataset.title;
      lightboxTitle.textContent = btn.dataset.title;
      lightboxDate.textContent = btn.dataset.date;
      lightboxCategory.textContent = btn.dataset.category;
      lightboxDescription.textContent = btn.dataset.description;
      lightbox.classList.add("open");
    };

    document.querySelectorAll(".view-achievement-btn").forEach((btn) => {
      btn.addEventListener("click", () => openAchievementLightbox(btn));
    });

    // Clicking the certificate/achievement image does the same thing as
    // clicking its card's "View Achievement" button.
    document.querySelectorAll(".achievement-card").forEach((card) => {
      const img = card.querySelector(".achievement-image");
      const btn = card.querySelector(".view-achievement-btn");
      if (img && btn) {
        img.addEventListener("click", () => openAchievementLightbox(btn));
      }
    });

    const closeLightbox = () => lightbox.classList.remove("open");
    closeBtn.addEventListener("click", closeLightbox);
    backdrop.addEventListener("click", closeLightbox);
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape") closeLightbox();
    });
  }
});
