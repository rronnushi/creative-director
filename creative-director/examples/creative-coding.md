# Choose a renderer for a poster tool

Provenance: synthetic illustration, not real user feedback or measured results.

## Input

“Build a vector poster editor with scalable export and a few hundred shapes.”

## Mode and process

BUILD. SVG is a reasonable starting hypothesis because editable geometry and vector export are central. Keep scene data independent of DOM controls. Measure real interaction performance before moving to Canvas/WebGL.

## Actionable outcome

A compact DOM toolbar manipulates one scene; exporting serializes that scene with an explicit viewBox. Avoid a 3D dependency solely for 2D rectangles.

## Verification and limits

Resize without regeneration, reopen exported SVG, test text/font behavior and verify keyboard alternatives to drag.

