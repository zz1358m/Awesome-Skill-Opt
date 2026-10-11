"""Validate the catalog and render both READMEs."""
import argparse
import datetime as dt
import json
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
START = '<!-- GENERATED CATALOG:START -->'
END = '<!-- GENERATED CATALOG:END -->'
CATEGORIES = [
    ('optimization', 'Skill evolution and optimization', 'Skill 进化与优化'),
    ('induction', 'Skill induction from experience', '从经验中归纳 Skill'),
    ('transfer', 'Cross-model and cross-harness transfer', '跨模型与跨 harness 迁移'),
    ('routing', 'Retrieval, selection, and exposure', '检索、选择与呈现'),
    ('evaluation', 'Benchmarks and empirical studies', '基准与实证研究'),
    ('internalization', 'Internalizing skills into weights', '把 Skill 内化进权重'),
    ('adjacent', 'Adjacent work', '邻近工作'),
]
CODE_STATUS = {'author-linked', 'not located', 'not checked'}


def validate(data):
    dt.date.fromisoformat(data['last_checked'])
    seen = set()
    for p in data['papers']:
        for field in ['name', 'title', 'category', 'date', 'summary', 'summary_zh', 'checked_on', 'code_status']:
            assert p.get(field), f'Missing {field}: {p.get("title")}'
        assert p['category'] in {c[0] for c in CATEGORIES}, p['title']
        assert re.fullmatch(r'20\d{2}-\d{2}(-\d{2})?', p['date']), p['title']
        dt.date.fromisoformat(p['checked_on'])
        assert bool(p.get('arxiv_id')) != bool(p.get('openreview_id')), f'Exactly one primary source: {p["title"]}'
        if p.get('arxiv_id'):
            assert re.fullmatch(r'\d{4}\.\d{4,5}', p['arxiv_id']), p['title']
            assert p['authors'], f'Missing authors: {p["title"]}'
        else:
            assert p['venue'], f'Anonymous submission needs a venue label: {p["title"]}'
        key = p['title'].lower()
        assert key not in seen, f'Duplicate title: {p["title"]}'
        seen.add(key)
        assert p['code_status'] in CODE_STATUS and (p['code_status'] == 'author-linked') == bool(p.get('code_url'))
        for url in [p.get('code_url')] if p.get('code_url') else []:
            parsed = urlparse(url)
            assert parsed.scheme == 'https' and parsed.hostname and not parsed.username


def paper_url(p):
    if p.get('arxiv_id'):
        return f'https://arxiv.org/abs/{p["arxiv_id"]}'
    return f'https://openreview.net/forum?id={p["openreview_id"]}'


def catalog(data, zh=False):
    out = START + '\n'
    for key, en, cn in CATEGORIES:
        papers = sorted((p for p in data['papers'] if p['category'] == key), key=lambda p: p['date'], reverse=True)
        if not papers:
            continue
        out += f'<a id="{key}"></a>\n\n## {cn if zh else en}\n\n'
        out += '| 日期 | 工作 | 贡献 | 资源 |\n| --- | --- | --- | --- |\n' if zh else '| Date | Work | Contribution | Resources |\n| --- | --- | --- | --- |\n'
        for p in papers:
            resources = f'[paper]({paper_url(p)})'
            if p.get('code_url'):
                resources += f' · [code]({p["code_url"]})'
            elif p['code_status'] == 'not located':
                resources += ' · 代码未定位' if zh else ' · code not located'
            if p.get('venue'):
                resources += f' · {p["venue"]}'
            work = f'**{p["name"]}** — {p["title"]}' if p['name'] != p['title'] else f'**{p["title"]}**'
            summary = p['summary_zh' if zh else 'summary'].replace('|', '\\|')
            out += f'| {p["date"]} | {work} | {summary} | {resources} |\n'
        out += '\n'
    return out + END


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    data = json.loads((ROOT / 'data/papers.json').read_text(encoding='utf-8'))
    validate(data)
    for relative, zh in [('README.md', False), ('README_zh.md', True)]:
        path = ROOT / relative
        text = path.read_text(encoding='utf-8')
        head, rest = text.split(START, 1)
        tail = rest.split(END, 1)[1]
        count = '**最近一次文献检查：{} · {} 篇。**' if zh else '**Last literature check: {} · {} papers.**'
        head = re.sub(r'\*\*(Last literature check|最近一次文献检查)[^\n]*\*\*', count.format(data['last_checked'], len(data['papers'])), head)
        body = head + catalog(data, zh) + tail
        if args.check:
            assert text == body, f'Stale generated file: {relative}'
        else:
            path.write_text(body, encoding='utf-8')
    print(f'Validated {len(data["papers"])} papers and generated-file consistency.')


if __name__ == '__main__':
    main()
