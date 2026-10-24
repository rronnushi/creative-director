# Typography and colour

Load when selecting type, building palettes, themes or legibility.

## Principles

Assign semantic roles before choosing values. Expressive display type can coexist with readable task text. Perceptually smoother colour interpolation does not guarantee accessible contrast.

## Decision framework

Choose font roles by language coverage, legibility at real size, loading cost, available weights and licensing. Pair by role contrast rather than collecting fonts. Generate candidate palettes in OKLCH/OKLab when helpful, gamut-map and verify actual displayed pairs.

## Implementation

Use relative units and bounded responsive type, a readable line length, fallbacks and stable font metrics where possible. Tokenize surface/ink/accent/status. Test dark and light themes separately; test focus, disabled and error states. For normal text target WCAG AA 4.5:1 and large text 3:1; large text is at least 18pt or 14pt bold, approximately 24px or 18.67px. Do not apply text thresholds blindly to all content.

## Example and contextual exception

A warm accent can mark selected filters while text stays a separate high-contrast ink. Lightening all colours for dark mode often destroys role relationships; choose theme-specific values. Data art may use low-contrast texture while controls remain readable.

## Failure patterns

Random hex values per component; status communicated only by colour; excessive font weights; assuming an accessible primary button proves the whole palette accessible.

## Validation

Measure real foreground/background pairs including opacity and images. Test zoom, missing fonts, long labels and required scripts. Verify non-text controls and focus indicators with the appropriate criteria.

## Evidence boundary

The decision framework and examples are authored guidance, not findings from a user study. Technical source: **wcag** in [the source register](../knowledge/sources.json). See its version, review date, supported claims and freshness status. Recheck version-sensitive APIs against the installed package/browser before implementation.

