{
    'Version' : '2012-10-17',
    {% if not pid == None %}
    'Id' : '{{ pid }}',
    {% endif %}
    'Statement' : [
        {% for stat in statement %}
        {
            {% if not stat.sid == None %}
            'Sid' : '{{ stat.sid }}',
            {% endif %}

            'Effect' : '{{ stat.effect }}',

            {% if not stat.principal == 'None' %}
            'Principal' : {{ stat.principal }},
            {% elif not stat.notprincipal == 'None' %}
            'NotPrincipal' : {{ stat.notprincipal }},
            {% endif %}

            {% if not stat.action == 'None' %}
            'Action' : {{ stat.action }},
            {% elif not stat.notaction == 'None' %}
            'NotAction' : '{{ stat.notaction }}',
            {% endif %}

            {% if not stat.resource == 'None' %}
            'Resource' : {{ stat.resource }},
            {% elif not stat.notresource == 'None' %}
            'NotResource' : {{ stat.notresource.v }},
            {% endif %}

            {% if stat.condition %}
            'Condition' : {{ stat.condition }}
            {% endif %}

        },
        {% endfor %}   
    ]
}