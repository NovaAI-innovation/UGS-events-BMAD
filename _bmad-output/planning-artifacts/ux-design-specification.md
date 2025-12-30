---
stepsCompleted: [1, 2]
inputDocuments:
  - '_bmad-output/planning-artifacts/prd.md'
  - '_bmad-output/implementation-artifacts/brand-guidelines.md'
  - '_bmad-output/implementation-artifacts/webpage-content-consolidated.md'
  - '_bmad-output/planning-artifacts/research/prd-research-summary.md'
---
# UX Design Specification UGS-events-BMAD

**Author:** Casey
**Date:** 2026-01-29

---

<!-- UX design content will be appended sequentially through collaborative workflow steps -->

## Executive Summary

### Project Vision

Underground Sound Events is building a mobile-first, community-driven event platform that revolutionizes how event companies engage with their community. This isn't just a website—it's a community-driven ecosystem where hip-hop, EDM, and fashion show events are discovered, promoted, and experienced through seamless integration of ticketing, live streaming, and community engagement.

The platform's core philosophy centers on community ownership: events are proposed by the community, artists are recommended by members, and causes are selected through community input. The brand voice rejects corporate polish in favor of authentic, genuine communication that resonates with Gen Z values: "Your community. Your events. Your culture."

**Key Differentiators:**
- **Bottom Sheet + Modal Hybrid Architecture:** Bottom sheet patterns for critical actions (mobile-native, thumb-optimized) combined with overlay modals for detailed views—phased implementation starting with bottom sheet actions
- **Feed-Inspired Discovery with Stories Pattern:** Visual feed-style event listing with horizontal swipe-through event "stories" (preview highlights) before commitment—progressive enhancement from traditional scrolling to swipe gestures
- **Community-Centered Visual Hierarchy:** Community voices, friend activity, and trending events take visual prominence through layout and design (achievable without complex architecture)
- **Unified "Join Event" Bottom Sheet:** Bottom sheet action panel combines ticket selection (cart-style) + purchase + stream access in single streamlined flow—sticky bottom action bar always visible
- **Stories-Based Event Previews:** Adapt Instagram Stories pattern—swipe horizontally through event highlights (performers, fashion, vibe) before committing to ticket purchase
- **Transparent, Fee-Free Ticketing:** Internal ticketing system eliminates third-party fees, giving full control over pricing and user experience

### Target Users

**Primary Users: Event Attendees (Ages 21-24)**
- Gen Z/early millennial demographic who primarily use mobile phones
- Seek authentic experiences and community connection over corporate events
- Heavy users of Instagram, TikTok, Snapchat—expect seamless social sharing and Stories-style previews
- Price-conscious but value experiences and community belonging
- Digital natives who expect fast, intuitive mobile experiences with bottom sheet patterns (familiar from mobile apps)
- Use this product to discover events (feed-inspired browsing with Stories previews), purchase tickets (bottom sheet cart-style selection), watch live streams (embedded in event cards), and engage with community (integrated bottom sheet actions)

**Secondary Users: Emerging Artists/Performers**
- Looking for platforms and opportunities to showcase talent
- Discovered through community recommendations (integrated into feed discovery)
- Need easy submission and engagement processes (bottom sheet actions, not separate pages)

**Tertiary Users: Fashion Designers, Vendors, Sponsors**
- Fashion designers building their brands
- Vendors/sponsors targeting Gen Z demographic
- Seeking authentic community connection over transactional relationships

### Key Design Challenges

1. **Mobile-First Experience with Bottom Sheet + Modal Hybrid Architecture**
   - Phase 1: Implement bottom sheet patterns for critical actions (ticket selection, engagement) with cart-style selection interface—more mobile-native than modals
   - Phase 2: Feed-inspired visual layout with Stories pattern (horizontal swipe through event previews) using traditional scrolling for feed itself
   - Phase 3: Progressive enhancement with swipe gestures for feed navigation (after validating user understanding)
   - Sticky bottom action bar with "Join Event" always visible (eliminates hunting for action buttons)
   - Achieve fast load times (< 3 seconds on 4G) with skeleton screens (show structure while loading, not spinners)
   - Balance innovation (bottom sheets, Stories pattern) with familiarity (traditional scrolling foundation)

2. **Community-Driven UX Patterns Through Visual Hierarchy and Bottom Sheet Actions**
   - Integrate community voting and recommendations into feed-inspired listing (visual integration, bottom sheet for actions)
   - Visualize community impact prominently (magnified social proof: friend activity, trending events, limited tickets)
   - Reverse traditional hierarchy: show "what's happening now" first, then upcoming, then past events
   - Community actions accessible from universal bottom sheet (not separate pages or complex navigation)
   - Create feedback loops that feel like social engagement (achievable through UI design and bottom sheet interactions)

3. **Authentic Brand Expression with Mobile-Native Patterns**
   - Integrate brand story into experience flow naturally (onboarding overlay tours, not separate pages)
   - Use Stories pattern for event previews (familiar Instagram pattern, authentic mobile-native feel)
   - Bottom sheet patterns feel more authentic than traditional modals (native mobile app patterns)
   - Balance authenticity with conversion optimization—visual-first, social-media-native communication

4. **Unified "Join Event" Bottom Sheet Flow**
   - Bottom sheet combines cart-style ticket selection + purchase + stream access in single flow
   - Cart-style selection interface (familiar shopping pattern, not form-based)
   - Handle edge cases gracefully (stream not available, payment failures, network issues) within bottom sheet context
   - Sticky bottom action bar ensures "Join Event" always accessible (eliminates scrolling to find action)
   - Social sharing integrated into checkout flow (share while purchasing, invite friends during checkout)
   - Maintain accessibility standards (bottom sheet keyboard navigation, screen reader support)

### Design Opportunities

1. **Feed-Inspired Discovery with Stories Pattern (Phased)**
   - Phase 1: Visual feed-style layout with traditional scrolling, horizontal Stories-style previews (swipe through event highlights before committing)
   - Phase 2: Progressive enhancement with swipe gestures for feed navigation (optional, after validation)
   - Visual-first event cards with Stories preview overlay (tap card to see Stories-style highlights)
   - Show friend activity, trending events, and "happening now" prominently in feed layout
   - Skeleton screens during loading (show card structure, not spinners)

2. **Bottom Sheet + Modal Hybrid System**
   - Bottom sheet for critical actions (ticket selection cart, engagement actions, universal action panel)
   - Overlay modals for detailed views (event details, full community discussion)
   - Sticky bottom action bar with "Join Event" always visible (thumb-zone optimized)
   - Cart-style ticket selection (familiar shopping pattern, not form-based)
   - Smooth bottom sheet animations (native mobile app feel)
   - Browser history integration for bottom sheet back-button support

3. **Community-Centered Visual Hierarchy (Achievable Through Design)**
   - Reverse discovery flow: "what's happening now" first (live/upcoming events prioritized)
   - Magnified social proof: friend activity, trending events, limited tickets prominently displayed
   - Community actions accessible from universal bottom sheet (integrated, not separate)
   - Community impact visualization prominently displayed (data-driven design)
   - Past events in feed drive future discovery (content marketing integration)

4. **Stories Pattern for Event Previews**
   - Horizontal swipe through event "stories" (highlights, performers, fashion, vibe)
   - Stories accessible from event cards (tap to preview, swipe to explore)
   - Stories become marketing content (past events' Stories drive future discovery)
   - Familiar Instagram pattern adapted for event discovery

5. **Performance-Optimized with Skeleton Screens**
   - Skeleton screens during loading (show structure, not spinners)
   - Virtual scrolling for feed with many events (performance optimization)
   - Progressive enhancement: start traditional, enhance with Stories and swipe gestures
   - Fast initial load with skeleton screens creating perceived performance

