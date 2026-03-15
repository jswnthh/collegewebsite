# Department Website – Implementation Plan

A bold, creative department website built with Django. The design theme is **modern brutalism** — raw typography, high contrast, thick borders, strong grids, bold colours, and unexpected layout energy. It will stand apart from every generic college website in Chennai.

> [!IMPORTANT]
> **Design decision — Brutalist modern style:** This means stark black/white contrast, oversized type, coloured accent blocks (electric yellow `#FFE600`, neon cyan `#00F5D4`), heavy grid lines, and deliberate "unfinished" aesthetic details. The goal is to be instantly memorable.

---

## Proposed Changes

### Data Layer

#### [MODIFY] [models.py](file:///home/master/Projects/python/DeptWebsite/core/models.py)
Add two models:
- **`BlogPost`** — `title`, `slug` (auto), `body` (TextField), `author` (CharField), `published_date`, `image` (optional ImageField), `created_at`
- **`GalleryItem`** — `title`, `image` (ImageField), `caption`, `uploaded_at`

> [!NOTE]
> `Pillow` is required for `ImageField`. We'll verify it is installed before adding the model.

---

### URL Routing

#### [MODIFY] [core/urls.py](file:///home/master/Projects/python/DeptWebsite/core/urls.py)
Add routes:
| URL | View | Name |
|-----|------|------|
| `/` | [index](file:///home/master/Projects/python/DeptWebsite/core/views.py#4-7) | [index](file:///home/master/Projects/python/DeptWebsite/core/views.py#4-7) |
| `/blog/` | `blog_list` | `blog_list` |
| `/blog/<slug:slug>/` | `blog_detail` | `blog_detail` |
| `/gallery/` | `gallery` | `gallery` |

---

### Views

#### [MODIFY] [core/views.py](file:///home/master/Projects/python/DeptWebsite/core/views.py)
- [index](file:///home/master/Projects/python/DeptWebsite/core/views.py#4-7) — Render homepage with latest 3 blog posts and 4 gallery items as teasers
- `blog_list` — All published blog posts, ordered by date descending
- `blog_detail` — Single post looked up by `slug`
- `gallery` — All gallery items ordered by `uploaded_at` descending

---

### Templates

#### [MODIFY] [core/templates/index.html](file:///home/master/Projects/python/DeptWebsite/core/templates/index.html)
Converted to extend [base.html](file:///home/master/Projects/python/DeptWebsite/venv/lib/python3.13/site-packages/django/contrib/admin/templates/admin/base.html). Contains:
- Hero block: bold department name + tagline, animated text
- "Latest Posts" strip (3 cards)
- "From the Gallery" teaser (4 images)
- CTA strip

#### [NEW] `core/templates/base.html`
Shared layout: Google Fonts, nav, footer, static CSS/JS.

#### [NEW] `core/templates/blog/blog_list.html`
Masonry-style blog card grid.

#### [NEW] `core/templates/blog/blog_detail.html`
Full post view with sidebar (author, date, back link).

#### [NEW] `core/templates/gallery.html`
CSS Grid photo gallery with hover overlay captions.

---

### Static Files

#### [MODIFY] [static/css/styles.css](file:///home/master/Projects/python/DeptWebsite/static/css/styles.css)
Full brutalist design system:
- Variables: `--black`, `--white`, `--yellow: #FFE600`, `--cyan: #00F5D4`
- Google Fonts: **Space Grotesk** (headings), **Inter** (body)
- Nav: black bar, yellow underline active
- Cards: thick black borders, offset box-shadow, hover lifts
- Hero: full-viewport, oversized type, raw grid lines

#### [MODIFY] [static/js/script.js](file:///home/master/Projects/python/DeptWebsite/static/js/script.js)
- Mobile nav hamburger toggle
- Scroll-reveal for cards (Intersection Observer)
- Nav active link highlighting

---

### Admin

#### [MODIFY] [core/admin.py](file:///home/master/Projects/python/DeptWebsite/core/admin.py)
Register `BlogPost` (with `list_display`, `prepopulated_fields` for slug) and `GalleryItem`.

---

## Verification Plan

### Automated
- Run Django system check:
  ```bash
  cd /home/master/Projects/python/DeptWebsite && python manage.py check
  ```
- Apply migrations:
  ```bash
  python manage.py migrate
  ```

### Browser Testing
Start server with:
```bash
python manage.py runserver
```
Then visit and verify each page loads with correct design and no console errors:
1. `http://127.0.0.1:8000/` — Homepage
2. `http://127.0.0.1:8000/blog/` — Blog list (empty state shown gracefully)
3. `http://127.0.0.1:8000/gallery/` — Gallery (empty state shown gracefully)
4. `http://127.0.0.1:8000/admin/` — Admin registers both models
5. Create a blog post + gallery item via admin, verify they appear on site pages
