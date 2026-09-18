(() => {
  const form = document.querySelector('[data-shop-filters]');
  const products = Array.from(document.querySelectorAll('[data-shop-product]'));
  const counter = document.querySelector('[data-result-count]');
  const empty = document.querySelector('[data-shop-empty]');
  if (!form || !products.length) return;

  const normalize = value => value
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .toLowerCase()
    .trim();

  const applyFilters = () => {
    const data = new FormData(form);
    const query = normalize(data.get('query') || '');
    const brand = data.get('brand') || '';
    const display = data.get('display') || '';
    const size = data.get('size') || '';
    let visible = 0;

    products.forEach(product => {
      const matches = (!query || normalize(product.dataset.search || '').includes(query))
        && (!brand || product.dataset.brand === brand)
        && (!display || product.dataset.display === display)
        && (!size || product.dataset.size === size);
      product.hidden = !matches;
      if (matches) visible += 1;
    });

    if (counter) counter.textContent = String(visible);
    if (empty) empty.hidden = visible !== 0;
  };

  form.addEventListener('input', applyFilters);
  form.addEventListener('change', applyFilters);
  form.addEventListener('reset', () => requestAnimationFrame(applyFilters));
})();
