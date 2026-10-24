# Generative art

Load when seeded output, composition rules or visual variety is central.

## Principles

Randomness should explore an authored composition grammar. Distinctness comes from structure, hierarchy, rhythm and palette roles, not just more random parameters.

## Decision framework

Define invariants, controlled dimensions and constraints. Separate composition, geometry and palette streams so changing one does not accidentally scramble all others. Store seed, parameters and engine version for reproducibility.

## Implementation

Use a stable seeded PRNG and explicit canonical input normalization. Constrain overlap, margins, density and contrast where the concept needs them. Build a fixed seed contact sheet covering sparse/dense and edge cases; review silhouettes and hierarchy in addition to metadata diversity.

## Example and contextual exception

A grid engine can vary subdivision strategy, focal cell and rhythm while keeping palette roles coherent. Merely assigning random colours to the same arrangement produces parameter variety with little compositional variety.

## Failure patterns

Unseeded random calls during render; every seed looking alike; rejection loops without bounds; accidental seed changes on export; declaring beauty from numeric diversity.

## Validation

Repeat a seed and compare scene data; verify export composition. Review a documented seed set and flag duplicate structural families. Metrics such as occupied area and family counts support human review but cannot certify aesthetic quality.

## Evidence boundary

The decision framework and examples are authored guidance, not findings from a user study. Technical source: **canvas** in [the source register](../knowledge/sources.json). See its version, review date, supported claims and freshness status. Recheck version-sensitive APIs against the installed package/browser before implementation.

