const canonical = document.querySelector('link[rel="canonical"]')?.href || '';
const isComparisonPage = canonical.includes('/comparatifs/');
const isComparisonHub = /\/comparatifs\/$/.test(canonical);
const isUsagePage = canonical.includes('/usages/');
const isUsageHub = /\/usages\/$/.test(canonical);
const isGuidePage = canonical.includes('/guides/');
const isGuideHub = /\/guides\/$/.test(canonical);
const isDealPage = canonical.includes('/bons-plans/');
const isDealHub = /\/bons-plans\/$/.test(canonical);

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

if (isUsagePage) {
  document.documentElement.classList.add('usage-page');
  if (isUsageHub) document.documentElement.classList.add('usage-hub-page');

  if (!document.querySelector('link[data-usage-styles]')) {
    const stylesheet = document.createElement('link');
    stylesheet.rel = 'stylesheet';
    stylesheet.href = '/usages.css';
    stylesheet.dataset.usageStyles = 'true';
    document.head.appendChild(stylesheet);
  }
}

if (isGuidePage || isDealPage) {
  document.documentElement.classList.add(isGuidePage ? 'guide-page' : 'deal-page');
  if (isGuideHub) document.documentElement.classList.add('guide-hub-page');
  if (isDealHub) document.documentElement.classList.add('deal-hub-page');

  if (!document.querySelector('link[data-guide-deal-styles]')) {
    const stylesheet = document.createElement('link');
    stylesheet.rel = 'stylesheet';
    stylesheet.href = '/guides-deals.css';
    stylesheet.dataset.guideDealStyles = 'true';
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

  navigation.addEventListener('click', event => {
    if (event.target.closest('a') && window.matchMedia('(max-width: 768px)').matches) {
      closeMenu();
    }
  });

  document.addEventListener('keydown', event => {
    if (event.key === 'Escape') closeMenu();
  });

  window.addEventListener('resize', () => {
    if (!window.matchMedia('(max-width: 768px)').matches) closeMenu();
  });
}

if (isGuideHub) {
  const hubGrid = document.querySelector('.hub-grid');
  if (hubGrid) {
    const linksByHref = new Map(
      Array.from(hubGrid.querySelectorAll('.hub-link'), link => [new URL(link.href, window.location.origin).pathname, link])
    );

    const groups = [
      {
        title: 'Bien choisir',
        description: 'Les arbitrages à faire avant de comparer les modèles.',
        routes: [
          '/guides/choisir-bloc-notes-numerique/',
          '/guides/liseuse-ou-bloc-notes-numerique/',
          '/guides/tablette-classique-ou-tablette-e-ink/',
          '/guides/taille-ecran-bloc-notes-numerique/',
          '/guides/bloc-notes-numerique-couleur-ou-noir-et-blanc/',
          '/guides/bloc-notes-numerique-avec-ou-sans-abonnement/',
          '/guides/prix-bloc-notes-numerique/',
          '/guides/ecosysteme-ouvert-ou-ferme/'
        ]
      },
      {
        title: 'Comprendre l’E Ink',
        description: 'Écran, latence, autonomie et reconnaissance manuscrite.',
        routes: [
          '/guides/tablette-e-ink/',
          '/guides/encre-electronique-fonctionnement/',
          '/guides/latence-ecriture/',
          '/guides/ocr-manuscrit/',
          '/guides/autonomie-tablette-e-ink/'
        ]
      },
      {
        title: 'Fichiers et cloud',
        description: 'Compatibilité, export et synchronisation avec vos outils.',
        routes: [
          '/guides/formats-fichiers-compatibles/',
          '/guides/exporter-notes/',
          '/guides/synchroniser-notes-cloud/',
          '/guides/bloc-notes-numerique-google-drive/',
          '/guides/bloc-notes-numerique-onedrive/',
          '/guides/bloc-notes-numerique-dropbox/'
        ]
      },
      {
        title: 'Utiliser et organiser ses notes',
        description: 'Annoter, convertir, classer, transférer et imprimer.',
        routes: [
          '/guides/annoter-pdf-tablette-e-ink/',
          '/guides/convertir-notes-manuscrites-en-texte/',
          '/guides/organiser-notes-numeriques/',
          '/guides/transfert-notes-vers-ordinateur/',
          '/guides/imprimer-notes-numeriques/'
        ]
      }
    ];

    hubGrid.classList.add('editorial-hub-groups');
    hubGrid.replaceChildren();

    groups.forEach((group, groupIndex) => {
      const section = document.createElement('section');
      section.className = 'editorial-hub-section';

      const heading = document.createElement('div');
      heading.className = 'editorial-hub-heading';
      const title = document.createElement('h2');
      title.textContent = group.title;
      const description = document.createElement('p');
      description.textContent = group.description;
      heading.append(title, description);

      const links = document.createElement('div');
      links.className = 'editorial-hub-links';

      group.routes.forEach((route, routeIndex) => {
        const link = linksByHref.get(route);
        if (!link) return;

        if (groupIndex === 0 && routeIndex === 0) {
          link.classList.add('hub-link--featured');
          const text = link.querySelector('span:first-child');
          if (text) {
            const kicker = document.createElement('span');
            kicker.className = 'hub-link-kicker';
            kicker.textContent = 'Point de départ';
            text.prepend(kicker);
          }
        }
        links.appendChild(link);
      });

      section.append(heading, links);
      hubGrid.appendChild(section);
    });
  }
}

if (isDealHub) {
  const dealMeta = {
    '/bons-plans/bloc-notes-numerique/': ['Synthèse multi-marques, offres et prix à surveiller.', 'Synthèse', 'verified'],
    '/bons-plans/remarkable/': ['Bundles, prix de référence et reconditionné officiel.', 'Offres vérifiées', 'verified'],
    '/bons-plans/kindle-scribe/': ['Historique de baisse et seuils à surveiller par génération.', 'Surveillance', 'watch'],
    '/bons-plans/kobo-elipsa/': ['Prix catalogue et promotions réellement vérifiées.', 'Surveillance', 'watch'],
    '/bons-plans/boox/': ['Stock, bundle, TVA et checkout contrôlés avant de qualifier une remise.', 'Stock sensible', 'watch'],
    '/bons-plans/bloc-notes-numerique-occasion/': ['Reconditionné officiel, état, garantie et décote.', 'Occasion', 'verified'],
    '/bons-plans/black-friday/': ['Baselines avant le Black Friday du 27 novembre 2026.', 'Événement à venir', 'future']
  };

  document.querySelectorAll('.hub-grid .hub-link').forEach(link => {
    const path = new URL(link.href, window.location.origin).pathname;
    const metadata = dealMeta[path];
    if (!metadata) return;

    const label = link.querySelector('span:first-child');
    if (!label) return;

    const main = document.createElement('span');
    main.className = 'hub-link-main';

    const title = document.createElement('span');
    title.className = 'hub-link-title';
    title.textContent = label.textContent.trim();

    const meta = document.createElement('span');
    meta.className = 'hub-link-meta';
    meta.textContent = metadata[0];

    const state = document.createElement('span');
    state.className = `hub-link-state state-${metadata[2]}`;
    state.textContent = metadata[1];

    main.append(title, meta, state);
    label.replaceWith(main);
  });
}

if (isDealPage && !isDealHub) {
  document.querySelectorAll('.content-main table').forEach(table => {
    if (!table.classList.contains('comp-table')) table.classList.add('comp-table');

    if (!table.parentElement?.classList.contains('table-wrapper')) {
      const wrapper = document.createElement('div');
      wrapper.className = 'table-wrapper';
      table.before(wrapper);
      wrapper.appendChild(table);
    }

    const finalHeader = table.querySelector('thead th:last-child')?.textContent.trim().toLowerCase() || '';
    if (!finalHeader.includes('statut')) return;

    table.querySelectorAll('tbody tr').forEach(row => {
      const statusCell = row.lastElementChild;
      if (!statusCell) return;
      const text = statusCell.textContent.trim().toLowerCase();

      statusCell.classList.add('deal-status-cell');
      if (/(rupture|sold out|épuis)/.test(text)) statusCell.classList.add('status-soldout');
      else if (/(surveill|stock|catalogue)/.test(text)) statusCell.classList.add('status-watch');
      else statusCell.classList.add('status-active');
    });
  });
}

const tableOfContents = document.querySelector('.sidebar-toc');
const article = document.querySelector('.content-main');
const contentSidebar = document.querySelector('.content-sidebar');

if (tableOfContents && article) {
  const headings = article.querySelectorAll('h2, h3');
  const usedIds = new Set(Array.from(document.querySelectorAll('[id]'), element => element.id));
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

  if ((isComparisonPage || isUsagePage || isGuidePage || isDealPage) && tocLinks.length && 'IntersectionObserver' in window) {
    const setActive = activeLink => {
      tocLinks.forEach(({ link }) => link.classList.toggle('is-active', link === activeLink));
    };

    const observer = new IntersectionObserver(entries => {
      const visible = entries
        .filter(entry => entry.isIntersecting)
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

if ((isGuidePage || isDealPage) && !isGuideHub && !isDealHub && tableOfContents && article && contentSidebar) {
  const moveEditorialToc = () => {
    if (window.matchMedia('(max-width: 1024px)').matches) {
      if (tableOfContents.parentElement !== article) {
        const intro = isGuidePage
          ? article.querySelector(':scope > .article-answer')
          : article.querySelector(':scope > p:first-of-type');
        if (intro) intro.insertAdjacentElement('afterend', tableOfContents);
        else article.prepend(tableOfContents);
      }
    } else if (tableOfContents.parentElement !== contentSidebar) {
      contentSidebar.insertBefore(tableOfContents, contentSidebar.firstChild);
    }
  };

  moveEditorialToc();
  window.addEventListener('resize', moveEditorialToc);
}
