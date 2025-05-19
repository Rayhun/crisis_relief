# myapp/templatetags/checklist_tags.py
from django import template
from django.utils.safestring import mark_safe
import re

register = template.Library()


@register.filter(name='render_checklist')
def render_checklist(value, task_id):
    # Convert - [ ] and - [x] inside <p> tags to HTML checkboxes
    value = re.sub(
        r'<p>- \[ \](.*?)<\/p>',
        f'<div class="checklist-item" data-id="{task_id}"><input type="checkbox" class="checklist-input" value="{task_id}"> <span>\\1</span></div>',
        str(value)
    )
    value = re.sub(
        r'<p>- \[x\](.*?)<\/p>',
        f'<div class="checklist-item" data-id="{task_id}"><input type="checkbox" class="checklist-input" checked value="{task_id}"> <span>\\1</span></div>',
        str(value)
    )
    # Handle cases with <br> tags
    value = re.sub(
        r'- \[ \](.*?)<br>',
        f'<div class="checklist-item" data-id="{task_id}"><input type="checkbox" class="checklist-input" value="{task_id}"> <span>\\1</span></div>',
        value
    )
    value = re.sub(
        r'- \[x\](.*?)<br>',
        f'<div class="checklist-item" data-id="{task_id}"><input type="checkbox" class="checklist-input" checked value="{task_id}"> <span>\\1</span></div>',
        value
    )
    return mark_safe(value)
