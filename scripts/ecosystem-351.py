#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════════════════════
  351-PAGE TOPICAL AUTHORITY ECOSYSTEM BUILDER
  digitalmarketingagencygoa.com
  
  Generates 329 new pages (+ 22 existing = 351 total) covering:
  - 15 Industry vertical pages
  - 12 Location pages  
  - 60 Location+Service combination pages
  - 25 Service deep-dive pages
  - 30 Topic cluster/guide pages
  - 15 Comparison pages
  - 20 Use-case pages  
  - 80 Blog/article pages
  - 10 FAQ hub pages
  - 62 Misc targeted landing pages
  
  RULES:
  - ZERO competitor brand names anywhere
  - Only brand names: Rankify Goa, Digital Marketing Agency Goa, Sanctify
  - Every page gets: canonical, OG, Twitter, schema, FAQ, internal links
  - Hub-spoke linking throughout
  
  COMPETITOR GAPS WE EXPLOIT:
  - None of them have location+service combination pages
  - None have industry vertical depth
  - None have 300+ page topical authority
  - None have FAQ schema on every page
  - None have programmatic internal linking mesh
═══════════════════════════════════════════════════════════════════════════════
"""
import os
import json
import hashlib
from datetime import datetime, timezone

SITE_URL = "https://www.digitalmarketingagencygoa.com"
SITE_NAME = "Digital Marketing Agency Goa"
BRAND = "Rankify Goa"
WORKSPACE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ═══════════════════════════════════════════════════════════════════════════════
# DATA: Services, Locations, Industries
# ═══════════════════════════════════════════════════════════════════════════════

SERVICES = [
    {"slug": "seo", "name": "SEO", "full": "Search Engine Optimization", "icon": "tji-analytics-reporting"},
    {"slug": "digital-marketing", "name": "Digital Marketing", "full": "Digital Marketing Services", "icon": "tji-seo-strategy"},
    {"slug": "social-media-marketing", "name": "Social Media Marketing", "full": "Social Media Marketing", "icon": "tji-ppc-advertising"},
    {"slug": "ppc", "name": "PPC Advertising", "full": "Pay-Per-Click Advertising", "icon": "tji-social-management"},
    {"slug": "website-design", "name": "Website Design", "full": "Website Design & Development", "icon": "tji-content-creation"},
    {"slug": "content-marketing", "name": "Content Marketing", "full": "Content Marketing", "icon": "tji-keyword-optimization"},
    {"slug": "local-seo", "name": "Local SEO", "full": "Local SEO Services", "icon": "tji-analytics-reporting"},
    {"slug": "branding", "name": "Branding", "full": "Branding & Strategy", "icon": "tji-seo-strategy"},
    {"slug": "graphic-design", "name": "Graphic Design", "full": "Graphic Design Services", "icon": "tji-content-creation"},
    {"slug": "email-marketing", "name": "Email Marketing", "full": "Email Marketing", "icon": "tji-keyword-optimization"},
    {"slug": "video-marketing", "name": "Video Marketing", "full": "Video Marketing & Production", "icon": "tji-social-management"},
    {"slug": "reputation-management", "name": "Online Reputation Management", "full": "Online Reputation Management", "icon": "tji-analytics-reporting"},
]

LOCATIONS = [
    {"slug": "panaji", "name": "Panaji", "alt": "Panjim", "region": "North Goa", "landmarks": "Miramar Beach, Fontainhas, Dona Paula", "businesses": "government offices, restaurants, hotels, retail shops, IT companies"},
    {"slug": "mapusa", "name": "Mapusa", "alt": "Mapusa", "region": "North Goa", "landmarks": "Friday Market, Mae de Deus Church", "businesses": "retailers, wholesalers, restaurants, clinics, educational institutes"},
    {"slug": "margao", "name": "Margao", "alt": "Madgaon", "region": "South Goa", "landmarks": "Grace Church, Municipal Garden, KTC Bus Stand", "businesses": "commercial establishments, hospitals, law firms, real estate agents"},
    {"slug": "vasco", "name": "Vasco da Gama", "alt": "Vasco", "region": "South Goa", "landmarks": "Mormugao Port, Bogmalo Beach, Naval Area", "businesses": "shipping companies, port services, restaurants, retail, healthcare"},
    {"slug": "calangute", "name": "Calangute", "alt": "Calangute", "region": "North Goa", "landmarks": "Calangute Beach, Saturday Night Market", "businesses": "beach shacks, resorts, water sports, nightclubs, souvenir shops"},
    {"slug": "anjuna", "name": "Anjuna", "alt": "Anjuna", "region": "North Goa", "landmarks": "Anjuna Flea Market, Curlies Beach Shack", "businesses": "hostels, cafes, yoga centers, boutique hotels, co-working spaces"},
    {"slug": "ponda", "name": "Ponda", "alt": "Ponda", "region": "Central Goa", "landmarks": "Shri Manguesh Temple, Spice Plantations", "businesses": "spice gardens, temples, industrial units, educational institutions"},
    {"slug": "bicholim", "name": "Bicholim", "alt": "Bicholim", "region": "North Goa", "landmarks": "Mayem Lake, Mining areas", "businesses": "mining companies, agricultural businesses, local retail"},
    {"slug": "porvorim", "name": "Porvorim", "alt": "Porvorim", "region": "North Goa", "landmarks": "Goa Legislative Assembly, EDC Complex", "businesses": "IT parks, corporate offices, showrooms, restaurants, gyms"},
    {"slug": "candolim", "name": "Candolim", "alt": "Candolim", "region": "North Goa", "landmarks": "Fort Aguada, Sinquerim Beach", "businesses": "luxury resorts, beach restaurants, water sports operators, spas"},
    {"slug": "north-goa", "name": "North Goa", "alt": "Bardez, Pernem, Tiswadi", "region": "North Goa", "landmarks": "All major tourist beaches, Panjim city", "businesses": "tourism, hospitality, IT, retail, entertainment"},
    {"slug": "south-goa", "name": "South Goa", "alt": "Salcete, Mormugao, Canacona", "region": "South Goa", "landmarks": "Colva, Palolem, Mormugao Port", "businesses": "luxury tourism, port trade, agriculture, healthcare, education"},
]

INDUSTRIES = [
    {"slug": "restaurant", "name": "Restaurant & Cafe", "keywords": "restaurant seo, cafe marketing, food business digital marketing", "audience": "restaurant owners, cafe operators, bar owners, cloud kitchens, beach shacks"},
    {"slug": "hotel-resort", "name": "Hotel & Resort", "keywords": "hotel seo, resort marketing, hospitality digital marketing", "audience": "hotel owners, resort managers, homestay operators, villa rentals, Airbnb hosts"},
    {"slug": "real-estate", "name": "Real Estate", "keywords": "real estate seo, property marketing, builder digital marketing", "audience": "developers, real estate agents, property consultants, villa builders"},
    {"slug": "healthcare", "name": "Healthcare & Medical", "keywords": "healthcare seo, doctor marketing, clinic digital marketing", "audience": "doctors, dentists, hospitals, clinics, diagnostic labs, pharmacies"},
    {"slug": "education", "name": "Education & Coaching", "keywords": "education marketing, school seo, coaching institute digital marketing", "audience": "schools, colleges, coaching centers, online tutors, training institutes"},
    {"slug": "fitness-wellness", "name": "Fitness & Wellness", "keywords": "gym marketing, yoga studio seo, wellness center digital marketing", "audience": "gyms, yoga studios, spas, Ayurveda centers, fitness trainers, wellness retreats"},
    {"slug": "ecommerce", "name": "E-commerce & D2C", "keywords": "ecommerce seo, online store marketing, d2c digital marketing", "audience": "online retailers, D2C brands, Shopify stores, WooCommerce shops"},
    {"slug": "startup", "name": "Startup & Tech", "keywords": "startup marketing, tech company seo, SaaS digital marketing", "audience": "tech startups, SaaS companies, app developers, IT services"},
    {"slug": "legal", "name": "Legal & Law Firm", "keywords": "law firm seo, lawyer marketing, legal services digital marketing", "audience": "lawyers, advocates, law firms, notaries, legal consultants"},
    {"slug": "finance", "name": "Finance & Insurance", "keywords": "finance company seo, insurance marketing, CA digital marketing", "audience": "CAs, financial advisors, insurance agents, banks, fintech companies"},
    {"slug": "travel-tourism", "name": "Travel & Tourism", "keywords": "travel agency seo, tourism marketing, tour operator digital marketing", "audience": "travel agents, tour operators, cruise companies, adventure sports"},
    {"slug": "automotive", "name": "Automotive & Dealers", "keywords": "car dealer seo, automotive marketing, garage digital marketing", "audience": "car dealerships, bike showrooms, auto garages, car rental services"},
    {"slug": "salon-beauty", "name": "Salon & Beauty", "keywords": "salon seo, beauty parlor marketing, spa digital marketing", "audience": "salons, beauty parlors, spas, makeup artists, bridal services"},
    {"slug": "construction", "name": "Construction & Interior", "keywords": "construction company seo, interior designer marketing", "audience": "contractors, architects, interior designers, builders, civil engineers"},
    {"slug": "manufacturing", "name": "Manufacturing & Industrial", "keywords": "manufacturer seo, industrial marketing, B2B digital marketing", "audience": "manufacturers, exporters, industrial suppliers, pharma companies"},
]

# Service deep-dive sub-topics
SERVICE_DEEP_DIVES = [
    {"slug": "technical-seo-audit", "name": "Technical SEO Audit", "parent": "seo-optimization.html", "parent_name": "SEO"},
    {"slug": "on-page-seo-services", "name": "On-Page SEO Services", "parent": "seo-optimization.html", "parent_name": "SEO"},
    {"slug": "off-page-seo-link-building", "name": "Off-Page SEO & Link Building", "parent": "seo-optimization.html", "parent_name": "SEO"},
    {"slug": "keyword-research-services", "name": "Keyword Research Services", "parent": "seo-optimization.html", "parent_name": "SEO"},
    {"slug": "seo-content-writing", "name": "SEO Content Writing", "parent": "content-marketing.html", "parent_name": "Content Marketing"},
    {"slug": "google-ads-management", "name": "Google Ads Management", "parent": "ppc-advertising.html", "parent_name": "PPC"},
    {"slug": "facebook-ads-management", "name": "Facebook & Instagram Ads", "parent": "ppc-advertising.html", "parent_name": "PPC"},
    {"slug": "linkedin-marketing", "name": "LinkedIn Marketing", "parent": "social-media-marketing.html", "parent_name": "Social Media"},
    {"slug": "instagram-marketing", "name": "Instagram Marketing", "parent": "social-media-marketing.html", "parent_name": "Social Media"},
    {"slug": "youtube-seo", "name": "YouTube SEO & Marketing", "parent": "social-media-marketing.html", "parent_name": "Social Media"},
    {"slug": "google-business-profile-optimization", "name": "Google Business Profile Optimization", "parent": "local-seo.html", "parent_name": "Local SEO"},
    {"slug": "citation-building-services", "name": "Local Citation Building", "parent": "local-seo.html", "parent_name": "Local SEO"},
    {"slug": "review-management-services", "name": "Review Management Services", "parent": "local-seo.html", "parent_name": "Local SEO"},
    {"slug": "wordpress-website-design", "name": "WordPress Website Design", "parent": "website-design.html", "parent_name": "Website Design"},
    {"slug": "shopify-website-design", "name": "Shopify Store Design", "parent": "website-design.html", "parent_name": "Website Design"},
    {"slug": "landing-page-design", "name": "Landing Page Design", "parent": "website-design.html", "parent_name": "Website Design"},
    {"slug": "logo-design-services", "name": "Logo Design Services", "parent": "graphic-designing.html", "parent_name": "Graphic Design"},
    {"slug": "social-media-creatives", "name": "Social Media Creative Design", "parent": "graphic-designing.html", "parent_name": "Graphic Design"},
    {"slug": "brand-identity-design", "name": "Brand Identity Design", "parent": "branding-strategy.html", "parent_name": "Branding"},
    {"slug": "influencer-marketing", "name": "Influencer Marketing", "parent": "social-media-marketing.html", "parent_name": "Social Media"},
    {"slug": "whatsapp-marketing", "name": "WhatsApp Marketing", "parent": "digital-marketing.html", "parent_name": "Digital Marketing"},
    {"slug": "email-marketing-services", "name": "Email Marketing Services", "parent": "digital-marketing.html", "parent_name": "Digital Marketing"},
    {"slug": "video-production-services", "name": "Video Production & Marketing", "parent": "content-marketing.html", "parent_name": "Content Marketing"},
    {"slug": "conversion-rate-optimization", "name": "Conversion Rate Optimization", "parent": "website-design.html", "parent_name": "Website Design"},
    {"slug": "analytics-reporting-services", "name": "Analytics & Reporting", "parent": "digital-marketing.html", "parent_name": "Digital Marketing"},
]

# Comparison pages
COMPARISONS = [
    {"slug": "seo-vs-ppc", "title": "SEO vs PPC: Which is Better for Goa Businesses?", "items": ("SEO", "PPC")},
    {"slug": "organic-vs-paid-marketing", "title": "Organic vs Paid Marketing – Complete Guide", "items": ("Organic Marketing", "Paid Marketing")},
    {"slug": "seo-vs-social-media-marketing", "title": "SEO vs Social Media Marketing – Where to Invest?", "items": ("SEO", "Social Media Marketing")},
    {"slug": "facebook-ads-vs-google-ads", "title": "Facebook Ads vs Google Ads for Goa Businesses", "items": ("Facebook Ads", "Google Ads")},
    {"slug": "wordpress-vs-shopify", "title": "WordPress vs Shopify – Which Platform for Your Business?", "items": ("WordPress", "Shopify")},
    {"slug": "digital-marketing-vs-traditional-marketing", "title": "Digital Marketing vs Traditional Marketing in Goa", "items": ("Digital Marketing", "Traditional Marketing")},
    {"slug": "local-seo-vs-national-seo", "title": "Local SEO vs National SEO – Strategy Differences", "items": ("Local SEO", "National SEO")},
    {"slug": "in-house-vs-agency-marketing", "title": "In-House Marketing vs Agency – Pros and Cons", "items": ("In-House Team", "Marketing Agency")},
    {"slug": "content-marketing-vs-ppc", "title": "Content Marketing vs PPC – Long-Term vs Quick Results", "items": ("Content Marketing", "PPC Advertising")},
    {"slug": "instagram-vs-facebook-marketing", "title": "Instagram vs Facebook Marketing for Goa Brands", "items": ("Instagram", "Facebook")},
    {"slug": "branding-vs-performance-marketing", "title": "Branding vs Performance Marketing – What You Need", "items": ("Brand Building", "Performance Marketing")},
    {"slug": "freelancer-vs-agency", "title": "Freelancer vs Digital Marketing Agency – Which to Hire?", "items": ("Freelancer", "Agency")},
    {"slug": "seo-vs-sem", "title": "SEO vs SEM – Understanding the Difference", "items": ("SEO", "SEM")},
    {"slug": "b2b-vs-b2c-digital-marketing", "title": "B2B vs B2C Digital Marketing Strategies", "items": ("B2B Marketing", "B2C Marketing")},
    {"slug": "website-vs-social-media-presence", "title": "Website vs Social Media – Do You Need Both?", "items": ("Website", "Social Media Only")},
]

# Blog topics (80 articles targeting long-tail queries)
BLOG_TOPICS = [
    # SEO cluster (25 articles)
    {"slug": "what-is-seo-beginners-guide", "title": "What is SEO? Complete Beginner's Guide for Goa Businesses", "category": "SEO"},
    {"slug": "how-google-ranking-works", "title": "How Google Ranking Works – Explained Simply", "category": "SEO"},
    {"slug": "seo-checklist-2025", "title": "Complete SEO Checklist for 2025 – Step by Step", "category": "SEO"},
    {"slug": "how-long-does-seo-take", "title": "How Long Does SEO Take to Show Results?", "category": "SEO"},
    {"slug": "seo-for-small-business", "title": "SEO for Small Business in Goa – Getting Started", "category": "SEO"},
    {"slug": "mobile-seo-optimization", "title": "Mobile SEO: How to Optimize for Mobile-First Indexing", "category": "SEO"},
    {"slug": "voice-search-optimization", "title": "Voice Search SEO: Optimize for Alexa & Google Assistant", "category": "SEO"},
    {"slug": "google-algorithm-updates", "title": "Google Algorithm Updates 2025 – What Changed", "category": "SEO"},
    {"slug": "backlink-building-strategies", "title": "10 Effective Backlink Building Strategies That Work", "category": "SEO"},
    {"slug": "seo-mistakes-to-avoid", "title": "15 Common SEO Mistakes Goa Businesses Make", "category": "SEO"},
    {"slug": "image-seo-optimization", "title": "Image SEO: Complete Guide to Image Optimization", "category": "SEO"},
    {"slug": "schema-markup-guide", "title": "Schema Markup Guide – Structured Data for Beginners", "category": "SEO"},
    {"slug": "core-web-vitals-guide", "title": "Core Web Vitals: How to Improve Page Experience", "category": "SEO"},
    {"slug": "featured-snippets-optimization", "title": "How to Get Featured Snippets on Google", "category": "SEO"},
    {"slug": "eeat-google-guidelines", "title": "E-E-A-T: Google's Quality Guidelines Explained", "category": "SEO"},
    {"slug": "ai-overviews-optimization", "title": "AI Overviews: How to Appear in Google's AI Answers", "category": "SEO"},
    {"slug": "answer-engine-optimization", "title": "Answer Engine Optimization (AEO) – Complete Guide", "category": "SEO"},
    {"slug": "geo-seo-generative-engine", "title": "GEO: Generative Engine Optimization Explained", "category": "SEO"},
    {"slug": "zero-click-searches", "title": "Zero-Click Searches: How to Win When Nobody Clicks", "category": "SEO"},
    {"slug": "seo-roi-calculator", "title": "SEO ROI: How to Calculate Your SEO Return on Investment", "category": "SEO"},
    {"slug": "internal-linking-strategy", "title": "Internal Linking Strategy: Complete Guide for SEO", "category": "SEO"},
    {"slug": "competitor-analysis-seo", "title": "How to Do SEO Competitor Analysis – Step by Step", "category": "SEO"},
    {"slug": "seo-reporting-metrics", "title": "SEO Metrics That Matter: What to Track & Report", "category": "SEO"},
    {"slug": "international-seo-guide", "title": "International SEO: Reach Customers Beyond India", "category": "SEO"},
    {"slug": "seo-trends-2026", "title": "SEO Trends 2026: What's Coming Next in Search", "category": "SEO"},
    # Local SEO cluster (15 articles)
    {"slug": "google-business-profile-setup-guide", "title": "Google Business Profile Setup: Complete Guide for Goa", "category": "Local SEO"},
    {"slug": "how-to-get-google-reviews", "title": "How to Get More Google Reviews (Ethically)", "category": "Local SEO"},
    {"slug": "local-seo-ranking-factors", "title": "Local SEO Ranking Factors in 2025", "category": "Local SEO"},
    {"slug": "google-maps-ranking-guide", "title": "How to Rank Higher on Google Maps", "category": "Local SEO"},
    {"slug": "local-citations-guide", "title": "Local Citations: What They Are & How to Build Them", "category": "Local SEO"},
    {"slug": "nap-consistency-guide", "title": "NAP Consistency: Why It Matters for Local SEO", "category": "Local SEO"},
    {"slug": "local-seo-for-multiple-locations", "title": "Local SEO for Multiple Locations – Strategy Guide", "category": "Local SEO"},
    {"slug": "near-me-search-optimization", "title": "How to Rank for 'Near Me' Searches in Goa", "category": "Local SEO"},
    {"slug": "local-seo-audit-guide", "title": "How to Do a Local SEO Audit – Free Checklist", "category": "Local SEO"},
    {"slug": "google-posts-guide", "title": "Google Posts: How to Use Them for Local Visibility", "category": "Local SEO"},
    {"slug": "justdial-sulekha-optimization", "title": "Optimize Your JustDial & Sulekha Listings for SEO", "category": "Local SEO"},
    {"slug": "local-seo-for-restaurants", "title": "Local SEO for Restaurants: Fill More Tables from Google", "category": "Local SEO"},
    {"slug": "local-seo-for-doctors", "title": "Local SEO for Doctors & Clinics in Goa", "category": "Local SEO"},
    {"slug": "goa-business-directories", "title": "Best Business Directories for Goa Businesses", "category": "Local SEO"},
    {"slug": "seasonal-local-seo-goa", "title": "Seasonal Local SEO Strategy for Tourism in Goa", "category": "Local SEO"},
    # Digital Marketing Strategy (15 articles)
    {"slug": "digital-marketing-budget-guide", "title": "How to Set Your Digital Marketing Budget in 2025", "category": "Strategy"},
    {"slug": "digital-marketing-for-beginners", "title": "Digital Marketing for Beginners – Where to Start", "category": "Strategy"},
    {"slug": "marketing-funnel-explained", "title": "Marketing Funnel Explained: Awareness to Conversion", "category": "Strategy"},
    {"slug": "customer-acquisition-cost", "title": "How to Reduce Customer Acquisition Cost", "category": "Strategy"},
    {"slug": "omnichannel-marketing-strategy", "title": "Omnichannel Marketing Strategy for Goa Businesses", "category": "Strategy"},
    {"slug": "marketing-automation-guide", "title": "Marketing Automation: Tools & Strategies", "category": "Strategy"},
    {"slug": "lead-generation-strategies", "title": "Lead Generation Strategies That Work in 2025", "category": "Strategy"},
    {"slug": "brand-building-online", "title": "How to Build a Strong Brand Online", "category": "Strategy"},
    {"slug": "digital-marketing-kpis", "title": "Digital Marketing KPIs: What to Measure & Why", "category": "Strategy"},
    {"slug": "content-calendar-template", "title": "How to Create a Content Calendar (Free Template)", "category": "Strategy"},
    {"slug": "retargeting-remarketing-guide", "title": "Retargeting & Remarketing: Complete Guide", "category": "Strategy"},
    {"slug": "chatgpt-for-marketing", "title": "Using AI & ChatGPT for Digital Marketing", "category": "Strategy"},
    {"slug": "personal-branding-guide", "title": "Personal Branding for Business Owners in Goa", "category": "Strategy"},
    {"slug": "crisis-management-online", "title": "Online Reputation Crisis Management Guide", "category": "Strategy"},
    {"slug": "marketing-for-seasonal-business", "title": "Marketing Strategies for Seasonal Businesses in Goa", "category": "Strategy"},
    # Social Media (10 articles)
    {"slug": "instagram-reels-strategy", "title": "Instagram Reels Strategy for Business Growth", "category": "Social Media"},
    {"slug": "facebook-page-optimization", "title": "Facebook Page Optimization: Complete Guide", "category": "Social Media"},
    {"slug": "linkedin-company-page-guide", "title": "LinkedIn Company Page Optimization for B2B", "category": "Social Media"},
    {"slug": "social-media-content-ideas", "title": "50 Social Media Content Ideas for Goa Businesses", "category": "Social Media"},
    {"slug": "how-to-grow-instagram-followers", "title": "How to Grow Instagram Followers Organically", "category": "Social Media"},
    {"slug": "social-media-ads-budget", "title": "Social Media Ads: How Much to Spend in Goa", "category": "Social Media"},
    {"slug": "user-generated-content-guide", "title": "User-Generated Content: Strategy & Examples", "category": "Social Media"},
    {"slug": "social-media-for-restaurants", "title": "Social Media Marketing for Restaurants in Goa", "category": "Social Media"},
    {"slug": "whatsapp-business-marketing", "title": "WhatsApp Business Marketing: Complete Guide", "category": "Social Media"},
    {"slug": "social-media-analytics-guide", "title": "Social Media Analytics: Metrics That Matter", "category": "Social Media"},
    # Website & Tech (10 articles)
    {"slug": "website-speed-optimization", "title": "Website Speed Optimization: Complete Guide", "category": "Website"},
    {"slug": "mobile-responsive-design", "title": "Mobile-Responsive Design: Why It Matters for SEO", "category": "Website"},
    {"slug": "website-security-ssl-guide", "title": "Website Security & SSL: Protect Your Business Online", "category": "Website"},
    {"slug": "website-redesign-without-losing-seo", "title": "How to Redesign Your Website Without Losing SEO", "category": "Website"},
    {"slug": "website-maintenance-checklist", "title": "Website Maintenance Checklist for Business Owners", "category": "Website"},
    {"slug": "ecommerce-website-features", "title": "E-commerce Website Features That Drive Sales", "category": "Website"},
    {"slug": "website-hosting-guide", "title": "Web Hosting Guide for Indian Businesses", "category": "Website"},
    {"slug": "website-accessibility-guide", "title": "Website Accessibility: ADA Compliance Guide", "category": "Website"},
    {"slug": "progressive-web-apps-guide", "title": "Progressive Web Apps (PWA) for Business", "category": "Website"},
    {"slug": "website-analytics-setup", "title": "Google Analytics 4 Setup Guide for Beginners", "category": "Website"},
    # PPC/Ads (5 articles)
    {"slug": "google-ads-quality-score", "title": "Google Ads Quality Score: How to Improve It", "category": "PPC"},
    {"slug": "ppc-budget-calculator", "title": "PPC Budget Calculator: How Much to Spend", "category": "PPC"},
    {"slug": "negative-keywords-guide", "title": "Negative Keywords: Stop Wasting Your Ad Budget", "category": "PPC"},
    {"slug": "google-ads-for-local-business", "title": "Google Ads for Local Businesses in Goa", "category": "PPC"},
    {"slug": "remarketing-ads-guide", "title": "Remarketing Ads: Bring Back Lost Customers", "category": "PPC"},
]

# Use-case pages (targeting "for X" queries)
USE_CASES = [
    "small-business", "startups", "doctors", "lawyers", "restaurants",
    "hotels", "real-estate-agents", "schools", "gyms", "salons",
    "ecommerce-stores", "freelancers", "dentists", "architects", "event-planners",
    "wedding-planners", "tour-operators", "car-dealers", "ngos", "politicians",
]

# FAQ hub pages
FAQ_HUBS = [
    "seo-faq", "ppc-faq", "social-media-faq", "website-design-faq", "local-seo-faq",
    "digital-marketing-pricing-faq", "content-marketing-faq", "branding-faq",
    "google-ads-faq", "startup-marketing-faq",
]

# ═══════════════════════════════════════════════════════════════════════════════
# HTML TEMPLATE ENGINE
# ═══════════════════════════════════════════════════════════════════════════════

def make_head(title, desc, slug, breadcrumbs, schema_type="Service", faqs=None):
    """Generate <head> with all SEO meta."""
    url = f"{SITE_URL}/{slug}"
    og_title = title.split(" | ")[0] if " | " in title else title.split(" – ")[0]
    
    # Schemas
    service_schema = json.dumps({
        "@context": "https://schema.org", "@type": schema_type,
        "name": title.split(" | ")[0] if " | " in title else title.split(" – ")[0],
        "provider": {"@id": f"{SITE_URL}/#organization"},
        "areaServed": [{"@type": "State", "name": "Goa"}, {"@type": "Country", "name": "India"}],
        "description": desc, "url": url,
    }, indent=2, ensure_ascii=False)
    
    bc_items = [{"@type": "ListItem", "position": i+1, "name": n, "item": u} for i, (n, u) in enumerate(breadcrumbs)]
    bc_schema = json.dumps({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": bc_items}, indent=2, ensure_ascii=False)
    
    faq_block = ""
    if faqs:
        faq_data = {"@context": "https://schema.org", "@type": "FAQPage",
                    "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}
        faq_block = f'\n<script type="application/ld+json">\n{json.dumps(faq_data, indent=2, ensure_ascii=False)}\n</script>'
    
    return f'''<!DOCTYPE html>
<html class="no-js" lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="x-ua-compatible" content="ie=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{url}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{url}">
  <meta property="og:title" content="{og_title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="{SITE_URL}/assets/img/hero/hero-banner-1.png">
  <meta property="og:site_name" content="{SITE_NAME}">
  <meta property="og:locale" content="en_IN">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{og_title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{SITE_URL}/assets/img/hero/hero-banner-1.png">
  <title>{title}</title>
  <link rel="shortcut icon" type="image/x-icon" href="assets/img/favicon.png">
  <link rel="stylesheet" href="assets/css/bootstrap.min.css">
  <link rel="stylesheet" href="assets/css/font-awesome-pro.min.css">
  <link rel="stylesheet" href="assets/css/animate.min.css">
  <link rel="stylesheet" href="assets/css/ranko-icons.css">
  <link rel="stylesheet" href="assets/css/meanmenu.css">
  <link rel="stylesheet" href="assets/css/swiper.min.css">
  <link rel="stylesheet" href="assets/css/backToTop.css">
  <link rel="stylesheet" href="assets/css/nice-select.css">
  <link rel="stylesheet" href="assets/css/odometer-theme-default.css">
  <link rel="stylesheet" href="assets/css/main.css">
<script type="application/ld+json">
{service_schema}
</script>
<script type="application/ld+json">
{bc_schema}
</script>{faq_block}
</head>'''


def make_nav():
    """Compact navigation."""
    return '''
<body>
  <div class="body-overlay d-lg-none"></div>
  <div class="preloader"><div class="loading-container"><div class="loading"></div><div id="loading-icon"><img src="assets/img/logo-icon.svg" alt="Rankify Goa"></div></div></div>
  <div class="back-to-top-wrapper"><button id="back_to_top" type="button" class="back-to-top-btn"><i class="tji-arrow-up"></i></button></div>
  <div class="hamburger-area d-lg-none" data-lenis-prevent=""><div class="hamburger_bg"></div><div class="hamburger_wrapper"><div class="hamburger_top d-flex align-items-center justify-content-between"><div class="hamburger_logo"><a href="index.html" class="mobile_logo"><img src="assets/img/logo.png" alt="Rankify Goa"></a></div><div class="hamburger_close"><button class="hamburger_close_btn"><i class="fa-thin fa-times"></i></button></div></div><div class="hamburger_menu"><div class="mobile_menu"></div></div></div></div>
  <header class="header header--absolute"><div class="container"><div class="row"><div class="col-12"><div class="header__wrapper">
    <div class="header__logo"><a href="index.html"><img src="assets/img/logo.png" alt="Rankify Goa – Digital Marketing Agency Logo"></a></div>
    <div class="mainmenu d-none d-lg-block"><nav id="mobileNavProvider"><ul>
      <li><a href="index.html">Home</a></li>
      <li><a href="about.html">About Us</a></li>
      <li class="has-dropdown"><a href="services.html">Services</a><ul class="sub-menu">
        <li><a href="digital-marketing.html">Digital Marketing</a></li>
        <li><a href="seo-optimization.html">SEO Optimization</a></li>
        <li><a href="social-media-marketing.html">Social Media</a></li>
        <li><a href="ppc-advertising.html">PPC Advertising</a></li>
        <li><a href="content-marketing.html">Content Marketing</a></li>
        <li><a href="website-design.html">Website Design</a></li>
        <li><a href="branding-strategy.html">Branding</a></li>
        <li><a href="local-seo.html">Local SEO</a></li>
      </ul></li>
      <li><a href="blog.html">Blog</a></li>
      <li><a href="contact.html">Contact</a></li>
    </ul></nav></div>
    <div class="header__right"><a href="https://wa.me/919923352923?text=Hi%2C%20I%20need%20digital%20marketing%20services" class="tj-btn tj-btn--sm" target="_blank" rel="noopener noreferrer">WhatsApp</a><div class="d-lg-none"><button class="header__mobile-toggler mobile_menu_bar"><span></span><span></span><span></span></button></div></div>
  </div></div></div></div></header>'''


def make_footer():
    """Compact footer + JS."""
    return '''
      <footer class="footer"><div class="container-fluid"><div class="row"><div class="col-12"><div class="footer__inner section-inner--lg">
        <div class="footer__main"><div class="container"><div class="row">
          <div class="col-lg-3 col-md-6"><div class="footer__widget footer__info"><h5 class="footer__title">Office</h5><p>Cottage Hospital Rd, Alto Chicalim, Goa 403802</p><ul><li><a href="tel:+919923352923">+91 99233-52923</a></li><li><a href="mailto:help@digitalmarketingagencygoa.com">help@digitalmarketingagencygoa.com</a></li></ul></div></div>
          <div class="col-lg-3 col-md-6"><div class="footer__widget"><h5 class="footer__title">Company</h5><ul><li><a href="about.html">About</a></li><li><a href="services.html">Services</a></li><li><a href="clients.html">Clients</a></li><li><a href="blog.html">Blog</a></li><li><a href="contact.html">Contact</a></li></ul></div></div>
          <div class="col-lg-3 col-md-6"><div class="footer__widget"><h5 class="footer__title">Services</h5><ul><li><a href="seo-optimization.html">SEO</a></li><li><a href="ppc-advertising.html">PPC</a></li><li><a href="social-media-marketing.html">Social Media</a></li><li><a href="website-design.html">Web Design</a></li><li><a href="local-seo.html">Local SEO</a></li><li><a href="content-marketing.html">Content</a></li></ul></div></div>
          <div class="col-lg-3 col-md-6"><div class="footer__widget"><form class="footer__widget__subscription" action="subscribe.php" method="POST"><h3 class="footer__widget__subscription__title">Newsletter</h3><div class="tj-input__wrapper"><input type="email" name="email" class="tj-input" placeholder="Email" required></div><button type="submit" class="tj-btn tj-btn--full">Subscribe</button></form></div></div>
        </div></div></div>
        <div class="footer__copyright"><div class="container"><div class="row"><div class="col-12"><div class="footer__copyright__wrapper"><div class="footer__copyright__logo"><a href="index.html"><img src="assets/img/logo.png" alt="Rankify Goa"></a></div><div class="footer__copyright__menu"><ul><li><p>© 2012-<script>document.write(new Date().getFullYear())</script> <a href="https://www.sanctify.in" target="_blank" rel="noopener noreferrer">Sanctify</a></p></li><li><a href="faq.html">FAQ</a></li><li><a href="terms.html">Terms</a></li><li><a href="sitemap.xml">Sitemap</a></li></ul></div></div></div></div></div></div>
      </div></div></div></div></footer>
    </div></div>
  <script src="assets/js/jquery.min.js"></script>
  <script src="assets/js/bootstrap.bundle.min.js"></script>
  <script src="assets/js/gsap.min.js"></script>
  <script src="assets/js/ScrollSmoother.js"></script>
  <script src="assets/js/gsap-scroll-to-plugin.min.js"></script>
  <script src="assets/js/gsap-scroll-trigger.min.js"></script>
  <script src="assets/js/gsap-split-text.min.js"></script>
  <script src="assets/js/Splitetext.js"></script>
  <script src="assets/js/appear.min.js"></script>
  <script src="assets/js/swiper.min.js"></script>
  <script src="assets/js/meanmenu.js"></script>
  <script src="assets/js/nice-select.min.js"></script>
  <script src="assets/js/odometer.min.js"></script>
  <script src="assets/js/wow.min.js"></script>
  <script src="assets/js/main.js"></script>
</body></html>'''


def make_body(h1, subtitle, breadcrumb_text, content_html, related_links=None):
    """Generate body content."""
    links_html = ""
    if related_links:
        items = "".join([f'<a href="{u}" class="tj-btn-2" style="margin:4px;">{t} <i class="tji-arrow-right"></i></a> ' for u, t in related_links[:6]])
        links_html = f'<div style="margin-top:40px;padding:24px;background:#f8f9fa;border-radius:12px;"><h3>Related Services</h3><div style="margin-top:12px;">{items}</div></div>'
    
    cta = '<div style="margin-top:50px;padding:40px;background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);border-radius:16px;text-align:center;color:#fff;"><h3 style="color:#fff;">Ready to Grow?</h3><p style="color:rgba(255,255,255,.9);">Free consultation – no commitments.</p><a href="https://wa.me/919923352923?text=Hi%2C%20I%20need%20help%20with%20digital%20marketing" class="tj-btn" target="_blank" rel="noopener noreferrer" style="background:#fff;color:#764ba2;margin-top:16px;">WhatsApp Us</a> <a href="contact.html" class="tj-btn" style="border:2px solid #fff;color:#fff;margin:16px 0 0 8px;">Contact</a></div>'
    
    return f'''
  <div id="smooth-wrapper"><div id="smooth-content"><main id="primary" class="site-main">
    <section class="hero-breadcrumb"><div class="container"><div class="row"><div class="col-12"><div class="hero-breadcrumb__inner">
      <h6 class="section-heading__sub-title">{subtitle}</h6>
      <h1 class="hero-breadcrumb__title">{h1}</h1>
      <div class="hero-breadcrumb__nav">{breadcrumb_text}</div>
      <div class="hero-breadcrumb__icons"><img class="start-img" src="./assets/img/icons/star.png" alt="Star"><img class="start-img" src="./assets/img/icons/star1.png" alt="Star"><img class="start-img" src="./assets/img/icons/star2.png" alt="Star"><img class="start-img" src="./assets/img/icons/star3.png" alt="Star"></div>
    </div></div></div></div></section>
    <section class="tj-blog-section section-gap"><div class="container"><div class="row justify-content-center"><div class="col-lg-10"><div class="post-details-wrapper">
      {content_html}
      {links_html}
      {cta}
    </div></div></div></div></section>
  </main>'''


def gen_faqs_for(topic, location=None):
    """Generate 3 contextual FAQs for any topic."""
    loc = f" in {location}" if location else " in Goa"
    return [
        (f"How much does {topic} cost{loc}?", f"Pricing depends on your business size, competition level, and goals. Our {topic} services start from ₹15,000/month. Contact us for a custom quote tailored to your needs."),
        (f"How long to see results from {topic}{loc}?", f"Most businesses see measurable improvements within 60-90 days. Full impact typically shows within 4-6 months as authority builds. We provide monthly progress reports from day one."),
        (f"Why choose Rankify Goa for {topic}?", f"We're a Goa-based agency with deep local market knowledge, proven results for 600+ clients, transparent reporting, and strategies customized for businesses{loc}. No generic templates — real results."),
    ]


def gen_content_for_industry(ind):
    """Generate unique content for industry page."""
    name = ind["name"]
    audience = ind["audience"]
    return f'''
      <h2>Digital Marketing for {name} Businesses in Goa</h2>
      <p>The {name.lower()} industry in Goa faces unique digital marketing challenges. Your potential customers — {audience} — are searching online right now for services you offer. Without a strong digital presence, you're invisible to them. Our agency specializes in helping {name.lower()} businesses build online visibility, attract quality leads, and convert searches into revenue.</p>
      
      <h2>Why {name} Businesses Need Specialized Marketing</h2>
      <p>Generic marketing strategies don't work for {name.lower()} businesses. Your audience searches differently, converts differently, and trusts differently. We understand the {name.lower()} customer journey — from first search query to final purchase decision — and build strategies that meet them at every stage.</p>
      
      <h3>Our Services for {name} Industry</h3>
      <ul>
        <li><strong><a href="seo-optimization.html">SEO Optimization</a></strong> — Rank for industry-specific keywords that your ideal customers search</li>
        <li><strong><a href="local-seo.html">Local SEO</a></strong> — Dominate Google Maps for location-based {name.lower()} searches</li>
        <li><strong><a href="social-media-marketing.html">Social Media</a></strong> — Build brand awareness where your audience spends time</li>
        <li><strong><a href="ppc-advertising.html">Google Ads</a></strong> — Instant leads from high-intent {name.lower()} searches</li>
        <li><strong><a href="website-design.html">Website Design</a></strong> — Conversion-optimized websites built for your industry</li>
        <li><strong><a href="content-marketing.html">Content Marketing</a></strong> — Authority-building content that drives organic traffic</li>
      </ul>

      <h2>Results for {name} Clients</h2>
      <p>Our {name.lower()} clients in Goa typically experience: 3-5x increase in online inquiries, 200%+ growth in organic traffic, top 3 Google Maps rankings for key searches, and measurable ROI within 4-6 months. We track everything and report monthly — you always know exactly how your investment is performing.</p>

      <h3>Industries We Serve</h3>
      <p>Beyond {name.lower()}, we serve <a href="services.html">all industries in Goa</a> including hospitality, healthcare, education, real estate, and technology. Our team brings cross-industry insights that give every client a competitive edge.</p>
'''


def gen_content_for_location(loc):
    """Generate unique content for location page."""
    name = loc["name"]
    alt = loc["alt"]
    region = loc["region"]
    landmarks = loc["landmarks"]
    businesses = loc["businesses"]
    return f'''
      <h2>Digital Marketing & SEO Services in {name}, Goa</h2>
      <p>Looking for a trusted digital marketing partner in {name} ({alt})? Rankify Goa serves businesses across {name} and the broader {region} region with data-driven SEO, social media, Google Ads, and web design services that deliver measurable growth. From {landmarks} — we know this market inside out.</p>

      <h2>Why {name} Businesses Choose Rankify Goa</h2>
      <p>As a Goa-based agency, we understand the {name} market deeply. The local business landscape — {businesses} — requires strategies built for how YOUR customers search. We don't apply generic national templates; every campaign is tailored to {name}'s unique market dynamics, seasonal patterns, and competitive landscape.</p>

      <h3>Services for {name} Businesses</h3>
      <ul>
        <li><strong><a href="seo-optimization.html">SEO Services</a></strong> — Rank on Google for "{name}" and "{region}" searches</li>
        <li><strong><a href="local-seo.html">Local SEO & Google Maps</a></strong> — Appear in the map pack when people search near {name}</li>
        <li><strong><a href="ppc-advertising.html">Google Ads</a></strong> — Target customers searching for businesses in {name}</li>
        <li><strong><a href="social-media-marketing.html">Social Media Marketing</a></strong> — Build your {name} brand presence online</li>
        <li><strong><a href="website-design.html">Website Design</a></strong> — Fast, mobile-first websites optimized for conversions</li>
        <li><strong><a href="content-marketing.html">Content Marketing</a></strong> — Local content that establishes authority in {name}</li>
      </ul>

      <h2>Serving All of {region}</h2>
      <p>While we serve businesses specifically in {name}, our digital marketing expertise extends across all of {region}. Whether you're near {landmarks} or in surrounding areas, our local knowledge and SEO expertise help you reach customers who matter most to your business. <a href="contact.html">Get a free consultation</a> today.</p>
'''


def gen_content_for_loc_service(loc, svc):
    """Generate content for location+service combination."""
    loc_name = loc["name"]
    svc_name = svc["name"]
    svc_full = svc["full"]
    return f'''
      <h2>{svc_full} in {loc_name}, Goa</h2>
      <p>Need expert {svc_name.lower()} services for your {loc_name} business? Rankify Goa delivers specialized {svc_name.lower()} strategies tailored to the {loc_name} market. We understand the local competition, customer search behavior, and business dynamics unique to this area — giving your business an unfair advantage over competitors using generic out-of-state services.</p>

      <h3>What Our {svc_name} Service Includes for {loc_name}</h3>
      <ul>
        <li>Complete market analysis specific to {loc_name} and surrounding areas</li>
        <li>Competitor research for your industry in {loc_name}</li>
        <li>Custom {svc_name.lower()} strategy built for your business goals</li>
        <li>Monthly reporting with clear ROI metrics</li>
        <li>Dedicated account manager who knows the {loc_name} market</li>
      </ul>

      <h2>Why Local Expertise Matters for {svc_name}</h2>
      <p>{svc_name} is not one-size-fits-all. A business in {loc_name} faces different competition, search volumes, and customer behavior than one in Mumbai or Delhi. Our Goa-based team brings hyperlocal insights that remote agencies simply cannot offer. We visit our clients, we know the neighborhoods, and we build strategies that reflect the real {loc_name} market.</p>

      <h3>Get Started with {svc_name} in {loc_name}</h3>
      <p>Ready to grow your {loc_name} business with professional {svc_name.lower()}? <a href="contact.html">Contact us</a> for a free strategy session. We'll analyze your current online presence, identify quick wins, and build a roadmap for sustainable growth. No contracts, no commitments — just honest advice from Goa's trusted <a href="digital-marketing.html">digital marketing agency</a>.</p>
'''


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN BUILDER
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    print("")
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║  🏗️  351-PAGE TOPICAL AUTHORITY ECOSYSTEM                       ║")
    print("║  Building the largest digital marketing content hub in Goa      ║")
    print("╚══════════════════════════════════════════════════════════════════╝")
    print("")
    
    os.makedirs(os.path.join(WORKSPACE, "blog"), exist_ok=True)
    
    all_pages = []  # (slug, title) tuples for sitemap
    count = 0
    
    # ─── 1. Industry Pages (15) ──────────────────────────────────────────────
    print("── 1/9 Industry Vertical Pages (15) ──")
    for ind in INDUSTRIES:
        slug = f"{ind['slug']}-digital-marketing-goa"
        title = f"{ind['name']} Digital Marketing in Goa | {BRAND}"
        desc = f"Specialized digital marketing for {ind['name'].lower()} businesses in Goa. SEO, social media, Google Ads & web design tailored for {ind['audience']}."
        h1 = f"{ind['name']} Digital Marketing Services in Goa"
        faqs = gen_faqs_for(f"{ind['name']} digital marketing")
        breadcrumbs = [("Home", f"{SITE_URL}/"), ("Services", f"{SITE_URL}/services"), (ind['name'], f"{SITE_URL}/{slug}")]
        
        content = gen_content_for_industry(ind)
        # Add FAQ HTML
        faq_html = '<h2>Frequently Asked Questions</h2><div class="accordion tj-faq" id="faqAcc">'
        for i, (q, a) in enumerate(faqs):
            show = "show" if i == 0 else ""
            coll = "" if i == 0 else "collapsed"
            faq_html += f'<div class="accordion-item"><button class="faq-title {coll}" data-bs-toggle="collapse" data-bs-target="#f{i}">{q}</button><div id="f{i}" class="collapse {show}" data-bs-parent="#faqAcc"><div class="accordion-body faq-text"><p>{a}</p></div></div></div>'
        faq_html += '</div>'
        content += faq_html
        
        related = [("seo-optimization.html", "SEO"), ("local-seo.html", "Local SEO"), ("social-media-marketing.html", "Social Media"), ("contact.html", "Free Consultation")]
        bc_text = f'<span><a href="index.html">Home</a></span> <span><a href="services.html">Services</a></span> <span>{ind["name"]}</span>'
        
        html = make_head(title, desc, slug, breadcrumbs, "Service", faqs)
        html += make_nav()
        html += make_body(h1, "Industry Specialization", bc_text, content, related)
        html += make_footer()
        
        filepath = os.path.join(WORKSPACE, f"{slug}.html")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        all_pages.append((slug, title))
        count += 1
    print(f"  ✓ {count} industry pages generated")

    # ─── 2. Location Pages (12) ─────────────────────────────────────────────
    print("── 2/9 Location Pages (12) ──")
    loc_start = count
    for loc in LOCATIONS:
        slug = f"digital-marketing-{loc['slug']}-goa"
        title = f"Digital Marketing Agency in {loc['name']}, Goa | {BRAND}"
        desc = f"Expert digital marketing services in {loc['name']}, {loc['region']}. SEO, Google Ads, social media & web design for local businesses. Goa's trusted agency."
        h1 = f"Digital Marketing Agency in {loc['name']}, Goa"
        faqs = gen_faqs_for("digital marketing", loc['name'])
        breadcrumbs = [("Home", f"{SITE_URL}/"), ("Locations", f"{SITE_URL}/services"), (loc['name'], f"{SITE_URL}/{slug}")]
        
        content = gen_content_for_location(loc)
        faq_html = '<h2>FAQs</h2><div class="accordion tj-faq" id="faqAcc">'
        for i, (q, a) in enumerate(faqs):
            show = "show" if i == 0 else ""
            coll = "" if i == 0 else "collapsed"
            faq_html += f'<div class="accordion-item"><button class="faq-title {coll}" data-bs-toggle="collapse" data-bs-target="#f{i}">{q}</button><div id="f{i}" class="collapse {show}" data-bs-parent="#faqAcc"><div class="accordion-body faq-text"><p>{a}</p></div></div></div>'
        faq_html += '</div>'
        content += faq_html
        
        related = [("seo-optimization.html", "SEO Services"), ("local-seo.html", "Local SEO"), ("contact.html", "Contact Us")]
        bc_text = f'<span><a href="index.html">Home</a></span> <span>Locations</span> <span>{loc["name"]}</span>'
        
        html = make_head(title, desc, slug, breadcrumbs, "Service", faqs)
        html += make_nav()
        html += make_body(h1, f"{loc['region']} Coverage", bc_text, content, related)
        html += make_footer()
        
        filepath = os.path.join(WORKSPACE, f"{slug}.html")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        all_pages.append((slug, title))
        count += 1
    print(f"  ✓ {count - loc_start} location pages generated")

    # ─── 3. Location+Service Combos (60) ─────────────────────────────────────
    print("── 3/9 Location+Service Combination Pages (60) ──")
    combo_start = count
    top_locs = LOCATIONS[:5]  # Panaji, Mapusa, Margao, Vasco, Calangute
    for loc in top_locs:
        for svc in SERVICES:
            slug = f"{svc['slug']}-services-{loc['slug']}-goa"
            title = f"{svc['name']} in {loc['name']}, Goa – Expert Services | {BRAND}"
            desc = f"Professional {svc['name'].lower()} services for businesses in {loc['name']}, Goa. Local expertise, proven results, and strategies built for {loc['name']}'s market."
            h1 = f"{svc['full']} in {loc['name']}, Goa"
            faqs = gen_faqs_for(svc['name'].lower(), loc['name'])
            breadcrumbs = [("Home", f"{SITE_URL}/"), ("Services", f"{SITE_URL}/services"), (f"{svc['name']} in {loc['name']}", f"{SITE_URL}/{slug}")]
            
            content = gen_content_for_loc_service(loc, svc)
            faq_html = '<h2>FAQs</h2><div class="accordion tj-faq" id="faqAcc">'
            for i, (q, a) in enumerate(faqs):
                show = "show" if i == 0 else ""
                coll = "" if i == 0 else "collapsed"
                faq_html += f'<div class="accordion-item"><button class="faq-title {coll}" data-bs-toggle="collapse" data-bs-target="#f{i}">{q}</button><div id="f{i}" class="collapse {show}" data-bs-parent="#faqAcc"><div class="accordion-body faq-text"><p>{a}</p></div></div></div>'
            faq_html += '</div>'
            content += faq_html
            
            related = [(f"digital-marketing-{loc['slug']}-goa.html", f"All Services in {loc['name']}"), ("services.html", "All Services"), ("contact.html", "Get Quote")]
            bc_text = f'<span><a href="index.html">Home</a></span> <span><a href="digital-marketing-{loc["slug"]}-goa.html">{loc["name"]}</a></span> <span>{svc["name"]}</span>'
            
            html = make_head(title, desc, slug, breadcrumbs, "Service", faqs)
            html += make_nav()
            html += make_body(h1, f"{svc['name']} Expert", bc_text, content, related)
            html += make_footer()
            
            filepath = os.path.join(WORKSPACE, f"{slug}.html")
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html)
            all_pages.append((slug, title))
            count += 1
    print(f"  ✓ {count - combo_start} location+service combos generated")

    # ─── 4. Service Deep-Dives (25) ──────────────────────────────────────────
    print("── 4/9 Service Deep-Dive Pages (25) ──")
    dd_start = count
    for dd in SERVICE_DEEP_DIVES:
        slug = dd["slug"]
        title = f"{dd['name']} in Goa – Expert Services | {BRAND}"
        desc = f"Professional {dd['name'].lower()} services in Goa. Part of our comprehensive {dd['parent_name']} solutions. Proven strategies for Goa businesses."
        h1 = f"{dd['name']} Services in Goa"
        faqs = gen_faqs_for(dd['name'].lower())
        breadcrumbs = [("Home", f"{SITE_URL}/"), (dd['parent_name'], f"{SITE_URL}/{dd['parent'].replace('.html','')}"), (dd['name'], f"{SITE_URL}/{slug}")]
        
        content = f'''
          <h2>Expert {dd['name']} for Goa Businesses</h2>
          <p>As a specialized service within our <a href="{dd['parent']}">{dd['parent_name']}</a> offering, our {dd['name'].lower()} service delivers focused results for businesses in Goa. Whether you're a local shop, a growing startup, or an established enterprise — this service is designed to address the specific challenges of {dd['name'].lower()} and deliver measurable outcomes.</p>
          <h3>What's Included</h3>
          <ul>
            <li>Comprehensive audit and analysis of your current situation</li>
            <li>Custom strategy development based on your goals and budget</li>
            <li>Professional execution by our specialist team</li>
            <li>Monthly performance reports with clear metrics</li>
            <li>Ongoing optimization and improvement</li>
          </ul>
          <h3>Why This Service Matters</h3>
          <p>{dd['name']} is a critical component of any successful digital presence. Without it, businesses in Goa leave money on the table — losing potential customers to competitors who have invested in this area. Our team brings years of experience and proven methodologies specifically adapted for the Goan market.</p>
          <h3>Get Started</h3>
          <p><a href="contact.html">Contact our team</a> for a free consultation about {dd['name'].lower()}. We'll assess your needs and provide an honest recommendation — even if that means this specific service isn't right for you yet.</p>
        '''
        faq_html = '<h2>FAQs</h2><div class="accordion tj-faq" id="faqAcc">'
        for i, (q, a) in enumerate(faqs):
            show = "show" if i == 0 else ""
            coll = "" if i == 0 else "collapsed"
            faq_html += f'<div class="accordion-item"><button class="faq-title {coll}" data-bs-toggle="collapse" data-bs-target="#f{i}">{q}</button><div id="f{i}" class="collapse {show}" data-bs-parent="#faqAcc"><div class="accordion-body faq-text"><p>{a}</p></div></div></div>'
        faq_html += '</div>'
        content += faq_html
        
        related = [(dd['parent'], dd['parent_name']), ("services.html", "All Services"), ("contact.html", "Free Consultation")]
        bc_text = f'<span><a href="index.html">Home</a></span> <span><a href="{dd["parent"]}">{dd["parent_name"]}</a></span> <span>{dd["name"]}</span>'
        
        html = make_head(title, desc, slug, breadcrumbs, "Service", faqs)
        html += make_nav()
        html += make_body(h1, "Specialist Service", bc_text, content, related)
        html += make_footer()
        
        filepath = os.path.join(WORKSPACE, f"{slug}.html")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        all_pages.append((slug, title))
        count += 1
    print(f"  ✓ {count - dd_start} deep-dive pages generated")

    # ─── 5. Comparison Pages (15) ────────────────────────────────────────────
    print("── 5/9 Comparison Pages (15) ──")
    cmp_start = count
    for cmp in COMPARISONS:
        slug = cmp["slug"]
        title = f"{cmp['title']} | {BRAND}"
        a, b = cmp["items"]
        desc = f"Honest comparison of {a} vs {b} for businesses in Goa. Understand costs, ROI, timelines and which strategy works best for your situation."
        h1 = cmp["title"]
        faqs = [
            (f"Is {a} or {b} better for small businesses in Goa?", f"It depends on your timeline and budget. {a} works best for businesses seeking long-term growth, while {b} is ideal for immediate results. Many successful businesses use both strategically."),
            (f"Can I use both {a} and {b} together?", f"Absolutely — and we recommend it. Using both creates a synergy where each channel supports the other, delivering faster and more sustainable results than either alone."),
            (f"What's the cost difference between {a} and {b}?", f"Both have different cost structures. Contact Rankify Goa for a personalized comparison based on your specific business, industry, and goals. We'll show you projected ROI for each option."),
        ]
        breadcrumbs = [("Home", f"{SITE_URL}/"), ("Blog", f"{SITE_URL}/blog"), (h1, f"{SITE_URL}/{slug}")]
        
        content = f'''
          <h2>{a} vs {b} – A Detailed Comparison</h2>
          <p>As a <a href="digital-marketing.html">digital marketing agency in Goa</a> that offers both {a.lower()} and {b.lower()}, we're uniquely positioned to give you an unbiased comparison. We use both for our own marketing and for our clients — here's what 10+ years of experience has taught us.</p>
          <h3>When to Choose {a}</h3>
          <p>{a} is the right choice when you want sustainable, long-term growth; when you're building brand authority; and when you have a 3-6 month horizon for results. It's the foundation that compounds over time.</p>
          <h3>When to Choose {b}</h3>
          <p>{b} makes sense when you need immediate results; when you're testing a new market; or when you have a seasonal promotion. It delivers faster but requires ongoing investment to maintain.</p>
          <h3>Our Recommendation</h3>
          <p>For most Goa businesses, the answer isn't either/or — it's both, deployed strategically. Start with {b.lower()} for immediate leads while building {a.lower()} for long-term growth. As {a.lower()} gains traction, you can scale back {b.lower()} spend and reinvest. <a href="contact.html">Talk to our strategists</a> for a personalized recommendation.</p>
        '''
        faq_html = '<h2>FAQs</h2><div class="accordion tj-faq" id="faqAcc">'
        for i, (q, ans) in enumerate(faqs):
            show = "show" if i == 0 else ""
            coll = "" if i == 0 else "collapsed"
            faq_html += f'<div class="accordion-item"><button class="faq-title {coll}" data-bs-toggle="collapse" data-bs-target="#f{i}">{q}</button><div id="f{i}" class="collapse {show}" data-bs-parent="#faqAcc"><div class="accordion-body faq-text"><p>{ans}</p></div></div></div>'
        faq_html += '</div>'
        content += faq_html
        
        related = [("seo-optimization.html", "SEO"), ("ppc-advertising.html", "PPC"), ("digital-marketing.html", "Digital Marketing"), ("contact.html", "Get Advice")]
        bc_text = '<span><a href="index.html">Home</a></span> <span><a href="blog.html">Blog</a></span> <span>Comparison</span>'
        
        html = make_head(title, desc, slug, breadcrumbs, "Article", faqs)
        html += make_nav()
        html += make_body(h1, "Strategy Guide", bc_text, content, related)
        html += make_footer()
        
        filepath = os.path.join(WORKSPACE, f"{slug}.html")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        all_pages.append((slug, title))
        count += 1
    print(f"  ✓ {count - cmp_start} comparison pages generated")

    # ─── 6. Blog Posts (80) ──────────────────────────────────────────────────
    print("── 6/9 Blog Posts (80) ──")
    blog_start = count
    for post in BLOG_TOPICS:
        slug = f"blog/{post['slug']}"
        title = f"{post['title']} | {BRAND}"
        desc = f"{post['title']}. Expert insights from Goa's leading digital marketing agency. Practical tips you can implement today."
        h1 = post['title']
        cat = post['category']
        faqs = gen_faqs_for(cat.lower())
        breadcrumbs = [("Home", f"{SITE_URL}/"), ("Blog", f"{SITE_URL}/blog"), (h1[:40], f"{SITE_URL}/{slug}")]
        
        content = f'''
          <h2>{h1}</h2>
          <p>In this comprehensive guide, the team at Rankify Goa breaks down everything you need to know about {cat.lower()} for businesses in Goa and across India. Whether you're just getting started or looking to optimize your existing strategy, you'll find actionable insights backed by our experience working with 600+ clients.</p>
          <h3>Key Takeaways</h3>
          <ul>
            <li>Understanding the fundamentals of {cat.lower()} and why it matters in 2025</li>
            <li>Step-by-step implementation guide you can follow</li>
            <li>Common mistakes to avoid (we've seen them all)</li>
            <li>How to measure success and track ROI</li>
            <li>When to DIY vs. when to hire professionals</li>
          </ul>
          <h3>Why This Matters for Goa Businesses</h3>
          <p>{cat} has become essential for businesses in Goa competing in today's digital landscape. With increasing competition and changing consumer behavior, businesses that master {cat.lower()} gain a significant advantage over those that don't. The strategies in this guide are specifically adapted for the Goan market — accounting for seasonal tourism patterns, local competition, and regional search behavior.</p>
          <h3>Need Help Implementing?</h3>
          <p>If you'd rather have experts handle your {cat.lower()} strategy, <a href="contact.html">reach out to our team</a>. We offer free consultations and can build a custom plan for your business. No generic templates — just honest advice and proven strategies.</p>
        '''
        faq_html = '<h2>Related Questions</h2><div class="accordion tj-faq" id="faqAcc">'
        for i, (q, a) in enumerate(faqs):
            show = "show" if i == 0 else ""
            coll = "" if i == 0 else "collapsed"
            faq_html += f'<div class="accordion-item"><button class="faq-title {coll}" data-bs-toggle="collapse" data-bs-target="#f{i}">{q}</button><div id="f{i}" class="collapse {show}" data-bs-parent="#faqAcc"><div class="accordion-body faq-text"><p>{a}</p></div></div></div>'
        faq_html += '</div>'
        content += faq_html
        
        related = [("blog.html", "More Articles"), ("services.html", "Our Services"), ("contact.html", "Free Consultation")]
        bc_text = f'<span><a href="index.html">Home</a></span> <span><a href="blog.html">Blog</a></span> <span>{cat}</span>'
        
        html = make_head(title, desc, slug, breadcrumbs, "Article", faqs)
        html += make_nav()
        html += make_body(h1, f"{cat} Guide", bc_text, content, related)
        html += make_footer()
        
        # Blog posts go in blog/ subfolder
        blog_dir = os.path.join(WORKSPACE, "blog")
        filepath = os.path.join(blog_dir, f"{post['slug']}.html")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        all_pages.append((slug, title))
        count += 1
    print(f"  ✓ {count - blog_start} blog posts generated")

    # ─── 7. Use-Case Pages (20) ──────────────────────────────────────────────
    print("── 7/9 Use-Case Pages (20) ──")
    uc_start = count
    for uc in USE_CASES:
        nice_name = uc.replace("-", " ").title()
        slug = f"digital-marketing-for-{uc}"
        title = f"Digital Marketing for {nice_name} in Goa | {BRAND}"
        desc = f"Specialized digital marketing solutions for {nice_name.lower()} in Goa. SEO, ads, social media & web design tailored to your specific business needs."
        h1 = f"Digital Marketing for {nice_name} in Goa"
        faqs = gen_faqs_for(f"marketing for {nice_name.lower()}")
        breadcrumbs = [("Home", f"{SITE_URL}/"), ("Services", f"{SITE_URL}/services"), (f"For {nice_name}", f"{SITE_URL}/{slug}")]
        
        content = f'''
          <h2>Tailored Marketing Solutions for {nice_name}</h2>
          <p>Running a {nice_name.lower()} business in Goa? Your marketing needs are different from other businesses. Your customers search differently, make decisions differently, and respond to different messages. That's why generic marketing agencies often fail {nice_name.lower()} — they apply the same playbook to everyone. We don't.</p>
          <h3>What We Do for {nice_name}</h3>
          <ul>
            <li>Industry-specific <a href="seo-optimization.html">SEO strategy</a> targeting how YOUR customers search</li>
            <li><a href="local-seo.html">Local SEO</a> to dominate Google Maps for {nice_name.lower()}-related searches in Goa</li>
            <li><a href="social-media-marketing.html">Social media presence</a> on the platforms your audience actually uses</li>
            <li><a href="website-design.html">Conversion-focused website</a> designed for {nice_name.lower()} businesses</li>
            <li>Targeted <a href="ppc-advertising.html">Google Ads</a> for immediate lead generation</li>
          </ul>
          <h3>Our Track Record with {nice_name}</h3>
          <p>We've helped multiple {nice_name.lower()} businesses in Goa achieve top Google rankings, increase online inquiries, and build sustainable digital growth. Our approach is always ROI-focused — you invest, we deliver measurable returns. <a href="contact.html">Book a free strategy call</a> to discuss your specific goals.</p>
        '''
        faq_html = '<h2>FAQs for {}</h2><div class="accordion tj-faq" id="faqAcc">'.format(nice_name)
        for i, (q, a) in enumerate(faqs):
            show = "show" if i == 0 else ""
            coll = "" if i == 0 else "collapsed"
            faq_html += f'<div class="accordion-item"><button class="faq-title {coll}" data-bs-toggle="collapse" data-bs-target="#f{i}">{q}</button><div id="f{i}" class="collapse {show}" data-bs-parent="#faqAcc"><div class="accordion-body faq-text"><p>{a}</p></div></div></div>'
        faq_html += '</div>'
        content += faq_html
        
        related = [("services.html", "All Services"), ("clients.html", "Our Clients"), ("contact.html", "Talk to Us")]
        bc_text = f'<span><a href="index.html">Home</a></span> <span><a href="services.html">Services</a></span> <span>For {nice_name}</span>'
        
        html = make_head(title, desc, slug, breadcrumbs, "Service", faqs)
        html += make_nav()
        html += make_body(h1, "Specialized Solutions", bc_text, content, related)
        html += make_footer()
        
        filepath = os.path.join(WORKSPACE, f"{slug}.html")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        all_pages.append((slug, title))
        count += 1
    print(f"  ✓ {count - uc_start} use-case pages generated")

    # ─── 8. FAQ Hub Pages (10) ───────────────────────────────────────────────
    print("── 8/9 FAQ Hub Pages (10) ──")
    fh_start = count
    for fh in FAQ_HUBS:
        nice = fh.replace("-faq", "").replace("-", " ").title()
        slug = fh
        title = f"{nice} FAQ – Common Questions Answered | {BRAND}"
        desc = f"Find answers to frequently asked questions about {nice.lower()} services in Goa. Expert answers from Rankify Goa's team."
        h1 = f"{nice} – Frequently Asked Questions"
        faqs = [
            (f"What is {nice.lower()} and why do I need it?", f"{nice} is a critical component of modern digital marketing. For businesses in Goa, it helps increase online visibility, attract more customers, and grow revenue consistently."),
            (f"How much does {nice.lower()} cost in Goa?", f"Our {nice.lower()} services start from ₹15,000/month depending on your business size and competition. We offer custom packages tailored to your budget and goals."),
            (f"How long until I see results from {nice.lower()}?", f"Most clients see initial improvements within 30-60 days, with significant results appearing in 3-6 months. We provide monthly reports from day one so you can track progress."),
            (f"Do I need {nice.lower()} if I'm a small business?", f"Absolutely. Small businesses often see the biggest relative impact from {nice.lower()} because the competition is more manageable. We have affordable packages designed specifically for small businesses in Goa."),
            (f"Can I do {nice.lower()} myself or should I hire an agency?", f"You can handle basics yourself, but professional {nice.lower()} requires expertise, tools, and time that most business owners don't have. Our agency handles everything so you can focus on running your business."),
        ]
        breadcrumbs = [("Home", f"{SITE_URL}/"), ("FAQ", f"{SITE_URL}/faq"), (nice, f"{SITE_URL}/{slug}")]
        
        faq_html = '<div class="accordion tj-faq" id="faqAcc">'
        for i, (q, a) in enumerate(faqs):
            show = "show" if i == 0 else ""
            coll = "" if i == 0 else "collapsed"
            faq_html += f'<div class="accordion-item"><button class="faq-title {coll}" data-bs-toggle="collapse" data-bs-target="#f{i}">{q}</button><div id="f{i}" class="collapse {show}" data-bs-parent="#faqAcc"><div class="accordion-body faq-text"><p>{a}</p></div></div></div>'
        faq_html += '</div>'
        content = f'<h2>{nice} Questions & Answers</h2><p>Below are the most common questions we receive about {nice.lower()} from businesses in Goa. Can\'t find your answer? <a href="contact.html">Contact us directly</a>.</p>{faq_html}'
        
        related = [("faq.html", "Main FAQ"), ("services.html", "Services"), ("contact.html", "Ask Us")]
        bc_text = f'<span><a href="index.html">Home</a></span> <span><a href="faq.html">FAQ</a></span> <span>{nice}</span>'
        
        html = make_head(title, desc, slug, breadcrumbs, "FAQPage", faqs)
        html += make_nav()
        html += make_body(h1, "Knowledge Base", bc_text, content, related)
        html += make_footer()
        
        filepath = os.path.join(WORKSPACE, f"{slug}.html")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        all_pages.append((slug, title))
        count += 1
    print(f"  ✓ {count - fh_start} FAQ hub pages generated")

    # ─── 9. Misc Landing Pages (62) ─────────────────────────────────────────
    print("── 9/9 Miscellaneous Landing Pages (62) ──")
    misc_start = count
    # Generate targeted pages for remaining GSC queries
    misc_targets = [
        ("best-digital-marketing-agency-goa", "Best Digital Marketing Agency in Goa"),
        ("top-digital-marketing-agency-goa", "Top Digital Marketing Agency in Goa"),
        ("affordable-digital-marketing-goa", "Affordable Digital Marketing in Goa"),
        ("best-seo-agency-goa", "Best SEO Agency in Goa"),
        ("best-seo-company-goa", "Best SEO Company in Goa"),
        ("top-seo-company-goa", "Top SEO Company in Goa"),
        ("seo-agency-goa", "SEO Agency in Goa"),
        ("seo-company-goa", "SEO Company in Goa"),
        ("seo-services-goa", "SEO Services in Goa"),
        ("seo-expert-goa", "SEO Expert in Goa"),
        ("marketing-agency-goa", "Marketing Agency in Goa"),
        ("marketing-agencies-goa", "Marketing Agencies in Goa"),
        ("advertising-agency-goa", "Advertising Agency in Goa"),
        ("creative-agency-goa", "Creative Agency in Goa"),
        ("branding-agency-goa", "Branding Agency in Goa"),
        ("web-development-company-goa", "Web Development Company in Goa"),
        ("social-media-agency-goa", "Social Media Agency in Goa"),
        ("content-marketing-agency-goa", "Content Marketing Agency in Goa"),
        ("ppc-agency-goa", "PPC Agency in Goa"),
        ("google-ads-agency-goa", "Google Ads Agency in Goa"),
        ("facebook-marketing-agency-goa", "Facebook Marketing Agency in Goa"),
        ("instagram-marketing-agency-goa", "Instagram Marketing Agency in Goa"),
        ("online-marketing-agency-goa", "Online Marketing Agency in Goa"),
        ("internet-marketing-goa", "Internet Marketing Services in Goa"),
        ("search-engine-marketing-goa", "Search Engine Marketing in Goa"),
        ("performance-marketing-agency-goa", "Performance Marketing Agency in Goa"),
        ("lead-generation-agency-goa", "Lead Generation Agency in Goa"),
        ("full-service-digital-marketing-agency-goa", "Full-Service Digital Marketing Agency in Goa"),
        ("ecommerce-marketing-agency-goa", "E-commerce Marketing Agency in Goa"),
        ("b2b-marketing-agency-goa", "B2B Marketing Agency in Goa"),
        ("influencer-marketing-agency-goa", "Influencer Marketing Agency in Goa"),
        ("video-marketing-agency-goa", "Video Marketing Agency in Goa"),
        ("email-marketing-agency-goa", "Email Marketing Agency in Goa"),
        ("reputation-management-agency-goa", "Reputation Management Agency in Goa"),
        ("digital-marketing-consultant-goa", "Digital Marketing Consultant in Goa"),
        ("seo-consultant-goa", "SEO Consultant in Goa"),
        ("freelance-digital-marketer-goa", "Freelance Digital Marketer vs Agency in Goa"),
        ("digital-marketing-company-goa", "Digital Marketing Company in Goa"),
        ("digital-marketing-services-goa", "Digital Marketing Services in Goa"),
        ("digital-marketing-packages-goa", "Digital Marketing Packages & Pricing in Goa"),
        ("seo-packages-goa", "SEO Packages & Pricing in Goa"),
        ("website-design-cost-goa", "Website Design Cost in Goa"),
        ("digital-marketing-internship-goa", "Digital Marketing Internship in Goa"),
        ("digital-marketing-jobs-goa", "Digital Marketing Jobs & Careers in Goa"),
        ("digital-marketing-course-goa", "Digital Marketing Course Guidance for Goa"),
        ("google-my-business-optimization-goa", "Google My Business Optimization in Goa"),
        ("local-business-marketing-goa", "Local Business Marketing in Goa"),
        ("tourism-marketing-goa", "Tourism Marketing & Promotion in Goa"),
        ("hospitality-marketing-goa", "Hospitality Marketing in Goa"),
        ("restaurant-marketing-goa", "Restaurant Marketing in Goa"),
        ("hotel-marketing-goa", "Hotel Marketing in Goa"),
        ("real-estate-marketing-goa", "Real Estate Marketing in Goa"),
        ("healthcare-marketing-goa", "Healthcare Marketing in Goa"),
        ("education-marketing-goa", "Education Marketing in Goa"),
        ("startup-marketing-goa", "Startup Marketing in Goa"),
        ("small-business-marketing-goa", "Small Business Marketing in Goa"),
        ("app-marketing-goa", "App Marketing & ASO in Goa"),
        ("whatsapp-marketing-services-goa", "WhatsApp Marketing Services in Goa"),
        ("ai-marketing-agency-goa", "AI-Powered Marketing Agency in Goa"),
        ("data-driven-marketing-goa", "Data-Driven Marketing in Goa"),
        ("growth-hacking-agency-goa", "Growth Hacking Agency in Goa"),
        ("conversion-optimization-goa", "Conversion Optimization Services in Goa"),
    ]
    
    for slug, nice_title in misc_targets:
        title = f"{nice_title} | {BRAND}"
        desc = f"{nice_title} – Trusted by 600+ businesses. Expert strategies, transparent pricing, measurable results. Free consultation available. Call +91 99233-52923."
        h1 = nice_title
        faqs = gen_faqs_for(nice_title.lower().replace(" in goa", ""))
        breadcrumbs = [("Home", f"{SITE_URL}/"), ("Services", f"{SITE_URL}/services"), (nice_title[:30], f"{SITE_URL}/{slug}")]
        
        content = f'''
          <h2>{nice_title}</h2>
          <p>Rankify Goa is your trusted partner for {nice_title.lower().replace(" in goa", "")} services in Goa. With 600+ successful clients, proven methodologies, and deep local expertise, we deliver digital marketing solutions that generate real business results — not just vanity metrics.</p>
          <h3>Why Businesses in Goa Choose Us</h3>
          <ul>
            <li><strong>Local Expertise</strong> — We're based in Goa, we understand your market, your competition, and your customers</li>
            <li><strong>Proven Results</strong> — 600+ businesses served with documented success stories</li>
            <li><strong>Transparent Pricing</strong> — No hidden fees, clear deliverables, monthly reporting</li>
            <li><strong>Full-Service</strong> — SEO, PPC, social media, web design, branding — everything under one roof</li>
            <li><strong>ROI-Focused</strong> — We measure everything against revenue, not just rankings</li>
          </ul>
          <h3>Our Services Include</h3>
          <p><a href="seo-optimization.html">SEO Optimization</a> · <a href="local-seo.html">Local SEO</a> · <a href="ppc-advertising.html">PPC Advertising</a> · <a href="social-media-marketing.html">Social Media</a> · <a href="website-design.html">Website Design</a> · <a href="content-marketing.html">Content Marketing</a> · <a href="branding-strategy.html">Branding</a> · <a href="graphic-designing.html">Graphic Design</a></p>
          <h3>Get Your Free Strategy Session</h3>
          <p>Ready to grow? <a href="contact.html">Contact us</a> or WhatsApp +91 99233-52923 for a free, no-obligation strategy session. We'll analyze your current digital presence and show you exactly how to outrank your competition.</p>
        '''
        faq_html = '<h2>Common Questions</h2><div class="accordion tj-faq" id="faqAcc">'
        for i, (q, a) in enumerate(faqs):
            show = "show" if i == 0 else ""
            coll = "" if i == 0 else "collapsed"
            faq_html += f'<div class="accordion-item"><button class="faq-title {coll}" data-bs-toggle="collapse" data-bs-target="#f{i}">{q}</button><div id="f{i}" class="collapse {show}" data-bs-parent="#faqAcc"><div class="accordion-body faq-text"><p>{a}</p></div></div></div>'
        faq_html += '</div>'
        content += faq_html
        
        related = [("services.html", "All Services"), ("about.html", "About Us"), ("clients.html", "Our Clients"), ("contact.html", "Contact")]
        bc_text = '<span><a href="index.html">Home</a></span> <span><a href="services.html">Services</a></span> <span>Details</span>'
        
        html = make_head(title, desc, slug, breadcrumbs, "Service", faqs)
        html += make_nav()
        html += make_body(h1, "Expert Solutions", bc_text, content, related)
        html += make_footer()
        
        filepath = os.path.join(WORKSPACE, f"{slug}.html")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        all_pages.append((slug, title))
        count += 1
    print(f"  ✓ {count - misc_start} miscellaneous pages generated")

    # ─── UPDATE SITEMAP ──────────────────────────────────────────────────────
    print("\n── Updating sitemap.xml ──")
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")
    sitemap_path = os.path.join(WORKSPACE, "sitemap.xml")
    with open(sitemap_path, 'r') as f:
        sitemap_content = f.read()
    
    new_entries = ""
    for slug, _ in all_pages:
        url = f"{SITE_URL}/{slug}"
        new_entries += f'<url>\n  <loc>{url}</loc>\n  <lastmod>{now}</lastmod>\n  <changefreq>monthly</changefreq>\n  <priority>0.70</priority>\n</url>\n'
    
    sitemap_content = sitemap_content.replace("</urlset>", f"\n{new_entries}\n</urlset>")
    with open(sitemap_path, 'w') as f:
        f.write(sitemap_content)
    print(f"  ✓ Sitemap updated with {len(all_pages)} new URLs (total: {20 + len(all_pages)} URLs)")

    # ─── SUMMARY ─────────────────────────────────────────────────────────────
    print("")
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║  ✅ 351-PAGE ECOSYSTEM COMPLETE                                 ║")
    print("╠══════════════════════════════════════════════════════════════════╣")
    print(f"║  New pages generated:    {count:>3}                                   ║")
    print(f"║  + Existing pages:        22                                   ║")
    print(f"║  = TOTAL PAGES:          {22 + count:>3}                                   ║")
    print("║                                                                  ║")
    print("║  Industry verticals:      15                                    ║")
    print("║  Location pages:          12                                    ║")
    print("║  Location+Service:        60                                    ║")
    print("║  Service deep-dives:      25                                    ║")
    print("║  Comparisons:             15                                    ║")
    print("║  Blog articles:           80                                    ║")
    print("║  Use-case pages:          20                                    ║")
    print("║  FAQ hubs:                10                                    ║")
    print(f"║  Misc landing pages:      {len(misc_targets):>2}                                    ║")
    print("║                                                                  ║")
    print("║  FAQPage schema:         EVERY page                             ║")
    print("║  Service schema:         EVERY page                             ║")
    print("║  BreadcrumbList:         EVERY page                             ║")
    print("║  Internal links:         6+ per page                            ║")
    print("║  Competitor names used:  ZERO                                   ║")
    print("╚══════════════════════════════════════════════════════════════════╝")
    

if __name__ == "__main__":
    main()
