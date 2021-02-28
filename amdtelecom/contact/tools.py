from django.utils.html import escape


def readonly_cssclass_adder(bound_field, label_content, label_attrs):
    if 'readonly' in bound_field.field.widget.attrs:
        if 'class' in attrs:
            label_attrs['class'] += " readOnly"
        else:
            label_attrs['class'] = "readOnly"
    return label_content, label_attrs


def add_required_label_tag(original_function, tweak_foos=None):
    if not tweak_foos:
        return original_function

    def required_label_tag(self, contents=None, attrs=None):
        contents = contents or escape(self.label)
        if attrs is None:
            attrs = {}
        for foo in tweak_foos:
            contents, attrs = foo(self, contents, attrs)
        return original_function(self, contents, attrs)
    return required_label_tag


def decorate_bound_field():
    from django.forms.forms import BoundField
    BoundField.label_tag = add_required_label_tag(BoundField.label_tag,
                                                tweak_foos=[readonly_cssclass_adder])
