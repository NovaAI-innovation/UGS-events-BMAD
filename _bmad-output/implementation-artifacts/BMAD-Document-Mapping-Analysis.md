# BMAD Method Workflow - Document Placement Analysis

## Executive Summary

This analysis maps your existing business, legal, and content documents to the BMAD (BMad Method) workflow phases. Understanding where each document fits helps you leverage them effectively during development and ensures nothing is overlooked.

---

## BMAD Method Overview

**BMAD Method Workflow Phases:**
- **Phase 0 (Prerequisite):** Documentation (brownfield projects only)
- **Phase 1 (Optional):** Analysis - Discovery, research, product brief
- **Phase 2 (Required):** Planning - PRD, tech-spec, UX design
- **Phase 3 (Track-dependent):** Solutioning - Architecture, epics/stories
- **Phase 4 (Required):** Implementation - Sprint-based development

---

## Document Placement Matrix

| Document | Primary Phase | Secondary Phase | Workflow/Use Case | Status |
|----------|--------------|-----------------|-------------------|--------|
| `prd.md` | **Phase 2: Planning** | Phase 1 (input) | `prd` workflow output/input | ✅ Ready |
| `brand-guidelines.md` | **Phase 2: Planning** | Phase 3 (UX) | `create-ux-design`, design system | ✅ Ready |
| `webpage-content-consolidated.md` | **Phase 4: Implementation** | Phase 2 (content planning) | Content implementation stories | ✅ Ready |
| `webpage-content-README.md` | Phase 4 | Phase 2 | Content documentation | ✅ Ready |
| `webpage-content-community-driven-notes.md` | Phase 4 | Phase 2 | Content strategy notes | ✅ Ready |
| `fashion-divine-divas-vol1.md` | **Phase 4: Implementation** | Phase 2 (requirements) | Event data/content stories | ✅ Ready |
| `privacy-policy.md` | **Phase 2: Planning** (NFR) | Phase 4 (implementation) | Legal requirement (NFR) | ✅ Ready |
| `terms-of-service.md` | **Phase 2: Planning** (NFR) | Phase 4 (implementation) | Legal requirement (NFR) | ✅ Ready |
| `copyright-notice.md` | **Phase 2: Planning** (NFR) | Phase 4 (implementation) | Legal requirement (NFR) | ✅ Ready |
| `dmca-takedown-policy.md` | **Phase 2: Planning** (NFR) | Phase 4 (implementation) | Legal requirement (NFR) | ✅ Ready |
| `footer-copyright-template.md` | **Phase 4: Implementation** | Phase 3 (design system) | Implementation asset | ✅ Ready |
| `ip-protection-checklist.md` | **Phase 2: Planning** | Phase 4 (validation) | Legal/compliance checklist | ✅ Ready |
| `artist-performer-contract-template.md` | **Phase 1: Analysis** (business) | Phase 2 (NFR) | Business process documentation | ✅ Ready |
| `content-licensing-agreement.md` | **Phase 1: Analysis** (business) | Phase 2 (NFR) | Business process documentation | ✅ Ready |
| `photo-video-release-form.md` | **Phase 1: Analysis** (business) | Phase 2 (NFR) | Business process documentation | ✅ Ready |
| `claude-sponsorship.md` | **Phase 1: Analysis** | Phase 2 (business requirements) | Business strategy/research | ✅ Ready |

---

## Detailed Phase-by-Phase Analysis

### Phase 0: Documentation (Prerequisite)
**Status:** Not applicable (greenfield project)

**Documents:** None
- This phase is only for brownfield projects that need codebase documentation
- Your project appears to be greenfield (new website development)

---

### Phase 1: Analysis (Optional)
**Purpose:** Discovery, research, strategic thinking before planning

#### Documents That Belong Here:

1. **`claude-sponsorship.md`**
   - **Workflow:** `research` (market/competitive) or `brainstorm-project`
   - **Use Case:** Business model research, partnership strategy
   - **How to Use:** Input for market analysis, business model validation
   - **Recommended Action:** Reference during `research` workflow if exploring sponsorship features

2. **`artist-performer-contract-template.md`**
   - **Workflow:** `product-brief` or `research` (domain)
   - **Use Case:** Business process documentation, operational requirements
   - **How to Use:** Defines business rules that inform functional requirements
   - **Recommended Action:** Document business processes that need system support

3. **`content-licensing-agreement.md`**
   - **Workflow:** `product-brief` or `research` (domain)
   - **Use Case:** Content management requirements, legal constraints
   - **How to Use:** Defines content licensing rules that become NFRs
   - **Recommended Action:** Reference when defining content management features

4. **`photo-video-release-form.md`**
   - **Workflow:** `product-brief` or `research` (domain)
   - **Use Case:** Event management requirements, legal compliance
   - **How to Use:** Defines data collection and consent requirements
   - **Recommended Action:** Reference when defining user-generated content features

#### Integration Notes:
- These documents define **business context** that should inform Phase 2 planning
- They help identify **non-functional requirements** (legal compliance, business rules)
- Consider running `research` workflow with these as domain context

---

### Phase 2: Planning (Required)
**Purpose:** Define requirements (FRs and NFRs) in PRD or tech-spec

#### Documents That Belong Here:

1. **`prd.md`** ⭐ PRIMARY WORKFLOW DOCUMENT
   - **Workflow:** `prd` (PM agent)
   - **Use Case:** This IS your PRD - use as-is or enhance via workflow
   - **How to Use:** 
     - **Option A:** Use existing PRD as-is (skip `prd` workflow)
     - **Option B:** Run `prd` workflow to formalize/enhance it
   - **Recommended Action:** 
     - Review PRD against BMAD standards
     - Ensure it has clear FRs and NFRs
     - Use as input if running workflow to refine

2. **`brand-guidelines.md`**
   - **Workflow:** `create-ux-design` (UX Designer agent)
   - **Use Case:** Design system foundation, brand identity constraints
   - **How to Use:** 
     - Reference during UX design workflow
     - Defines design tokens (colors, fonts, logo usage)
     - Becomes part of design system documentation
   - **Recommended Action:** 
     - Use as input for `create-ux-design` workflow
     - Extract design tokens for implementation
     - Ensure UX spec aligns with brand guidelines

3. **Legal Documents (Privacy Policy, Terms of Service, Copyright Notice, DMCA)**
   - **Workflow:** `prd` (as Non-Functional Requirements - NFRs)
   - **Use Case:** Legal compliance requirements
   - **How to Use:**
     - Document as **NFRs** in PRD (e.g., "NFR-001: Privacy Policy compliance")
     - These become implementation requirements in Phase 4
     - Must be accessible on website (footer links, etc.)
   - **Recommended Action:**
     - Add legal compliance section to PRD with references to these documents
     - Define implementation requirements (e.g., "Footer must link to Privacy Policy")
     - Mark as NFRs with acceptance criteria

4. **`ip-protection-checklist.md`**
   - **Workflow:** `prd` (compliance NFRs)
   - **Use Case:** Legal/compliance checklist
   - **How to Use:** 
     - Convert checklist items to NFRs
     - Use as validation checklist during Phase 4
     - Ensures all legal requirements are captured
   - **Recommended Action:** 
     - Review checklist items
     - Add any missing requirements to PRD as NFRs
     - Use as Phase 4 validation checklist

#### Integration Notes:
- **Primary Workflow:** `prd` workflow (PM agent) - creates PRD with FRs/NFRs
- Your existing `prd.md` can serve as the PRD document
- Legal documents become **NFRs** (non-functional requirements)
- Brand guidelines feed into **UX design workflow** (optional but recommended)

---

### Phase 3: Solutioning (Track-Dependent)
**Purpose:** Technical architecture and design decisions

#### Documents That Belong Here:

1. **`brand-guidelines.md`** (continued from Phase 2)
   - **Workflow:** `architecture` (design system section)
   - **Use Case:** Design system architecture
   - **How to Use:**
     - Extract design tokens (colors, typography, spacing)
     - Define CSS architecture based on brand guidelines
     - Document component design system
   - **Recommended Action:**
     - Architect will reference brand guidelines when designing frontend architecture
     - Design system decisions should be documented in architecture.md

2. **`footer-copyright-template.md`**
   - **Workflow:** `architecture` (design system)
   - **Use Case:** Component specification
   - **How to Use:**
     - Defines footer component requirements
     - Becomes part of component architecture
   - **Recommended Action:**
     - Reference during architecture design
     - Include in design system documentation

#### Integration Notes:
- Architecture workflow creates `architecture.md` with ADRs (Architecture Decision Records)
- Brand guidelines inform frontend architecture decisions
- Legal requirements from Phase 2 inform security/legal architecture sections

---

### Phase 4: Implementation (Required)
**Purpose:** Sprint-based development, story-by-story implementation

#### Documents That Belong Here:

1. **`webpage-content-consolidated.md`** ⭐ PRIMARY CONTENT DOCUMENT
   - **Workflow:** `dev-story` (DEV agent) - content implementation stories
   - **Use Case:** Source content for all website pages
   - **How to Use:**
     - Content for Homepage → Story: "Implement homepage with content"
     - Content for About Page → Story: "Implement about page with content"
     - Content for Events Page → Story: "Implement events listing page"
     - Content for Contact Page → Story: "Implement contact page"
     - Content for Event Detail Page → Story: "Implement event detail page template"
   - **Recommended Action:**
     - Break into stories by page/section
     - Each page becomes one or more stories
     - Content should be extracted into appropriate page templates during implementation

2. **`webpage-content-README.md`**
   - **Workflow:** Story documentation
   - **Use Case:** Content documentation and guidelines
   - **How to Use:**
     - Reference for content structure and organization
     - Helps developers understand content architecture
   - **Recommended Action:**
     - Keep as reference documentation
     - Include in project documentation

3. **`webpage-content-community-driven-notes.md`**
   - **Workflow:** Story context/requirements
   - **Use Case:** Content strategy and community approach
   - **How to Use:**
     - Informs content implementation approach
     - Defines community-driven features (voting, suggestions, etc.)
   - **Recommended Action:**
     - Reference when implementing community features
     - May generate additional stories for community functionality

4. **`fashion-divine-divas-vol1.md`**
   - **Workflow:** `dev-story` - event data/content
   - **Use Case:** Event data for event detail page implementation
   - **How to Use:**
     - Sample event data for development/testing
     - Defines event data structure
     - Can be used to implement event detail page template
   - **Recommended Action:**
     - Use as sample data during event detail page development
     - May inform event data model/schema

5. **`footer-copyright-template.md`**
   - **Workflow:** `dev-story` - footer component
   - **Use Case:** Footer implementation specification
   - **How to Use:**
     - Exact footer text/template to implement
     - HTML structure reference
     - Implementation guide
   - **Recommended Action:**
     - Create story: "Implement footer component with copyright notice"
     - Use template as exact implementation spec

6. **Legal Documents Implementation**
   - **Workflow:** `dev-story` - legal pages
   - **Use Case:** Legal page implementation
   - **How to Use:**
     - Privacy Policy → Story: "Implement Privacy Policy page"
     - Terms of Service → Story: "Implement Terms of Service page"
     - Copyright Notice → Story: "Implement Copyright Notice page"
     - DMCA Policy → Story: "Implement DMCA Takedown Policy page"
   - **Recommended Action:**
     - Create stories for each legal page
     - Link from footer (defined in footer story)
     - Ensure accessibility and proper formatting

#### Integration Notes:
- Phase 4 uses **story-centric workflow** - one story at a time
- Content documents provide **implementation specifications**
- Each page/section becomes one or more stories
- Stories reference architecture decisions from Phase 3

---

## Workflow Integration Recommendations

### Recommended BMAD Workflow Path

Based on your documents, here's the recommended workflow:

#### Step 1: Phase 2 - Planning (Required)
```
1. Load PM agent
2. Run `prd` workflow OR use existing prd.md
   - Input: Your existing prd.md
   - Review/Enhance: Add NFRs for legal compliance
   - Output: Enhanced PRD with FRs/NFRs
```

**NFRs to Add:**
- NFR-001: Privacy Policy must be accessible
- NFR-002: Terms of Service must be accessible
- NFR-003: Copyright notice in footer
- NFR-004: DMCA policy accessible
- NFR-005: Brand guidelines compliance
- NFR-006: Legal documents linked in footer

#### Step 2: Phase 2 - UX Design (Optional but Recommended)
```
1. Load UX Designer agent
2. Run `create-ux-design` workflow
   - Input: brand-guidelines.md, PRD
   - Output: ux-spec.md with design system
```

#### Step 3: Phase 3 - Solutioning (Required for BMad Method)
```
1. Load Architect agent
2. Run `architecture` workflow
   - Input: PRD, UX spec (if created)
   - Reference: brand-guidelines.md for design system
   - Output: architecture.md with ADRs
```

#### Step 4: Phase 3 - Epics and Stories
```
1. Load PM agent
2. Run `create-epics-and-stories` workflow
   - Input: PRD, architecture.md
   - Output: Epic files with stories
```

**Expected Epic Breakdown:**
- Epic 1: Core Website Pages (Home, About, Events, Contact)
- Epic 2: Event Management (Event listing, Event detail)
- Epic 3: Legal/Compliance Pages (Privacy, Terms, Copyright, DMCA)
- Epic 4: Design System Implementation
- Epic 5: Content Integration
- (Additional epics based on PRD features)

#### Step 5: Phase 4 - Implementation
```
1. Load SM agent
2. Run `sprint-planning` workflow
3. For each story:
   - SM: `create-story`
   - DEV: `dev-story` (references content documents)
   - DEV: `code-review`
```

**Content Integration Stories:**
- Story: "Implement Homepage with content from webpage-content-consolidated.md"
- Story: "Implement About Page with content"
- Story: "Implement Events Listing Page"
- Story: "Implement Event Detail Page template (use fashion-divine-divas-vol1.md as sample data)"
- Story: "Implement Contact Page with contact form"
- Story: "Implement Footer component with copyright notice"
- Story: "Implement Privacy Policy page"
- Story: "Implement Terms of Service page"
- Story: "Implement Copyright Notice page"
- Story: "Implement DMCA Takedown Policy page"

---

## Document Status Assessment

### ✅ Ready for BMAD Workflow

All documents are ready to use in BMAD workflows:

1. **PRD (`prd.md`)** - Complete and ready
   - Can be used as-is OR enhanced via `prd` workflow
   - Already contains requirements

2. **Content Documents** - Complete and ready
   - `webpage-content-consolidated.md` - All page content ready
   - `fashion-divine-divas-vol1.md` - Sample event data ready
   - Content is well-structured for implementation

3. **Legal Documents** - Complete and ready
   - All legal documents are complete templates
   - Ready to be implemented as pages
   - Should be added as NFRs to PRD

4. **Brand Guidelines** - Complete and ready
   - Ready for UX design workflow
   - Design tokens can be extracted
   - Logo/color specifications available

5. **Business Process Documents** - Complete
   - Contracts and agreements are documented
   - Can inform business logic requirements
   - May generate additional features (contract management)

---

## Next Steps

### Immediate Actions

1. **Review PRD Against BMAD Standards**
   - Ensure FRs (Functional Requirements) are clearly defined
   - Add NFRs (Non-Functional Requirements) section
   - Include legal compliance requirements as NFRs
   - Reference: `_bmad/bmm/docs/workflows-planning.md`

2. **Prepare for Phase 2 Workflow**
   - Decide: Use existing PRD as-is OR run `prd` workflow to enhance
   - If enhancing: Load PM agent → Run `prd` workflow
   - Add legal compliance NFRs (reference legal documents)

3. **Optional: Run UX Design Workflow**
   - Load UX Designer agent
   - Run `create-ux-design` workflow
   - Input: `brand-guidelines.md` + PRD
   - Extract design tokens for implementation

4. **Phase 3: Architecture**
   - Load Architect agent
   - Run `architecture` workflow
   - Reference: PRD, UX spec (if created), brand guidelines
   - Focus on technical decisions (vanilla HTML/CSS/JS stack)

5. **Phase 3: Create Epics and Stories**
   - Load PM agent
   - Run `create-epics-and-stories` workflow
   - Content documents will inform story breakdown

6. **Phase 4: Implementation**
   - Content documents become story specifications
   - Each page becomes one or more stories
   - Legal documents become legal page implementation stories

---

## Summary

**Key Findings:**

1. **Your `prd.md` is ready** - Can be used directly or enhanced via BMAD `prd` workflow
2. **Content is complete** - All webpage content is ready for Phase 4 implementation
3. **Legal requirements** - Need to be added as NFRs to PRD
4. **Brand guidelines** - Ready for UX design workflow
5. **Business documents** - Provide context but don't directly map to technical workflows

**Recommended Workflow:**
- Phase 2: Use/enhance PRD, add legal NFRs, optional UX design
- Phase 3: Architecture + Epics/Stories
- Phase 4: Implement content pages story-by-story

**All documents are ready to integrate into BMAD workflows!** ✅

