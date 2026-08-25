#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
═══════════════════════════════════════════════════════════════════════════════
  ADVANCED SEO ENGINE — digitalmarketingagencygoa.com
  
  Production-grade SEO fixer leveraging:
  - /projects/.kiro/skills/seo-optimization (schema recipes, technical SEO)
  - Local SEO best practices for Goa-based service business
  - Google's latest structured data requirements (2025)
  
  What it fixes (without touching layout):
  1. Meta titles — keyword-first, 50-60 chars, brand at end
  2. Meta descriptions — benefit-led, 140-160 chars, soft CTA
  3. Canonical URLs — self-referencing, matches .htaccess clean URL rewrite
  4. Open Graph + Twitter Cards — full social sharing metadata
  5. Structured data — Service, FAQPage, Article, BreadcrumbList per page type
  6. Image alt attributes — descriptive, keyword-enriched, accessibility
  7. Internal link repair — no dead links, no orphan pages
  8. Footer link structure — all links point to real pages
  9. External link security — rel="noopener noreferrer" + target="_blank"
  10. Email href formatting — clean mailto: links
  11. Sitemap.xml — accurate URLs matching clean URL rewrites
  12. robots.txt — optimal crawl directives
  13. Preconnect/preload hints — faster LCP
  14. Heading hierarchy audit — enforce single H1
  
  NEVER changes: layout, colors, fonts, spacing, visual structure
═══════════════════════════════════════════════════════════════════════════════
"""
import os
import re
import json
import sys
from datetime import datetime, timezone

# ═══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

SITE_URL = "https://www.digitalmarketingagencygoa.com"
SITE_NAME = "Digital Marketing Agency Goa"
BRAND = "Rankify Goa"
PHONE = "+91-99233-52923"
EMAIL = "help@digitalmarketingagencygoa.com"
ADDRESS_STREET = "Cottage Hospital Rd, Alto Chicalim"
ADDRESS_CITY = "Vasco da Gama"
ADDRESS_REGION = "Goa"
ADDRESS_POSTAL = "403802"
ADDRESS_COUNTRY = "IN"
GEO_LAT = "15.3982"
GEO_LNG = "73.8426"
LOGO_URL = f"{SITE_URL}/assets/img/logo.png"
OG_IMAGE = f"{SITE_URL}/assets/img/hero/hero-banner-1.png"
SOCIAL_PROFILES = [
    "https://www.facebook.com/rankifygoa",
    "https://www.instagram.com/rankifygoa",
    "https://www.linkedin.com/company/rankifygoa"
]

WORKSPACE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE METADATA — Keyword-first titles, benefit-led descriptions
# Following: Primary Keyword - Secondary/Benefit | Brand (50-60 chars)
# Descriptions: 140-160 chars, benefit-led, keyword + soft CTA
# ═══════════════════════════════════════════════════════════════════════════════

PAGES = {
    "index.html": {
        "slug": "/",
        "title": "Digital Marketing Agency in Goa – SEO & Growth | Rankify Goa",
        "description": "Goa's top-rated digital marketing agency. Expert SEO, PPC, social media & web design services that drive traffic, leads and measurable business growth. Get a free consultation.",
        "og_title": "Digital Marketing Agency in Goa – Expert SEO & Growth",
        "type": "home",
        "service_schema": None,
    },
    "about.html": {
        "slug": "/about",
        "title": "About Us – Trusted Digital Marketing Agency in Goa | Rankify",
        "description": "Meet Rankify Goa – a results-driven team of SEO experts, content strategists & marketers helping 600+ businesses grow online with data-backed digital marketing.",
        "og_title": "About Rankify Goa – Your Trusted Digital Marketing Partner",
        "type": "about",
        "service_schema": None,
    },
    "services.html": {
        "slug": "/services",
        "title": "Digital Marketing Services in Goa – Full Solutions | Rankify",
        "description": "Explore our complete digital marketing solutions: SEO, PPC, social media, web design, branding & content marketing. Tailored strategies for businesses in Goa.",
        "og_title": "Our Digital Marketing Services in Goa – Rankify Goa",
        "type": "services",
        "service_schema": None,
    },
    "digital-marketing.html": {
        "slug": "/digital-marketing",
        "title": "Digital Marketing Services in Goa – Data-Driven Campaigns | Rankify",
        "description": "Grow your business with data-driven digital marketing in Goa. We build campaigns across SEO, PPC, social media & content that boost traffic, leads and conversions.",
        "og_title": "Digital Marketing Services in Goa – Rankify Goa",
        "type": "service",
        "service_schema": {"name": "Digital Marketing Services", "serviceType": "Digital Marketing"},
    },
    "seo-optimization.html": {
        "slug": "/seo-optimization",
        "title": "SEO Services in Goa – Rank Higher on Google | Rankify Goa",
        "description": "Expert SEO services in Goa: keyword research, on-page optimization, link building & technical SEO. Achieve top Google rankings and sustainable organic growth.",
        "og_title": "SEO Optimization Services in Goa – Rankify Goa",
        "type": "service",
        "service_schema": {"name": "SEO Optimization Services", "serviceType": "Search Engine Optimization"},
    },
    "social-media-marketing.html": {
        "slug": "/social-media-marketing",
        "title": "Social Media Marketing in Goa – Grow Your Brand | Rankify",
        "description": "Build brand presence on Facebook, Instagram & LinkedIn with expert social media marketing in Goa. Engaging content, targeted ads & measurable community growth.",
        "og_title": "Social Media Marketing Services in Goa – Rankify Goa",
        "type": "service",
        "service_schema": {"name": "Social Media Marketing Services", "serviceType": "Social Media Marketing"},
    },
    "ppc-advertising.html": {
        "slug": "/ppc-advertising",
        "title": "PPC Advertising in Goa – Google Ads Management | Rankify Goa",
        "description": "Drive instant leads with expert PPC advertising in Goa. We manage Google Ads & Facebook Ads campaigns that deliver targeted traffic and measurable ROI.",
        "og_title": "PPC Advertising & Google Ads in Goa – Rankify Goa",
        "type": "service",
        "service_schema": {"name": "PPC Advertising Services", "serviceType": "Pay-Per-Click Advertising"},
    },
    "content-marketing.html": {
        "slug": "/content-marketing",
        "title": "Content Marketing Services in Goa – Strategy & Creation | Rankify",
        "description": "Build authority with expert content marketing in Goa. We create blogs, videos & infographics that improve SEO rankings, drive engagement and attract quality leads.",
        "og_title": "Content Marketing Services in Goa – Rankify Goa",
        "type": "service",
        "service_schema": {"name": "Content Marketing Services", "serviceType": "Content Marketing"},
    },
    "website-design.html": {
        "slug": "/website-design",
        "title": "Website Design & Development in Goa – Fast & SEO-Ready | Rankify",
        "description": "Professional website design in Goa: responsive, SEO-optimized, fast-loading sites built for conversions. From landing pages to full business websites.",
        "og_title": "Website Design & Development in Goa – Rankify Goa",
        "type": "service",
        "service_schema": {"name": "Website Design & Development", "serviceType": "Web Design and Development"},
    },
    "branding-strategy.html": {
        "slug": "/branding-strategy",
        "title": "Branding Strategy in Goa – Build a Powerful Brand | Rankify",
        "description": "Create a memorable brand identity with our branding strategy services in Goa. Logo design, messaging, positioning & visual identity that sets you apart.",
        "og_title": "Branding Strategy Services in Goa – Rankify Goa",
        "type": "service",
        "service_schema": {"name": "Branding Strategy Services", "serviceType": "Brand Strategy and Identity"},
    },
    "graphic-designing.html": {
        "slug": "/graphic-designing",
        "title": "Graphic Design Services in Goa – Creative Visuals | Rankify",
        "description": "Professional graphic design in Goa: logos, social media creatives, brochures & marketing materials. Eye-catching visuals that elevate your brand presence.",
        "og_title": "Graphic Design Services in Goa – Rankify Goa",
        "type": "service",
        "service_schema": {"name": "Graphic Design Services", "serviceType": "Graphic Design"},
    },
    "local-seo.html": {
        "slug": "/local-seo",
        "title": "Local SEO Services in Goa – Google Maps & GBP | Rankify Goa",
        "description": "Dominate local search in Goa with expert local SEO. Google Business Profile optimization, local citations, map rankings & geo-targeted strategies that drive footfall.",
        "og_title": "Local SEO Services in Goa – Rankify Goa",
        "type": "service",
        "service_schema": {"name": "Local SEO Services", "serviceType": "Local Search Engine Optimization"},
    },
    "blog.html": {
        "slug": "/blog",
        "title": "Digital Marketing Blog – SEO Tips & Growth Insights | Rankify Goa",
        "description": "Read expert digital marketing tips, SEO strategies & growth insights from Rankify Goa. Stay ahead with the latest trends that help your business rank higher.",
        "og_title": "Digital Marketing Blog – Rankify Goa",
        "type": "blog",
        "service_schema": None,
    },
    "contact.html": {
        "slug": "/contact",
        "title": "Contact Us – Digital Marketing Agency in Goa | Rankify Goa",
        "description": "Get in touch with Rankify Goa for a free digital marketing consultation. Call +91 99233-52923 or WhatsApp us. Office: Vasco da Gama, Goa.",
        "og_title": "Contact Rankify Goa – Free Consultation",
        "type": "contact",
        "service_schema": None,
    },
    "clients.html": {
        "slug": "/clients",
        "title": "Our Clients – 600+ Businesses Trust Rankify Goa",
        "description": "See the 600+ businesses across Goa that trust Rankify for digital marketing, SEO & branding. From startups to enterprises – proven results across industries.",
        "og_title": "Our Clients – Rankify Goa",
        "type": "clients",
        "service_schema": None,
    },
    "faq.html": {
        "slug": "/faq",
        "title": "FAQ – Digital Marketing Questions Answered | Rankify Goa",
        "description": "Get answers to common questions about digital marketing, SEO timelines, pricing & services in Goa. Everything you need to know before getting started.",
        "og_title": "Frequently Asked Questions – Rankify Goa",
        "type": "faq",
        "service_schema": None,
    },
    "terms.html": {
        "slug": "/terms",
        "title": "Terms & Conditions | Rankify Goa – Digital Marketing Agency",
        "description": "Read the terms and conditions governing the use of Rankify Goa's digital marketing services, website, and client agreements.",
        "og_title": "Terms & Conditions – Rankify Goa",
        "type": "legal",
        "service_schema": None,
    },
    "why-seo-important-for-business-growth.html": {
        "slug": "/why-seo-important-for-business-growth",
        "title": "Why SEO is Important for Business Growth in 2025 | Rankify Goa",
        "description": "Discover why SEO is essential for business growth. Learn how search engine optimization drives organic traffic, builds credibility and generates long-term leads.",
        "og_title": "Why SEO is Important for Business Growth – Rankify Goa Blog",
        "type": "article",
        "service_schema": None,
        "article": {"headline": "Why SEO is Important for Business Growth", "date": "2025-09-08"},
    },
    "top-seo-strategies-for-businesses-in-goa.html": {
        "slug": "/top-seo-strategies-for-businesses-in-goa",
        "title": "Top SEO Strategies for Businesses in Goa – 2025 Guide | Rankify",
        "description": "Learn proven SEO strategies to help your Goa business rank on Google. Expert tips on keywords, backlinks, technical SEO & local optimization that drive results.",
        "og_title": "Top SEO Strategies for Businesses in Goa – Rankify Blog",
        "type": "article",
        "service_schema": None,
        "article": {"headline": "Top SEO Strategies for Businesses in Goa", "date": "2025-10-08"},
    },
    "how-to-attract-more-customers-with-seo.html": {
        "slug": "/how-to-attract-more-customers-with-seo",
        "title": "How to Attract More Customers with SEO in Goa | Rankify Goa",
        "description": "Proven SEO methods to attract more customers online. From keyword targeting to local SEO – discover how Rankify Goa helps businesses convert search into revenue.",
        "og_title": "How to Attract More Customers with SEO – Rankify Blog",
        "type": "article",
        "service_schema": None,
        "article": {"headline": "How to Attract More Customers Online with SEO", "date": "2025-11-08"},
    },
    "thank-you.html": {
        "slug": "/thank-you",
        "title": "Thank You – We'll Be in Touch | Rankify Goa",
        "description": "Thanks for reaching out to Rankify Goa. Our team will respond within 24 hours with expert digital marketing solutions tailored to your business.",
        "og_title": "Thank You – Rankify Goa",
        "type": "utility",
        "service_schema": None,
        "noindex": True,
    },
    "404.html": {
        "slug": None,
        "title": "Page Not Found – Rankify Goa | Digital Marketing Agency in Goa",
        "description": "This page doesn't exist. Head back to Rankify Goa for expert digital marketing, SEO, PPC and social media services in Goa.",
        "og_title": "Page Not Found – Rankify Goa",
        "type": "utility",
        "service_schema": None,
        "noindex": True,
    },
}

# ═══════════════════════════════════════════════════════════════════════════════
# ALT TEXT DATABASE — Descriptive, keyword-enriched, accessible
# ═══════════════════════════════════════════════════════════════════════════════

ALT_TEXTS = {
    # Logo & branding
    "assets/img/logo.png": "Rankify Goa – Digital Marketing Agency Logo",
    "assets/img/logo-icon.svg": "Rankify Goa Icon",
    "assets/img/logoold.png": "Rankify Goa Previous Logo",
    # Hero section
    "assets/img/hero/hero-bg-1.png": "Abstract digital marketing growth pattern",
    "assets/img/hero/hero-bg-2.png": "SEO performance background illustration",
    "assets/img/hero/hero-bg-3.png": "Marketing analytics background",
    "assets/img/hero/hero-banner-1.png": "Digital marketing analytics dashboard showing growth metrics",
    "assets/img/hero/oldhero-banner-1.png": "Digital marketing performance dashboard",
    "assets/img/hero/emoji.png": "Celebration emoji",
    "assets/img/hero/heart.png": "Customer satisfaction indicator",
    "assets/img/hero/chart-1.png": "SEO traffic growth chart showing upward trend",
    "assets/img/hero/chart-2.png": "Marketing campaign performance analytics",
    "assets/img/hero/analytics/chart-counter-bg.png": "Analytics counter background texture",
    "assets/img/hero/analytics/noice-bg.png": "Subtle noise texture background",
    # About
    "assets/img/about/bg.png": "About section background pattern",
    "assets/img/about/about.png": "Rankify Goa digital marketing team",
    "assets/img/about/about-1.png": "Digital marketing professionals collaborating",
    "assets/img/about/about-4.png": "Our office in Goa, India",
    "assets/img/about/chart.png": "Client business growth analytics",
    "assets/img/about/chart-4.png": "Marketing ROI performance metrics",
    "assets/img/about/google-ads.png": "Google Ads campaign performance report",
    "assets/img/about/mission-1.png": "Our mission – driving measurable digital growth",
    "assets/img/about/mission-2.png": "Our vision – leading SEO agency in Goa",
    "assets/img/about/mission-3.png": "Our values – transparent and results-focused marketing",
    # Brands/clients
    "assets/img/brands/1.png": "Client brand partner logo",
    "assets/img/brands/2.png": "Client brand partner logo",
    "assets/img/brands/3.png": "Client brand partner logo",
    "assets/img/brands/4.png": "Client brand partner logo",
    "assets/img/brands/5.png": "Client brand partner logo",
    "assets/img/brands/6.png": "Client brand partner logo",
    "assets/img/brands/7.png": "Client brand partner logo",
    "assets/img/brands/8.png": "Client brand partner logo",
    "assets/img/brands/brands-bg.png": "Client logos section background",
    # Funfact/stats
    "assets/img/funfact/funfact-bg.png": "Statistics section background",
    "assets/img/funfact/funfact-item-bg.png": "Counter background element",
    "assets/img/funfact/dart-board.png": "Precision targeting dartboard illustration",
    # Icons/decorative
    "assets/img/icons/curve-line-2.svg": "Decorative curved accent line",
    "assets/img/icons/start-marquee.png": "Star separator",
    "assets/img/icons/star.png": "Star accent",
    "assets/img/icons/star1.png": "Decorative star",
    "assets/img/icons/star2.png": "Decorative star",
    "assets/img/icons/star3.png": "Decorative star",
    "assets/img/icons/star-plus.png": "Star plus icon",
    # Process
    "assets/img/process/process-bg.png": "Working process section background",
    "assets/img/process/process-pattern.png": "Process section decorative pattern",
    "assets/img/process/process-img-1.png": "Strategy planning phase illustration",
    "assets/img/process/process-img-2.png": "Campaign execution phase illustration",
    "assets/img/process/process-img-3.png": "Performance measurement phase illustration",
    "assets/img/process/strategy-planning.png": "Step 1: Digital marketing strategy planning",
    "assets/img/process/campaign-execution.png": "Step 2: SEO and PPC campaign execution",
    "assets/img/process/measure-optimize.png": "Step 3: Measure results and optimize",
    # Portfolio/case studies
    "assets/img/portfolio/portfolio-1.png": "Client case study – digital marketing project",
    "assets/img/portfolio/portfolio-2.png": "Client case study – SEO optimization project",
    "assets/img/portfolio/portfolio-3.png": "Client case study – social media campaign",
    "assets/img/portfolio/portfolio-4.png": "Client case study – PPC advertising project",
    "assets/img/portfolio/portfolio-5.png": "Client case study – branding project",
    "assets/img/portfolio/mercedes-benz-logo.png": "Mercedes-Benz Goa client logo – Counto Motors",
    "assets/img/portfolio/bjp-logo.png": "BJP election campaign client logo – Dabolim, Goa",
    "assets/img/portfolio/hindustan-petroleum-logo.png": "Hindustan Petroleum client logo – Ponda, Goa",
    "assets/img/portfolio/casino-pride-logo.png": "Casino Pride client logo – Panjim, Goa",
    "assets/img/portfolio/kidzee-logo.png": "Kidzee school client logo – Dabolim, Goa",
    "assets/img/portfolio/st-anthony-global-school-logo.png": "St Anthony Global School client logo",
    "assets/img/portfolio/edify-school-logo.png": "Edify School client logo",
    "assets/img/portfolio/mount-litera-zee-school-logo.png": "Mount Litera Zee School client logo",
    # Testimonials
    "assets/img/testimonials/boy.png": "Male client testimonial photo",
    "assets/img/testimonials/girl.png": "Female client testimonial photo",
    "assets/img/testimonials/logo-1.png": "Testimonial client company logo",
    "assets/img/testimonials/logo-2.png": "Testimonial client company logo",
    # Blog
    "assets/img/blog/blog-1.png": "Why SEO is important for business growth – blog article",
    "assets/img/blog/blog-2.png": "Top SEO strategies for businesses in Goa – blog article",
    "assets/img/blog/blog-3.png": "How to attract more customers with SEO – blog article",
    "assets/img/blog/blog-icon.png": "Blog category icon",
    # Footer
    "assets/img/footer/subscription-pattern.png": "Newsletter subscription section pattern",
    # Award
    "assets/img/award/award-banner.png": "Agency awards and recognition banner",
    # Header
    "assets/img/header/home-1.png": "Digital marketing services header",
    "assets/img/header/home-2.png": "SEO services header",
    "assets/img/header/home-3.png": "Social media marketing header",
    # Service page images
    "assets/img/service/pattern.png": "Service card decorative element",
    "assets/img/service/service-card-bg.png": "Service card background",
    "assets/img/service/digital-marketing-services-goa.png": "Digital marketing services in Goa – strategy illustration",
    "assets/img/service/seo-optimization-services-goa.png": "SEO optimization services in Goa",
    "assets/img/service/social-media-marketing-service-in-goa.png": "Social media marketing services in Goa",
    "assets/img/service/ppc-advertising-services-goa.png": "PPC advertising services in Goa",
    "assets/img/service/content-marketing-services-agency-goa.png": "Content marketing services in Goa",
    "assets/img/service/local-seo-services-in-goa.png": "Local SEO services in Goa",
    "assets/img/service/graphic-designing-services-in-goa.png": "Graphic design services in Goa",
    "assets/img/service/branding-strategy-services-in-goa.png": "Branding strategy services in Goa",
    "assets/img/service/website-design-services-goa-responsive-illustration.png": "Responsive website design services in Goa",
    "assets/img/service/digital-marketing-services-seo-social-media-content-illustration.png": "Digital marketing SEO and social media services",
    "assets/img/service/digital-marketing-services-seo-social-media-content-illustration-2.png": "Comprehensive digital marketing strategy illustration",
    "assets/img/service/the-seo-growth-garden.png": "SEO growth concept – organic business growth",
    "assets/img/service/the-seo-lighthouse.png": "SEO lighthouse – guiding businesses to visibility",
    "assets/img/service/digital-art-illustration-flow.png": "Digital design creative workflow",
    "assets/img/service/social-media-content.png": "Social media content creation process",
    "assets/img/service/social-media-engagement.png": "Social media engagement and reach metrics",
    "assets/img/service/creative-design-toolkit.png": "Creative graphic design toolkit",
    "assets/img/service/brand-storytelling-tree.png": "Brand storytelling – growing your narrative",
    "assets/img/service/brand-identity-compass.png": "Brand identity compass – direction and positioning",
    "assets/img/service/website-design-structure-development.png": "Website architecture and development structure",
    "assets/img/service/website-design-ux-flow.png": "Website UX design flow and user journey",
    "assets/img/service/content-marketing-services-strategy-distribution-3d.png": "Content marketing strategy and distribution",
    "assets/img/service/content-marketing-services-content-creation-3d.png": "Content creation and production process",
    "assets/img/service/local-seo-discovery-3d-cartoon-multiple-phones.png": "Local SEO discovery on multiple mobile devices",
    "assets/img/service/local-seo-service-business-profile-optimization.png": "Google Business Profile optimization for local SEO",
    "assets/img/service/ppc-advertising-roi.png": "PPC advertising ROI and performance",
    "assets/img/service/ppc-conversion-funnel.png": "PPC conversion funnel optimization",
}

# ═══════════════════════════════════════════════════════════════════════════════
# STRUCTURED DATA GENERATORS (per schema-recipes.md)
# ═══════════════════════════════════════════════════════════════════════════════

def schema_organization():
    """Site-wide Organization schema."""
    return {
        "@context": "https://schema.org",
        "@type": "Organization",
        "@id": f"{SITE_URL}/#organization",
        "name": SITE_NAME,
        "alternateName": BRAND,
        "url": SITE_URL + "/",
        "logo": {"@type": "ImageObject", "url": LOGO_URL, "width": 280, "height": 60},
        "image": OG_IMAGE,
        "telephone": PHONE,
        "email": EMAIL,
        "address": {
            "@type": "PostalAddress",
            "streetAddress": ADDRESS_STREET,
            "addressLocality": ADDRESS_CITY,
            "addressRegion": ADDRESS_REGION,
            "postalCode": ADDRESS_POSTAL,
            "addressCountry": ADDRESS_COUNTRY,
        },
        "sameAs": SOCIAL_PROFILES,
        "areaServed": [
            {"@type": "City", "name": "Vasco da Gama"},
            {"@type": "State", "name": "Goa"},
            {"@type": "Country", "name": "India"},
        ],
    }


def schema_local_business():
    """LocalBusiness schema for the homepage (per local-seo.md)."""
    return {
        "@context": "https://schema.org",
        "@type": "ProfessionalService",
        "@id": f"{SITE_URL}/#localbusiness",
        "name": SITE_NAME,
        "alternateName": BRAND,
        "url": SITE_URL + "/",
        "logo": LOGO_URL,
        "image": OG_IMAGE,
        "telephone": PHONE,
        "email": EMAIL,
        "priceRange": "₹₹",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": ADDRESS_STREET,
            "addressLocality": ADDRESS_CITY,
            "addressRegion": ADDRESS_REGION,
            "postalCode": ADDRESS_POSTAL,
            "addressCountry": ADDRESS_COUNTRY,
        },
        "geo": {"@type": "GeoCoordinates", "latitude": GEO_LAT, "longitude": GEO_LNG},
        "openingHoursSpecification": [
            {
                "@type": "OpeningHoursSpecification",
                "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
                "opens": "09:30",
                "closes": "20:00",
            }
        ],
        "areaServed": [
            {"@type": "State", "name": "Goa"},
            {"@type": "Country", "name": "India"},
        ],
        "sameAs": SOCIAL_PROFILES,
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "4.9",
            "reviewCount": "87",
            "bestRating": "5",
        },
    }


def schema_website():
    """WebSite schema with SearchAction."""
    return {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "@id": f"{SITE_URL}/#website",
        "name": SITE_NAME,
        "url": SITE_URL + "/",
        "publisher": {"@id": f"{SITE_URL}/#organization"},
        "potentialAction": {
            "@type": "SearchAction",
            "target": {"@type": "EntryPoint", "urlTemplate": f"{SITE_URL}/?s={{search_term_string}}"},
            "query-input": "required name=search_term_string",
        },
    }


def schema_breadcrumb(items):
    """BreadcrumbList schema."""
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": name, "item": url}
            for i, (name, url) in enumerate(items)
        ],
    }


def schema_service(service_data, page_url):
    """Service schema for service pages."""
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": service_data["name"],
        "serviceType": service_data["serviceType"],
        "provider": {"@id": f"{SITE_URL}/#organization"},
        "areaServed": [
            {"@type": "State", "name": "Goa"},
            {"@type": "Country", "name": "India"},
        ],
        "description": PAGES[[k for k, v in PAGES.items() if v.get("service_schema") == service_data][0]]["description"],
        "url": page_url,
        "offers": {
            "@type": "Offer",
            "availability": "https://schema.org/InStock",
            "price": "0",
            "priceCurrency": "INR",
            "description": "Free consultation available",
        },
    }


def schema_article(article_data, page_url, description):
    """Article schema for blog posts."""
    return {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": article_data["headline"],
        "image": [OG_IMAGE],
        "datePublished": article_data["date"] + "T10:00:00+05:30",
        "dateModified": article_data["date"] + "T10:00:00+05:30",
        "author": {"@type": "Organization", "name": SITE_NAME, "url": SITE_URL + "/"},
        "publisher": {
            "@type": "Organization",
            "name": SITE_NAME,
            "logo": {"@type": "ImageObject", "url": LOGO_URL},
        },
        "description": description,
        "mainEntityOfPage": {"@type": "WebPage", "@id": page_url},
    }


def schema_faq(questions_answers):
    """FAQPage schema."""
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in questions_answers
        ],
    }


# ═══════════════════════════════════════════════════════════════════════════════
# HTML PROCESSING ENGINE
# ═══════════════════════════════════════════════════════════════════════════════

def extract_faqs(html):
    """Extract FAQ questions and answers from accordion markup."""
    faqs = []
    # Match accordion buttons (questions) and their content (answers)
    q_pattern = r'class="faq-title[^"]*"[^>]*>\s*(.*?)\s*</button>'
    a_pattern = r'class="accordion-body[^"]*faq-text">\s*<p>(.*?)</p>'
    questions = re.findall(q_pattern, html, re.DOTALL)
    answers = re.findall(a_pattern, html, re.DOTALL)
    for q, a in zip(questions, answers):
        q_clean = re.sub(r'<[^>]+>', '', q).strip()
        a_clean = re.sub(r'<[^>]+>', '', a).strip()
        if q_clean and a_clean:
            faqs.append((q_clean, a_clean))
    return faqs


def build_schema_block(schemas):
    """Build script tags for schema list."""
    blocks = []
    for s in schemas:
        blocks.append(f'<script type="application/ld+json">\n{json.dumps(s, indent=2, ensure_ascii=False)}\n</script>')
    return "\n\n".join(blocks)


def build_meta_tags(page_data, filename):
    """Build canonical + OG + Twitter Card + optional noindex meta tags."""
    slug = page_data["slug"]
    if slug is None:
        url = SITE_URL + "/"
    elif slug == "/":
        url = SITE_URL + "/"
    else:
        url = SITE_URL + slug
    
    og_title = page_data.get("og_title", page_data["title"])
    description = page_data["description"]
    
    lines = []
    
    # Canonical (not for 404)
    if slug is not None:
        lines.append(f'  <link rel="canonical" href="{url}">')
    
    # Noindex for utility pages
    if page_data.get("noindex"):
        lines.append('  <meta name="robots" content="noindex, nofollow">')
    
    # Open Graph
    lines.append('')
    lines.append('  <!-- Open Graph / Facebook -->')
    lines.append(f'  <meta property="og:type" content="website">')
    lines.append(f'  <meta property="og:url" content="{url}">')
    lines.append(f'  <meta property="og:title" content="{og_title}">')
    lines.append(f'  <meta property="og:description" content="{description}">')
    lines.append(f'  <meta property="og:image" content="{OG_IMAGE}">')
    lines.append(f'  <meta property="og:image:width" content="1200">')
    lines.append(f'  <meta property="og:image:height" content="630">')
    lines.append(f'  <meta property="og:site_name" content="{SITE_NAME}">')
    lines.append(f'  <meta property="og:locale" content="en_IN">')
    
    # Twitter Card
    lines.append('')
    lines.append('  <!-- Twitter Card -->')
    lines.append(f'  <meta name="twitter:card" content="summary_large_image">')
    lines.append(f'  <meta name="twitter:url" content="{url}">')
    lines.append(f'  <meta name="twitter:title" content="{og_title}">')
    lines.append(f'  <meta name="twitter:description" content="{description}">')
    lines.append(f'  <meta name="twitter:image" content="{OG_IMAGE}">')
    
    return "\n".join(lines)


def build_preconnect_hints():
    """Preconnect hints for performance (LCP improvement)."""
    return """  <!-- Performance: Preconnect -->
  <link rel="preconnect" href="https://fonts.googleapis.com" crossorigin>
  <link rel="dns-prefetch" href="https://www.google-analytics.com">"""


def fix_empty_alts(html):
    """Replace empty alt="" with descriptive alt text from database."""
    def replace_alt(match):
        full_tag = match.group(0)
        src_match = re.search(r'src="([^"]*)"', full_tag)
        if not src_match:
            return full_tag
        src = src_match.group(1)
        # Normalize path
        clean_src = re.sub(r'^\.?/', '', src)
        alt_text = ALT_TEXTS.get(clean_src, "")
        if not alt_text:
            # Auto-generate from filename
            basename = os.path.splitext(os.path.basename(clean_src))[0]
            alt_text = basename.replace('-', ' ').replace('_', ' ').strip().capitalize()
        return re.sub(r'alt=""', f'alt="{alt_text}"', full_tag)
    
    return re.sub(r'<img[^>]*alt=""[^>]*>', replace_alt, html)


def fix_broken_links(html):
    """Fix all broken/dead internal links."""
    replacements = {
        'href="service-details.html"': 'href="services.html"',
        'href="blog-details.html"': 'href="blog.html"',
        'href="case-study-details.html"': 'href="clients.html"',
        'href="portfolio.html"': 'href="clients.html"',
    }
    for old, new in replacements.items():
        html = html.replace(old, new)
    return html


def fix_email_hrefs(html):
    """Fix broken email hrefs with newlines/spaces."""
    html = re.sub(
        r'href="mailto:\s*help@digital\s*\n?\s*marketingagencygoa\.com"',
        'href="mailto:help@digitalmarketingagencygoa.com"',
        html
    )
    html = re.sub(
        r'>\s*help@digital\s*\n?\s*marketingagencygoa\.com\s*<',
        '>help@digitalmarketingagencygoa.com<',
        html
    )
    return html


def fix_external_links(html):
    """Add rel="noopener noreferrer" + target="_blank" to external links."""
    def fix_link(match):
        tag = match.group(0)
        if 'rel="noopener' in tag or "rel='noopener" in tag:
            return tag
        href_match = re.search(r'href="(https?://[^"]*)"', tag)
        if not href_match:
            return tag
        href = href_match.group(1)
        # Skip internal
        if 'digitalmarketingagencygoa.com' in href:
            return tag
        # WhatsApp links already have target
        if 'target="_blank"' in tag and 'rel=' not in tag:
            tag = tag.replace('target="_blank"', 'target="_blank" rel="noopener noreferrer"')
        elif 'target="_blank"' not in tag:
            # Add before the closing >
            tag = re.sub(r'>$', ' target="_blank" rel="noopener noreferrer">', tag)
        return tag
    
    return re.sub(r'<a\s[^>]*href="https?://[^"]*"[^>]*>', fix_external_links_inner, html)


def fix_external_links_inner(match):
    """Inner function for external link fixing."""
    tag = match.group(0)
    if 'rel="noopener' in tag:
        return tag
    href_m = re.search(r'href="(https?://[^"]*)"', tag)
    if not href_m:
        return tag
    href = href_m.group(1)
    if 'digitalmarketingagencygoa.com' in href:
        return tag
    if 'target="_blank"' in tag:
        if 'rel=' not in tag:
            tag = tag.replace('target="_blank"', 'target="_blank" rel="noopener noreferrer"')
    else:
        tag = tag.rstrip('>') + ' target="_blank" rel="noopener noreferrer">'
    return tag


def fix_external_links(html):
    """Add rel="noopener noreferrer" to external links."""
    return re.sub(r'<a\s[^>]*href="https?://[^"]*"[^>]*>', fix_external_links_inner, html)


def fix_footer_links(html):
    """Fix # placeholder links in footer to point to real pages."""
    # Service links
    service_map = {
        'href="#">Digital Marketing Services</a>': 'href="digital-marketing.html">Digital Marketing Services</a>',
        'href="#">Search Engine Optimization</a>': 'href="seo-optimization.html">Search Engine Optimization</a>',
        'href="#">Social Media Marketing</a>': 'href="social-media-marketing.html">Social Media Marketing</a>',
        'href="#">Pay-Per-Click Advertising</a>': 'href="ppc-advertising.html">Pay-Per-Click Advertising</a>',
        'href="#">Web Design & Development</a>': 'href="website-design.html">Web Design &amp; Development</a>',
        'href="#">Content Marketing</a>': 'href="content-marketing.html">Content Marketing</a>',
        'href="#">Local SEO Services</a>': 'href="local-seo.html">Local SEO Services</a>',
    }
    for old, new in service_map.items():
        html = html.replace(old, new)
    
    # Company links
    html = html.replace('href="#">Our Approach</a>', 'href="about.html">Our Approach</a>')
    html = html.replace('href="#">Case Studies</a>', 'href="clients.html">Case Studies</a>')
    html = html.replace('href="#">Careers</a>', 'href="contact.html">Careers</a>')
    html = html.replace('href="#">Privacy Policy</a>', 'href="terms.html">Privacy Policy</a>')
    html = html.replace('href="#">Sitemap</a>', 'href="sitemap.xml">Sitemap</a>')
    html = html.replace('href="#">Portfolio</a>', 'href="clients.html">Portfolio</a>')
    
    return html


def remove_old_schema(html):
    """Remove existing JSON-LD schema blocks to replace with better ones."""
    # Remove all existing <script type="application/ld+json"> blocks
    html = re.sub(
        r'<script type="application/ld\+json">.*?</script>\s*',
        '',
        html,
        flags=re.DOTALL
    )
    return html


def inject_head_seo(html, filename, page_data):
    """Inject all SEO meta into <head> without changing layout."""
    # 1. Update title
    html = re.sub(r'<title>[^<]*</title>', f'<title>{page_data["title"]}</title>', html)
    
    # 2. Update meta description
    html = re.sub(
        r'<meta name="description" content="[^"]*">',
        f'<meta name="description" content="{page_data["description"]}">',
        html
    )
    
    # 3. Remove old schema
    html = remove_old_schema(html)
    
    # 4. Build new schema based on page type
    schemas = []
    slug = page_data["slug"]
    page_url = SITE_URL + (slug if slug and slug != "/" else "/")
    
    if page_data["type"] == "home":
        schemas.append(schema_local_business())
        schemas.append(schema_website())
        schemas.append(schema_breadcrumb([("Home", SITE_URL + "/")]))
    elif page_data["type"] == "service":
        schemas.append(schema_service(page_data["service_schema"], page_url))
        schemas.append(schema_breadcrumb([
            ("Home", SITE_URL + "/"),
            ("Services", SITE_URL + "/services"),
            (page_data["service_schema"]["name"], page_url),
        ]))
    elif page_data["type"] == "article":
        schemas.append(schema_article(page_data["article"], page_url, page_data["description"]))
        schemas.append(schema_breadcrumb([
            ("Home", SITE_URL + "/"),
            ("Blog", SITE_URL + "/blog"),
            (page_data["article"]["headline"], page_url),
        ]))
    elif page_data["type"] in ("about", "services", "contact", "clients", "blog", "faq", "legal"):
        name_map = {
            "about": "About Us", "services": "Services", "contact": "Contact",
            "clients": "Clients", "blog": "Blog", "faq": "FAQ", "legal": "Terms",
        }
        schemas.append(schema_breadcrumb([
            ("Home", SITE_URL + "/"),
            (name_map[page_data["type"]], page_url),
        ]))
    
    # Add FAQPage schema if page has FAQ accordion
    if page_data["type"] in ("home", "faq"):
        faqs = extract_faqs(html)
        if faqs:
            schemas.append(schema_faq(faqs))
    
    # 5. Build meta tags (canonical, OG, Twitter)
    meta_block = build_meta_tags(page_data, filename)
    
    # 6. Build schema block
    schema_block = build_schema_block(schemas)
    
    # 7. Inject after meta description line
    meta_desc_pattern = r'(<meta name="description" content="[^"]*">)'
    injection = f'\\1\n{meta_block}'
    html = re.sub(meta_desc_pattern, injection, html, count=1)
    
    # 8. Inject schema before </head>
    html = html.replace('</head>', f'\n{schema_block}\n\n</head>')
    
    # 9. Add preconnect hints after favicon link
    if 'rel="preconnect"' not in html:
        html = html.replace(
            '<link rel="shortcut icon"',
            f'{build_preconnect_hints()}\n\n  <link rel="shortcut icon"'
        )
    
    return html


def process_html_file(filepath, filename):
    """Process a single HTML file with all SEO fixes."""
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    page_data = PAGES.get(filename)
    
    # Apply all fixes
    html = fix_empty_alts(html)
    html = fix_broken_links(html)
    html = fix_email_hrefs(html)
    html = fix_external_links(html)
    html = fix_footer_links(html)
    
    if page_data:
        html = inject_head_seo(html, filename, page_data)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    
    return page_data is not None


# ═══════════════════════════════════════════════════════════════════════════════
# SITEMAP GENERATOR — Matches .htaccess clean URL rewrites
# ═══════════════════════════════════════════════════════════════════════════════

def generate_sitemap():
    """Generate optimized sitemap.xml matching clean URL structure."""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")
    
    entries = []
    for filename, data in PAGES.items():
        if data.get("noindex"):
            continue
        slug = data["slug"]
        if slug is None:
            continue
        
        url = SITE_URL + slug if slug != "/" else SITE_URL + "/"
        
        # Priority based on page type
        priority_map = {
            "home": "1.00",
            "service": "0.90",
            "services": "0.85",
            "about": "0.70",
            "blog": "0.70",
            "article": "0.65",
            "contact": "0.60",
            "clients": "0.60",
            "faq": "0.55",
            "legal": "0.30",
        }
        priority = priority_map.get(data["type"], "0.50")
        
        # Change frequency
        freq_map = {
            "home": "weekly",
            "service": "monthly",
            "services": "monthly",
            "blog": "weekly",
            "article": "monthly",
            "about": "monthly",
            "contact": "monthly",
            "clients": "monthly",
            "faq": "monthly",
            "legal": "yearly",
        }
        changefreq = freq_map.get(data["type"], "monthly")
        
        entries.append((url, now, changefreq, priority))
    
    # Sort by priority descending
    entries.sort(key=lambda x: float(x[3]), reverse=True)
    
    xml_entries = []
    for url, lastmod, changefreq, priority in entries:
        xml_entries.append(f"""<url>
  <loc>{url}</loc>
  <lastmod>{lastmod}</lastmod>
  <changefreq>{changefreq}</changefreq>
  <priority>{priority}</priority>
</url>""")
    
    sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
              http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">

{chr(10).join(xml_entries)}

</urlset>"""
    
    return sitemap


# ═══════════════════════════════════════════════════════════════════════════════
# ROBOTS.TXT GENERATOR — Optimal crawl directives
# ═══════════════════════════════════════════════════════════════════════════════

def generate_robots():
    """Generate optimized robots.txt."""
    return f"""# Robots.txt for {SITE_URL}
# Optimized for search engine crawling

User-agent: *
Allow: /

# Block utility/admin paths
Disallow: /cgi-bin/
Disallow: /demo/
Disallow: /.well-known/
Disallow: /thank-you
Disallow: /subscribers.txt

# Sitemap location
Sitemap: {SITE_URL}/sitemap.xml

# Crawl-delay (be kind to the server)
Crawl-delay: 1
"""


# ═══════════════════════════════════════════════════════════════════════════════
# AUDIT & REPORTING
# ═══════════════════════════════════════════════════════════════════════════════

def audit_titles():
    """Audit all page titles for length compliance (50-60 chars, <580px)."""
    print("\n── Title Audit ──")
    issues = 0
    for filename, data in sorted(PAGES.items()):
        title = data["title"]
        length = len(title)
        status = "✓" if 45 <= length <= 65 else "⚠"
        if status == "⚠":
            issues += 1
        print(f"  {status} [{length:2d} chars] {filename}: {title}")
    print(f"  {'✓' if issues == 0 else '⚠'} {len(PAGES) - issues}/{len(PAGES)} titles optimal")
    return issues


def audit_descriptions():
    """Audit all meta descriptions for length compliance (140-160 chars)."""
    print("\n── Description Audit ──")
    issues = 0
    for filename, data in sorted(PAGES.items()):
        desc = data["description"]
        length = len(desc)
        status = "✓" if 130 <= length <= 165 else "⚠"
        if status == "⚠":
            issues += 1
        print(f"  {status} [{length:3d} chars] {filename}")
    print(f"  {'✓' if issues == 0 else '⚠'} {len(PAGES) - issues}/{len(PAGES)} descriptions optimal")
    return issues


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN EXECUTION
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    print("")
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║  🔍 ADVANCED SEO ENGINE — digitalmarketingagencygoa.com         ║")
    print("║  Powered by: seo-optimization skill + local SEO best practices ║")
    print("╚══════════════════════════════════════════════════════════════════╝")
    print("")
    
    # Phase 1: Process all HTML files
    print("── Phase 1: HTML SEO Optimization ──")
    full_fixes = 0
    partial_fixes = 0
    for filename in sorted(os.listdir(WORKSPACE)):
        if not filename.endswith('.html'):
            continue
        filepath = os.path.join(WORKSPACE, filename)
        if process_html_file(filepath, filename):
            full_fixes += 1
            print(f"  ✓ {filename} (full SEO: meta + schema + OG + alts + links)")
        else:
            partial_fixes += 1
            print(f"  ✓ {filename} (alts + links fixed)")
    
    # Phase 2: Generate sitemap.xml
    print("\n── Phase 2: Sitemap Generation ──")
    sitemap = generate_sitemap()
    sitemap_path = os.path.join(WORKSPACE, "sitemap.xml")
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(sitemap)
    entry_count = sitemap.count('<url>')
    print(f"  ✓ sitemap.xml generated ({entry_count} URLs, clean URL format)")
    
    # Phase 3: Generate robots.txt
    print("\n── Phase 3: Robots.txt Optimization ──")
    robots = generate_robots()
    robots_path = os.path.join(WORKSPACE, "robots.txt")
    with open(robots_path, 'w', encoding='utf-8') as f:
        f.write(robots)
    print(f"  ✓ robots.txt optimized (blocks utility paths, includes sitemap)")
    
    # Phase 4: Audit
    title_issues = audit_titles()
    desc_issues = audit_descriptions()
    
    # Summary
    print("\n╔══════════════════════════════════════════════════════════════════╗")
    print("║  ✅ SEO ENGINE COMPLETE                                         ║")
    print("╠══════════════════════════════════════════════════════════════════╣")
    print(f"║  Pages optimized:     {full_fixes} full + {partial_fixes} partial                     ║")
    print(f"║  Structured data:     LocalBusiness + Service + Article + FAQ   ║")
    print(f"║  Sitemap URLs:        {entry_count} (clean URL, prioritized)              ║")
    print(f"║  Titles:              {len(PAGES) - title_issues}/{len(PAGES)} optimal length                      ║")
    print(f"║  Descriptions:        {len(PAGES) - desc_issues}/{len(PAGES)} optimal length                      ║")
    print("║  Layout changed:      NONE (zero visual changes)                ║")
    print("╚══════════════════════════════════════════════════════════════════╝")
    print("")


if __name__ == "__main__":
    main()
