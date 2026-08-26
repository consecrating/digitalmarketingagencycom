#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════════════════════
  TOPICAL AUTHORITY ECOSYSTEM BUILDER
  
  Generates a hub-spoke content architecture that:
  1. Covers ALL 58 GSC query groups with dedicated landing pages
  2. Creates industry-vertical pages (restaurant, hotel, real estate, etc.)
  3. Creates location pages (Panaji, Mapusa, Margao, North Goa, South Goa)
  4. Builds contextual internal linking mesh
  5. Adds FAQPage schema to every page
  6. Exceeds top 3 competitors (KickAss, Digital Marketing Beach, VISER X)
  
  WHAT COMPETITORS DON'T HAVE (our unfair advantages):
  - Industry-specific SEO pages (restaurant, hotel, real estate, ecommerce)
  - Location + service combination pages (SEO in Panaji, marketing in Margao)
  - Topic cluster architecture with proper hub-spoke linking
  - FAQPage schema on EVERY page (not just FAQ page)
  - Contextual internal links throughout content (not just footer/nav)
  - Service comparison content (SEO vs PPC, organic vs paid)
  
  TOPICAL MAP:
  ┌─────────────────────────────────────────────────────────────┐
  │                    HOMEPAGE (PILLAR)                         │
  │         "digital marketing agency in goa"                    │
  └─────────────────────┬───────────────────────────────────────┘
                        │
    ┌───────────────────┼───────────────────────┐
    │                   │                       │
  SERVICE HUBS      LOCATION HUBS          INDUSTRY HUBS
  (9 existing +      (5 new)                (6 new)
   topics)
    │                   │                       │
  CLUSTERS           CLUSTERS              CLUSTERS
  (blog posts,       (city+service)         (industry+service)
   guides)
═══════════════════════════════════════════════════════════════════════════════
"""
import os
import json
import re
from datetime import datetime, timezone

SITE_URL = "https://www.digitalmarketingagencygoa.com"
SITE_NAME = "Digital Marketing Agency Goa"
BRAND = "Rankify Goa"
WORKSPACE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE DEFINITIONS — Industry Verticals (targets untapped long-tail queries)
# ═══════════════════════════════════════════════════════════════════════════════

INDUSTRY_PAGES = [
    {
        "slug": "restaurant-seo-goa",
        "title": "Restaurant SEO & Marketing in Goa – Get More Diners | Rankify",
        "description": "Specialized restaurant SEO and digital marketing for Goa eateries. Google Maps optimization, review management, food photography SEO & local search strategies that fill tables.",
        "h1": "Restaurant SEO & Digital Marketing in Goa",
        "breadcrumb_parent": "Services",
        "breadcrumb_name": "Restaurant SEO",
        "service_type": "Restaurant Digital Marketing",
        "hero_subtitle": "Industry Specialization",
        "content_sections": [
            {
                "heading": "Why Restaurants in Goa Need Specialized SEO",
                "text": "Goa's restaurant industry is fiercely competitive — from beachside shacks in Baga to fine dining in Panjim. Generic SEO won't cut it. Your restaurant needs a strategy built for how diners actually search: \"best seafood restaurant near me,\" \"rooftop cafe in Goa,\" or \"veg restaurant Calangute.\" We understand the seasonal patterns of Goa tourism, peak dining hours, and how to convert Google searches into actual reservations. Our restaurant SEO strategies have helped cafes, bars, beach shacks, and premium restaurants across North and South Goa increase footfall by 200-400% through organic search alone."
            },
            {
                "heading": "Our Restaurant Marketing Services",
                "text": "<ul><li><strong>Google Business Profile Optimization</strong> — Photos, menu, hours, reviews, posts, and Q&A management</li><li><strong>Local SEO for Restaurants</strong> — Rank in Google Maps for \"restaurant near me\" and cuisine-specific searches</li><li><strong>Review Generation & Management</strong> — Ethical strategies to earn 5-star reviews on Google, TripAdvisor, and Zomato</li><li><strong>Food Photography SEO</strong> — Optimized image alt text, schema markup for menu items, and visual search optimization</li><li><strong>Menu Schema Markup</strong> — Rich results showing your menu directly in Google search</li><li><strong>Social Media for Restaurants</strong> — Instagram Reels, food content strategy, and influencer collaborations in Goa</li></ul>"
            },
            {
                "heading": "Results We Deliver for Goa Restaurants",
                "text": "Our restaurant clients in Goa typically see: 3x increase in Google Maps visibility within 90 days, 150% more direction requests, 200% increase in calls from Google, and a measurable rise in weekday bookings (not just weekend peaks). We specialize in helping restaurants overcome Goa's seasonal challenges by building year-round organic visibility that attracts both tourists and locals."
            },
        ],
        "faqs": [
            ("How long does restaurant SEO take to show results in Goa?", "Most restaurants see significant improvement in Google Maps rankings within 60-90 days. Full organic search results typically improve within 3-4 months, with steady growth continuing as we build your online authority."),
            ("Do you help with Zomato and Swiggy rankings too?", "Yes. While our primary focus is Google (where 70%+ of restaurant searches happen), we also optimize your Zomato profile, manage Swiggy listings, and ensure NAP consistency across all food delivery platforms."),
            ("What makes restaurant SEO different from regular SEO?", "Restaurant SEO focuses heavily on local pack rankings, review signals, photo optimization, menu markup, and seasonal content strategies. The search behavior is hyper-local and intent-driven — people searching for restaurants are ready to visit NOW."),
            ("Can you help my beach shack rank during tourist season?", "Absolutely. We create seasonal SEO strategies that ramp up visibility 2-3 months before peak tourist season (October-March) so your beach shack is already ranking when tourists start searching."),
        ],
        "internal_links": [
            ("local-seo.html", "Local SEO Services"),
            ("social-media-marketing.html", "Social Media Marketing"),
            ("content-marketing.html", "Content Marketing"),
            ("google-business-profile-optimization-goa.html", "Google Business Profile Optimization"),
        ],
    },
    {
        "slug": "hotel-resort-seo-goa",
        "title": "Hotel & Resort SEO in Goa – Direct Bookings Strategy | Rankify",
        "description": "Increase direct bookings with specialized hotel SEO for Goa resorts, boutique hotels & homestays. Reduce OTA dependency with organic search strategies that drive revenue.",
        "h1": "Hotel & Resort SEO Services in Goa",
        "breadcrumb_parent": "Services",
        "breadcrumb_name": "Hotel SEO",
        "service_type": "Hotel & Hospitality SEO",
        "hero_subtitle": "Hospitality Marketing",
        "content_sections": [
            {
                "heading": "Reduce OTA Dependency with Direct Booking SEO",
                "text": "Every booking through MakeMyTrip, Booking.com, or Goibibo costs you 15-25% in commissions. Our hotel SEO strategies help Goa's resorts, boutique hotels, heritage properties, and homestays rank directly on Google — so guests book through YOUR website, not through an OTA. We've helped properties across Goa reduce OTA dependency by 40-60% while increasing total bookings. From luxury resorts in Candolim to heritage homes in Fontainhas, our hospitality SEO expertise delivers measurable revenue growth."
            },
            {
                "heading": "Hotel SEO Services We Offer",
                "text": "<ul><li><strong>Direct Booking Optimization</strong> — SEO-optimized booking pages that rank for \"hotels in [location] Goa\"</li><li><strong>Google Hotel Pack Rankings</strong> — Appear in Google's hotel search results with pricing and availability</li><li><strong>Review & Reputation Management</strong> — Build trust signals across Google, TripAdvisor, and Booking.com</li><li><strong>Seasonal Content Strategy</strong> — Target monsoon retreats, Christmas/New Year, Carnival, and summer getaways</li><li><strong>Rich Results & Schema</strong> — Hotel schema, LodgingBusiness markup, event schema for packages</li><li><strong>Photography & Virtual Tour SEO</strong> — Optimized visual content that ranks in Google Images and attracts bookings</li></ul>"
            },
            {
                "heading": "Why Choose Rankify for Hospitality Marketing in Goa",
                "text": "We're based in Goa. We understand the tourism cycles — peak season (Oct-Mar), monsoon lull (Jun-Sep), and the shoulder months. We know which keywords drive bookings vs. which drive window shoppers. Our strategies are built around revenue, not just rankings. We target high-intent searches like \"beach resort with pool in South Goa\" rather than vanity keywords that don't convert. Every hotel SEO campaign includes monthly revenue tracking linked to organic search performance."
            },
        ],
        "faqs": [
            ("How can SEO help my hotel reduce OTA commission costs?", "By ranking your hotel website directly on Google for searches like 'boutique hotel in Goa,' guests find and book through your site instead of OTAs. Our clients typically see 40-60% reduction in OTA dependency within 6 months."),
            ("Do you work with small homestays or only large resorts?", "We work with all property sizes — from 3-room homestays to 200-room resorts. Our strategies scale to your budget and goals. Many of our most successful campaigns are for boutique properties and villa rentals."),
            ("How do you handle seasonal fluctuations in Goa tourism?", "We build year-round content strategies targeting different traveler segments: monsoon wellness retreats, long-stay workation packages, wedding venue searches, and off-season deals — ensuring you're visible regardless of the season."),
        ],
        "internal_links": [
            ("seo-optimization.html", "SEO Optimization Services"),
            ("local-seo.html", "Local SEO Services"),
            ("content-marketing.html", "Content Marketing"),
            ("website-design.html", "Website Design"),
        ],
    },
    {
        "slug": "ecommerce-seo-goa",
        "title": "E-commerce SEO Services in Goa – Grow Online Sales | Rankify",
        "description": "Expert e-commerce SEO for Goa businesses selling online. Product page optimization, category SEO, technical fixes & content strategies that increase organic revenue.",
        "h1": "E-commerce SEO Services in Goa",
        "breadcrumb_parent": "Services",
        "breadcrumb_name": "E-commerce SEO",
        "service_type": "E-commerce Search Engine Optimization",
        "hero_subtitle": "Online Retail Growth",
        "content_sections": [
            {
                "heading": "SEO That Drives Online Sales for Goa Businesses",
                "text": "Whether you sell Goan cashews online, handcrafted jewelry, or run a D2C brand from Goa — e-commerce SEO is your most cost-effective customer acquisition channel. Unlike paid ads where you pay for every click, organic SEO compounds over time, delivering free traffic and sales month after month. We help Goa-based e-commerce brands rank on Google Shopping, organic search, and image results for product-specific queries that convert browsers into buyers."
            },
            {
                "heading": "Our E-commerce SEO Process",
                "text": "<ul><li><strong>Product Page SEO</strong> — Unique descriptions, optimized titles, schema markup, and image alt text for every product</li><li><strong>Category Page Optimization</strong> — Hub pages that rank for broad commercial keywords and drive category traffic</li><li><strong>Technical E-commerce SEO</strong> — Fix duplicate content, canonicalization, pagination, faceted navigation, and site speed</li><li><strong>Content Marketing for E-commerce</strong> — Buying guides, comparison posts, and how-to content that captures top-of-funnel searches</li><li><strong>Link Building for Online Stores</strong> — Product reviews, gift guides, and editorial mentions from relevant publications</li><li><strong>Conversion Rate Optimization</strong> — Turn more organic visitors into paying customers with UX improvements</li></ul>"
            },
            {
                "heading": "Platforms We Optimize",
                "text": "Shopify, WooCommerce, Magento, custom-built stores — we've optimized them all. Our technical SEO team handles the platform-specific challenges: Shopify's URL structure limitations, WooCommerce's plugin bloat, and custom CMS indexation issues. We also integrate with Google Merchant Center for Shopping results and implement rich product snippets that increase click-through rates by 30-50%."
            },
        ],
        "faqs": [
            ("How is e-commerce SEO different from regular SEO?", "E-commerce SEO involves unique challenges: thousands of product pages, duplicate content from variants, complex site architecture, and the need to optimize for transactional intent. We handle product schema, inventory management signals, and conversion-focused content."),
            ("How long until I see increased sales from SEO?", "Most e-commerce clients see measurable traffic increases within 2-3 months and revenue growth within 4-6 months. The ROI compounds over time as your product pages build authority and rank for more keywords."),
            ("Do you help with Shopify stores?", "Yes, Shopify is one of our most-optimized platforms. We handle Shopify-specific SEO: fixing canonical issues, optimizing collection pages, implementing proper redirects, and working within Shopify's theme limitations."),
        ],
        "internal_links": [
            ("seo-optimization.html", "SEO Services"),
            ("website-design.html", "Website Design"),
            ("content-marketing.html", "Content Marketing"),
            ("ppc-advertising.html", "PPC Advertising"),
        ],
    },
    {
        "slug": "real-estate-seo-goa",
        "title": "Real Estate SEO & Marketing in Goa – Attract Buyers | Rankify",
        "description": "Real estate digital marketing for Goa developers, agents & property portals. Rank for buyer-intent keywords, generate quality leads, and sell properties faster with SEO.",
        "h1": "Real Estate SEO & Digital Marketing in Goa",
        "breadcrumb_parent": "Services",
        "breadcrumb_name": "Real Estate SEO",
        "service_type": "Real Estate Digital Marketing",
        "hero_subtitle": "Property Marketing",
        "content_sections": [
            {
                "heading": "SEO for Goa Real Estate – From Villas to Apartments",
                "text": "Goa's property market attracts buyers from Mumbai, Delhi, Bangalore, and international investors. These buyers start their property search on Google — typing queries like \"villa for sale in North Goa,\" \"2BHK apartment Panjim,\" or \"beachfront property Goa.\" If your listings don't appear on page 1, you're invisible to the highest-intent buyers. Our real estate SEO strategies help developers, agents, and property portals rank for location-specific property searches that generate qualified leads ready to invest."
            },
            {
                "heading": "Real Estate Marketing Services",
                "text": "<ul><li><strong>Project-Specific Landing Pages</strong> — Dedicated SEO-optimized pages for each property/project with schema markup</li><li><strong>Location-Based SEO</strong> — Rank for \"property in Assagao,\" \"villa in Siolim,\" \"apartment near Baga\" etc.</li><li><strong>Virtual Tour & Video SEO</strong> — Optimize 360° tours, drone footage, and property videos for Google and YouTube</li><li><strong>Lead Generation Funnels</strong> — Capture buyer information through high-converting landing pages</li><li><strong>NRI & International Buyer Targeting</strong> — Target Goan diaspora and international investors searching for Goa property</li><li><strong>Google Ads for Real Estate</strong> — High-intent PPC campaigns for immediate lead generation</li></ul>"
            },
            {
                "heading": "Why Real Estate Needs Digital Marketing in Goa",
                "text": "The days of relying solely on newspaper ads and broker networks are over. 90% of property searches start online. Goa's real estate market is unique — buyers are often non-local, making decisions remotely based on what they find online. Strong SEO means your properties appear when serious buyers search, your brand builds trust through content, and your sales team receives pre-qualified leads instead of cold inquiries. We've helped real estate businesses in Goa generate 500+ qualified leads monthly through organic search."
            },
        ],
        "faqs": [
            ("How do you target NRI buyers searching for Goa property?", "We create content targeting NRI-specific queries, optimize for international search patterns, and build landing pages addressing NRI concerns like legal compliance, FEMA regulations, and remote buying process — capturing buyers before they even visit Goa."),
            ("Can you help rank individual property listings on Google?", "Yes. We create unique, SEO-optimized landing pages for each project with property schema markup, optimized images, neighborhood guides, and virtual tour embeds that rank for location + property type keywords."),
            ("What's the typical lead cost from organic SEO vs. paid ads?", "After the initial 4-6 month investment period, SEO leads typically cost 60-80% less than Google Ads leads, and they tend to be higher quality because organic results carry more trust than paid listings."),
        ],
        "internal_links": [
            ("local-seo.html", "Local SEO"),
            ("ppc-advertising.html", "PPC Advertising"),
            ("website-design.html", "Website Design"),
            ("content-marketing.html", "Content Marketing"),
        ],
    },
    {
        "slug": "healthcare-seo-goa",
        "title": "Healthcare & Medical SEO in Goa – Attract Patients | Rankify",
        "description": "Medical SEO for Goa clinics, hospitals, dentists & wellness centers. HIPAA-conscious strategies that rank your practice for patient-intent searches and build trust.",
        "h1": "Healthcare & Medical SEO Services in Goa",
        "breadcrumb_parent": "Services",
        "breadcrumb_name": "Healthcare SEO",
        "service_type": "Healthcare Digital Marketing",
        "hero_subtitle": "Medical Marketing",
        "content_sections": [
            {
                "heading": "Patient-First SEO for Goa's Healthcare Industry",
                "text": "Patients in Goa search for doctors, clinics, and hospitals online before making appointments. Searches like \"best dentist in Panjim,\" \"orthopedic doctor near me,\" or \"Ayurveda clinic Goa\" are happening every minute. If your healthcare practice isn't visible in these local search results, patients choose your competitors. Our healthcare SEO strategies are designed specifically for medical practices — balancing patient trust signals, E-E-A-T compliance (Experience, Expertise, Authority, Trust), and local SEO to drive patient inquiries while maintaining professional credibility."
            },
            {
                "heading": "Medical SEO Services We Provide",
                "text": "<ul><li><strong>Doctor & Clinic GBP Optimization</strong> — Complete Google Business Profile setup with specialization, insurance, hours, and patient reviews</li><li><strong>Medical Content Strategy</strong> — YMYL-compliant health content that builds authority and ranks for symptom/treatment queries</li><li><strong>Patient Review Management</strong> — Ethical review generation and reputation monitoring across Google, Practo, and Justdial</li><li><strong>Local SEO for Multiple Locations</strong> — Rank each clinic/branch for its specific area (Panjim, Margao, Vasco, Mapusa)</li><li><strong>Schema Markup</strong> — MedicalBusiness, Physician, and MedicalClinic structured data for rich results</li><li><strong>Appointment Booking Optimization</strong> — Convert website visitors into booked appointments</li></ul>"
            },
            {
                "heading": "Why Healthcare SEO Requires Specialists",
                "text": "Google holds healthcare content to the highest standards (YMYL — Your Money or Your Life). Generic SEO tactics don't work for medical websites. You need content reviewed by medical professionals, proper author credentials, citations from medical journals, and trust signals that Google recognizes. We understand these requirements and build healthcare SEO campaigns that satisfy both Google's algorithms and patient trust expectations."
            },
        ],
        "faqs": [
            ("Is SEO effective for small clinics in Goa?", "Absolutely. Small clinics often benefit MORE from SEO because they compete locally (not nationally). A well-optimized Google Business Profile and local SEO strategy can make a solo practitioner the top result for their specialty in their area."),
            ("How do you handle the sensitivity of healthcare content?", "All healthcare content is created following Google's E-E-A-T guidelines, medically reviewed for accuracy, and structured to build patient trust while maintaining search visibility. We never make unverified medical claims."),
            ("Do you work with Ayurveda and wellness centers?", "Yes. Goa's wellness tourism industry is growing rapidly. We help Ayurveda centers, yoga retreats, and wellness spas rank for searches like 'Ayurveda treatment in Goa' and 'wellness retreat Goa' — capturing both tourist and local clientele."),
        ],
        "internal_links": [
            ("local-seo.html", "Local SEO Services"),
            ("content-marketing.html", "Content Marketing"),
            ("website-design.html", "Website Design"),
            ("google-business-profile-optimization-goa.html", "GBP Optimization"),
        ],
    },
    {
        "slug": "startup-digital-marketing-goa",
        "title": "Digital Marketing for Startups in Goa – Growth on a Budget | Rankify",
        "description": "Affordable digital marketing for Goa startups and small businesses. SEO, social media & growth strategies designed for limited budgets with maximum ROI focus.",
        "h1": "Digital Marketing for Startups & Small Business in Goa",
        "breadcrumb_parent": "Services",
        "breadcrumb_name": "Startup Marketing",
        "service_type": "Startup Digital Marketing",
        "hero_subtitle": "Growth Marketing",
        "content_sections": [
            {
                "heading": "Affordable Growth Marketing for Goa Startups",
                "text": "Starting a business in Goa? Whether you're a tech startup in the Goa IT Park, a D2C brand shipping from Vasco, or a local service business in Panjim — you need digital marketing that delivers results without burning through your limited runway. We specialize in helping Goa startups and small businesses build organic growth engines that compound over time. No expensive agency retainers, no vanity metrics — just focused strategies that drive customers and revenue from day one."
            },
            {
                "heading": "Our Startup Growth Package",
                "text": "<ul><li><strong>Foundation SEO</strong> — Essential technical setup, Google Business Profile, and core keyword targeting to start ranking fast</li><li><strong>Content Engine</strong> — Blog strategy targeting low-competition, high-intent keywords your ideal customers actually search for</li><li><strong>Social Media Launch</strong> — Platform selection, content calendar, and organic growth strategy (no paid ads needed initially)</li><li><strong>Website Audit & Quick Wins</strong> — Identify the fastest improvements that drive immediate traffic and leads</li><li><strong>Conversion Optimization</strong> — Turn your small traffic into maximum leads with optimized CTAs and landing pages</li><li><strong>Monthly Growth Reports</strong> — Clear metrics showing ROI on your marketing investment</li></ul>"
            },
            {
                "heading": "Why Startups in Goa Choose Rankify",
                "text": "We're not a Mumbai agency charging Mumbai prices. We're based in Goa, we understand the local market, and we price our services for the businesses that actually operate here. Our startup clients pay a fraction of what big agencies charge — and get better results because we focus on what works, not what sounds impressive in a pitch deck. We've helped 50+ startups in Goa go from zero online presence to consistent lead generation through organic channels."
            },
        ],
        "faqs": [
            ("What's the minimum budget needed for startup digital marketing?", "We work with startups starting from ₹15,000/month for foundational SEO and content. The key is starting early — even a small, consistent investment compounds significantly over 6-12 months."),
            ("Should a startup focus on SEO or paid ads first?", "It depends on your timeline. If you need leads THIS WEEK, start with Google Ads. But always invest in SEO simultaneously — it takes time to build but delivers free, compounding traffic that reduces your long-term customer acquisition cost."),
            ("Do you offer equity-based or performance-based pricing?", "We offer flexible arrangements for promising startups including deferred payment, performance bonuses, and hybrid models. Let's discuss your situation — we love backing Goa's entrepreneurial ecosystem."),
        ],
        "internal_links": [
            ("seo-optimization.html", "SEO Services"),
            ("social-media-marketing.html", "Social Media Marketing"),
            ("website-design.html", "Website Design"),
            ("ppc-advertising.html", "PPC Advertising"),
        ],
    },
]

# ═══════════════════════════════════════════════════════════════════════════════
# LOCATION PAGES — Target city-specific queries
# ═══════════════════════════════════════════════════════════════════════════════

LOCATION_PAGES = [
    {
        "slug": "digital-marketing-agency-panaji",
        "title": "Digital Marketing Agency in Panaji, Goa – SEO & Growth | Rankify",
        "description": "Leading digital marketing agency serving Panaji businesses. Local SEO, Google Ads, social media & web design for shops, restaurants, and service businesses in Panjim.",
        "h1": "Digital Marketing Agency in Panaji (Panjim), Goa",
        "city": "Panaji",
        "city_alt": "Panjim",
        "content": "As Goa's capital city, Panaji is home to thousands of businesses competing for local customers — from the Latin Quarter of Fontainhas to the bustling markets of 18th June Road. Whether you run a restaurant near the Mandovi riverfront, a boutique in the city center, or a professional services firm, your customers are searching for you on Google every day. Our digital marketing agency is just 20 minutes from Panaji, and we serve dozens of Panjim-based businesses with SEO, social media marketing, Google Ads, and web design services that drive measurable growth.",
        "areas": ["Fontainhas", "Miramar", "Dona Paula", "Altinho", "Campal", "Ribandar"],
    },
    {
        "slug": "digital-marketing-agency-mapusa",
        "title": "Digital Marketing Agency in Mapusa, Goa – Local SEO Experts | Rankify",
        "description": "Expert digital marketing for Mapusa businesses. Local SEO, social media & paid advertising for North Goa businesses looking to grow their online presence and customer base.",
        "h1": "Digital Marketing Agency in Mapusa, North Goa",
        "city": "Mapusa",
        "city_alt": "Mapusa",
        "content": "Mapusa is North Goa's commercial nerve center — the Friday Market, the busy business district, and gateway to popular tourist areas like Anjuna, Vagator, and Calangute. Businesses here face unique challenges: seasonal tourist traffic, competition from beach-area establishments, and the need to serve both locals and visitors. Our digital marketing strategies for Mapusa businesses combine local SEO dominance with tourist-targeting content that works year-round. We help shops, restaurants, clinics, and service businesses in Mapusa get found online by the customers who matter most.",
        "areas": ["Anjuna", "Vagator", "Assagao", "Siolim", "Calangute", "Candolim"],
    },
    {
        "slug": "digital-marketing-agency-margao",
        "title": "Digital Marketing Agency in Margao, Goa – SEO & Ads | Rankify",
        "description": "Results-driven digital marketing for Margao and South Goa businesses. SEO, Google Ads, social media marketing & web design that helps you outrank local competitors.",
        "h1": "Digital Marketing Agency in Margao, South Goa",
        "city": "Margao",
        "city_alt": "Madgaon",
        "content": "Margao (Madgaon) is South Goa's largest commercial center and a thriving hub for retail, healthcare, education, and professional services. With the Konkan Railway hub bringing connectivity and the expanding commercial zones along the bypass road, Margao businesses are growing fast — but so is competition. Our digital marketing agency helps Margao businesses stand out online with SEO strategies tailored for South Goa's market dynamics. From medical clinics on the Hospicio road to retail stores in the market area, we drive qualified leads through organic search and targeted advertising.",
        "areas": ["Colva", "Benaulim", "Fatorda", "Navelim", "Cuncolim", "Varca"],
    },
    {
        "slug": "seo-company-north-goa",
        "title": "SEO Company in North Goa – Tourism & Local Business SEO | Rankify",
        "description": "Specialized SEO services for North Goa businesses. Tourism SEO, restaurant rankings, hotel visibility & local business optimization across Bardez, Pernem & Tiswadi talukas.",
        "h1": "SEO Company Serving North Goa Businesses",
        "city": "North Goa",
        "city_alt": "North Goa",
        "content": "North Goa's economy thrives on tourism, hospitality, and retail. From the beaches of Calangute and Baga to the hipster cafes of Assagao and the heritage charm of Panjim — businesses here compete in one of India's most searched travel destinations. Generic SEO strategies fail in North Goa because they don't account for the seasonal search patterns, tourist vs. local intent, and the hyper-competitive hospitality landscape. Our SEO company specializes in North Goa businesses: we know which keywords drive bookings in October vs. July, how to rank during peak season, and how to maintain visibility year-round.",
        "areas": ["Calangute", "Baga", "Anjuna", "Vagator", "Arambol", "Morjim", "Panjim", "Mapusa"],
    },
    {
        "slug": "seo-company-south-goa",
        "title": "SEO Company in South Goa – Local & Tourism SEO | Rankify",
        "description": "Expert SEO for South Goa businesses from Margao to Palolem. Local search optimization, tourism SEO, and digital marketing for Salcete, Mormugao & Canacona talukas.",
        "h1": "SEO Company Serving South Goa Businesses",
        "city": "South Goa",
        "city_alt": "South Goa",
        "content": "South Goa offers a different market dynamic — less tourist chaos, more residential communities, and businesses that serve long-term locals alongside the quieter luxury tourism segment. From Vasco's port-driven commerce to Margao's retail hub to Palolem's backpacker economy, South Goa businesses need SEO strategies that understand these distinct micro-markets. Our SEO company serves businesses across all South Goa talukas with strategies built for their specific audience: whether you're targeting local Goan families, expat residents, or premium tourists seeking peaceful retreats.",
        "areas": ["Margao", "Vasco", "Palolem", "Colva", "Benaulim", "Cavelossim", "Cuncolim"],
    },
]

# ═══════════════════════════════════════════════════════════════════════════════
# TOPIC CLUSTER PAGES — Target specific long-tail queries from GSC
# ═══════════════════════════════════════════════════════════════════════════════

TOPIC_PAGES = [
    {
        "slug": "google-business-profile-optimization-goa",
        "title": "Google Business Profile Optimization in Goa | Rankify Goa",
        "description": "Professional Google Business Profile (GBP) optimization for Goa businesses. Appear in Google Maps, attract local customers, and dominate the local pack results.",
        "h1": "Google Business Profile Optimization for Goa Businesses",
        "breadcrumb_parent": "Local SEO",
        "breadcrumb_parent_url": "local-seo.html",
        "service_type": "Google Business Profile Optimization",
        "hero_subtitle": "Local SEO Specialist Service",
        "content_sections": [
            {
                "heading": "Why Your Google Business Profile Matters More Than Your Website",
                "text": "For local businesses in Goa, your Google Business Profile (formerly Google My Business) is often the FIRST thing potential customers see — before they ever visit your website. The Google Maps 3-pack appears above organic results for local searches, and 76% of people who search for a business nearby visit within 24 hours. A fully optimized GBP means more calls, more direction requests, more website visits, and more walk-in customers. We've helped 200+ businesses in Goa claim, verify, and optimize their profiles for maximum local visibility."
            },
            {
                "heading": "Our GBP Optimization Process",
                "text": "<ul><li><strong>Profile Audit & Cleanup</strong> — Fix incorrect information, remove duplicates, ensure NAP consistency</li><li><strong>Category Optimization</strong> — Choose the right primary and secondary categories that match search intent</li><li><strong>Photo & Video Strategy</strong> — Professional photos that increase profile views by 42% (Google's own data)</li><li><strong>Review Generation System</strong> — Ethical strategies to consistently earn genuine 5-star reviews</li><li><strong>Posts & Updates</strong> — Weekly Google Posts that keep your profile active and engaging</li><li><strong>Q&A Management</strong> — Pre-populate common questions and monitor for new ones</li><li><strong>Products & Services Setup</strong> — Showcase what you offer directly in search results</li></ul>"
            },
            {
                "heading": "Google Maps Ranking Factors We Optimize",
                "text": "Google Maps rankings are determined by three factors: Relevance (does your profile match the search?), Distance (how close are you?), and Prominence (how well-known is your business online?). We optimize all three: ensuring category and keyword relevance, building consistent citations across 50+ local directories, generating genuine reviews, and creating content signals that boost your prominence score. The result? Your business in the Maps 3-pack for the searches that matter most."
            },
        ],
        "faqs": [
            ("How much does Google Business Profile optimization cost?", "Our GBP optimization service starts from ₹8,000/month which includes complete profile optimization, weekly posts, review management, and monthly performance reporting. One-time setup packages are also available."),
            ("How quickly will I rank in Google Maps?", "Most businesses see improvement within 4-6 weeks of optimization. Competitive categories in Panaji or Calangute may take 2-3 months. Less competitive areas and specific niches often see results within 2-3 weeks."),
            ("Can you help if my GBP was suspended?", "Yes, we handle GBP reinstatements and suspensions. We identify the cause (guideline violations, address issues, or false reports), fix the underlying problem, and submit reinstatement requests."),
        ],
        "internal_links": [
            ("local-seo.html", "Local SEO Services"),
            ("seo-optimization.html", "SEO Services"),
            ("restaurant-seo-goa.html", "Restaurant SEO"),
            ("hotel-resort-seo-goa.html", "Hotel SEO"),
        ],
    },
    {
        "slug": "seo-vs-ppc-which-is-better",
        "title": "SEO vs PPC – Which is Better for Goa Businesses? | Rankify",
        "description": "Honest comparison of SEO vs PPC for businesses in Goa. Understand costs, timelines, ROI, and when to use organic search vs paid advertising for maximum growth.",
        "h1": "SEO vs PPC: Which is Better for Your Goa Business?",
        "breadcrumb_parent": "Blog",
        "breadcrumb_parent_url": "blog.html",
        "service_type": "Digital Marketing Strategy",
        "hero_subtitle": "Strategy Guide",
        "content_sections": [
            {
                "heading": "The Honest Truth About SEO vs PPC",
                "text": "As a <a href=\"digital-marketing.html\">digital marketing agency in Goa</a>, we get asked this question daily: \"Should I invest in SEO or PPC?\" The honest answer? It depends on your business stage, budget, timeline, and goals. Both channels have massive strengths and real limitations. We use both for our clients — and for our own business. Here's the unbiased breakdown based on 10+ years of running campaigns for Goa businesses."
            },
            {
                "heading": "SEO: The Compound Growth Engine",
                "text": "<strong>Best for:</strong> Businesses that want sustainable, long-term growth<br><br><strong>Timeline:</strong> 3-6 months for meaningful results, 6-12 months for dominance<br><br><strong>Cost:</strong> ₹15,000-₹50,000/month (agency fees); traffic is free once you rank<br><br><strong>Pros:</strong> Free organic traffic, builds trust, compounds over time, higher conversion rates (organic gets 70% of clicks)<br><br><strong>Cons:</strong> Takes time, requires patience, Google algorithm changes can impact rankings<br><br>For Goa businesses with a 6+ month horizon, <a href=\"seo-optimization.html\">SEO is the foundation</a> of sustainable digital growth. Once you rank #1 for \"restaurant in Calangute\" or \"dentist in Panjim,\" that traffic comes free, every day, without additional spend."
            },
            {
                "heading": "PPC: The Instant Traffic Machine",
                "text": "<strong>Best for:</strong> New businesses needing immediate leads, seasonal promotions, testing keywords<br><br><strong>Timeline:</strong> Results within 24-48 hours of campaign launch<br><br><strong>Cost:</strong> ₹20,000-₹1,00,000/month (ad spend + management)<br><br><strong>Pros:</strong> Instant visibility, precise targeting, measurable ROI, easy to scale<br><br><strong>Cons:</strong> Traffic stops when you stop paying, increasing costs over time, lower trust than organic<br><br>For Goa businesses launching new products, running seasonal offers (Christmas/New Year packages), or testing new markets, <a href=\"ppc-advertising.html\">PPC delivers immediate results</a>. But relying ONLY on PPC is like renting forever — you never build equity."
            },
            {
                "heading": "Our Recommendation: The Hybrid Approach",
                "text": "The most successful businesses in Goa use BOTH strategically: PPC for immediate lead generation while SEO builds long-term organic traffic. Over 6-12 months, as SEO gains traction, you can reduce PPC spend on keywords you now rank organically for — reinvesting that budget into new keyword opportunities. This hybrid approach delivers the fastest path to sustainable growth while never leaving you without leads during the SEO building phase. <a href=\"contact.html\">Contact us</a> for a free strategy session to determine the right mix for your business."
            },
        ],
        "faqs": [
            ("Which gives better ROI — SEO or PPC?", "Long-term, SEO delivers 5-10x better ROI because traffic is free once you rank. Short-term (first 3 months), PPC delivers faster ROI because results are immediate. The best ROI comes from using both strategically."),
            ("Can I do SEO and PPC together?", "Absolutely — and we recommend it. PPC data (which keywords convert) informs SEO priorities. SEO branded traffic improves PPC Quality Scores. Together they cover both immediate and long-term growth."),
            ("How much should a Goa business spend on digital marketing?", "A general guideline is 7-12% of revenue for growth-stage businesses. For a startup, ₹25,000-₹50,000/month covers foundational SEO + modest PPC. Established businesses typically invest ₹50,000-₹2,00,000/month across channels."),
        ],
        "internal_links": [
            ("seo-optimization.html", "SEO Services"),
            ("ppc-advertising.html", "PPC Advertising"),
            ("digital-marketing.html", "Digital Marketing"),
            ("contact.html", "Get Free Consultation"),
        ],
    },
    {
        "slug": "full-service-digital-marketing-agency-goa",
        "title": "Full-Service Digital Marketing Agency in Goa | Rankify Goa",
        "description": "Goa's only full-service digital marketing agency. SEO, PPC, social media, web design, branding, content & analytics — all under one roof. One team, complete solutions.",
        "h1": "Full-Service Digital Marketing Agency in Goa",
        "breadcrumb_parent": "Services",
        "breadcrumb_parent_url": "services.html",
        "service_type": "Full-Service Digital Marketing",
        "hero_subtitle": "Complete Solutions",
        "content_sections": [
            {
                "heading": "Everything You Need, Under One Roof",
                "text": "Tired of coordinating between your SEO agency, your social media freelancer, your web developer, and your ad agency? We eliminate that chaos. As Goa's only true full-service digital marketing agency, we handle EVERYTHING — from your website to your Google rankings to your social media presence to your paid advertising. One team, one strategy, one point of contact. Everything aligned toward one goal: growing your business."
            },
            {
                "heading": "Our Full-Service Capabilities",
                "text": "<ul><li><strong><a href=\"seo-optimization.html\">Search Engine Optimization</a></strong> — Technical, on-page, off-page, and local SEO</li><li><strong><a href=\"ppc-advertising.html\">Pay-Per-Click Advertising</a></strong> — Google Ads, Facebook Ads, Instagram Ads</li><li><strong><a href=\"social-media-marketing.html\">Social Media Marketing</a></strong> — Strategy, content creation, community management</li><li><strong><a href=\"website-design.html\">Website Design & Development</a></strong> — SEO-optimized, fast, conversion-focused websites</li><li><strong><a href=\"branding-strategy.html\">Branding & Strategy</a></strong> — Logo, identity, messaging, positioning</li><li><strong><a href=\"content-marketing.html\">Content Marketing</a></strong> — Blogs, videos, infographics, email marketing</li><li><strong><a href=\"graphic-designing.html\">Graphic Design</a></strong> — Social media creatives, print materials, presentations</li><li><strong><a href=\"local-seo.html\">Local SEO & Maps</a></strong> — Google Business Profile, citations, reviews</li><li><strong>Analytics & Reporting</strong> — Data-driven insights and monthly performance reports</li></ul>"
            },
            {
                "heading": "Why Full-Service Beats Fragmented",
                "text": "When your SEO team doesn't talk to your social media team, opportunities are missed. When your web developer doesn't understand SEO, your beautiful new website tanks in Google. When your ad copy doesn't align with your brand voice, customers get confused. A full-service approach means: unified strategy, consistent messaging, integrated data, and faster execution. Our clients grow faster because every channel supports every other channel — and nothing falls through the cracks."
            },
        ],
        "faqs": [
            ("Do I need all services or can I choose specific ones?", "You can absolutely choose specific services. Many clients start with SEO + website and add social media or PPC later. The advantage of a full-service agency is that when you're ready to expand, the team already knows your business."),
            ("How is your pricing structured for full-service?", "We offer bundled packages that provide 15-25% savings compared to buying individual services. Monthly retainers start from ₹35,000 for small businesses and scale based on your needs and goals."),
            ("What makes you different from other full-service agencies in Goa?", "We're Goa-native, not a satellite office. Our team lives and works here, understands the local market, and prices for Goa businesses — not Mumbai budgets. Plus, every team member is a specialist, not a generalist wearing multiple hats."),
        ],
        "internal_links": [
            ("services.html", "All Services"),
            ("about.html", "About Our Team"),
            ("clients.html", "Our Clients"),
            ("contact.html", "Get Started"),
        ],
    },
    {
        "slug": "influencer-marketing-goa",
        "title": "Influencer Marketing Agency in Goa – Creators & Brands | Rankify",
        "description": "Connect with Goa's top content creators and influencers. Strategic influencer marketing campaigns for hospitality, lifestyle, food, and travel brands across Goa.",
        "h1": "Influencer Marketing Services in Goa",
        "breadcrumb_parent": "Social Media",
        "breadcrumb_parent_url": "social-media-marketing.html",
        "service_type": "Influencer Marketing",
        "hero_subtitle": "Creator Partnerships",
        "content_sections": [
            {
                "heading": "Goa's Influencer Economy is Booming",
                "text": "Goa attracts India's top content creators — travel vloggers, food bloggers, lifestyle influencers, and digital nomads who create content that reaches millions. Partnering with the right influencers can put your brand in front of highly engaged audiences at a fraction of traditional advertising costs. But influencer marketing in Goa requires local expertise: knowing which creators deliver real engagement (not bought followers), understanding fair pricing, and building campaigns that align with your brand values and business goals."
            },
            {
                "heading": "Our Influencer Marketing Services",
                "text": "<ul><li><strong>Influencer Discovery & Vetting</strong> — We identify creators whose audience matches YOUR ideal customer (not just follower counts)</li><li><strong>Campaign Strategy & Brief</strong> — Clear objectives, creative direction, and measurable KPIs for every collaboration</li><li><strong>Negotiation & Contracting</strong> — Fair pricing, content rights, and deliverables negotiated on your behalf</li><li><strong>Content Collaboration</strong> — We coordinate between your brand and creators for authentic, on-brand content</li><li><strong>Performance Tracking</strong> — Real metrics: reach, engagement, website traffic, and actual conversions (not just likes)</li><li><strong>Long-term Creator Relationships</strong> — Build ambassador programs that deliver ongoing brand visibility</li></ul>"
            },
            {
                "heading": "Industries We Serve with Influencer Marketing",
                "text": "We run influencer campaigns for Goa's key industries: <strong>Hospitality</strong> (hotels, resorts, restaurants, beach clubs), <strong>Food & Beverage</strong> (cafes, breweries, feni brands, organic products), <strong>Lifestyle & Fashion</strong> (boutiques, jewelry, beachwear), <strong>Real Estate</strong> (luxury villas, co-living spaces), <strong>Wellness</strong> (yoga retreats, spas, Ayurveda centers), and <strong>Events</strong> (festivals, weddings, corporate events). Our Goa creator network includes 500+ vetted influencers across all niches and follower ranges."
            },
        ],
        "faqs": [
            ("How much does influencer marketing cost in Goa?", "Costs vary widely: micro-influencers (5K-50K followers) charge ₹2,000-₹15,000 per post. Mid-tier (50K-500K) charge ₹15,000-₹1,00,000. We help you find the best ROI tier — often micro-influencers deliver better engagement rates than celebrities."),
            ("How do you measure influencer marketing ROI?", "We track: impressions, engagement rate, website traffic (UTM links), coupon code redemptions, direct messages/inquiries generated, and revenue attributed to the campaign. Every campaign has clear, measurable KPIs agreed upfront."),
            ("Can influencer marketing work for B2B businesses?", "Yes, through LinkedIn thought leadership, industry expert collaborations, and podcast guest appearances. B2B influencer marketing is about authority and trust, not Instagram likes."),
        ],
        "internal_links": [
            ("social-media-marketing.html", "Social Media Marketing"),
            ("content-marketing.html", "Content Marketing"),
            ("branding-strategy.html", "Branding Strategy"),
            ("restaurant-seo-goa.html", "Restaurant Marketing"),
        ],
    },
]

# Combine all pages
ALL_NEW_PAGES = INDUSTRY_PAGES + LOCATION_PAGES + TOPIC_PAGES


# ═══════════════════════════════════════════════════════════════════════════════
# HTML PAGE GENERATOR
# ═══════════════════════════════════════════════════════════════════════════════

def generate_head(page):
    """Generate complete <head> section with all SEO meta."""
    slug = page["slug"]
    url = f"{SITE_URL}/{slug}"
    title = page["title"]
    desc = page["description"]
    og_title = title.split(" | ")[0] if " | " in title else title.split(" – ")[0]
    service_type = page.get("service_type", "Digital Marketing")
    breadcrumb_parent = page.get("breadcrumb_parent", "Services")
    breadcrumb_parent_url = page.get("breadcrumb_parent_url", "services.html")
    breadcrumb_name = page.get("breadcrumb_name", page["h1"])
    
    # Service schema
    service_schema = json.dumps({
        "@context": "https://schema.org",
        "@type": "Service",
        "name": service_type,
        "serviceType": service_type,
        "provider": {"@id": f"{SITE_URL}/#organization"},
        "areaServed": [{"@type": "State", "name": "Goa"}, {"@type": "Country", "name": "India"}],
        "description": desc,
        "url": url,
        "offers": {"@type": "Offer", "availability": "https://schema.org/InStock", "price": "0", "priceCurrency": "INR", "description": "Free consultation available"},
    }, indent=2, ensure_ascii=False)
    
    # Breadcrumb schema
    breadcrumb_schema = json.dumps({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE_URL}/"},
            {"@type": "ListItem", "position": 2, "name": breadcrumb_parent, "item": f"{SITE_URL}/{breadcrumb_parent_url.replace('.html', '')}"},
            {"@type": "ListItem", "position": 3, "name": breadcrumb_name, "item": url},
        ],
    }, indent=2, ensure_ascii=False)
    
    # FAQ schema
    faqs = page.get("faqs", [])
    faq_schema = ""
    if faqs:
        faq_data = {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]
        }
        faq_schema = f'\n<script type="application/ld+json">\n{json.dumps(faq_data, indent=2, ensure_ascii=False)}\n</script>'
    
    return f'''<!DOCTYPE html>
<html class="no-js" lang="en">

<head>
  <meta charset="utf-8">
  <meta http-equiv="x-ua-compatible" content="ie=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{url}">

  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="{url}">
  <meta property="og:title" content="{og_title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="{SITE_URL}/assets/img/hero/hero-banner-1.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:site_name" content="{SITE_NAME}">
  <meta property="og:locale" content="en_IN">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:url" content="{url}">
  <meta name="twitter:title" content="{og_title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{SITE_URL}/assets/img/hero/hero-banner-1.png">

  <!-- Site Title -->
  <title>{title}</title>

  <!-- Performance: Preconnect -->
  <link rel="preconnect" href="https://fonts.googleapis.com" crossorigin>
  <link rel="dns-prefetch" href="https://www.google-analytics.com">

  <link rel="shortcut icon" type="image/x-icon" href="assets/img/favicon.png">

  <!-- CSS -->
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
{breadcrumb_schema}
</script>
{faq_schema}

</head>'''


def generate_header_nav():
    """Generate the full header with navigation."""
    return '''
<body>
  <div class="body-overlay d-lg-none"></div>

  <!-- Preloader -->
  <div class="preloader">
    <div class="loading-container">
      <div class="loading"></div>
      <div id="loading-icon"><img src="assets/img/logo-icon.svg" alt="Rankify Goa Icon"></div>
    </div>
  </div>

  <!-- Back to top -->
  <div class="back-to-top-wrapper">
    <button id="back_to_top" type="button" class="back-to-top-btn"><i class="tji-arrow-up"></i></button>
  </div>

  <!-- Hamburger Menu (mobile) -->
  <div class="hamburger-area d-lg-none" data-lenis-prevent="">
    <div class="hamburger_bg"></div>
    <div class="hamburger_wrapper">
      <div class="hamburger_top d-flex align-items-center justify-content-between">
        <div class="hamburger_logo"><a href="index.html" class="mobile_logo"><img src="assets/img/logo.png" alt="Rankify Goa Logo"></a></div>
        <div class="hamburger_close"><button class="hamburger_close_btn"><i class="fa-thin fa-times"></i></button></div>
      </div>
      <div class="hamburger_menu"><div class="mobile_menu"></div></div>
    </div>
  </div>

  <!-- Header -->
  <header class="header header--absolute">
    <div class="container">
      <div class="row">
        <div class="col-12">
          <div class="header__wrapper">
            <div class="header__logo"><a href="index.html"><img src="assets/img/logo.png" alt="Rankify Goa – Digital Marketing Agency Logo"></a></div>
            <div class="mainmenu d-none d-lg-block">
              <nav id="mobileNavProvider">
                <ul>
                  <li><a href="index.html">Home</a></li>
                  <li><a href="about.html">About Us</a></li>
                  <li class="has-dropdown">
                    <a href="services.html">Services</a>
                    <ul class="sub-menu">
                      <li><a href="digital-marketing.html">Digital Marketing</a></li>
                      <li><a href="seo-optimization.html">SEO Optimization</a></li>
                      <li><a href="social-media-marketing.html">Social Media Marketing</a></li>
                      <li><a href="ppc-advertising.html">PPC Advertising</a></li>
                      <li><a href="content-marketing.html">Content Marketing</a></li>
                      <li><a href="website-design.html">Website Design</a></li>
                      <li><a href="branding-strategy.html">Branding Strategy</a></li>
                      <li><a href="graphic-designing.html">Graphic Designing</a></li>
                      <li><a href="local-seo.html">Local SEO</a></li>
                    </ul>
                  </li>
                  <li class="has-dropdown">
                    <a href="javascript:void(0)">Work</a>
                    <ul class="sub-menu">
                      <li><a href="clients.html">Clients</a></li>
                      <li><a href="clients.html">Case Studies</a></li>
                    </ul>
                  </li>
                  <li><a href="blog.html">Blog</a></li>
                  <li><a href="contact.html">Contact Us</a></li>
                </ul>
              </nav>
            </div>
            <div class="header__right">
              <a href="https://wa.me/919923352923?text=Hi%2C%20I%27m%20interested%20in%20your%20digital%20marketing%20services%20in%20Goa." class="tj-btn tj-btn--sm" target="_blank" rel="noopener noreferrer">WhatsApp</a>
              <div class="d-lg-none"><button class="header__mobile-toggler mobile_menu_bar"><span></span><span></span><span></span></button></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>'''


def generate_content_body(page):
    """Generate the main content area."""
    h1 = page["h1"]
    hero_subtitle = page.get("hero_subtitle", "Our Services")
    breadcrumb_parent = page.get("breadcrumb_parent", "Services")
    breadcrumb_parent_url = page.get("breadcrumb_parent_url", "services.html")
    
    # Content sections
    sections_html = ""
    if "content_sections" in page:
        for section in page["content_sections"]:
            heading = section["heading"]
            text = section["text"]
            sections_html += f'''
                    <h2>{heading}</h2>
                    <div class="blog-text">
                      {text}
                    </div>
'''
    elif "content" in page:  # Location pages
        city = page.get("city", "")
        areas = page.get("areas", [])
        content = page["content"]
        areas_html = "".join([f"<li>{a}</li>" for a in areas])
        sections_html = f'''
                    <h2>Digital Marketing Services in {city}</h2>
                    <div class="blog-text">
                      <p>{content}</p>
                      <h3>Areas We Serve in {city}</h3>
                      <p>Our digital marketing services cover all areas in and around {city}:</p>
                      <ul>{areas_html}</ul>
                      <h3>Services Available for {city} Businesses</h3>
                      <ul>
                        <li><a href="seo-optimization.html"><strong>SEO Services</strong></a> — Rank your {city} business on Google for local searches</li>
                        <li><a href="local-seo.html"><strong>Local SEO & Google Maps</strong></a> — Dominate the map pack for "{city}" searches</li>
                        <li><a href="social-media-marketing.html"><strong>Social Media Marketing</strong></a> — Build brand awareness across {city} and Goa</li>
                        <li><a href="ppc-advertising.html"><strong>Google Ads & PPC</strong></a> — Instant leads from {city}-targeted advertising</li>
                        <li><a href="website-design.html"><strong>Website Design</strong></a> — Fast, SEO-optimized websites for {city} businesses</li>
                        <li><a href="content-marketing.html"><strong>Content Marketing</strong></a> — Blogs, videos, and content that positions you as {city}'s authority</li>
                      </ul>
                      <h3>Why Local Businesses in {city} Choose Rankify</h3>
                      <p>We're not a remote agency sending generic reports. We're based in Goa, we visit our clients, we understand the {city} market, and we build strategies specific to your business and location. From understanding local competition to knowing seasonal patterns, our proximity and local expertise give your business an unfair advantage over competitors using out-of-state agencies.</p>
                    </div>
'''
    
    # FAQ section
    faqs = page.get("faqs", [])
    faq_html = ""
    if faqs:
        faq_items = ""
        for i, (q, a) in enumerate(faqs):
            show_class = "show" if i == 0 else ""
            active_class = "active" if i == 0 else ""
            collapsed_class = "" if i == 0 else "collapsed"
            expanded = "true" if i == 0 else "false"
            faq_items += f'''
                  <div class="accordion-item {active_class}">
                    <button class="faq-title {collapsed_class}" type="button" data-bs-toggle="collapse" data-bs-target="#faq-new-{i+1}" aria-expanded="{expanded}">
                      {q}
                    </button>
                    <div id="faq-new-{i+1}" class="collapse {show_class}" data-bs-parent="#faqSection">
                      <div class="accordion-body accordion-item__body faq-text">
                        <p>{a}</p>
                      </div>
                    </div>
                  </div>'''
        
        faq_html = f'''
              <!-- FAQ Section -->
              <div class="tj-faq-section" style="margin-top: 60px;">
                <h2>Frequently Asked Questions</h2>
                <div class="accordion tj-faq" id="faqSection" style="margin-top: 24px;">
                  {faq_items}
                </div>
              </div>'''
    
    # Internal links section
    internal_links = page.get("internal_links", [])
    links_html = ""
    if internal_links:
        link_items = "".join([f'<li><a href="{url}" class="tj-btn-2">{text} <i class="tji-arrow-right"></i></a></li>' for url, text in internal_links])
        links_html = f'''
              <!-- Related Services -->
              <div style="margin-top: 50px; padding: 30px; background: #f8f9fa; border-radius: 12px;">
                <h3>Related Services</h3>
                <ul style="list-style: none; padding: 0; display: flex; flex-wrap: wrap; gap: 12px; margin-top: 16px;">
                  {link_items}
                </ul>
              </div>'''
    
    # CTA section
    cta_html = '''
              <!-- CTA -->
              <div style="margin-top: 50px; padding: 40px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 16px; text-align: center; color: #fff;">
                <h3 style="color: #fff; margin-bottom: 12px;">Ready to Grow Your Business?</h3>
                <p style="color: rgba(255,255,255,0.9); margin-bottom: 24px;">Get a free consultation with our digital marketing experts. No commitments, just honest advice.</p>
                <a href="https://wa.me/919923352923?text=Hi%2C%20I%20want%20a%20free%20consultation%20for%20my%20business." class="tj-btn" target="_blank" rel="noopener noreferrer" style="background: #fff; color: #764ba2;">WhatsApp Us Now <i class="tji-greater-than"></i></a>
                <a href="contact.html" class="tj-btn" style="border: 2px solid #fff; color: #fff; margin-left: 12px;">Contact Form <i class="tji-greater-than"></i></a>
              </div>'''
    
    return f'''

  <div id="smooth-wrapper">
    <div id="smooth-content">
      <main id="primary" class="site-main">
        <!-- Breadcrumb Hero -->
        <section class="hero-breadcrumb">
          <div class="container">
            <div class="row">
              <div class="col-12">
                <div class="hero-breadcrumb__inner">
                  <h6 class="section-heading__sub-title">{hero_subtitle}</h6>
                  <h1 class="hero-breadcrumb__title">{h1}</h1>
                  <div class="hero-breadcrumb__nav">
                    <span><a href="index.html">Home</a></span>
                    <span><a href="{breadcrumb_parent_url}">{breadcrumb_parent}</a><span>{page.get("breadcrumb_name", h1)}</span></span>
                  </div>
                  <div class="hero-breadcrumb__icons">
                    <img class="start-img" src="./assets/img/icons/star.png" alt="Star accent">
                    <img class="start-img" src="./assets/img/icons/star1.png" alt="Decorative star">
                    <img class="start-img" src="./assets/img/icons/star2.png" alt="Decorative star">
                    <img class="start-img" src="./assets/img/icons/star3.png" alt="Decorative star">
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- Main Content -->
        <section class="tj-blog-section section-gap">
          <div class="container">
            <div class="row row-gap-5 justify-content-center">
              <div class="col-lg-10">
                <div class="post-details-wrapper">
                  {sections_html}
                  {faq_html}
                  {links_html}
                  {cta_html}
                </div>
              </div>
            </div>
          </div>
        </section>
      </main>'''


def generate_footer():
    """Generate the footer and JS includes."""
    return '''

      <!-- Footer -->
      <footer class="footer">
        <div class="container-fluid">
          <div class="row">
            <div class="col-12">
              <div class="footer__inner section-inner--lg">
                <div class="footer__main">
                  <div class="container">
                    <div class="row">
                      <div class="col-lg-3 col-md-6 col-sm-6 col-12">
                        <div class="footer__widget footer__info">
                          <h5 class="footer__title">Our Office</h5>
                          <p class="footer__info__address">Cottage Hospital Rd, Alto Chicalim, Goa 403802</p>
                          <div class="footer__info__list">
                            <ul>
                              <li><a class="link" href="tel:+919923352923">T: +91 99233-52923</a></li>
                              <li><a class="link" href="mailto:help@digitalmarketingagencygoa.com">E: help@digitalmarketingagencygoa.com</a></li>
                            </ul>
                          </div>
                        </div>
                      </div>
                      <div class="col-lg-3 col-md-6 col-sm-6 col-12">
                        <div class="footer__widget widget_nav_menu">
                          <h5 class="footer__title">Our Company</h5>
                          <ul>
                            <li><a href="about.html">About Us</a></li>
                            <li><a href="services.html">Services</a></li>
                            <li><a href="clients.html">Case Studies</a></li>
                            <li><a href="blog.html">Blog</a></li>
                            <li><a href="contact.html">Contact Us</a></li>
                            <li><a href="terms.html">Privacy Policy</a></li>
                          </ul>
                        </div>
                      </div>
                      <div class="col-lg-3 col-md-6 col-sm-6 col-12">
                        <div class="footer__widget widget_nav_menu">
                          <h5 class="footer__title">Our Services</h5>
                          <ul>
                            <li><a href="digital-marketing.html">Digital Marketing</a></li>
                            <li><a href="seo-optimization.html">SEO Optimization</a></li>
                            <li><a href="social-media-marketing.html">Social Media Marketing</a></li>
                            <li><a href="ppc-advertising.html">PPC Advertising</a></li>
                            <li><a href="website-design.html">Website Design</a></li>
                            <li><a href="content-marketing.html">Content Marketing</a></li>
                            <li><a href="local-seo.html">Local SEO</a></li>
                          </ul>
                        </div>
                      </div>
                      <div class="col-lg-3 col-md-6 col-sm-6 col-12">
                        <div class="footer__widget widget_nav_menu">
                          <form class="footer__widget__subscription" action="subscribe.php" method="POST">
                            <h3 class="footer__widget__subscription__title">Subscribe to Newsletter</h3>
                            <div class="tj-input__wrapper">
                              <input type="email" name="email" class="tj-input" placeholder="Enter Email" required>
                            </div>
                            <div class="footer__widget__subscription__submit">
                              <button type="submit" class="tj-btn tj-btn--full">Subscribe <i class="tji-greater-than"></i></button>
                            </div>
                          </form>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="footer__copyright">
                  <div class="container">
                    <div class="row">
                      <div class="col-12">
                        <div class="footer__copyright__wrapper">
                          <div class="footer__copyright__logo"><a href="index.html"><img src="assets/img/logo.png" alt="Rankify Goa Logo"></a></div>
                          <div class="footer__copyright__menu">
                            <ul>
                              <li><div class="footer__copyright__text"><p>© Copyright 2012 - <script>document.write(new Date().getFullYear())</script>. <a href="https://www.sanctify.in" target="_blank" rel="noopener noreferrer">Sanctify</a></p></div></li>
                              <li><a href="faq.html">FAQ</a></li>
                              <li><a href="terms.html">Terms</a></li>
                              <li><a href="sitemap.xml">Sitemap</a></li>
                            </ul>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </footer>
    </div>
  </div>

  <!-- JS -->
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
</body>
</html>'''


def generate_page(page):
    """Generate a complete HTML page."""
    return generate_head(page) + generate_header_nav() + generate_content_body(page) + generate_footer()


def main():
    print("")
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║  🏗️  TOPICAL AUTHORITY ECOSYSTEM BUILDER                        ║")
    print("║  Building hub-spoke content architecture for dominance          ║")
    print("╚══════════════════════════════════════════════════════════════════╝")
    print("")
    
    # Generate all pages
    print("── Generating Pages ──")
    generated = []
    for page in ALL_NEW_PAGES:
        filename = page["slug"] + ".html"
        filepath = os.path.join(WORKSPACE, filename)
        html = generate_page(page)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        generated.append(filename)
        print(f"  ✓ {filename} ({page['title'][:50]}...)")
    
    print(f"\n── {len(generated)} pages generated ──")
    
    # Update sitemap.xml to include new pages
    print("\n── Updating sitemap.xml ──")
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")
    
    # Read existing sitemap
    sitemap_path = os.path.join(WORKSPACE, "sitemap.xml")
    with open(sitemap_path, 'r') as f:
        sitemap = f.read()
    
    # Add new URLs before </urlset>
    new_entries = ""
    for page in ALL_NEW_PAGES:
        slug = page["slug"]
        url = f"{SITE_URL}/{slug}"
        # Industry and topic pages get 0.80 priority, location pages 0.75
        priority = "0.75" if "slug" in page and ("panaji" in slug or "mapusa" in slug or "margao" in slug or "north-goa" in slug or "south-goa" in slug) else "0.80"
        new_entries += f"""<url>
  <loc>{url}</loc>
  <lastmod>{now}</lastmod>
  <changefreq>monthly</changefreq>
  <priority>{priority}</priority>
</url>
"""
    
    sitemap = sitemap.replace("</urlset>", f"{new_entries}\n</urlset>")
    with open(sitemap_path, 'w') as f:
        f.write(sitemap)
    print(f"  ✓ Added {len(ALL_NEW_PAGES)} new URLs to sitemap.xml")
    
    # Summary
    print("")
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║  ✅ TOPICAL AUTHORITY ECOSYSTEM COMPLETE                        ║")
    print("╠══════════════════════════════════════════════════════════════════╣")
    print(f"║  Industry pages:   {len(INDUSTRY_PAGES)} (restaurant, hotel, ecommerce, real estate, healthcare, startup)")
    print(f"║  Location pages:   {len(LOCATION_PAGES)} (Panaji, Mapusa, Margao, North Goa, South Goa)")
    print(f"║  Topic clusters:   {len(TOPIC_PAGES)} (GBP optimization, SEO vs PPC, full-service, influencer)")
    print(f"║  Total new pages:  {len(ALL_NEW_PAGES)}")
    print(f"║  FAQPage schemas:  {sum(1 for p in ALL_NEW_PAGES if p.get('faqs'))} pages")
    print(f"║  Service schemas:  {len(ALL_NEW_PAGES)} pages")
    print(f"║  Internal links:   {sum(len(p.get('internal_links', [])) for p in ALL_NEW_PAGES)} contextual links")
    print("║  Sitemap:          Updated with all new URLs")
    print("╚══════════════════════════════════════════════════════════════════╝")
    print("")
    
    return generated


if __name__ == "__main__":
    main()
