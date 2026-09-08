#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import json
from pathlib import Path

PALETTE = {
    "background": "#F7F6F1",
    "white": "#FFFFFF",
    "text": "#202321",
    "muted": "#6B6E6A",
    "primary": "#52675A",
    "accent": "#C66A4A",
    "border": "#D8D9D3",
    "soft": "#ECECE7",
    "soft_accent": "#F4E5DF",
}

STYLE = {
    "primary": ("#52675A", "#52675A", "#FFFFFF"),
    "accent": ("#F4E5DF", "#C66A4A", "#202321"),
    "neutral": ("#FFFFFF", "#D8D9D3", "#202321"),
    "muted": ("#ECECE7", "#D8D9D3", "#202321"),
}


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def node_center(node: dict) -> tuple[float, float]:
    return node["x"] + node["w"] / 2, node["y"] + node["h"] / 2


def render_node(node: dict) -> str:
    fill, stroke, text = STYLE.get(node.get("style", "neutral"), STYLE["neutral"])
    x, y, w, h = (node[k] for k in ("x", "y", "w", "h"))
    lines = node.get("lines", [])
    font_size = int(node.get("font_size", 21))
    line_height = int(node.get("line_height", 28))
    total = max(0, (len(lines) - 1) * line_height)
    first_y = y + h / 2 - total / 2 + 7
    tspans = []
    for i, line in enumerate(lines):
        weight = "700" if i == 0 and node.get("bold_first", True) else "500"
        tspans.append(
            f'<tspan x="{x + w/2}" y="{first_y + i*line_height}" font-weight="{weight}">{esc(line)}</tspan>'
        )
    return (
        f'<g id="node-{esc(node["id"])}">'
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'
        f'<text text-anchor="middle" font-family="Manrope, Arial, sans-serif" font-size="{font_size}" fill="{text}">'
        + "".join(tspans)
        + "</text></g>"
    )


def render_edge(edge: dict, nodes: dict[str, dict]) -> str:
    source = nodes[edge["from"]]
    target = nodes[edge["to"]]
    sx, sy = node_center(source)
    tx, ty = node_center(target)
    sy = source["y"] + source["h"]
    ty = target["y"]
    mid_y = (sy + ty) / 2
    d = f"M {sx} {sy} C {sx} {mid_y}, {tx} {mid_y}, {tx} {ty}"
    label = edge.get("label")
    label_svg = ""
    if label:
        lx = (sx + tx) / 2
        ly = mid_y - 8
        label_svg = (
            f'<rect x="{lx-38}" y="{ly-17}" width="76" height="28" rx="14" fill="#F7F6F1"/>'
            f'<text x="{lx}" y="{ly+3}" text-anchor="middle" font-family="Manrope, Arial, sans-serif" '
            f'font-size="15" font-weight="700" fill="#6B6E6A">{esc(label)}</text>'
        )
    return f'<path d="{d}" fill="none" stroke="#9A9D98" stroke-width="2.5" marker-end="url(#arrow)"/>{label_svg}'


def render_decision_tree(spec: dict) -> str:
    width = int(spec.get("canvas", {}).get("width", 1200))
    height = int(spec.get("canvas", {}).get("height", 900))
    nodes = {node["id"]: node for node in spec.get("nodes", [])}
    title = esc(spec.get("title", ""))
    subtitle = esc(spec.get("subtitle", ""))
    accessible_title = esc(spec.get("alt", spec.get("title", "Diagramme")))
    caption = esc(spec.get("caption", ""))

    edges_svg = "".join(render_edge(edge, nodes) for edge in spec.get("edges", []))
    nodes_svg = "".join(render_node(node) for node in spec.get("nodes", []))

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="svg-title svg-desc">
  <title id="svg-title">{accessible_title}</title>
  <desc id="svg-desc">{caption}</desc>
  <defs>
    <filter id="shadow" x="-10%" y="-10%" width="120%" height="120%"><feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#202321" flood-opacity="0.08"/></filter>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L0,6 L9,3 z" fill="#9A9D98"/></marker>
  </defs>
  <rect width="{width}" height="{height}" rx="28" fill="#F7F6F1"/>
  <text x="60" y="58" font-family="Newsreader, Georgia, serif" font-size="38" font-weight="600" fill="#202321">{title}</text>
  <text x="60" y="92" font-family="Manrope, Arial, sans-serif" font-size="18" fill="#6B6E6A">{subtitle}</text>
  <g filter="url(#shadow)">{edges_svg}{nodes_svg}</g>
</svg>'''


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--root", default=".")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    manifest = Path(args.manifest)
    if not manifest.is_absolute():
        manifest = root / manifest
    spec = json.loads(manifest.read_text(encoding="utf-8"))

    if spec.get("type") != "decision_tree":
        raise SystemExit(f"Unsupported visual type for current renderer: {spec.get('type')}")

    output = root / spec["output"]
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_decision_tree(spec), encoding="utf-8")
    print(f"generated {output.relative_to(root)}")


if __name__ == "__main__":
    main()
