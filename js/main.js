// Python Learning Hub — Main JavaScript
// Handles: sidebar toggle, section collapse, search, active nav, progress

(function () {
    'use strict';

    // ── Sidebar Toggle (mobile) ──────────────────────────────────
    const sidebar = document.getElementById('sidebar');
    const mobileToggle = document.getElementById('mobileToggle');
    const sidebarToggle = document.getElementById('sidebarToggle');

    if (mobileToggle) {
        mobileToggle.addEventListener('click', () => {
            sidebar.classList.toggle('open');
        });
    }

    // Close sidebar when clicking outside on mobile
    document.addEventListener('click', (e) => {
        if (window.innerWidth <= 900 && sidebar && sidebar.classList.contains('open')) {
            if (!sidebar.contains(e.target) && e.target !== mobileToggle) {
                sidebar.classList.remove('open');
            }
        }
    });

    // ── Section Collapse ────────────────────────────────────────
    window.toggleSection = function (header) {
        const items = header.nextElementSibling;
        header.classList.toggle('collapsed');
        if (items.classList.contains('hidden')) {
            items.classList.remove('hidden');
            items.style.maxHeight = items.scrollHeight + 'px';
        } else {
            items.classList.add('hidden');
            items.style.maxHeight = '0';
        }
    };

    // Initialize section items height
    document.querySelectorAll('.nav-section-items').forEach(items => {
        items.style.maxHeight = items.scrollHeight + 'px';
    });

    // ── Active Nav Item ─────────────────────────────────────────
    function setActiveNav() {
        const currentPath = window.location.pathname.replace(/\\/g, '/');
        document.querySelectorAll('.nav-item').forEach(item => {
            const href = item.getAttribute('href');
            if (href && currentPath.endsWith(href.replace('./', '').replace('../', ''))) {
                item.classList.add('active');
                // Expand parent section
                const section = item.closest('.nav-section');
                if (section) {
                    const header = section.querySelector('.nav-section-header');
                    const items = section.querySelector('.nav-section-items');
                    if (header && header.classList.contains('collapsed')) {
                        header.classList.remove('collapsed');
                        items.classList.remove('hidden');
                        items.style.maxHeight = items.scrollHeight + 'px';
                    }
                }
            }
        });
    }
    setActiveNav();

    // ── Search ──────────────────────────────────────────────────
    const searchInput = document.getElementById('searchInput');
    if (searchInput) {
        searchInput.addEventListener('input', function () {
            const query = this.value.toLowerCase().trim();
            document.querySelectorAll('.nav-item').forEach(item => {
                const text = item.textContent.toLowerCase();
                const section = item.closest('.nav-section');
                if (query === '') {
                    item.style.display = '';
                } else {
                    item.style.display = text.includes(query) ? '' : 'none';
                    // Show section if any item matches
                    if (section) {
                        const items = section.querySelector('.nav-section-items');
                        const visible = [...items.querySelectorAll('.nav-item')].some(i => i.style.display !== 'none');
                        section.style.display = visible ? '' : 'none';
                        if (visible) {
                            items.style.maxHeight = '10000px';
                            items.classList.remove('hidden');
                        }
                    }
                }
            });
            if (query === '') {
                document.querySelectorAll('.nav-section').forEach(s => s.style.display = '');
            }
        });
    }

    // ── Reading Progress ────────────────────────────────────────
    const progressFill = document.getElementById('progressFill');
    const progressPercent = document.getElementById('progressPercent');
    if (progressFill) {
        document.addEventListener('scroll', () => {
            const docHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            const scrolled = Math.round((window.scrollY / docHeight) * 100);
            const clamped = Math.min(100, Math.max(0, scrolled));
            progressFill.style.width = clamped + '%';
            if (progressPercent) progressPercent.textContent = clamped + '%';
        });
    }

    // ── Copy Code Buttons ────────────────────────────────────────
    document.querySelectorAll('.copy-btn').forEach(btn => {
        btn.addEventListener('click', function () {
            const wrapper = this.closest('.code-block-wrapper');
            const code = wrapper ? wrapper.querySelector('pre.code-block') : null;
            if (code) {
                navigator.clipboard.writeText(code.innerText).then(() => {
                    const orig = this.textContent;
                    this.textContent = '✓ Copied!';
                    setTimeout(() => { this.textContent = orig; }, 2000);
                });
            }
        });
    });

    // ── Smooth Anchor Links ──────────────────────────────────────
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

})();
