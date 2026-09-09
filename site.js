const canonical = document.querySelector('link[rel="canonical"]')?.href || '';
const isComparisonPage = canonical.includes('/comparatifs/');
const isComparisonHub = /\/comparatifs\/$/.test(canonical);

if (isComparisonPage) {
  document.documentElement.classList.add('comparison-page');
  if (isComparisonHub) document.documentElement.classList.add('comparison-hub-page');

  if (!document.querySelector('link[data-comparison-styles]')) {
    const stylesheet = document.createElement('link');
    stylesheet.rel = 'stylesheet';
    stylesheet.href = '/comparisons.css';
    stylesheet.dataset.comparisonStyles = 'true';
    document.head.appendChild(stylesheet);
  }
}

const burger = document.querySelector('.burger');
const navigation = document.querySelector('#site-navigation');

if (burger && navigation) {
  const closeMenu = () => {
    document.body.classList.remove('nav-open');
    burger.setAttribute('aria-expanded', 'false');
    burger.setAttribute('aria-label', 'Ouvrir le menu');
  };

  burger.addEventListener('click', () => {
    const isOpen = burger.getAttribute('aria-expanded') === 'true';
    if (isOpen) {
      closeMenu();
    } else {
      document.body.classList.add('nav-open');
      burger.setAttribute('aria-expanded', 'true');
      burger.setAttribute('aria-label', 'Fermer le menu');
    }
  });

  navigation.addEventListener('click', (event) => {
    if (event.target.closest('a') && window.matchMedia('(max-width: 768px)').matches) {
      closeMenu();
    }
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') closeMenu();
  });

  window.addEventListener('resize', () => {
    if (!window.matchMedia('(max-width: 768px)').matches) closeMenu();
  });
}

const tableOfContents = document.querySelector('.sidebar-toc');
const article = document.querySelector('.content-main');

if (tableOfContents && article) {
  const headings = article.querySelectorAll('h2, h3');
  const usedIds = new Set(Array.from(document.querySelectorAll('[id]'), (element) => element.id));
  const tocLinks = [];

  headings.forEach((heading, index) => {
    if (!heading.id) {
      const baseId = heading.textContent
        .trim()
        .toLowerCase()
        .normalize('NFD')
        .replace(/[\u0300-\u036f]/g, '')
        .replace(/[^a-z0-9]+/g, '-')
        .replace(/^-|-$/g, '') || `section-${index + 1}`;
      let uniqueId = baseId;
      let suffix = 2;

      while (usedIds.has(uniqueId)) {
        uniqueId = `${baseId}-${suffix}`;
        suffix += 1;
      }

      heading.id = uniqueId;
      usedIds.add(uniqueId);
    }

    const link = document.createElement('a');
    link.href = `#${heading.id}`;
    link.textContent = heading.textContent.trim();
    link.className = `toc-level-${heading.tagName === 'H3' ? '3' : '2'}`;
    tableOfContents.appendChild(link);
    tocLinks.push({ heading, link });
  });

  if (isComparisonPage && tocLinks.length && 'IntersectionObserver' in window) {
    const setActive = (activeLink) => {
      tocLinks.forEach(({ link }) => link.classList.toggle('is-active', link === activeLink));
    };

    const observer = new IntersectionObserver((entries) => {
      const visible = entries
        .filter((entry) => entry.isIntersecting)
        .sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
      if (!visible.length) return;
      const match = tocLinks.find(({ heading }) => heading === visible[0].target);
      if (match) setActive(match.link);
    }, {
      rootMargin: '-12% 0px -72% 0px',
      threshold: 0
    });

    tocLinks.forEach(({ heading }) => observer.observe(heading));
    setActive(tocLinks[0].link);
  }
}
