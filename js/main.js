/* ============================================
   Penta Services - Main JavaScript
   Digital Agency Website
   ============================================ */

// ── Preloader ────────────────────────────────
window.addEventListener('load', () => {
  const preloader = document.querySelector('.preloader');
  if (preloader) {
    preloader.style.transition = 'opacity 0.5s ease, visibility 0.5s ease';
    preloader.style.opacity = '0';
    preloader.style.visibility = 'hidden';
    setTimeout(() => {
      preloader.style.display = 'none';
    }, 500);
  }
});

document.addEventListener('DOMContentLoaded', () => {

  /* ──────────────────────────────────────────
     1. Navbar Scroll Effect
     ────────────────────────────────────────── */
  const navbar = document.querySelector('.navbar');

  const handleNavbarScroll = () => {
    if (!navbar) return;
    if (window.scrollY > 50) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  };

  window.addEventListener('scroll', handleNavbarScroll, { passive: true });
  handleNavbarScroll(); // run on load in case page is already scrolled


  /* ──────────────────────────────────────────
     2. Mobile Menu Toggle
     ────────────────────────────────────────── */
  const navToggle = document.querySelector('.nav-toggle');
  const navMenu = document.querySelector('.nav-menu');

  if (navToggle && navMenu) {
    navToggle.addEventListener('click', () => {
      navToggle.classList.toggle('active');
      navMenu.classList.toggle('active');
      document.body.classList.toggle('menu-open');
    });

    // Close menu when a nav link is clicked
    const navLinks = navMenu.querySelectorAll('a');
    navLinks.forEach(link => {
      link.addEventListener('click', () => {
        navToggle.classList.remove('active');
        navMenu.classList.remove('active');
        document.body.classList.remove('menu-open');
      });
    });
  }


  /* ──────────────────────────────────────────
     3. Smooth Scrolling
     ────────────────────────────────────────── */
  const NAVBAR_OFFSET = 80;

  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', (e) => {
      const href = anchor.getAttribute('href');
      if (href === '#' || href === '#!') return;

      const target = document.querySelector(href);
      if (!target) return;

      e.preventDefault();

      const targetPosition = target.getBoundingClientRect().top + window.scrollY - NAVBAR_OFFSET;

      window.scrollTo({
        top: targetPosition,
        behavior: 'smooth'
      });
    });
  });


  /* ──────────────────────────────────────────
     4. Stats Counter Animation
     ────────────────────────────────────────── */
  let statsAnimated = false;

  const easeOutQuad = (t) => t * (2 - t);

  const animateCounter = (element, target, duration = 2000) => {
    const start = performance.now();
    const isDecimal = String(target).includes('.');
    const suffix = element.dataset.suffix || '';

    const update = (currentTime) => {
      const elapsed = currentTime - start;
      const progress = Math.min(elapsed / duration, 1);
      const easedProgress = easeOutQuad(progress);
      const currentValue = easedProgress * target;

      if (isDecimal) {
        element.textContent = currentValue.toFixed(1) + suffix;
      } else {
        element.textContent = Math.floor(currentValue) + suffix;
      }

      if (progress < 1) {
        requestAnimationFrame(update);
      } else {
        element.textContent = (isDecimal ? target.toFixed(1) : target) + suffix;
      }
    };

    requestAnimationFrame(update);
  };

  const statsSection = document.querySelector('.stats');

  if (statsSection) {
    const statsObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting && !statsAnimated) {
          statsAnimated = true;
          const statNumbers = statsSection.querySelectorAll('.stat-number');
          statNumbers.forEach(stat => {
            const target = parseFloat(stat.dataset.target) || 0;
            animateCounter(stat, target);
          });
          statsObserver.unobserve(statsSection);
        }
      });
    }, { threshold: 0.3 });

    statsObserver.observe(statsSection);
  }


  /* ──────────────────────────────────────────
     5. Scroll Reveal Animations
     ────────────────────────────────────────── */
  const fadeElements = document.querySelectorAll('.fade-in-up');

  if (fadeElements.length > 0) {
    const revealObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const el = entry.target;

          // Check if parent has stagger-children class
          if (el.parentElement && el.parentElement.classList.contains('stagger-children')) {
            const siblings = Array.from(el.parentElement.querySelectorAll('.fade-in-up'));
            const index = siblings.indexOf(el);
            el.style.transitionDelay = `${index * 0.1}s`;
          }

          el.classList.add('visible');
          revealObserver.unobserve(el);
        }
      });
    }, { threshold: 0.15 });

    fadeElements.forEach(el => revealObserver.observe(el));
  }


  /* ──────────────────────────────────────────
     6. Active Nav Link Highlighting
     ────────────────────────────────────────── */
  const sections = document.querySelectorAll('section[id]');
  const allNavLinks = document.querySelectorAll('.nav-menu a[href^="#"]');

  const highlightNav = () => {
    const scrollPosition = window.scrollY + NAVBAR_OFFSET + 100;

    let currentSection = '';

    sections.forEach(section => {
      const sectionTop = section.offsetTop;
      const sectionHeight = section.offsetHeight;

      if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
        currentSection = section.getAttribute('id');
      }
    });

    allNavLinks.forEach(link => {
      link.classList.remove('active');
      const href = link.getAttribute('href');
      if (href === `#${currentSection}`) {
        link.classList.add('active');
      }
    });
  };

  window.addEventListener('scroll', highlightNav, { passive: true });
  highlightNav(); // run on load


  /* ──────────────────────────────────────────
     7. Contact Form Handling
     ────────────────────────────────────────── */
  const contactForm = document.getElementById('contact-form');

  if (contactForm) {
    const formSuccess = contactForm.parentElement.querySelector('.form-success') ||
                        document.querySelector('.form-success');

    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();

      // Basic validation
      const requiredFields = contactForm.querySelectorAll('[required]');
      let isValid = true;

      requiredFields.forEach(field => {
        // Remove previous error states
        field.classList.remove('error');

        const value = field.value.trim();
        if (!value) {
          isValid = false;
          field.classList.add('error');
        }

        // Basic email validation
        if (field.type === 'email' && value) {
          const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
          if (!emailRegex.test(value)) {
            isValid = false;
            field.classList.add('error');
          }
        }
      });

      if (!isValid) {
        // Shake animation on invalid form
        contactForm.classList.add('shake');
        setTimeout(() => contactForm.classList.remove('shake'), 600);
        return;
      }

      // Valid submission — hide form, show success
      contactForm.style.transition = 'opacity 0.4s ease';
      contactForm.style.opacity = '0';

      setTimeout(() => {
        contactForm.style.display = 'none';

        if (formSuccess) {
          formSuccess.innerHTML = `
            <div class="success-content">
              <div class="success-icon">✓</div>
              <h3>Thank You!</h3>
              <p>Your message has been sent successfully. We'll get back to you within 24 hours.</p>
            </div>
          `;
          formSuccess.style.display = 'block';
          formSuccess.style.opacity = '0';
          requestAnimationFrame(() => {
            formSuccess.style.transition = 'opacity 0.4s ease';
            formSuccess.style.opacity = '1';
          });
        }
      }, 400);
    });

    // Clear error state on input
    contactForm.querySelectorAll('input, textarea, select').forEach(field => {
      field.addEventListener('input', () => {
        field.classList.remove('error');
      });
    });
  }


  /* ──────────────────────────────────────────
     8. Language Selector
     ────────────────────────────────────────── */
  const langSelector = document.querySelector('.lang-selector');

  if (langSelector) {
    const langToggle = langSelector.querySelector('.lang-toggle') || langSelector;
    const langDropdown = langSelector.querySelector('.lang-dropdown');

    if (langDropdown) {
      langToggle.addEventListener('click', (e) => {
        e.stopPropagation();
        langSelector.classList.toggle('open');
        langDropdown.classList.toggle('active');
      });

      // Close dropdown when clicking outside
      document.addEventListener('click', (e) => {
        if (!langSelector.contains(e.target)) {
          langSelector.classList.remove('open');
          langDropdown.classList.remove('active');
        }
      });

      // Select a language
      langDropdown.querySelectorAll('a, button, li').forEach(item => {
        item.addEventListener('click', () => {
          const lang = item.dataset.lang || item.textContent.trim();
          const currentLabel = langToggle.querySelector('span') || langToggle;
          if (currentLabel.tagName === 'SPAN') {
            currentLabel.textContent = lang;
          }
          langSelector.classList.remove('open');
          langDropdown.classList.remove('active');
        });
      });
    }
  }


  /* ──────────────────────────────────────────
     9. Portfolio Filter
     ────────────────────────────────────────── */
  const filterBtns = document.querySelectorAll('.filter-btn');
  const portfolioItems = document.querySelectorAll('.portfolio-card, .portfolio-item');

  if (filterBtns.length > 0 && portfolioItems.length > 0) {
    filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        // Update active button
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        const filterValue = btn.dataset.filter || 'all';

        portfolioItems.forEach(item => {
          const category = item.dataset.category || '';

          if (filterValue === 'all' || category === filterValue) {
            item.style.opacity = '0';
            item.style.transform = 'scale(0.8)';

            requestAnimationFrame(() => {
              item.style.display = '';
              requestAnimationFrame(() => {
                item.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
                item.style.opacity = '1';
                item.style.transform = 'scale(1)';
              });
            });
          } else {
            item.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
            item.style.opacity = '0';
            item.style.transform = 'scale(0.8)';
            setTimeout(() => {
              item.style.display = 'none';
            }, 300);
          }
        });
      });
    });
  }


  /* ──────────────────────────────────────────
     10. Typing Effect (Hero Subtitle)
     ────────────────────────────────────────── */
  const typingElement = document.querySelector('.typing-text');

  if (typingElement) {
    const phrases = [
      'Web Design & Development',
      'Mobile App Development',
      'Search Engine Optimization',
      'Generative Engine Optimization',
      'UX/UI Design & Branding'
    ];

    let phraseIndex = 0;
    let charIndex = 0;
    let isDeleting = false;
    let typingSpeed = 80;

    const type = () => {
      const currentPhrase = phrases[phraseIndex];

      if (isDeleting) {
        typingElement.textContent = currentPhrase.substring(0, charIndex - 1);
        charIndex--;
        typingSpeed = 40;
      } else {
        typingElement.textContent = currentPhrase.substring(0, charIndex + 1);
        charIndex++;
        typingSpeed = 80;
      }

      // Finished typing the phrase
      if (!isDeleting && charIndex === currentPhrase.length) {
        typingSpeed = 2000; // pause before deleting
        isDeleting = true;
      }

      // Finished deleting the phrase
      if (isDeleting && charIndex === 0) {
        isDeleting = false;
        phraseIndex = (phraseIndex + 1) % phrases.length;
        typingSpeed = 400; // pause before typing next
      }

      setTimeout(type, typingSpeed);
    };

    // Start typing after a short delay
    setTimeout(type, 1000);
  }


  /* ──────────────────────────────────────────
     11. Back to Top Button
     ────────────────────────────────────────── */
  const backToTopBtn = document.querySelector('.back-to-top');

  if (backToTopBtn) {
    const toggleBackToTop = () => {
      if (window.scrollY > 500) {
        backToTopBtn.classList.add('visible');
      } else {
        backToTopBtn.classList.remove('visible');
      }
    };

    window.addEventListener('scroll', toggleBackToTop, { passive: true });
    toggleBackToTop(); // run on load

    backToTopBtn.addEventListener('click', (e) => {
      e.preventDefault();
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }

}); // end DOMContentLoaded
