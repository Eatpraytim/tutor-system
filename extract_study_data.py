#!/usr/bin/env python3
"""
Parses all revision pack markdown files into study_data.json and study_data.js.
Run: python3 extract_study_data.py
"""

import json
import re
import os
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)  # revision packs are one level up


def extract_sections(content):
    """Extract ## N) titled sections using balanced boundary detection."""
    sections = {}
    boundaries = list(re.finditer(r'^## (\d)\) .+$', content, re.MULTILINE))
    for i, m in enumerate(boundaries):
        num = m.group(1)
        start = m.end()
        end = boundaries[i + 1].start() if i + 1 < len(boundaries) else len(content)
        body = content[start:end].strip()
        body = re.sub(r'\n---\s*$', '', body).strip()
        sections[num] = body
    return sections


def extract_formulas(text):
    """Parse | concept | formula | table rows into structured list."""
    if not text:
        return []
    formulas = []
    for line in text.split('\n'):
        m = re.match(r'\|\s*(.+?)\s*\|\s*(.+?)\s*\|', line)
        if not m:
            continue
        concept = m.group(1).strip()
        formula = m.group(2).strip()
        if concept.startswith('-') or concept.lower() in ('concept', ''):
            continue
        formulas.append({'concept': concept, 'formula': formula})
    return formulas


def extract_questions(text):
    """Parse numbered questions, capturing optional (N min) time allocations."""
    if not text:
        return []
    questions = []
    for m in re.finditer(r'(\d+)\.\s+(.*?)(?=\n\d+\.\s|\Z)', text, re.DOTALL):
        body = m.group(2).strip()
        tm = re.match(r'\*\*\((\d+)\s*min\)\*\*\s*(.*)', body, re.DOTALL)
        if tm:
            questions.append({
                'time_minutes': int(tm.group(1)),
                'text': tm.group(2).strip()
            })
        else:
            questions.append({'time_minutes': None, 'text': body})
    return questions


def extract_key_terms(text):
    """Extract unique **bold** terms for fill-in-the-blank Feynman mode."""
    if not text:
        return []
    seen = set()
    terms = []
    for t in re.findall(r'\*\*(.+?)\*\*', text):
        if t.lower() not in seen:
            seen.add(t.lower())
            terms.append(t)
    return terms


def parse_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    fname = os.path.basename(filepath)
    m = re.match(r'(\d{4}-\d{2}-\d{2})_([A-Z]{2}\d{4})_(.*?)\.md', fname)
    if not m:
        return None

    date_str, module, slug = m.groups()
    title_m = re.match(r'#\s+(.+)', content)
    title = title_m.group(1).strip() if title_m else slug.replace('-', ' ').title()

    sections = extract_sections(content)
    feynman = sections.get('0', '')

    return {
        'filename': fname,
        'date': date_str,
        'module': module,
        'topicSlug': slug,
        'title': title,
        'sections': sections,
        'formulas': extract_formulas(sections.get('2', '')),
        'questions': extract_questions(sections.get('4', '')),
        'feynmanText': feynman,
        'feynmanKeyTerms': extract_key_terms(feynman),
        'modelAnswer': sections.get('5', ''),
        'commonTraps': sections.get('6', ''),
        'hasFullSections': bool(feynman and sections.get('4')),
    }


def main():
    files = sorted(
        f for f in os.listdir(BASE_DIR)
        if re.match(r'\d{4}-\d{2}-\d{2}_[A-Z]{2}\d{4}_.*\.md', f)
    )

    topics = []
    for f in files:
        data = parse_file(os.path.join(BASE_DIR, f))
        if data:
            topics.append(data)

    modules = {}
    schedule = {}
    for t in topics:
        modules.setdefault(t['module'], []).append(t['filename'])
        schedule.setdefault(t['date'], []).append(t['filename'])

    output = {
        'generated': datetime.now().isoformat(),
        'totalFiles': len(topics),
        'modules': modules,
        'schedule': schedule,
        'topics': topics,
    }

    json_path = os.path.join(SCRIPT_DIR, 'study_data.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    js_path = os.path.join(SCRIPT_DIR, 'study_data.js')
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write('const STUDY_DATA = ')
        json.dump(output, f, indent=2, ensure_ascii=False)
        f.write(';\n')

    print(f'Extracted {len(topics)} topics -> study_data.json + study_data.js')
    for mod in sorted(modules):
        print(f'  {mod}: {len(modules[mod])} files')


if __name__ == '__main__':
    main()
