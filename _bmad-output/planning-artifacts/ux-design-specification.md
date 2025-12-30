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
- **Bottom Sheet + Modal Hybrid Architecture with Onboarding:** Bottom sheet patterns for critical actions (mobile-native, thumb-optimized) combined with overlay modals for detailed views—phased implementation with clear onboarding tutorials and fallback to familiar patterns if users struggle with new interactions
- **Feed-Inspired Discovery with Utility-Focused Stories Pattern:** Visual feed-style event listing with horizontal swipe-through event "stories" providing genuine utility (exclusive content, behind-the-scenes, artist interviews)—not just promotional material—with progressive enhancement from traditional scrolling to swipe gestures
- **Community-Centered Visual Hierarchy with Smart Curation:** Community voices, friend activity, and trending events take visual prominence through layout and design, with intelligent filtering and algorithmic diversity to prevent echo chambers and information overload
- **Unified "Join Event" Bottom Sheet with Smart Sticky Behavior:** Bottom sheet action panel combines ticket selection (cart-style) + purchase + stream access in single streamlined flow—smart sticky bottom action bar (hide on scroll down, show on scroll up) that balances accessibility with content visibility
- **Stories-Based Event Previews with Content Strategy:** Adapt Instagram Stories pattern with focus on utility—exclusive content, behind-the-scenes, artist interviews—not just promotional highlights, with content guidelines ensuring genuine value
- **Transparent, Fee-Free Ticketing:** Internal ticketing system eliminates third-party fees, giving full control over pricing and user experience
- **Desktop Experience Excellence:** Mobile-first foundation with excellent desktop experience through layout adaptations and different interaction patterns (hover states, multi-column layouts, keyboard shortcuts), not just responsive scaling

### Target Users

**Primary Users: Event Attendees (Ages 21-24, with flexibility for 25-30 demographic)**
- Gen Z/early millennial demographic who primarily use mobile phones, with growing desktop usage in 25-30 segment
- Seek authentic experiences and community connection over corporate events
- Heavy users of Instagram, TikTok, Snapchat (21-24)—expect seamless social sharing and Stories-style previews
- Broader social media usage including LinkedIn/Facebook groups (25-30 demographic)
- Price-conscious but value experiences and community belonging
- Digital natives who expect fast, intuitive mobile experiences with bottom sheet patterns (familiar from mobile apps), but also appreciate quality desktop experiences when planning events
- Use this product to discover events (feed-inspired browsing with Stories previews), purchase tickets (bottom sheet cart-style selection), watch live streams (embedded in event cards), and engage with community (integrated bottom sheet actions)
- Potential concern: Filter bubbles and echo chambers from community recommendations—need balanced discovery algorithms that mix community input with algorithmic diversity

**Secondary Users: Emerging Artists/Performers**
- Looking for platforms and opportunities to showcase talent
- Discovered through community recommendations (integrated into feed discovery) but need serendipity features to prevent echo chambers
- Need easy submission and engagement processes (bottom sheet actions, not separate pages)

**Tertiary Users: Fashion Designers, Vendors, Sponsors**
- Fashion designers building their brands
- Vendors/sponsors targeting Gen Z demographic
- Seeking authentic community connection over transactional relationships

### Key Design Challenges

1. **Mobile-First Experience with Bottom Sheet + Modal Hybrid Architecture and User Onboarding**
   - Phase 1: Implement bottom sheet patterns for critical actions (ticket selection, engagement) with cart-style selection interface—more mobile-native than modals, with clear onboarding tutorials and visual cues
   - Phase 2: Feed-inspired visual layout with Stories pattern (horizontal swipe through event previews) using traditional scrolling for feed itself—with onboarding overlays explaining Stories pattern
   - Phase 3: Progressive enhancement with swipe gestures for feed navigation (after validating user understanding through analytics and user feedback)
   - Smart sticky bottom action bar: Hide on scroll down, show on scroll up (like mobile browsers) to balance accessibility with content visibility—prevents blocking important content while maintaining action accessibility
   - Achieve fast load times (< 3 seconds on 4G) with skeleton screens (show structure while loading, not spinners) and progressive enhancement strategy—load core content first, enhance with richer content/animations after initial render
   - Performance budget per page/section—prioritize critical path (discovery → ticket purchase), defer non-critical enhancements
   - Balance innovation (bottom sheets, Stories pattern) with familiarity (traditional scrolling foundation, fallback patterns if users struggle)
   - Clear visual cues and onboarding flows to help users understand new interaction patterns
   - Fallback to traditional patterns if analytics show user confusion or low engagement with new patterns

2. **Community-Driven UX Patterns Through Visual Hierarchy with Smart Curation and Balanced Discovery**
   - Integrate community voting and recommendations into feed-inspired listing (visual integration, bottom sheet for actions)
   - Visualize community impact prominently (magnified social proof: friend activity, trending events, limited tickets)
   - Smart default with easy switching: Default to "happening now" for discovery/impulse, but provide prominent filter/tab to switch to "upcoming" for planning—clear visual distinction between live/now vs upcoming
   - Community actions accessible from universal bottom sheet (not separate pages or complex navigation)
   - Create feedback loops that feel like social engagement (achievable through UI design and bottom sheet interactions)
   - Smart filtering and curation to prevent information overload: AI-assisted or algorithm-driven surfacing of most relevant community content, not showing everything—elegant filtering, sorting, and personalization controls
   - Balanced recommendation algorithm: Mix community recommendations with algorithmic diversity—"discover something new" prompts, serendipity features, "trending in other communities" sections, diversity badges—prevents echo chambers and filter bubbles while maintaining community-driven feel
   - UX patterns that encourage exploration beyond recommendations (random discovery features, cross-community trending, diversity indicators)

3. **Authentic Brand Expression with Mobile-Native Patterns and Content Strategy**
   - Integrate brand story into experience flow naturally (onboarding overlay tours, not separate pages)
   - Use Stories pattern for event previews with content strategy focus: Stories must provide genuine utility (exclusive content, behind-the-scenes, artist interviews, performer Q&As)—not just promotional material—with content guidelines ensuring genuine value
   - Bottom sheet patterns feel more authentic than traditional modals (native mobile app patterns)
   - Balance authenticity with conversion optimization—visual-first, social-media-native communication
   - Content strategy for Stories: Guidelines for what makes Stories valuable (behind-the-scenes footage, exclusive artist content, community member spotlights, event preparation content), not just event highlights

4. **Unified "Join Event" Bottom Sheet Flow with Smart Sticky Behavior**
   - Bottom sheet combines cart-style ticket selection + purchase + stream access in single flow
   - Cart-style selection interface (familiar shopping pattern, not form-based)
   - Handle edge cases gracefully (stream not available, payment failures, network issues) within bottom sheet context
   - Smart sticky bottom action bar: Hide on scroll down, show on scroll up to prevent blocking content while maintaining action accessibility—or make collapsible/minimizable
   - Social sharing integrated into checkout flow (share while purchasing, invite friends during checkout)
   - Maintain accessibility standards (bottom sheet keyboard navigation, screen reader support)
   - Balance between always-available actions and content visibility—smart sticky behavior prevents intrusive feel

5. **Desktop Experience Excellence (Not Just Responsive Scaling)**
   - Mobile-first foundation with excellent desktop experience through layout adaptations, not just responsive scaling
   - Different interaction patterns for desktop: Hover states, multi-column layouts, keyboard shortcuts, right-click context menus
   - Desktop-specific features: Side-by-side comparison of events, advanced filtering panels, multi-window workflows
   - Maintain mobile-first core while providing desktop users with optimized experience—don't treat desktop as second-class
   - Responsive design that adapts interaction patterns per device type, not just scales layout

6. **Competitive Differentiation Through Execution Quality**
   - As competitors adopt similar community-driven approaches, focus on execution quality and community authenticity
   - Deep integration of community input (not just collecting, but visibly implementing)
   - Genuine listening and visible impact—users need to see their input actually shaping outcomes, not just being collected
   - Community impact visualization becomes critical differentiator—show real examples of community recommendations implemented, votes that changed lineups, proposals that became events

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

