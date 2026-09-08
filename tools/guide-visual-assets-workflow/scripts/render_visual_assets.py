#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import json
from pathlib import Path

PALETTE = {
    "background": "#F7F6F1", "white": "#FFFFFF", "text": "#202321",
    "muted": "#6B6E6A", "primary": "#52675A", "accent": "#C66A4A",
    "border": "#D8D9D3", "soft": "#ECECE7", "soft_accent": "#F4E5DF",
}
STYLE = {
    "primary": ("#52675A", "#52675A", "#FFFFFF"),
    "accent": ("#F4E5DF", "#C66A4A", "#202321"),
    "neutral": ("#FFFFFF", "#D8D9D3", "#202321"),
    "muted": ("#ECECE7", "#D8D9D3", "#202321"),
}


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def text_lines(lines, x, y, size=18, line_height=26, anchor="middle", fill=None):
    fill = fill or PALETTE["text"]
    out = [f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Manrope, Arial, sans-serif" font-size="{size}" fill="{fill}">']
    for i, line in enumerate(lines):
        weight = "700" if i == 0 else "500"
        out.append(f'<tspan x="{x}" y="{y + i * line_height}" font-weight="{weight}">{esc(line)}</tspan>')
    out.append("</text>")
    return "".join(out)


def header(spec, width, height):
    return (
        f'<rect width="{width}" height="{height}" rx="28" fill="{PALETTE["background"]}"/>'
        f'<text x="60" y="58" font-family="Newsreader, Georgia, serif" font-size="38" font-weight="600" fill="{PALETTE["text"]}">{esc(spec.get("title", ""))}</text>'
        f'<text x="60" y="92" font-family="Manrope, Arial, sans-serif" font-size="18" fill="{PALETTE["muted"]}">{esc(spec.get("subtitle", ""))}</text>'
    )


def shell(spec, width, height, body):
    alt = esc(spec.get("alt", spec.get("title", "Diagramme")))
    caption = esc(spec.get("caption", ""))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="svg-title svg-desc">
<title id="svg-title">{alt}</title><desc id="svg-desc">{caption}</desc>
<defs><filter id="shadow" x="-10%" y="-10%" width="120%" height="120%"><feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#202321" flood-opacity="0.08"/></filter><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#9A9D98"/></marker></defs>
{header(spec, width, height)}<g filter="url(#shadow)">{body}</g></svg>'''


def render_node(node):
    fill, stroke, text = STYLE.get(node.get("style", "neutral"), STYLE["neutral"])
    x, y, width, height = (node[k] for k in ("x", "y", "w", "h"))
    lines = node.get("lines", [])
    font_size = int(node.get("font_size", 21))
    line_height = int(node.get("line_height", 28))
    first_y = y + height / 2 - max(0, (len(lines) - 1) * line_height) / 2 + 7
    return (
        f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="18" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'
        + text_lines(lines, x + width / 2, first_y, font_size, line_height, fill=text)
    )


def render_edge(edge, nodes):
    source = nodes[edge["from"]]
    target = nodes[edge["to"]]
    sx = source["x"] + source["w"] / 2
    sy = source["y"] + source["h"]
    tx = target["x"] + target["w"] / 2
    ty = target["y"]
    mid_y = (sy + ty) / 2
    path = f'<path d="M {sx} {sy} C {sx} {mid_y}, {tx} {mid_y}, {tx} {ty}" fill="none" stroke="#9A9D98" stroke-width="2.5" marker-end="url(#arrow)"/>'
    label = edge.get("label")
    if not label:
        return path
    lx = (sx + tx) / 2
    ly = mid_y - 8
    return path + f'<rect x="{lx-38}" y="{ly-17}" width="76" height="28" rx="14" fill="{PALETTE["background"]}"/><text x="{lx}" y="{ly+3}" text-anchor="middle" font-family="Manrope, Arial, sans-serif" font-size="15" font-weight="700" fill="{PALETTE["muted"]}">{esc(label)}</text>'


def render_decision_tree(spec):
    width = int(spec.get("canvas", {}).get("width", 1200))
    height = int(spec.get("canvas", {}).get("height", 820))
    nodes = {node["id"]: node for node in spec.get("nodes", [])}
    body = "".join(render_edge(edge, nodes) for edge in spec.get("edges", []))
    body += "".join(render_node(node) for node in spec.get("nodes", []))
    return shell(spec, width, height, body)


def render_process(spec, ecosystem=False):
    steps = spec.get("layers" if ecosystem else "steps", [])
    width = 1200
    count = len(steps)
    height = 390 if count <= 4 else 460
    x0 = 70
    gap = 22
    box_width = (width - 140 - gap * (count - 1)) / count
    y = 160
    box_height = 160
    body = []
    for i, item in enumerate(steps):
        x = x0 + i * (box_width + gap)
        if i:
            mid_y = y + box_height / 2
            body.append(f'<path d="M {x-gap} {mid_y} L {x-5} {mid_y}" stroke="#9A9D98" stroke-width="3" marker-end="url(#arrow)"/>')
        style = "primary" if i == 0 else ("accent" if i == count - 1 else "neutral")
        body.append(render_node({"x": x, "y": y, "w": box_width, "h": box_height, "style": style, "font_size": 18, "lines": item}))
    return shell(spec, width, height, "".join(body))


def render_checklist(spec):
    items = spec["items"]
    width = 1200
    card_width = 510
    card_height = 125
    gap_x = 40
    gap_y = 24
    rows = (len(items) + 1) // 2
    height = 165 + rows * (card_height + gap_y) + 45
    body = []
    for i, item in enumerate(items):
        col = i % 2
        row = i // 2
        x = 70 + col * (card_width + gap_x)
        y = 145 + row * (card_height + gap_y)
        body.append(f'<rect x="{x}" y="{y}" width="{card_width}" height="{card_height}" rx="18" fill="#FFFFFF" stroke="{PALETTE["border"]}" stroke-width="2"/>')
        body.append(f'<circle cx="{x+42}" cy="{y+42}" r="20" fill="{PALETTE["primary"]}"/><text x="{x+42}" y="{y+49}" text-anchor="middle" font-family="Manrope, Arial, sans-serif" font-size="18" font-weight="700" fill="#FFFFFF">{i+1}</text>')
        body.append(text_lines(item, x + 80, y + 40, 18, 26, anchor="start"))
    return shell(spec, width, height, "".join(body))


def render_cost(spec):
    items = spec["items"]
    width = 1200
    height = 180 + len(items) * 95 + 45
    body = []
    for i, item in enumerate(items):
        y = 145 + i * 95
        x = 110
        box_width = 980 - i * 45
        fill = PALETTE["primary"] if i == 0 else (PALETTE["soft_accent"] if i == len(items)-1 else "#FFFFFF")
        stroke = PALETTE["primary"] if i == 0 else (PALETTE["accent"] if i == len(items)-1 else PALETTE["border"])
        text = "#FFFFFF" if i == 0 else PALETTE["text"]
        body.append(f'<rect x="{x}" y="{y}" width="{box_width}" height="72" rx="16" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
        body.append(text_lines(item, x + 28, y + 31, 17, 23, anchor="start", fill=text))
        if i < len(items) - 1:
            body.append(f'<text x="82" y="{y+88}" font-family="Manrope, Arial, sans-serif" font-size="24" font-weight="700" fill="{PALETTE["accent"]}">+</text>')
    return shell(spec, width, height, "".join(body))


def render_sizes(spec):
    sizes = spec["sizes"]
    width = 1200
    height = 620
    body = []
    xs = [140, 400, 680, 960]
    for x, size in zip(xs, sizes):
        label, sw, sh, note = size
        scale = 2.0
        rw = sw * scale
        rh = sh * scale
        rx = x - rw / 2
        ry = 500 - rh
        body.append(f'<rect x="{rx}" y="{ry}" width="{rw}" height="{rh}" rx="12" fill="#FFFFFF" stroke="{PALETTE["primary"]}" stroke-width="3"/>')
        body.append(f'<rect x="{rx+12}" y="{ry+12}" width="{rw-24}" height="{rh-24}" rx="8" fill="{PALETTE["soft"]}"/>')
        body.append(text_lines([label, note], x, 534, 17, 24))
    return shell(spec, width, height, "".join(body))


RENDERERS = {
    "decision_tree": render_decision_tree,
    "process_flow": lambda spec: render_process(spec, False),
    "ecosystem_map": lambda spec: render_process(spec, True),
    "checklist": render_checklist,
    "cost_breakdown": render_cost,
    "size_comparison": render_sizes,
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    manifest = Path(args.manifest)
    if not manifest.is_absolute():
        manifest = root / manifest
    spec = json.loads(manifest.read_text(encoding="utf-8"))

    # Backward compatibility: historical manifests without asset_mode are diagrams.
    asset_mode = spec.get("asset_mode", "functional_diagram")

    if asset_mode == "no_visual":
        print(f"skip {manifest.relative_to(root)}: no_visual")
        return

    if asset_mode == "editorial_image":
        print(f"skip {manifest.relative_to(root)}: editorial_image is produced by an image generator, not the SVG renderer")
        return

    if asset_mode != "functional_diagram":
        raise SystemExit(f"Unsupported asset_mode: {asset_mode}")

    visual_type = spec.get("type")
    if visual_type not in RENDERERS:
        raise SystemExit(f"Unsupported functional diagram type: {visual_type}")

    output = root / spec["output"]
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(RENDERERS[visual_type](spec), encoding="utf-8")
    print(f"generated {output.relative_to(root)}")


if __name__ == "__main__":
    main()
